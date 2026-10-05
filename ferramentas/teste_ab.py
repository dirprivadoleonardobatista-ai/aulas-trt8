# -*- coding: utf-8 -*-
"""Teste para achar onde o final das palavras se perde: o mesmo trecho em
cinco versoes, cada uma acrescentando uma etapa do processo.

    python ferramentas/teste_ab.py   ->  saida/teste/1_...mp3 a 5_...mp3
"""
import asyncio
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from estudio import tts                      # noqa: E402
from estudio import render                   # noqa: E402

TRECHO = [
    ("FRANCISCA", "Vamos começar pela nacionalidade, nos artigos doze e treze."),
    ("FRANCISCA", "Nacionalidade é o vínculo jurídico-político entre a pessoa e o Estado."),
    ("THALITA", "E quais são as espécies?"),
    ("FRANCISCA", "São duas. A primária, ou originária, decorre do nascimento e dá o brasileiro nato."),
    ("FRANCISCA", "A secundária, ou adquirida, decorre de ato de vontade e dá o naturalizado."),
    ("THALITA", "Então a lei pode distinguir nato de naturalizado?"),
    ("FRANCISCA", "Não pode, salvo nos casos previstos na própria Constituição."),
]

PASTA = os.path.join(RAIZ, "saida", "teste")
CACHE = os.path.join(RAIZ, ".cache_teste")


def gravar_mp3(pcm, nome, cadeia=None):
    wav = os.path.join(PASTA, "tmp.wav")
    tts.gravar_wav(pcm, wav)
    destino = os.path.join(PASTA, nome + ".mp3")
    af = ["-af", cadeia] if cadeia else []
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", wav] + af +
                   ["-ar", "44100", "-ac", "1", "-c:a", "libmp3lame", "-b:a", "128k", destino], check=True)
    os.remove(wav)
    print(destino)


def bruto(wav):
    import wave
    with wave.open(wav, "rb") as w:
        return w.readframes(w.getnframes())


def main():
    os.makedirs(PASTA, exist_ok=True)
    wavs = tts.sintetizar(TRECHO, CACHE)
    voz_anterior = None

    # 1: exatamente como o servico de voz entrega, frase atras de frase
    gravar_mp3(b"".join(bruto(w) for w in wavs), "1_voz_pura_sem_nada")

    # 2: com as pausas longas entre frases e na troca de voz (sem mexer dentro da frase)
    pcm = []
    for (voz, txt), w in zip(TRECHO, wavs):
        if voz_anterior and voz != voz_anterior:
            pcm.append(tts.silencio(render.PAUSA_FALA - render.PAUSA_FRASE))
        pcm += [tts.ler_frase(w, ""), tts.silencio(render.PAUSA_FRASE)]
        voz_anterior = voz
    p2 = b"".join(pcm)
    gravar_mp3(p2, "2_pausas_entre_frases")

    # 3: + pausas na pontuacao (virgula, dois-pontos...)
    pcm, voz_anterior = [], None
    for (voz, txt), w in zip(TRECHO, wavs):
        if voz_anterior and voz != voz_anterior:
            pcm.append(tts.silencio(render.PAUSA_FALA - render.PAUSA_FRASE))
        pcm += [tts.ler_frase(w, txt), tts.silencio(render.PAUSA_FRASE)]
        voz_anterior = voz
    p3 = b"".join(pcm)
    gravar_mp3(p3, "3_pausas_entre_frases_e_na_pontuacao")

    # 4: + volume alto (a compressao atual)
    gravar_mp3(p3, "4_tudo_com_volume_alto", render.CADEIA_VOLUME)

    # 5: so o volume alto, sem pausa nenhuma na pontuacao
    gravar_mp3(p2, "5_pausas_entre_frases_com_volume_alto", render.CADEIA_VOLUME)


if __name__ == "__main__":
    main()
