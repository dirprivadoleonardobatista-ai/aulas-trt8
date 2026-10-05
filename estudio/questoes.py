# -*- coding: utf-8 -*-
"""Questoes da apostila: leitura do texto integral (enunciado e alternativas)
e identificacao de qual questao o roteiro esta comentando, para mostrar o
texto completo na tela."""
import re

_UNIDADES = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
             "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete",
             "dezoito", "dezenove"]
_DEZENAS = {20: "vinte", 30: "trinta", 40: "quarenta"}


def _por_extenso():
    m = {}
    for i, w in enumerate(_UNIDADES):
        m[w] = i
    m["quatorze"] = 14
    m["uma"] = 1
    for d, w in _DEZENAS.items():
        m[w] = d
        for u in range(1, 10):
            m["%s e %s" % (w, _UNIDADES[u])] = d + u
    return m


EXTENSO = _por_extenso()
_NUM = r"(\d{1,2}|" + "|".join(sorted((re.escape(k) for k in EXTENSO), key=len, reverse=True)) + r")"


def _valor(tok):
    tok = tok.lower()
    return int(tok) if tok.isdigit() else EXTENSO.get(tok)


def numeros_do_titulo(titulo):
    """'Questões dez a treze' -> [10, 11, 12, 13]; 'Questões 1 e 2' -> [1, 2].
    So conta numeros que vem depois de 'questão/questões' ou 'Q'."""
    m = re.search(r"\b(quest(?:ão|ões|ao|oes)|Q)\s*" + _NUM + r"((?:\s*(?:,|e|a|até)\s*" + _NUM + r")*)",
                  titulo, re.I)
    if not m:
        return []
    trecho = titulo[m.start(2):m.end()]
    toks = re.findall(_NUM + r"|\b(a|até)\b", trecho, re.I)
    nums, faixa = [], False
    for num, sep in toks:
        if sep:
            faixa = True
            continue
        v = _valor(num)
        if v is None:
            continue
        if faixa and nums and v > nums[-1]:
            nums += list(range(nums[-1] + 1, v + 1))
        else:
            nums.append(v)
        faixa = False
    return nums


def numero_citado(fala):
    """Numero da questao citada na fala ('Vamos à questão sete'), ou None."""
    m = re.search(r"\bquest(?:ão|ao)\s+(?:número\s+)?" + _NUM + r"\b", fala, re.I)
    return _valor(m.group(1)) if m else None


def _limpar(t):
    t = re.sub(r"\*\*|__|`", "", t)
    t = re.sub(r"^>+\s*", "", t)
    return t.strip()


def ler(fonte):
    """{numero: {"cabecalho", "enunciado": [paragrafos], "alternativas": [(letra, texto)]}}"""
    saida = {}
    blocos = re.split(r"^###\s+Questão\s+", fonte, flags=re.M)
    for b in blocos[1:]:
        m = re.match(r"(\d+)\s*(?:[—–-]\s*(.*))?", b)
        if not m:
            continue
        num = int(m.group(1))
        corpo = b.split("\n", 1)[1] if "\n" in b else ""
        corpo = re.split(r"^\*\*Gabarito|^\|", corpo, flags=re.M)[0]
        enun, alts = [], []
        for linha in corpo.splitlines():
            s = linha.strip()
            if not s:
                continue
            a = re.match(r"^\(?([A-E])\)\s*(.+)$", s)
            if a:
                alts.append((a.group(1), _limpar(a.group(2))))
            elif alts:
                letra, txt = alts[-1]
                alts[-1] = (letra, txt + " " + _limpar(s))
            else:
                enun.append(_limpar(s))
        if alts:
            saida[num] = {"cabecalho": (m.group(2) or "").strip(), "enunciado": enun, "alternativas": alts}
    return saida
