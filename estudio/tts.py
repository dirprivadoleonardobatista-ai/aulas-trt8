# -*- coding: utf-8 -*-
"""Narracao com edge-tts (gratuito). Cada fala vira um WAV PCM, para que a
linha do tempo do video seja exata (MP3 colado acumula atraso)."""
import asyncio
import hashlib
import os
import subprocess
import wave

TAXA = 24000          # Hz, mono, 16 bits: o que o edge-tts entrega

# voz, tom (negativo = mais grave), ritmo. Os ritmos igualam a velocidade
# das quatro (medido: Thalita e Francisca sao naturalmente mais rapidas).
VOZES_TTS = {
    "ANTONIO":   ("pt-BR-AntonioNeural",            "-10Hz", "-2%"),
    "FRANCISCA": ("pt-BR-FranciscaNeural",          "-8Hz",  "-5%"),
    "BRUNO":     ("en-US-BrianMultilingualNeural",  "-6Hz",  "+4%"),
    "THALITA":   ("pt-BR-ThalitaMultilingualNeural", "-10Hz", "-8%"),
}

PARALELO = int(os.environ.get("TTS_PARALELO", "6"))


def _chave(voz, texto):
    nome, tom, ritmo = VOZES_TTS[voz]
    return hashlib.sha1(("%s|%s|%s|%s" % (nome, tom, ritmo, texto)).encode("utf-8")).hexdigest()[:20]


async def _uma(sem, voz, texto, mp3):
    import edge_tts
    nome, tom, ritmo = VOZES_TTS[voz]
    async with sem:
        erro = None
        for tentativa in range(6):
            try:
                tmp = mp3 + ".parcial"
                await edge_tts.Communicate(texto, nome, rate=ritmo, pitch=tom).save(tmp)
                if os.path.getsize(tmp) > 1500:
                    os.replace(tmp, mp3)
                    return None
                erro = "arquivo vazio"
            except Exception as e:          # rede, 429, 503...
                erro = "%s: %s" % (type(e).__name__, str(e)[:120])
            await asyncio.sleep(2 + 4 * tentativa)
        return erro


def _wav(mp3, wav):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-ac", "1", "-ar", str(TAXA),
                    "-sample_fmt", "s16", wav], check=True)


def sintetizar(falas, cache):
    """falas = [(VOZ, texto)] -> [caminho_wav] na mesma ordem."""
    os.makedirs(cache, exist_ok=True)
    alvos = []
    for voz, texto in falas:
        base = os.path.join(cache, _chave(voz, texto))
        alvos.append((voz, texto, base + ".mp3", base + ".wav"))

    faltam = [(v, t, m) for v, t, m, w in alvos if not os.path.exists(w) and not os.path.exists(m)]

    async def tudo():
        sem = asyncio.Semaphore(PARALELO)
        return await asyncio.gather(*[_uma(sem, v, t, m) for v, t, m in faltam])

    if faltam:
        erros = [e for e in asyncio.run(tudo()) if e]
        if erros:
            raise RuntimeError("TTS falhou em %d falas (ex.: %s)" % (len(erros), erros[0]))

    from concurrent.futures import ThreadPoolExecutor
    pend = [(m, w) for _, _, m, w in alvos if not os.path.exists(w)]
    with ThreadPoolExecutor(max_workers=os.cpu_count() or 2) as ex:
        list(ex.map(lambda mw: _wav(*mw), pend))
    return [w for _, _, _, w in alvos]


def ler_pcm(wav):
    with wave.open(wav, "rb") as w:
        assert w.getframerate() == TAXA and w.getnchannels() == 1 and w.getsampwidth() == 2
        return w.readframes(w.getnframes())


def silencio(segundos):
    return b"\x00\x00" * int(round(segundos * TAXA))


def gravar_wav(pcm, destino):
    with wave.open(destino, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(TAXA)
        w.writeframes(pcm)
