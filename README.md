# Videoaulas TRT-8 (FCC)

A apostila `partes/*.md` vira cerca de 40 horas de videoaulas com slides e quatro
vozes que se alternam (Antônio, Francisca, Bruno e Thalita), sem avatar.

## Onde ficam as aulas

Na página **Releases → aulas** deste repositório. Cada aula tem três arquivos:

- `.mp4`: vídeo com slides e narração (720p)
- `.mp3`: só o áudio, para ouvir no celular
- `.srt`: legenda com o nome de quem fala

O texto do release traz o índice, com as horas já prontas.

## Como a produção anda sozinha

1. **Roteiros**: rotinas do Claude Code na nuvem rodam de hora em hora. Cada
   execução escreve até 12 segmentos em `roteiros/`, segundo o `CLAUDE.md`,
   e valida cada um com `ferramentas/roteirista.py`.
2. **Integração**: o GitHub Actions copia para o `main` só os roteiros válidos.
3. **Vídeo**: quando todos os segmentos de uma aula existem, o Actions gera as
   vozes (edge-tts, gratuito), os slides e o vídeo, e publica no release.

| Peça | Arquivo |
|---|---|
| Plano (248 segmentos, 73 aulas, metas de palavras) | `plano/plano.json`, gerado por `python -m estudio.plano` |
| Formato e validador do roteiro | `estudio/formato.py` |
| Vozes, slides e montagem | `estudio/tts.py`, `estudio/slides.py`, `estudio/render.py` |
| Workflow | `.github/workflows/producao.yml` |

## Comandos úteis

```
python ferramentas/roteirista.py status        # quantos roteiros faltam
python -m estudio.render --local --aula a001   # monta uma aula no seu PC, em saida/
```

Para refazer uma aula já publicada: Actions → producao → Run workflow → informe a aula (ex.: `a012`).

## Vozes

| Nome | Voz (edge-tts) | Papel |
|---|---|---|
| Antônio | pt-BR-AntonioNeural, tom -10 Hz | professor, conduz |
| Francisca | pt-BR-FranciscaNeural, tom -8 Hz | professora, lei e exemplos |
| Bruno | en-US-BrianMultilingualNeural, tom -6 Hz | especialista em FCC |
| Thalita | pt-BR-ThalitaMultilingualNeural, tom -10 Hz | concurseira, perguntas e resumos |

Para trocar uma voz, edite `VOZES_TTS` em `estudio/tts.py`.
