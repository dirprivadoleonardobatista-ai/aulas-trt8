# -*- coding: utf-8 -*-
"""Formato do roteiro (roteiros/sNNN.txt): leitura e validacao. So stdlib.

    SEGMENTO s012
    == SLIDE: Eficacia contida x limitada
    * Contida: nasce pronta; a lei pode restringir
    * Limitada: depende de lei para produzir efeitos
    ANTONIO: texto falado...
    THALITA: texto falado...
    == SLIDE: ...

Texto puro gasta menos tokens que JSON e nao tem problema de aspas.
"""
import re

VOZES = {
    "FRANCISCA": {"nome": "Francisca", "papel": "professora"},
    "THALITA": {"nome": "Thalita", "papel": "professora e especialista FCC"},
}

PEDIR_A_MAIS = 1.2                        # meta mostrada ao roteirista (ele entrega ~85% do pedido)
FAIXA_MIN, FAIXA_MAX = 0.90, 1.50        # aceito, sobre a meta do plano
MAX_PARTICIPACAO = 0.70                   # nenhuma voz passa disto
MIN_PARTICIPACAO = 0.10                   # (estrito) toda voz chega a isto
PALAVRAS_POR_SLIDE_MAX = 420              # (estrito) mais que isso pede outro slide
FALA_MAX_CHARS = 900

PROIBIDOS = [
    (r"§", "use 'parágrafo' por extenso"),
    (r"\b[Aa]rts?\.", "escreva 'artigo' por extenso"),
    (r"\b[Ii]ncs?\.", "escreva 'inciso' por extenso"),
    (r"\b[Nn]º", "escreva 'número' por extenso"),
    (r"[ºª°]", "escreva o ordinal por extenso (quinto, primeira)"),
    (r"\b[IVX]{2,}\b", "algarismo romano: escreva por extenso (inciso treze)"),
    (r"[\[\]*#|_`<>{}]", "sem marcação, colchetes ou símbolos na fala"),
    (r"\((risos|pausa|rindo|suspira)", "sem rubricas de cena"),
    (r"\b(aprox|ex|obs|p\.ex)\.", "sem abreviações na fala"),
]


def palavras(t):
    return len(re.findall(r"\w+", t))


def ler(texto):
    """-> dict {segmento, slides:[{titulo, topicos, falas:[(VOZ, texto)]}]} e lista de erros de sintaxe."""
    seg, slides, erros = None, [], []
    for n, bruta in enumerate(texto.splitlines(), 1):
        linha = bruta.strip()
        if not linha:
            continue
        if linha.upper().startswith("SEGMENTO "):
            seg = linha.split()[1].strip().lower()
        elif linha.startswith("== SLIDE:"):
            slides.append({"titulo": linha[len("== SLIDE:"):].strip(), "topicos": [], "falas": []})
        elif linha.startswith("* "):
            if not slides:
                erros.append("linha %d: tópico antes do primeiro '== SLIDE:'" % n)
                continue
            slides[-1]["topicos"].append(linha[2:].strip())
        else:
            m = re.match(r"^([A-ZÀ-Ú]+)\s*:\s*(.+)$", linha)
            if not m or m.group(1).upper() not in VOZES:
                erros.append("linha %d: não reconheci (%s). Use '== SLIDE:', '* tópico' ou "
                             "FRANCISCA:/THALITA:" % (n, linha[:50]))
                continue
            if not slides:
                erros.append("linha %d: fala antes do primeiro '== SLIDE:'" % n)
                continue
            slides[-1]["falas"].append((m.group(1).upper(), m.group(2).strip()))
    return {"segmento": seg, "slides": slides}, erros


def validar(texto, seg_plano, estrito=False):
    """-> (roteiro, erros, resumo). erros vazio = aprovado.
    estrito: regras de qualidade cobradas so de quem escreve (o roteirista);
    a integracao e a montagem aceitam roteiros antigos sem elas."""
    rot, erros = ler(texto)
    sid = seg_plano["id"]
    if rot["segmento"] != sid:
        erros.append("a primeira linha deve ser 'SEGMENTO %s'" % sid)
    slides = rot["slides"]
    if not slides:
        erros.append("nenhum slide")
        return rot, erros, ""

    por_voz = {v: 0 for v in VOZES}
    total, anterior = 0, None
    for i, s in enumerate(slides, 1):
        if not s["titulo"] or len(s["titulo"]) > 80:
            erros.append("slide %d: título vazio ou com mais de 80 caracteres" % i)
        if not 2 <= len(s["topicos"]) <= 6:
            erros.append("slide %d: precisa de 2 a 6 tópicos (tem %d)" % (i, len(s["topicos"])))
        for t in s["topicos"]:
            if len(t) > 110:
                erros.append("slide %d: tópico com mais de 110 caracteres: %s..." % (i, t[:40]))
        if len(s["falas"]) < 3:
            erros.append("slide %d: precisa de pelo menos 3 falas" % i)
        for voz, fala in s["falas"]:
            if voz == anterior:
                erros.append("slide %d: %s fala duas vezes seguidas; alterne as vozes" % (i, voz))
            anterior = voz
            if len(fala) > FALA_MAX_CHARS:
                erros.append("slide %d: fala de %s longa demais (%d caracteres; máx. %d)"
                             % (i, voz, len(fala), FALA_MAX_CHARS))
            for padrao, dica in PROIBIDOS:
                m = re.search(padrao, fala)
                if m:
                    erros.append("slide %d, fala de %s: '%s' -> %s" % (i, voz, m.group(0), dica))
                    break
            n = palavras(fala)
            por_voz[voz] += n
            total += n

    meta = seg_plano["meta_palavras"]
    lo, hi = int(meta * FAIXA_MIN), int(meta * FAIXA_MAX)
    if total < lo:
        erros.append("narração com %d palavras; faltam %d para o mínimo de %d. Acrescente de uma vez "
                     "um slide novo (exemplo, pegadinha ou questão) com %d palavras ou mais"
                     % (total, lo - total, lo, lo - total + 60))
    elif total > hi:
        erros.append("narração com %d palavras; o máximo é %d. Corte repetições" % (total, hi))
    minimo_vozes = 2
    presentes = [v for v, n in por_voz.items() if n > 0]
    if len(presentes) < minimo_vozes:
        erros.append("só %d voz participou; use as duas" % len(presentes))
    if estrito and meta >= 900:
        for v, n in por_voz.items():
            if total and n / total < MIN_PARTICIPACAO:
                erros.append("%s tem só %.0f%% das palavras (mín. %.0f%%): dê mais falas a ela/ele"
                             % (v, 100 * n / total, 100 * MIN_PARTICIPACAO))
        precisa = max(2, round(total / PALAVRAS_POR_SLIDE_MAX))
        if len(slides) < precisa:
            erros.append("só %d slides para %d palavras: divida em pelo menos %d slides"
                         % (len(slides), total, precisa))
    for v, n in por_voz.items():
        if total and n / total > MAX_PARTICIPACAO:
            erros.append("%s tem %.0f%% das palavras (máx. %.0f%%)" % (v, 100 * n / total, 100 * MAX_PARTICIPACAO))

    resumo = "%d slides, %d falas, %d palavras (meta %d) | %s" % (
        len(slides), sum(len(s["falas"]) for s in slides), total, meta,
        ", ".join("%s %d%%" % (v[:3], round(100 * n / total)) for v, n in por_voz.items()) if total else "-")
    # repete erros iguais so uma vez
    vistos, unicos = set(), []
    for e in erros:
        if e not in vistos:
            vistos.add(e)
            unicos.append(e)
    return rot, unicos, resumo
