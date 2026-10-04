# -*- coding: utf-8 -*-
"""Roda no GitHub Actions, com 'main' em checkout: traz para o main SO os
roteiros novos de um branch das sessoes na nuvem, valida cada um e faz o push.
Codigo e outros arquivos do branch sao ignorados de proposito.

    python ferramentas/integrar.py <branch>
"""
import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ)
from estudio.formato import validar  # noqa: E402


def git(*a):
    r = subprocess.run(["git"] + list(a), cwd=RAIZ, capture_output=True, text=True)
    if r.returncode:
        raise SystemExit("git %s falhou: %s" % (" ".join(a), r.stderr.strip()))
    return r.stdout


def main():
    branch = sys.argv[1]
    git("fetch", "origin", branch)
    ref = "origin/" + branch
    base = git("merge-base", "origin/main", ref).strip()
    nomes = [n for n in git("diff", "--name-only", "--diff-filter=AM", base, ref, "--", "roteiros/").split()
             if n.endswith(".txt")]
    with open(os.path.join(RAIZ, "plano", "plano.json"), encoding="utf-8") as f:
        segs = {s["id"]: s for s in json.load(f)["segmentos"]}

    aceitos = []
    for nome in nomes:
        sid = os.path.splitext(os.path.basename(nome))[0]
        if sid not in segs:
            print("ignorado (fora do plano): " + nome)
            continue
        if os.path.exists(os.path.join(RAIZ, nome)):
            print("ignorado (já existe no main): " + nome)
            continue
        texto = git("show", "%s:%s" % (ref, nome))
        _, erros, resumo = validar(texto, segs[sid])
        if erros:
            print("REPROVADO %s: %s" % (nome, "; ".join(erros[:3])))
            continue
        with open(os.path.join(RAIZ, nome), "w", encoding="utf-8", newline="\n") as f:
            f.write(texto)
        aceitos.append(nome)
        print("OK %s: %s" % (nome, resumo))

    if not aceitos:
        print("nada novo para integrar")
        return
    git("config", "user.name", "github-actions[bot]")
    git("config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    git("add", *aceitos)
    git("commit", "-m", "integra %d roteiro(s) de %s" % (len(aceitos), branch))
    for tentativa in range(3):
        r = subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=RAIZ, capture_output=True, text=True)
        if not r.returncode:
            print("integrados: %d" % len(aceitos))
            return
        git("pull", "--rebase", "origin", "main")
    raise SystemExit("push para o main falhou: " + r.stderr)


if __name__ == "__main__":
    main()
