# Roteirista das videoaulas TRT-8 (FCC)

Este repositório transforma a apostila `partes/*.md` em ~40 h de videoaulas com
slides e quatro vozes. Você, sessão na nuvem, escreve os ROTEIROS. A voz, os
slides e os vídeos são feitos depois pelo GitHub Actions; não mexa em nada fora
de `roteiros/`.

## Procedimento (siga à risca: ele controla o custo)

1. Rode `python ferramentas/roteirista.py proximo` com os parâmetros do pedido
   (ex.: `--turno par --limite 12 --lote 2`). Ele mostra os próximos segmentos:
   a FONTE da apostila, a META de palavras e a posição na aula. Rode o comando
   exatamente assim, SEM `| head`, `| tail`, `grep` ou `2>&1`: a fonte precisa
   chegar inteira.
2. Escreva cada roteiro inteiro de uma vez com a ferramenta Write em
   `roteiros/<id>.txt` — todos os segmentos mostrados, na MESMA resposta.
   Não leia outros arquivos, não abra a apostila inteira, não planeje em
   arquivo separado, não escreva texto fora das ferramentas.
3. Rode de novo o mesmo comando `proximo`. Ele valida, faz commit e mostra o
   seguinte. Se apontar erro, corrija com Edit só o trecho indicado e rode de novo.
4. Quando ele disser LIMITE ou NADA PENDENTE, rode
   `python ferramentas/roteirista.py encerrar` e termine com uma linha de resumo.

## Formato de `roteiros/<id>.txt`

```
SEGMENTO s012
== SLIDE: Título curto do slide
* tópico telegráfico (pode usar "art. 5º", siglas e números)
* outro tópico (2 a 6 por slide)
ANTONIO: fala...
THALITA: fala...
BRUNO: fala...
FRANCISCA: fala...
== SLIDE: ...
```

## As quatro vozes (todas participam de cada segmento)

- ANTONIO (Antônio, professor): conduz, explica a teoria, organiza o raciocínio.
- FRANCISCA (Francisca, professora): aprofunda, traz a lei em paráfrase, a jurisprudência e exemplos concretos.
- BRUNO (Bruno, especialista em FCC): mostra como a banca cobra, as pegadinhas, comenta as questões alternativa por alternativa.
- THALITA (Thalita, concurseira): pergunta o que o aluno perguntaria, pede exemplo, resume com macetes.

Alterne sempre (nunca a mesma voz duas vezes seguidas). Falas de 1 a 5 frases.
Cada voz fica entre 10% e 45% das palavras: a THALITA não só pergunta, ela
também resume, dá macetes e arrisca respostas (às vezes erradas, e alguém corrige). Conversa de verdade: um responde ao outro,
completa, discorda e corrige quando faz sentido. Chamar pelo nome, só de vez em quando.

## Escrever para o ouvido (a voz é sintética e lê tudo ao pé da letra)

- Por extenso: "artigo quinto, inciso treze", "parágrafo segundo", "artigo dez"
  (ordinal até nono, cardinal do dez em diante), "Lei oito mil cento e doze, de
  mil novecentos e noventa", "Súmula trezentos e trinta e um do TST", "cinquenta por cento".
- Nas falas não use: §, "art.", "inc.", "nº", º, ª, algarismos romanos,
  colchetes, asteriscos, emojis, rubricas como "(risos)", abreviações com ponto.
  O validador recusa.
- Frases curtas e diretas. Nada de "como vimos na tabela": quem ouve não vê a tabela.
- Lei em paráfrase. Citação literal no máximo de uma frase curta.

## Conteúdo

- Cubra TUDO o que a fonte traz, na ordem dela, sem inventar. Tabela vira
  explicação linha a linha; [ATENCAO] e [PROVA] viram alerta de pegadinha;
  [EXEMPLO] vira caso concreto; [JURIS] vira o entendimento do tribunal.
- Questões da fonte: leia o enunciado resumido, dê tempo para pensar
  ("pausa para você pensar") e comente cada alternativa.
- Se a fonte não sustenta um detalhe, não o afirme.
- Slides: um a cada ~330 palavras de fala (no máximo 420), título até 80 caracteres, tópicos
  até 110 caracteres. Os tópicos resumem o que as falas daquele slide explicam.

## Tamanho

Escreva a META de palavras já na primeira versão (conte por alto: um slide
completo tem ~330 palavras). Cada correção custa caro. Se o validador pedir
mais palavras, acrescente UM slide novo inteiro com uma só chamada de Edit
(exemplo, pegadinha ou questão), em vez de várias falas soltas.

## Exemplo (trecho)

```
SEGMENTO s012
== SLIDE: Eficácia contida: o direito já nasce pronto
* Aplicação direta e imediata, mas pode não ser integral
* A lei posterior pode RESTRINGIR (art. 5º, XIII)
* Exemplo: Exame de Ordem para advogar
ANTONIO: Agora a segunda espécie, a norma de eficácia contida. Guarde a ideia central: o direito já nasce pronto, e você pode exercê-lo hoje mesmo.
THALITA: Então para que serve a lei, se o direito já está pronto?
FRANCISCA: Para conter o alcance dele. O artigo quinto, inciso treze, garante o livre exercício de qualquer profissão, atendidas as qualificações que a lei estabelecer. Enquanto a lei não vem, o exercício é amplo.
BRUNO: E é aqui que a FCC gosta de armar. Ela escreve que a norma contida só produz efeitos depois da lei. Errado: isso é a limitada. Na contida a lei restringe; na limitada a lei completa.
THALITA: Restringe ou completa. Gostei, vou anotar assim.
```
