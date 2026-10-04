# -*- coding: utf-8 -*-
"""Slides em PNG (Pillow). Sem avatar e sem identificar quem fala: so titulo
e topicos."""
import os

from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1280, 720

FUNDO = "#F5F7FB"
AZUL_ESCURO = "#13294B"
AZUL = "#2E86C1"
TEXTO = "#1E2533"
CINZA = "#8A94A6"
RODAPE = "Legislação Estruturada · TRT-8 · FCC"

_fontes = {}


def fonte(tam, peso="Regular"):
    k = (tam, peso)
    if k not in _fontes:
        _fontes[k] = ImageFont.truetype(os.path.join(RAIZ, "fontes", "Inter-%s.ttf" % peso), tam)
    return _fontes[k]


_logo = None


def logo(alt):
    global _logo
    if _logo is None:
        _logo = Image.open(os.path.join(RAIZ, "marca", "logo_le.png")).convert("RGBA")
    w = int(_logo.width * alt / _logo.height)
    return _logo.resize((w, alt), Image.LANCZOS)


def quebrar(d, texto, f, largura):
    linhas, atual = [], ""
    for p in texto.split():
        teste = (atual + " " + p).strip()
        if d.textlength(teste, font=f) <= largura:
            atual = teste
        else:
            if atual:
                linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    return linhas


def _cabecalho(img, d, disciplina, aula_num):
    d.rectangle([0, 0, W, 62], fill=AZUL_ESCURO)
    f = fonte(19, "SemiBold")
    txt = disciplina.upper()
    if d.textlength(txt, font=f) > W - 260:
        while d.textlength(txt + "…", font=f) > W - 260 and len(txt) > 10:
            txt = txt[:-1]
        txt = txt.rstrip(" —-·") + "…"
    d.text((40, 20), txt, font=f, fill="white")
    marca = "AULA %02d" % aula_num
    fm = fonte(19, "Bold")
    d.text((W - 40 - d.textlength(marca, font=fm), 20), marca, font=fm, fill="#9CC9EA")


def _rodape(d, num, total):
    f = fonte(14)
    d.text((40, H - 34), RODAPE, font=f, fill=CINZA)
    if total:
        m = "%d / %d" % (num, total)
        d.text((W - 40 - d.textlength(m, font=f), H - 34), m, font=f, fill=CINZA)


def slide(destino, disciplina, aula_num, titulo, topicos, num, total):
    img = Image.new("RGB", (W, H), FUNDO)
    d = ImageDraw.Draw(img)
    _cabecalho(img, d, disciplina, aula_num)

    x, larg = 60, W - 120
    ft = fonte(38, "Bold")
    linhas = quebrar(d, titulo, ft, larg)
    if len(linhas) > 2:
        ft = fonte(32, "Bold")
        linhas = quebrar(d, titulo, ft, larg)[:2]
    y = 92
    for l in linhas:
        d.text((x, y), l, font=ft, fill=AZUL_ESCURO)
        y += int(ft.size * 1.22)
    y += 10
    d.rectangle([x, y, x + 110, y + 5], fill=AZUL)
    y += 32

    limite = H - 60
    for tam in (30, 28, 26, 24, 22, 20):
        f = fonte(tam)
        blocos = [quebrar(d, t, f, larg - 44) for t in topicos]
        alt = sum(len(b) * int(tam * 1.32) + int(tam * 0.75) for b in blocos)
        if y + alt <= limite:
            break
    for b in blocos:
        if y + int(f.size * 1.32) > limite:
            break
        cy = y + int(f.size * 0.42)
        d.rounded_rectangle([x + 2, cy, x + 14, cy + 12], radius=3, fill=AZUL)
        for l in b:
            if y + int(f.size * 1.32) > limite:
                break
            d.text((x + 36, y), l, font=f, fill=TEXTO)
            y += int(f.size * 1.32)
        y += int(f.size * 0.75)

    _rodape(d, num, total)
    img.save(destino, optimize=True)
    return destino


def capa(destino, aula, total_aulas, final=False, proxima=None):
    img = Image.new("RGB", (W, H), AZUL_ESCURO)
    d = ImageDraw.Draw(img)
    lg = logo(112)
    cx, cy, r = W - 60 - 70, 50 + 70, 74
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill="white")
    img.paste(lg, (cx - lg.width // 2, cy - lg.height // 2), lg)
    d.rectangle([0, H - 10, W, H], fill=AZUL)

    x, larg = 70, W - 140
    d.text((x, 70), ("FIM DA AULA %02d" if final else "AULA %02d") % aula["numero"]
           + ("" if final else "  ·  de %d" % total_aulas), font=fonte(22, "Bold"), fill="#9CC9EA")
    y = 120
    for l in quebrar(d, aula["disciplina"].upper(), fonte(24, "SemiBold"), larg - 180)[:3]:
        d.text((x, y), l, font=fonte(24, "SemiBold"), fill="#C9D6EA")
        y += 34
    y += 24
    if final:
        titulo = "Revise os pontos de prova e siga para a próxima aula."
        ft = fonte(40, "Bold")
        for l in quebrar(d, titulo, ft, larg)[:3]:
            d.text((x, y), l, font=ft, fill="white")
            y += 52
        if proxima:
            y += 30
            d.text((x, y), "A SEGUIR", font=fonte(18, "Bold"), fill="#9CC9EA")
            y += 32
            for l in quebrar(d, "Aula %02d — %s" % (proxima["numero"], proxima["temas"][0]),
                             fonte(26), larg)[:2]:
                d.text((x, y), l, font=fonte(26), fill="white")
                y += 36
    else:
        temas = aula["temas"]
        ft = fonte(44 if len(temas) <= 2 else 36, "Bold")
        for l in quebrar(d, temas[0], ft, larg)[:2]:
            d.text((x, y), l, font=ft, fill="white")
            y += int(ft.size * 1.2)
        y += 20
        for t in temas[1:7]:
            for i, l in enumerate(quebrar(d, t, fonte(24), larg - 30)[:2]):
                if i == 0:
                    d.rounded_rectangle([x, y + 10, x + 10, y + 20], radius=2, fill=AZUL)
                d.text((x + 28, y), l, font=fonte(24), fill="#E3EAF5")
                y += 32
            y += 6
            if y > H - 90:
                break
    d.text((x, H - 50), RODAPE, font=fonte(16), fill="#9CC9EA")
    img.save(destino, optimize=True)
    return destino
