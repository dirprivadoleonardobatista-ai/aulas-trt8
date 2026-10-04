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
from .formato import validar, VOZES

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAIDA = os.path.join(RAIZ, "saida")
CACHE = os.path.join(RAIZ, ".cache_tts")
TAG = "aulas"

PAUSA_FALA = 0.35
PAUSA_SLIDE = 0.8
CAPA_S = 3.5
FIM_S = 4.0


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


def indice_publicado():
    tmp = tempfile.mkdtemp()
    r = gh("release", "download", TAG, "-p", "indice.json", "-D", tmp, ok=True)
    arq = os.path.join(tmp, "indice.json")
    if r.returncode or not os.path.exists(arq):
        return {}
    with open(arq, encoding="utf-8") as f:
        return json.load(f)


def publicar(arquivos, indice, plano):
    gh("release", "upload", TAG, "--clobber", *arquivos)
    arq = os.path.join(SAIDA, "indice.json")
    with open(arq, "w", encoding="utf-8") as f:
        json.dump(indice, f, ensure_ascii=False, indent=1)
    notas = os.path.join(SAIDA, "notas.md")
    with open(notas, "w", encoding="utf-8") as f:
        f.write(texto_indice(indice, plano))
    gh("release", "upload", TAG, "--clobber", arq)
    gh("release", "edit", TAG, "--notes-file", notas)


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
            out.append("%d\n%s --> %s\n%s: %s\n" % (n, hms(t), hms(t + dur), VOZES[voz]["nome"], b))
            n += 1
            t += dur
    with open(destino, "w", encoding="utf-8") as f:
        f.write("\n".join(out))


def montar(aula, rots, plano, destino_dir):
    base = nome_base(aula)
    tmp = os.path.join(SAIDA, "_tmp", aula["id"])
    os.makedirs(tmp, exist_ok=True)
    os.makedirs(destino_dir, exist_ok=True)

    falas = [(v, t) for r in rots for s in r["slides"] for v, t in s["falas"]]
    log("%s: %d slides, %d falas -> voz" % (aula["id"], sum(len(r["slides"]) for r in rots), len(falas)))
    wavs = iter(tts.sintetizar(falas, CACHE))

    aulas = plano["aulas"]
    prox = aulas[aula["numero"]] if aula["numero"] < len(aulas) else None
    capa = sl.capa(os.path.join(tmp, "capa.png"), aula, len(aulas))
    fim = sl.capa(os.path.join(tmp, "fim.png"), aula, len(aulas), final=True, proxima=prox)

    total_slides = sum(len(r["slides"]) for r in rots)
    pcm = [tts.silencio(CAPA_S)]
    linha = [(capa, CAPA_S)]
    eventos, t, n = [], CAPA_S, 0
    imagens = {}
    for r in rots:
        for s in r["slides"]:
            n += 1
            for k, (voz, texto) in enumerate(s["falas"]):
                chave = (n, voz)
                if chave not in imagens:
                    imagens[chave] = sl.slide(os.path.join(tmp, "s%03d_%s.png" % (n, voz[:3])),
                                              aula["disciplina"], aula["numero"], s["titulo"],
                                              s["topicos"], voz, n, total_slides)
                audio = tts.ler_pcm(next(wavs))
                pausa = PAUSA_SLIDE if k == len(s["falas"]) - 1 else PAUSA_FALA
                dur = len(audio) / 2 / tts.TAXA
                pcm += [audio, tts.silencio(pausa)]
                linha.append((imagens[chave], dur + pausa))
                eventos.append((t, t + dur, voz, texto))
                t += dur + pausa
    pcm.append(tts.silencio(FIM_S))
    linha.append((fim, FIM_S))

    bruto = os.path.join(tmp, "bruto.wav")
    tts.gravar_wav(b"".join(pcm), bruto)
    norm = os.path.join(tmp, "norm.wav")
    ff("-i", bruto, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100", "-ac", "1", norm)

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
       "-c:a", "aac", "-b:a", "80k", "-movflags", "+faststart", "-shortest", mp4)
    ff("-i", norm, "-c:a", "libmp3lame", "-b:a", "64k", "-ac", "1", mp3)
    _srt(eventos, srt)
    shutil.rmtree(tmp, ignore_errors=True)
    return [mp4, mp3, srt], (t + FIM_S) / 60


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--aula")
    ap.add_argument("--local", action="store_true")
    ap.add_argument("--max-minutos", type=float, default=300)
    a = ap.parse_args()
    inicio = time.time()

    with open(os.path.join(RAIZ, "plano", "plano.json"), encoding="utf-8") as f:
        plano = json.load(f)
    segs = {s["id"]: s for s in plano["segmentos"]}

    if a.local:
        arq = os.path.join(SAIDA, "indice.json")
        indice = json.load(open(arq, encoding="utf-8")) if os.path.exists(arq) else {}
    else:
        release_garantido()
        indice = indice_publicado()

    feitas, pendencias = 0, []
    for aula in plano["aulas"]:
        if a.aula and aula["id"] != a.aula:
            continue
        if aula["id"] in indice and not a.aula:
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
        indice[aula["id"]] = {"arquivo": os.path.basename(arquivos[0]), "minutos": round(minutos, 1)}
        if a.local:
            with open(os.path.join(SAIDA, "indice.json"), "w", encoding="utf-8") as f:
                json.dump(indice, f, ensure_ascii=False, indent=1)
        else:
            publicar(arquivos, indice, plano)
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
