# -*- coding: utf-8 -*-
"""Monta as aulas cujos roteiros estao todos prontos: voz -> slides -> MP4/MP3/SRT
e (no GitHub Actions) publica no release "aulas".

    python -m estudio.render                    # todas as prontas e ainda nao publicadas
    python -m estudio.render --aula a012        # so uma
    python -m estudio.render --local            # nao publica; deixa em saida/
    python -m estudio.render --max-minutos 300  # para de pegar aula nova depois disso
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata

from . import slides as sl
from . import tts
from . import questoes as Q
from .formato import validar

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "saida")
CACHE = os.path.join(RAIZ, ".cache_tts")
TAG = "aulas"
VERSAO = 3          # suba quando mudar o visual: as aulas publicadas antes sao refeitas

# Pausas pensadas para quem ouve absorver (referencia medida: sustentacao oral
# humana, 127 palavras/min e uma pausa a cada ~3 s; aqui, mais calmo ainda).
PAUSA_FRASE = 1.3        # depois de cada frase
PAUSA_PERGUNTA = 1.6     # depois de frase com "?"
PAUSA_FALA = 2.0         # troca de voz
PAUSA_SLIDE = 3.3        # troca de slide
PAUSA_PENSAR = 5.0       # quando a fala pede para o aluno pensar
LEITURA_S = 120          # tempo de leitura de cada questao, como em simulado
AVISO_LEITURA = "Leia a questão com atenção. Você tem dois minutos."
CAPA_S = 4.0
FIM_S = 5.0
PENSAR = re.compile(r"(pausa para (você )?pensar|pense (um pouco|bem|antes)|tente responder|"
                    r"antes de (eu )?(responder|dar a resposta|ver o gabarito)|"
                    r"qual (é|seria) a (resposta|alternativa correta)|o que você (acha|marcaria)|"
                    r"faça uma pausa|pare e pense)", re.I)


def frases(texto):
    return [f.strip() for f in re.split(r"(?<=[.!?…])\s+", texto) if f.strip()]


def trechos(frase):
    """Frase partida na pontuacao interna (virgula, ponto e virgula, dois-pontos,
    travessao). Cada trecho e gerado separado e termina no proprio sinal, entao
    a voz fecha a palavra inteira com entonacao de continuacao; a pausa entra
    depois, em silencio real (cortar dentro da frase engolia o fim das palavras)."""
    partes = [p.strip() for p in re.split(r"(?<=[,;:—–])\s+", frase) if p.strip()]
    # trecho de uma palavra so ("Ora,") fica sozinho; nao ha o que juntar
    return partes or [frase]


def pausa_depois(frase, ultima_da_fala, ultima_do_slide):
    p = PAUSA_PERGUNTA if frase.rstrip().endswith("?") else PAUSA_FRASE
    if PENSAR.search(frase):
        p = max(p, PAUSA_PENSAR)
    if ultima_do_slide:
        p = max(p, PAUSA_SLIDE)
    elif ultima_da_fala:
        p = max(p, PAUSA_FALA)
    return p


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def slug(t, n=48):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^A-Za-z0-9]+", "_", t).strip("_").lower()
    return t[:n].rstrip("_")


def nome_base(aula):
    disc = re.sub(r"^(NOÇÕES DE |NOÇÕES SOBRE |DIREITO )", "", aula["disciplina"].split("—")[0].strip())
    sub = aula["disciplina"].split("—")[1].strip().split(".")[0] if "—" in aula["disciplina"] else ""
    return "A%03d_%s%s_%s" % (aula["numero"], slug(disc, 22), ("_" + slug(sub, 4)) if sub else "",
                              slug(aula["temas"][0], 40))


def ff(*args):
    r = subprocess.run(["ffmpeg", "-v", "error", "-y"] + list(args), capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError("ffmpeg: " + r.stderr[-600:])


# Volume: nivelador dinamico + compressor + limitador. Resultado medido: cerca
# de -13 LUFS com picos abaixo de -0,5 dB (as aulas antigas estavam em -16,6).
# Mais alto que isso exige compressao que abafa a voz e estoura picos (chiado).
CADEIA_VOLUME = ("dynaudnorm=f=200:g=15:p=0.95:m=30:t=0.001,"
                 "acompressor=threshold=-22dB:ratio=4:attack=2:release=80:makeup=6,"
                 "alimiter=limit=0.60:attack=1:release=40:level=0")


def normalizar(bruto, destino):
    ff("-i", bruto, "-af", CADEIA_VOLUME, "-ar", "44100", "-ac", "1", destino)


# ---------------------------------------------------------------- publicacao
def gh(*args, ok=False):
    r = subprocess.run(["gh"] + list(args), capture_output=True, text=True)
    if r.returncode and not ok:
        raise RuntimeError("gh %s: %s" % (args[0], r.stderr[-400:]))
    return r


def release_garantido():
    if gh("release", "view", TAG, ok=True).returncode:
        gh("release", "create", TAG, "--title", "Videoaulas TRT-8 (FCC)",
           "--notes", "Gerando... o índice aparece aqui conforme as aulas ficam prontas.")


PARTE = int(os.environ.get("PARTE", "0"))      # trabalho dividido entre maquinas
PARTES = int(os.environ.get("PARTES", "1"))


def indice_publicado():
    """Junta todos os indices do release (o geral e o de cada parte); para cada
    aula vale a entrada de versao mais nova."""
    tmp = tempfile.mkdtemp()
    gh("release", "download", TAG, "-p", "indice*.json", "-D", tmp, ok=True)
    junto = {}
    for nome in sorted(os.listdir(tmp)):
        with open(os.path.join(tmp, nome), encoding="utf-8") as f:
            for k, v in json.load(f).items():
                if v.get("versao", 1) >= junto.get(k, {}).get("versao", 0):
                    junto[k] = v
    return junto


def publicar(arquivos, meu_indice):
    """Sobe os arquivos da aula e o indice desta parte (cada maquina escreve so
    o seu, para nao pisar no das outras)."""
    gh("release", "upload", TAG, "--clobber", *arquivos)
    arq = os.path.join(SAIDA, "indice_parte_%d.json" % PARTE)
    with open(arq, "w", encoding="utf-8") as f:
        json.dump(meu_indice, f, ensure_ascii=False, indent=1)
    gh("release", "upload", TAG, "--clobber", arq)


def atualizar_indice_geral(plano):
    """Junta os indices das partes, publica indice.json e o texto do release."""
    release_garantido()
    indice = indice_publicado()
    os.makedirs(SAIDA, exist_ok=True)
    arq = os.path.join(SAIDA, "indice.json")
    with open(arq, "w", encoding="utf-8") as f:
        json.dump(indice, f, ensure_ascii=False, indent=1)
    notas = os.path.join(SAIDA, "notas.md")
    with open(notas, "w", encoding="utf-8") as f:
        f.write(texto_indice({k: v for k, v in indice.items() if v.get("versao", 1) >= VERSAO}, plano))
    gh("release", "upload", TAG, "--clobber", arq)
    gh("release", "edit", TAG, "--notes-file", notas)
    log("indice geral: %d aulas na versao atual" % sum(1 for v in indice.values() if v.get("versao", 1) >= VERSAO))


def texto_indice(indice, plano):
    feitas = [a for a in plano["aulas"] if a["id"] in indice]
    horas = sum(indice[a["id"]]["minutos"] for a in feitas) / 60
    linhas = ["**%d de %d aulas prontas · %.1f h de aula**\n" % (len(feitas), len(plano["aulas"]), horas),
              "Cada aula tem o vídeo (.mp4), só o áudio (.mp3) e a legenda (.srt), nos arquivos abaixo.\n",
              "| Aula | Disciplina | Temas | Duração |", "|---|---|---|---|"]
    for a in feitas:
        i = indice[a["id"]]
        linhas.append("| %02d | %s | %s | %d min |" % (
            a["numero"], a["disciplina"].replace("|", "/"),
            " · ".join(a["temas"]).replace("|", "/")[:180], round(i["minutos"])))
    return "\n".join(linhas) + "\n"


# --------------------------------------------------------------- montagem
def roteiros_da_aula(aula, segs):
    rots = []
    for sid in aula["segmentos"]:
        arq = os.path.join(RAIZ, "roteiros", sid + ".txt")
        if not os.path.exists(arq):
            return None, "falta %s" % sid
        with open(arq, encoding="utf-8") as f:
            rot, erros, _ = validar(f.read(), segs[sid])
        if erros:
            return None, "%s reprovado: %s" % (sid, erros[0])
        rots.append(rot)
    return rots, ""


def _srt(eventos, destino):
    def hms(s):
        return ("%02d:%02d:%06.3f" % (s // 3600, (s % 3600) // 60, s % 60)).replace(".", ",")
    out, n = [], 1
    for ini, fim, voz, texto in eventos:
        frases = [f for f in re.split(r"(?<=[.!?…])\s+", texto) if f.strip()]
        # junta frases curtas em legendas de ate ~120 caracteres
        blocos, buf = [], ""
        for fr in frases:
            if buf and len(buf) + len(fr) > 120:
                blocos.append(buf)
                buf = fr
            else:
                buf = (buf + " " + fr).strip()
        if buf:
            blocos.append(buf)
        total = sum(len(b) for b in blocos) or 1
        t = ini
        for b in blocos:
            dur = (fim - ini) * len(b) / total
            out.append("%d\n%s --> %s\n%s\n" % (n, hms(t), hms(t + dur), b))
            n += 1
            t += dur
    with open(destino, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


def montar(aula, rots, plano, destino_dir):
    base = nome_base(aula)
    tmp = os.path.join(SAIDA, "_tmp", aula["id"])
    os.makedirs(tmp, exist_ok=True)
    os.makedirs(destino_dir, exist_ok=True)

    pedacos = [(v, f) for r in rots for s in r["slides"] for v, t in s["falas"] for f in frases(t)]
    log("%s: %d slides, %d frases -> voz" % (aula["id"], sum(len(r["slides"]) for r in rots), len(pedacos)))
    wavs = iter(tts.sintetizar(pedacos, CACHE))

    aulas = plano["aulas"]
    prox = aulas[aula["numero"]] if aula["numero"] < len(aulas) else None
    capa = sl.capa(os.path.join(tmp, "capa.png"), aula, len(aulas))
    fim = sl.capa(os.path.join(tmp, "fim.png"), aula, len(aulas), final=True, proxima=prox)

    total_slides = sum(len(r["slides"]) for r in rots)
    pcm = [tts.silencio(CAPA_S)]
    linha = [(capa, CAPA_S)]
    eventos, t, n = [], CAPA_S, 0
    imagens = {}
    segs = {x["id"]: x for x in plano["segmentos"]}
    pool = {}                                   # questoes da aula inteira (reserva)
    for sid in aula["segmentos"]:
        for num, q in Q.ler(segs[sid]["fonte"]).items():
            pool.setdefault(num, q)
    telas_q = {}

    def tela_questao(sid, num):
        """imagens da questao num (texto integral), ou None se nao achar."""
        q = Q.ler(segs[sid]["fonte"]).get(num) or pool.get(num)
        if not q:
            return None
        if (sid, num) not in telas_q:
            telas_q[(sid, num)] = sl.questao(os.path.join(tmp, "q_%s_%02d" % (sid, num)),
                                             aula["disciplina"], aula["numero"], num, q)
        return telas_q[(sid, num)]

    aviso_wav = tts.sintetizar([("FRANCISCA", AVISO_LEITURA)], CACHE)[0]
    lidas = set()

    def bloco_de_leitura(sid, num):
        """aviso falado + 2 min com a questao na tela e cronometro + bipe."""
        nonlocal t
        tela = tela_questao(sid, num)[0]
        aviso = tts.ler_frase(aviso_wav, AVISO_LEITURA)
        dur = len(aviso) / 2 / tts.TAXA
        pcm.extend([aviso, tts.silencio(0.8)])
        linha.append((tela, dur + 0.8))
        eventos.append((t, t + dur, "FRANCISCA", AVISO_LEITURA))
        t += dur + 0.8
        for seg in range(LEITURA_S, 0, -1):
            img = sl.com_cronometro(tela, os.path.join(tmp, "q_%s_%02d_t%03d.png" % (sid, num, seg)), seg, LEITURA_S)
            linha.append((img, 1.0))
        pcm.append(tts.silencio(LEITURA_S))
        eventos.append((t, t + 3.0, "", "Tempo de leitura: dois minutos."))
        t += LEITURA_S
        bip = tts.bipe()
        pcm.extend([bip, tts.silencio(1.2)])
        linha.append((tela, len(bip) / 2 / tts.TAXA + 1.2))
        t += len(bip) / 2 / tts.TAXA + 1.2

    for r in rots:
        sid = r["segmento"]
        for s in r["slides"]:
            n += 1
            imagens[n] = sl.slide(os.path.join(tmp, "s%03d.png" % n), aula["disciplina"], aula["numero"],
                                  s["titulo"], s["topicos"], n, total_slides)
            nums = [x for x in Q.numeros_do_titulo(s["titulo"]) if tela_questao(sid, x)]
            atual = nums[0] if nums else None
            for k, (voz, texto) in enumerate(s["falas"]):
                citada = Q.numero_citado(texto)
                if nums and citada and tela_questao(sid, citada):
                    atual = citada
                tela = imagens[n]
                if atual and (sid, atual) not in lidas:
                    lidas.add((sid, atual))
                    bloco_de_leitura(sid, atual)
                if atual:
                    paginas = tela_questao(sid, atual)
                    tela = paginas[1] if len(paginas) > 1 and re.search(r"alternativa|letra [a-e]\b", texto, re.I) else paginas[0]
                fs = frases(texto)
                for j, fr in enumerate(fs):
                    # frase inteira: so assim a voz mantem a entonacao de continuacao
                    # na virgula (gerada em pedacos, ela baixa o tom em cada virgula)
                    audio = tts.ler_frase(next(wavs), fr)
                    ult_fala = j == len(fs) - 1
                    pausa = pausa_depois(fr, ult_fala, ult_fala and k == len(s["falas"]) - 1)
                    dur = len(audio) / 2 / tts.TAXA
                    pcm += [audio, tts.silencio(pausa)]
                    linha.append((tela, dur + pausa))
                    eventos.append((t, t + dur, voz, fr))
                    t += dur + pausa
    pcm.append(tts.silencio(FIM_S))
    linha.append((fim, FIM_S))

    bruto = os.path.join(tmp, "bruto.wav")
    tts.gravar_wav(b"".join(pcm), bruto)
    norm = os.path.join(tmp, "norm.wav")
    normalizar(bruto, norm)

    lista = os.path.join(tmp, "imagens.txt")
    with open(lista, "w", encoding="utf-8") as f:
        for img, dur in linha:
            f.write("file '%s'\nduration %.4f\n" % (os.path.abspath(img).replace("\\", "/"), dur))
        f.write("file '%s'\n" % os.path.abspath(linha[-1][0]).replace("\\", "/"))

    mp4 = os.path.join(destino_dir, base + ".mp4")
    mp3 = os.path.join(destino_dir, base + ".mp3")
    srt = os.path.join(destino_dir, base + ".srt")
    log("%s: video (%.1f min)" % (aula["id"], t / 60))
    ff("-f", "concat", "-safe", "0", "-i", lista, "-i", norm,
       "-c:v", "libx264", "-preset", "veryfast", "-tune", "stillimage", "-crf", "27",
       "-r", "4", "-g", "480", "-pix_fmt", "yuv420p",
       "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", "-shortest", mp4)
    ff("-i", norm, "-c:a", "libmp3lame", "-b:a", "96k", "-ac", "1", mp3)
    _srt(eventos, srt)
    shutil.rmtree(tmp, ignore_errors=True)
    return [mp4, mp3, srt], (t + FIM_S) / 60


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aula")
    ap.add_argument("--local", action="store_true")
    ap.add_argument("--max-minutos", type=float, default=300)
    ap.add_argument("--indice", action="store_true", help="so junta os indices e atualiza o release")
    a = ap.parse_args()
    inicio = time.time()

    with open(os.path.join(RAIZ, "plano", "plano.json"), encoding="utf-8") as f:
        plano = json.load(f)
    segs = {s["id"]: s for s in plano["segmentos"]}

    if a.indice:
        atualizar_indice_geral(plano)
        return

    meu_indice = {}
    if a.local:
        arq = os.path.join(SAIDA, "indice.json")
        indice = json.load(open(arq, encoding="utf-8")) if os.path.exists(arq) else {}
    else:
        release_garantido()
        indice = indice_publicado()
        da_parte = {x["id"] for x in plano["aulas"] if (x["numero"] - 1) % PARTES == PARTE}
        meu_indice = {k: v for k, v in indice.items() if k in da_parte}

    feitas, pendencias = 0, []
    for aula in plano["aulas"]:
        if a.aula and aula["id"] != a.aula:
            continue
        if not a.aula and (aula["numero"] - 1) % PARTES != PARTE:
            continue
        if indice.get(aula["id"], {}).get("versao", 1) >= VERSAO and not a.aula:
            continue
        rots, motivo = roteiros_da_aula(aula, segs)
        if rots is None:
            if "reprovado" in motivo:
                pendencias.append("%s: %s" % (aula["id"], motivo))
            continue
        if (time.time() - inicio) / 60 > a.max_minutos:
            log("tempo esgotado; o resto fica para a próxima execução")
            break
        try:
            arquivos, minutos = montar(aula, rots, plano, SAIDA)
        except Exception as e:
            log("FALHOU %s: %s" % (aula["id"], e))
            pendencias.append("%s: %s" % (aula["id"], str(e)[:200]))
            continue
        indice[aula["id"]] = {"arquivo": os.path.basename(arquivos[0]), "minutos": round(minutos, 1),
                              "versao": VERSAO}
        meu_indice[aula["id"]] = indice[aula["id"]]
        if a.local:
            with open(os.path.join(SAIDA, "indice.json"), "w", encoding="utf-8") as f:
                json.dump(indice, f, ensure_ascii=False, indent=1)
        else:
            publicar(arquivos, meu_indice)
            for x in arquivos:
                os.remove(x)
        feitas += 1
        log("PRONTA %s (%.1f min)" % (aula["id"], minutos))

    horas = sum(v["minutos"] for v in indice.values()) / 60
    log("nesta execução: %d aulas | publicadas no total: %d de %d (%.1f h)" % (
        feitas, len(indice), len(plano["aulas"]), horas))
    for p in pendencias:
        log("PENDÊNCIA " + p)
    if pendencias and not feitas:
        sys.exit(1)


if __name__ == "__main__":
    main()
