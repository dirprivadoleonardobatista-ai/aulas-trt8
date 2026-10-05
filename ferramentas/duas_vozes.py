# -*- coding: utf-8 -*-
"""Converte os roteiros de quatro vozes (ANTONIO, FRANCISCA, BRUNO, THALITA)
para duas vozes femininas (FRANCISCA e THALITA). Sem IA, por regras:

1. As falas passam a alternar FRANCISCA / THALITA. Como no original as vozes
   ja alternavam, pergunta e resposta continuam em vozes diferentes.
2. Nomes: quem e citado passa a ser a OUTRA voz (a que esta ouvindo), com o
   artigo no feminino ("o Bruno disse" -> "a Thalita disse").
3. Apresentacoes da abertura: fica uma por voz, reescrita; as demais saem.
4. Concordancia de quem fala: "obrigado" -> "obrigada" etc.
5. Falas seguidas da mesma voz (depois de cortes) sao unidas.

    python ferramentas/duas_vozes.py           # converte roteiros/ no lugar
    python ferramentas/duas_vozes.py --teste   # so mostra o resultado de s001
"""
import glob
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTRA = {"FRANCISCA": "THALITA", "THALITA": "FRANCISCA"}
NOME = {"FRANCISCA": "Francisca", "THALITA": "Thalita"}
NOMES_VELHOS = r"(Antônio|Antonio|Bruno|Francisca|Thalita)"

APRESENTA = {
    "FRANCISCA": "Eu sou a Francisca, professora, e vou explicar cada tema com calma, com a lei e com exemplos.",
    "THALITA": "E eu sou a Thalita. Vou fazer as perguntas que você faria, mostrar como a FCC cobra e resumir o que mais importa.",
}

# artigo/contracao masculina antes do nome -> feminina
CONTRACOES = [
    (r"\bdo\s+", "da "), (r"\bDo\s+", "Da "), (r"\bno\s+", "na "), (r"\bNo\s+", "Na "),
    (r"\bpelo\s+", "pela "), (r"\bPelo\s+", "Pela "), (r"\bao\s+", "à "), (r"\bAo\s+", "À "),
    (r"\bo\s+", "a "), (r"\bO\s+", "A "),
]

GENERO = [
    (r"\bobrigado\b", "obrigada"), (r"\bObrigado\b", "Obrigada"),
    (r"\beu mesmo\b", "eu mesma"), (r"\bconfuso\b", "confusa"),
    (r"\bpreocupado\b", "preocupada"), (r"\bcurioso\b", "curiosa"),
    (r"\bcansado\b", "cansada"), (r"\banimado\b", "animada"),
    (r"\bconcurseiro\b", "concurseira"),
]


def trocar_nomes(texto, ouvinte, protegidos=()):
    """protegidos: nomes que aparecem na fonte da apostila; ali sao
    personagens de caso ("o irmao Bruno"), nao apresentadores."""
    nome = NOME[ouvinte]
    alvo = "|".join(n for n in ("Antônio", "Antonio", "Bruno", "Francisca", "Thalita") if n not in protegidos)
    if not alvo:
        return texto
    NOMES_VELHOS = "(" + alvo + ")"

    # vocativo no inicio: "Bruno, ..." -> "Thalita, ..."
    texto = re.sub(r"^" + NOMES_VELHOS + r"(?=[,!?.])", nome, texto)

    # artigo/contracao + nome
    def com_artigo(m):
        art = m.group(1)
        for pad, novo in CONTRACOES:
            if re.fullmatch(pad, art):
                return novo + nome
        return art + nome
    texto = re.sub(r"\b((?:do|Do|no|No|pelo|Pelo|ao|Ao|o|O|da|Da|na|Na|pela|Pela|à|À|a|A)\s+)"
                   + NOMES_VELHOS + r"\b", com_artigo, texto)
    # nome solto (vocativo no meio/fim)
    texto = re.sub(r"\b" + NOMES_VELHOS + r"\b", nome, texto)
    return texto


def apresentacao(texto):
    return re.search(r"\b(sou|Sou) (o|a) " + NOMES_VELHOS + r"\b", texto) is not None


def converter(texto, protegidos=()):
    linhas_saida, falas = [], []
    cabeca, slides = [], []
    atual = None
    for linha in texto.splitlines():
        s = linha.strip()
        m = re.match(r"^(ANTONIO|FRANCISCA|BRUNO|THALITA)\s*:\s*(.+)$", s)
        if m:
            atual["falas"].append(m.group(2).strip())
        elif s.startswith("== SLIDE:"):
            atual = {"cab": [s], "falas": []}
            slides.append(atual)
        elif s.startswith("* ") and atual is not None:
            atual["cab"].append(s)
        elif s:
            cabeca.append(s)

    voz = "FRANCISCA"
    ja_apresentou = set()
    for sl in slides:
        novas = []
        for fala in sl["falas"]:
            fala = fala.replace("com três colegas", "com uma colega")
            fala = re.sub(r"Aqui é (o|a) (Antônio|Bruno|Francisca|Thalita) e esta", "Esta", fala)
            frases = re.split(r"(?<=[.!?])\s+", fala)
            partes = []
            for k, fr in enumerate(frases):
                if apresentacao(fr):
                    # apresentacao: o que vem depois dela e o papel da personagem
                    # antiga; sai junto. Cada voz se apresenta uma vez so.
                    if voz not in ja_apresentou:
                        txt = APRESENTA[voz]
                        if not ja_apresentou and txt.startswith("E eu"):
                            txt = "Eu" + txt[4:]
                        partes.append(txt)
                        ja_apresentou.add(voz)
                    break
                fr = trocar_nomes(fr, OUTRA[voz], protegidos)
                for pad, novo in GENERO:
                    fr = re.sub(pad, novo, fr)
                partes.append(fr)
            fala = " ".join(partes).strip()
            if not fala:
                continue
            if novas and novas[-1][0] == voz:      # nao deveria ocorrer, mas une
                novas[-1] = (voz, novas[-1][1] + " " + fala)
            else:
                novas.append((voz, fala))
            voz = OUTRA[voz]
        sl["novas"] = novas

    saida = cabeca[:]
    for sl in slides:
        saida += sl["cab"]
        saida += ["%s: %s" % (v, t) for v, t in sl["novas"]]
    return "\n".join(saida) + "\n"


def main():
    import json
    arqs = sorted(glob.glob(os.path.join(RAIZ, "roteiros", "*.txt")))
    with open(os.path.join(RAIZ, "plano", "plano.json"), encoding="utf-8") as f:
        fontes = {x["id"]: x["fonte"] for x in json.load(f)["segmentos"]}

    def protegidos(arq):
        fonte = fontes[os.path.splitext(os.path.basename(arq))[0]]
        return {n for n in ("Antônio", "Antonio", "Bruno", "Francisca", "Thalita")
                if re.search(r"\b%s\b" % n, fonte)}
    if "--teste" in sys.argv:
        print(converter(open(arqs[0], encoding="utf-8").read(), protegidos(arqs[0]))[:3000])
        return
    restos = 0
    for a in arqs:
        with open(a, encoding="utf-8") as f:
            prot = protegidos(a)
            novo = converter(f.read(), prot)
        restos += len([n for n in re.findall(r"\b(Antônio|Antonio|Bruno)\b", novo) if n not in prot])
        with open(a, "w", encoding="utf-8", newline="\n") as f:
            f.write(novo)
    print("convertidos: %d | citações a Antônio/Bruno que sobraram: %d" % (len(arqs), restos))


if __name__ == "__main__":
    main()
