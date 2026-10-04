# -*- coding: utf-8 -*-
"""Divide a apostila (partes/*.md) em SEGMENTOS e AULAS e grava plano/plano.json.

Segmento = unidade que o roteirista escreve de uma vez (uma secao "##" da
apostila, partida nos "###" se for grande ou juntada com a vizinha se for
pequena). Aula = segmentos seguidos da mesma disciplina, ~35 min, um MP4.

A meta de palavras de cada segmento e proporcional ao tamanho do trecho, de
modo que a soma feche HORAS_ALVO de narracao.

Uso:  python -m estudio.plano
"""
import glob
import json
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

HORAS_ALVO = 41.5            # pedido: 40 h; folga para o piso de 93% do validador
PALAVRAS_POR_MINUTO = 150    # medido na aula 1 renderizada (so a fala, sem pausas)
PAUSA_POR_FALA_S = 0.35      # silencio entre falas, ja descontado da meta
PALAVRAS_POR_FALA = 42       # media esperada, so para descontar as pausas

SEG_MIN, SEG_MAX = 900, 2300         # palavras da fonte por segmento
META_MIN, META_MAX = 700, 2600       # palavras de narracao por segmento
MINUTOS_POR_AULA = 35


def limpar(texto):
    """Texto como sera lido, para contar palavras."""
    t = re.sub(r"^\s*\|?\s*:?-{3,}.*$", " ", texto, flags=re.M)   # linha separadora de tabela
    t = re.sub(r"[|*#>`★]", " ", t)
    t = re.sub(r"\[(SINTESE|ATENCAO|DICA|EXEMPLO|JURIS|PROVA|APROFUNDANDO)\]", " ", t)
    return t


def palavras(texto):
    return len(re.findall(r"\w+", limpar(texto)))


def _disciplina(prefixo, primeiro_arquivo):
    with open(primeiro_arquivo, encoding="utf-8") as f:
        for linha in f:
            if linha.startswith("# "):
                return linha[2:].strip()
    return prefixo


def _secoes_h2(texto):
    """[(titulo, corpo)] cortando nos '## '. O que vem antes do 1o '##' (H1,
    introducao) vai como secao de titulo ''."""
    partes, titulo, buf = [], "", []
    for linha in texto.splitlines():
        if linha.startswith("## "):
            if "".join(buf).strip():
                partes.append((titulo, "\n".join(buf).strip()))
            titulo, buf = linha[3:].strip(), [linha]
        elif linha.startswith("# "):
            continue                                # H1 vira nome da disciplina
        else:
            buf.append(linha)
    if "".join(buf).strip():
        partes.append((titulo, "\n".join(buf).strip()))
    return partes


def _partir(titulo, corpo):
    """Secao grande demais: corta nos '###' (ou em paragrafos), em pedacos
    de ate SEG_MAX palavras."""
    if palavras(corpo) <= SEG_MAX:
        return [(titulo, corpo)]
    blocos, buf = [], []
    for linha in corpo.splitlines():
        if linha.startswith("### ") and buf:
            blocos.append("\n".join(buf))
            buf = []
        buf.append(linha)
    blocos.append("\n".join(buf))
    if len(blocos) == 1:                          # sem ###: corta por paragrafo
        blocos = [b for b in re.split(r"\n\s*\n", corpo) if b.strip()]

    pedacos, atual = [], []
    for b in blocos:
        if atual and palavras("\n\n".join(atual + [b])) > SEG_MAX:
            pedacos.append("\n\n".join(atual))
            atual = []
        atual.append(b)
    if atual:
        pedacos.append("\n\n".join(atual))
    n = len(pedacos)
    return [("%s (parte %d de %d)" % (titulo, i, n) if n > 1 else titulo, p)
            for i, p in enumerate(pedacos, 1)]


def _juntar(secoes):
    """Junta secoes vizinhas pequenas ate SEG_MIN."""
    saida = []
    for titulo, corpo in secoes:
        if saida and (palavras(saida[-1][1]) < SEG_MIN or palavras(corpo) < SEG_MIN * 0.5) \
                and palavras(saida[-1][1]) + palavras(corpo) <= SEG_MAX:
            t0, c0 = saida[-1]
            titulo_novo = " · ".join(x for x in (t0, titulo) if x)
            saida[-1] = (titulo_novo, c0 + "\n\n" + corpo)
        else:
            saida.append((titulo, corpo))
    return saida


def _limpar_titulo(t):
    def um(x):
        return re.sub(r"^\d+(\.\d+)*\.?\s*", "", x).replace("★", "").strip()
    t = " · ".join(filter(None, (um(x) for x in (t or "").split(" · "))))
    return t or "Introdução"


def montar():
    arquivos = sorted(glob.glob(os.path.join(RAIZ, "partes", "*.md")))
    por_disc = {}
    for a in arquivos:
        por_disc.setdefault(os.path.basename(a)[:2], []).append(a)

    disciplinas = []
    for pref in sorted(por_disc):
        nome = _disciplina(pref, por_disc[pref][0])
        secoes = []
        for a in por_disc[pref]:
            with open(a, encoding="utf-8") as f:
                for titulo, corpo in _secoes_h2(f.read()):
                    secoes.extend(_partir(titulo, corpo))
        disciplinas.append((pref, nome, _juntar(secoes)))

    total_fonte = sum(palavras(c) for _, _, ss in disciplinas for _, c in ss)
    n_seg = sum(len(ss) for _, _, ss in disciplinas)
    minutos_uteis = HORAS_ALVO * 60 - (total_fonte * 1.1 / PALAVRAS_POR_FALA) * PAUSA_POR_FALA_S / 60
    total_meta = minutos_uteis * PALAVRAS_POR_MINUTO
    fator = total_meta / total_fonte

    segmentos, aulas = [], []
    num_seg = 0
    for pref, nome, secoes in disciplinas:
        itens = []
        for titulo, corpo in secoes:
            num_seg += 1
            meta = int(round(min(META_MAX, max(META_MIN, palavras(corpo) * fator)) / 10.0) * 10)
            itens.append({
                "id": "s%03d" % num_seg,
                "disciplina": nome,
                "titulo": _limpar_titulo(titulo),
                "fonte": corpo,
                "palavras_fonte": palavras(corpo),
                "meta_palavras": meta,
            })

        # aulas: blocos seguidos de ~MINUTOS_POR_AULA
        total_disc = sum(i["meta_palavras"] for i in itens) / PALAVRAS_POR_MINUTO
        n_aulas = max(1, int(round(total_disc / MINUTOS_POR_AULA)))
        alvo = sum(i["meta_palavras"] for i in itens) / n_aulas
        grupos, atual, acum = [], [], 0
        for i in itens:
            if atual and acum + i["meta_palavras"] / 2 > alvo and len(grupos) < n_aulas - 1:
                grupos.append(atual)
                atual, acum = [], 0
            atual.append(i)
            acum += i["meta_palavras"]
        grupos.append(atual)

        for n, g in enumerate(grupos, 1):
            aid = "a%03d" % (len(aulas) + 1)
            titulos = [x["titulo"] for x in g]
            aulas.append({
                "id": aid,
                "numero": len(aulas) + 1,
                "disciplina": nome,
                "parte": n, "partes": len(grupos),
                "titulo": titulos[0] if len(titulos) == 1 else "%s e mais %d tema%s" % (
                    titulos[0], len(titulos) - 1, "s" if len(titulos) > 2 else ""),
                "temas": titulos,
                "segmentos": [x["id"] for x in g],
                "minutos_previstos": round(sum(x["meta_palavras"] for x in g) / PALAVRAS_POR_MINUTO, 1),
            })
            for k, x in enumerate(g):
                x["aula"] = aid
                x["posicao"] = ("unico" if len(g) == 1 else
                                "abertura" if k == 0 else
                                "fechamento" if k == len(g) - 1 else "meio")
                x["anterior"] = g[k - 1]["titulo"] if k > 0 else ""
                x["seguinte"] = g[k + 1]["titulo"] if k < len(g) - 1 else ""
                segmentos.append(x)

    plano = {
        "horas_alvo": HORAS_ALVO,
        "palavras_por_minuto": PALAVRAS_POR_MINUTO,
        "fator_expansao": round(fator, 3),
        "palavras_fonte": total_fonte,
        "palavras_meta": sum(s["meta_palavras"] for s in segmentos),
        "aulas": aulas,
        "segmentos": segmentos,
    }
    os.makedirs(os.path.join(RAIZ, "plano"), exist_ok=True)
    with open(os.path.join(RAIZ, "plano", "plano.json"), "w", encoding="utf-8") as f:
        json.dump(plano, f, ensure_ascii=False, indent=1)
    return plano


if __name__ == "__main__":
    p = montar()
    print("segmentos: %d | aulas: %d | fonte: %d palavras | meta: %d palavras (fator %.2f)" % (
        len(p["segmentos"]), len(p["aulas"]), p["palavras_fonte"], p["palavras_meta"], p["fator_expansao"]))
    print("horas previstas: %.1f" % (sum(a["minutos_previstos"] for a in p["aulas"]) / 60))
    tam = sorted(s["palavras_fonte"] for s in p["segmentos"])
    print("fonte por segmento: min %d, mediana %d, max %d" % (tam[0], tam[len(tam) // 2], tam[-1]))
    mins = sorted(a["minutos_previstos"] for a in p["aulas"])
    print("minutos por aula: min %.0f, mediana %.0f, max %.0f" % (mins[0], mins[len(mins) // 2], mins[-1]))
