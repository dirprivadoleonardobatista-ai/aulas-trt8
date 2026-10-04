# -*- coding: utf-8 -*-
"""Ferramenta do roteirista (sessoes do Claude Code na nuvem). So stdlib.

    python ferramentas/roteirista.py proximo [--turno par|impar] [--limite 12] [--lote 2]
        valida o que voce acabou de escrever, faz commit e mostra o proximo
        segmento pendente (fonte + meta de palavras + posicao na aula).
    python ferramentas/roteirista.py encerrar
        faz o push final e mostra o resumo.
    python ferramentas/roteirista.py status
        quanto falta.
"""
import argparse
import glob
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from estudio.formato import validar  # noqa: E402

PASTA = os.path.join(RAIZ, "roteiros")
CONTADOR = os.path.join(RAIZ, ".git", "roteirista_sessao.json")
PUSH_A_CADA = 3

POSICAO = {
    "abertura": "PRIMEIRO segmento da aula: comece com ANTONIO dando as boas-vindas, dizendo o "
                "número e o tema da aula e o roteiro do que vem; os outros se apresentam em uma "
                "frase curta cada. Não feche a aula no final: termine puxando o próximo tema.",
    "meio": "Segmento do MEIO da aula: sem boas-vindas e sem despedida. Comece ligando com o "
            "tema anterior em uma frase e termine puxando o próximo tema.",
    "fechamento": "ÚLTIMO segmento da aula: sem boas-vindas. Comece ligando com o tema anterior. "
                  "Termine com THALITA fazendo um resumo relâmpago dos pontos da aula que mais "
                  "caem na FCC e ANTONIO se despedindo em uma frase.",
    "unico": "Aula de um segmento só: abra com boas-vindas curtas (ANTONIO) e feche com resumo "
             "relâmpago (THALITA) e despedida em uma frase (ANTONIO).",
}


def git(*args, ok=False):
    r = subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    if r.returncode and not ok:
        print("[git %s] %s" % (" ".join(args), (r.stderr or r.stdout).strip()[:400]))
    return r


def plano():
    with open(os.path.join(RAIZ, "plano", "plano.json"), encoding="utf-8") as f:
        return json.load(f)


def contador(delta=0, zerar=False):
    d = {"escritos": 0, "commits_sem_push": 0}
    if os.path.exists(CONTADOR) and not zerar:
        with open(CONTADOR, encoding="utf-8") as f:
            d.update(json.load(f))
    if delta:
        d["escritos"] += delta
        d["commits_sem_push"] += delta
    os.makedirs(os.path.dirname(CONTADOR), exist_ok=True)
    with open(CONTADOR, "w", encoding="utf-8") as f:
        json.dump(d, f)
    return d


def push():
    if not git("config", "user.email", ok=True).stdout.strip():
        git("config", "user.email", "roteirista@aulas-trt8.local")
        git("config", "user.name", "Roteirista (Claude)")
    r = git("push", "-u", "origin", "HEAD", ok=True)
    if r.returncode:
        git("pull", "--rebase", "origin", git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip(), ok=True)
        r = git("push", "-u", "origin", "HEAD", ok=True)
    if r.returncode:
        print("AVISO: push falhou: %s" % (r.stderr or r.stdout).strip()[:300])
        return False
    d = contador()
    d["commits_sem_push"] = 0
    with open(CONTADOR, "w", encoding="utf-8") as f:
        json.dump(d, f)
    return True


def novos_arquivos():
    """Roteiros criados ou alterados e ainda sem commit."""
    r = git("status", "--porcelain", "--untracked-files=all", "--", "roteiros", ok=True)
    saida = []
    for linha in r.stdout.splitlines():
        caminho = linha[3:].strip().strip('"')
        if caminho.endswith(".txt"):
            saida.append(os.path.join(RAIZ, caminho))
    return sorted(saida)


def conferir_e_commitar(segs):
    """Valida os roteiros novos. Devolve False se algum precisa de correcao."""
    bons = []
    for arq in novos_arquivos():
        sid = os.path.splitext(os.path.basename(arq))[0]
        seg = segs.get(sid)
        if not seg:
            print("ERRO: %s não é um segmento do plano. Apague esse arquivo." % arq)
            return False
        with open(arq, encoding="utf-8") as f:
            _, erros, resumo = validar(f.read(), seg)
        if erros:
            print("=" * 70)
            print("CORRIJA roteiros/%s.txt antes de seguir (use Edit; não reescreva o arquivo todo):" % sid)
            for e in erros[:25]:
                print("  - " + e)
            if len(erros) > 25:
                print("  ... e mais %d" % (len(erros) - 25))
            print("Depois rode de novo: python ferramentas/roteirista.py proximo ...")
            return False
        print("OK %s: %s" % (sid, resumo))
        bons.append(arq)
    if bons:
        git("add", "--", *bons)
        if not git("config", "user.email", ok=True).stdout.strip():
            git("config", "user.email", "roteirista@aulas-trt8.local")
            git("config", "user.name", "Roteirista (Claude)")
        git("commit", "-m", "roteiro: " + " ".join(
            os.path.splitext(os.path.basename(b))[0] for b in bons))
        d = contador(len(bons))
        if d["commits_sem_push"] >= PUSH_A_CADA:
            push()
    return True


def pendentes(p, turno):
    feitos = {os.path.splitext(os.path.basename(a))[0] for a in glob.glob(os.path.join(PASTA, "*.txt"))}
    aulas = {a["id"]: a for a in p["aulas"]}
    out = []
    for s in p["segmentos"]:
        if s["id"] in feitos:
            continue
        num = aulas[s["aula"]]["numero"]
        if turno == "par" and num % 2:
            continue
        if turno == "impar" and not num % 2:
            continue
        out.append(s)
    return out


def mostrar(seg, aula, total):
    meta = seg["meta_palavras"]
    print("=" * 70)
    print("PRÓXIMO: %s  ->  escreva em roteiros/%s.txt (ferramenta Write)" % (seg["id"], seg["id"]))
    print("Aula %d de %d — %s (parte %d de %d da disciplina)" % (
        aula["numero"], total, aula["disciplina"], aula["parte"], aula["partes"]))
    print("Temas da aula: " + " | ".join(aula["temas"]))
    print("Tema deste segmento: " + seg["titulo"])
    if seg["anterior"]:
        print("Tema anterior: " + seg["anterior"])
    if seg["seguinte"]:
        print("Próximo tema: " + seg["seguinte"])
    print("Posição: " + POSICAO[seg["posicao"]])
    print("META: %d palavras faladas (aceito %d a %d), cerca de %d slides." % (
        meta, int(meta * 0.93), int(meta * 1.25), max(2, round(meta / 330))))
    print("=" * 70)
    print("FONTE (apostila):")
    print(seg["fonte"])
    print("=" * 70)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("acao", choices=["proximo", "encerrar", "status"])
    ap.add_argument("--turno", choices=["par", "impar", "todos"], default="todos")
    ap.add_argument("--limite", type=int, default=12)
    ap.add_argument("--lote", type=int, default=2, help="segmentos mostrados de uma vez")
    a = ap.parse_args()

    p = plano()
    segs = {s["id"]: s for s in p["segmentos"]}
    aulas = {x["id"]: x for x in p["aulas"]}

    if a.acao == "status":
        falta = pendentes(p, "todos")
        print("segmentos prontos: %d de %d | faltam %d (%d palavras)" % (
            len(segs) - len(falta), len(segs), len(falta), sum(s["meta_palavras"] for s in falta)))
        return

    if not conferir_e_commitar(segs):
        sys.exit(1)

    if a.acao == "encerrar":
        push()
        d = contador()
        print("ENCERRADO: %d roteiros nesta sessão. Pode terminar." % d["escritos"])
        contador(zerar=True)
        return

    d = contador()
    if d["escritos"] >= a.limite:
        print("LIMITE DESTA SESSÃO ATINGIDO (%d roteiros). Rode agora: "
              "python ferramentas/roteirista.py encerrar  — e termine." % d["escritos"])
        return
    falta = pendentes(p, a.turno)
    if not falta:
        print("NADA PENDENTE neste turno. Rode: python ferramentas/roteirista.py encerrar — e termine.")
        return
    lote = falta[:max(1, min(a.lote, a.limite - d["escritos"]))]
    for seg in lote:
        mostrar(seg, aulas[seg["aula"]], len(aulas))
    if len(lote) > 1:
        print("Escreva os %d segmentos acima, um arquivo cada, com %d chamadas de Write na MESMA resposta."
              % (len(lote), len(lote)))
    print("Depois rode: python ferramentas/roteirista.py proximo --turno %s --limite %d --lote %d"
          % (a.turno, a.limite, a.lote))


if __name__ == "__main__":
    main()
