# MATEMÁTICA E RACIOCÍNIO LÓGICO

## 1. Lógica proposicional: proposições, conectivos e tabela-verdade

> [SINTESE] Proposição = frase declarativa com valor lógico único (V ou F).
> • Cinco conectivos: não (~), e (∧), ou (∨), ou...ou (⊻), se...então (→), se e somente se (↔).
> • Cada conectivo tem UMA situação-chave que decide seu valor; decorá-la resolve 80% das questões.
> • Tabela-verdade com n proposições simples tem 2ⁿ linhas.
> • Classificação do resultado: tautologia, contradição ou contingência.

### 1.1 O que é (e o que não é) proposição

Proposição é toda oração declarativa que admite um, e só um, dos valores lógicos verdadeiro (V) ou falso (F). Os princípios clássicos que sustentam essa definição são três.

| Princípio | Enunciado | Consequência prática |
|---|---|---|
| **Identidade** | Uma proposição verdadeira é verdadeira; uma falsa é falsa | O valor não muda no meio do problema |
| **Não contradição** | Nenhuma proposição é V e F ao mesmo tempo | Duas afirmações contraditórias não podem ser ambas V |
| **Terceiro excluído** | Toda proposição é V ou F, não havendo terceira opção | Base do método de hipóteses (se não é V, é F) |

| Frase | É proposição? | Motivo |
|---|---|---|
| "Belém é a capital do Pará." | Sim | Declarativa, valor V |
| "7 é número par." | Sim | Declarativa, valor F (falsidade não impede) |
| "Que horas são?" | Não | Interrogativa |
| "Feche a porta." | Não | Imperativa |
| "Que dia lindo!" | Não | Exclamativa |
| "x + 2 = 5" | Não | Sentença aberta: depende de x |
| "Esta frase é falsa." | Não | Paradoxo: não admite valor único |

> [PROVA] A FCC pergunta "quantas das frases abaixo são proposições". Elimine perguntas, ordens, exclamações, sentenças abertas (com variável ou com "ele/ela" indeterminado) e paradoxos. Frase falsa continua sendo proposição.

### 1.2 Os conectivos e a situação-chave de cada um

| Conectivo | Símbolo e leitura | Situação-chave | Formas equivalentes na linguagem |
|---|---|---|---|
| **Negação** | ~p — "não p" | Inverte o valor de p | "não é verdade que", "é falso que" |
| **Conjunção** | p ∧ q — "p e q" | Só é V se ambas forem V | "mas", "porém", "embora", vírgula aditiva |
| **Disjunção inclusiva** | p ∨ q — "p ou q" | Só é F se ambas forem F | "ou" simples |
| **Disjunção exclusiva** | p ⊻ q — "ou p ou q" | V quando os valores são diferentes | "ou...ou", "ou p ou q, mas não ambos" |
| **Condicional** | p → q — "se p, então q" | Só é F no caso V → F ("Vera Fischer é Falsa") | "quando p, q"; "sempre que p, q"; "p implica q"; "todo p é q"; "p somente se q" |
| **Bicondicional** | p ↔ q — "p se e somente se q" | V quando os valores são iguais | "p se e só se q"; "p é condição necessária e suficiente para q" |

### 1.3 Tabela-verdade completa

| p | q | p ∧ q | p ∨ q | p ⊻ q | p → q | p ↔ q |
|---|---|---|---|---|---|---|
| V | V | V | V | F | V | V |
| V | F | F | V | V | F | F |
| F | V | F | V | V | V | F |
| F | F | F | F | F | V | V |

> [DICA] Repare: ⊻ e ↔ são exatamente opostos linha a linha. Por isso a negação de um é o outro.

| Nº de proposições simples | Linhas da tabela | Regra |
|---|---|---|
| 2 | 4 | 2² |
| 3 | 8 | 2³ |
| 4 | 16 | 2⁴ |
| n | 2ⁿ | Conte proposições distintas, não letras repetidas |

### 1.4 Condição suficiente e condição necessária

Na condicional p → q, o antecedente é **suficiente** para o consequente, e o consequente é **necessário** para o antecedente.

| Estrutura | Leitura | Exemplo |
|---|---|---|
| p → q | p é condição suficiente para q | "Ser oficial de justiça é suficiente para ser servidor" |
| p → q | q é condição necessária para p | "Ser servidor é necessário para ser oficial de justiça" |
| p → q | p somente se q | "Ana é nomeada somente se for aprovada" = se nomeada → aprovada |
| p ↔ q | p é necessária e suficiente para q | Ida e volta valem |

> [ATENCAO] "Somente se" introduz o CONSEQUENTE: "p somente se q" = p → q. Já "se p" (sem "somente") introduz o antecedente. A FCC inverte essa ordem nas alternativas erradas.

### 1.5 Calculando o valor lógico de expressões

Ordem: parênteses primeiro, depois negação, e por fim o conectivo principal.

> [EXEMPLO] Sejam p = V, q = F, r = V. Valor de (p → q) ∨ (~r ↔ q)?
> • p → q = V → F = F.
> • ~r = F; logo ~r ↔ q = F ↔ F = V.
> • F ∨ V = V. Resposta: a expressão é verdadeira.

| Classificação | Definição | Exemplo típico |
|---|---|---|
| **Tautologia** | Verdadeira em todas as linhas | p ∨ ~p; (p ∧ q) → p |
| **Contradição** | Falsa em todas as linhas | p ∧ ~p; p ↔ ~p |
| **Contingência** | Ao menos uma V e ao menos uma F | p → q; p ∨ q |

## 2. Equivalências e negações

> [SINTESE] Equivalentes = mesma tabela-verdade. Negação = tabela oposta.
> • Condicional tem duas equivalências clássicas: contrapositiva (~q → ~p) e "nem-ou" (~p ∨ q).
> • De Morgan: nega-se cada parte e troca-se "e" por "ou" (e vice-versa).
> • Negação da condicional: mantém o antecedente, "e", nega o consequente (p ∧ ~q).
> • Quantificadores: "todo" vira "algum... não"; "algum" vira "nenhum".

### 2.1 Equivalências mais cobradas

| Proposição | Equivalente | Como lembrar |
|---|---|---|
| **p → q** | ~q → ~p (contrapositiva) | Inverte a ordem e nega ambas |
| **p → q** | ~p ∨ q | "Nega o primeiro, troca → por OU, mantém o segundo" |
| **p ∨ q** | ~p → q | Volta da regra anterior |
| **p ↔ q** | (p → q) ∧ (q → p) | Condicional de ida e de volta |
| **p ⊻ q** | ~(p ↔ q) | Exclusiva é a negação da bicondicional |
| **~(~p)** | p | Dupla negação |

| Variação de p → q | Forma | É equivalente a p → q? |
|---|---|---|
| **Contrapositiva** | ~q → ~p | Sim |
| **Recíproca** | q → p | Não |
| **Inversa (contrária)** | ~p → ~q | Não |

> [ATENCAO] Recíproca e inversa NÃO são equivalentes à condicional original (são equivalentes entre si). "Se chove, a rua molha" não autoriza "se a rua molhou, choveu".

> [EXEMPLO] "Se Márcio é técnico, então trabalha no fórum."
> • Contrapositiva (equivalente): "Se Márcio não trabalha no fórum, então não é técnico."
> • Regra do ou (equivalente): "Márcio não é técnico ou trabalha no fórum."
> • Recíproca (não equivalente): "Se Márcio trabalha no fórum, então é técnico."

### 2.2 Negações (leis de De Morgan e outras)

| Proposição | Negação | Erro típico da alternativa falsa |
|---|---|---|
| **p ∧ q** | ~p ∨ ~q | Negar as partes e manter o "e" |
| **p ∨ q** | ~p ∧ ~q | Negar as partes e manter o "ou" |
| **p → q** | p ∧ ~q | Oferecer a inversa (~p → ~q) ou outra condicional |
| **p ↔ q** | p ⊻ q, ou (p ∧ ~q) ∨ (~p ∧ q) | Oferecer ~p ↔ ~q (que é equivalente, não negação) |
| **p ⊻ q** | p ↔ q | — |

> [PROVA] Negação de condicional é a questão de lógica mais frequente da FCC. A resposta NUNCA é uma condicional: procure a alternativa com "e" que mantém a primeira parte e nega a segunda.

> [EXEMPLO] Negar "Se Ana estuda, então Ana é aprovada": "Ana estuda e não é aprovada".
> Negar "Bruno é analista e Carla é técnica": "Bruno não é analista ou Carla não é técnica".
> Negar "Davi viaja ou Elisa trabalha": "Davi não viaja e Elisa não trabalha".

### 2.3 Quantificadores (todo, algum, nenhum)

| Proposição | Negação | Observação |
|---|---|---|
| **Todo A é B** | Algum A não é B | Basta UM contraexemplo |
| **Algum A é B** | Nenhum A é B | "Algum" = "pelo menos um" = "existe" |
| **Nenhum A é B** | Algum A é B | — |
| **Algum A não é B** | Todo A é B | — |

> [ATENCAO] A negação de "Todo servidor é pontual" NÃO é "Nenhum servidor é pontual" (essa é a contrária, e ambas podem ser falsas). Também não é "Todo servidor não é pontual". Correto: "Algum servidor não é pontual" ou "Pelo menos um servidor não é pontual" ou "Existe servidor que não é pontual".

> [DICA] Atalho: para negar "Todo", troque por "Algum/Pelo menos um/Existe" e acrescente "não". Para negar "Algum/Existe", troque por "Nenhum". O quantificador sempre muda; a frase universal nunca é negada por outra universal.

## 3. Argumentos, silogismos e diagramas

> [SINTESE] Argumento = premissas que pretendem sustentar uma conclusão.
> • Válido: sempre que as premissas forem V, a conclusão é obrigatoriamente V.
> • Validade é questão de forma, não de verdade dos fatos.
> • Ferramentas: regras de inferência (modus ponens, modus tollens), diagramas de conjuntos para quantificadores, e o método "parta da premissa simples".

### 3.1 Formas válidas e falácias

| Forma | Estrutura | Válida? |
|---|---|---|
| **Modus ponens** | p → q; p; logo q | Sim |
| **Modus tollens** | p → q; ~q; logo ~p | Sim |
| **Silogismo hipotético** | p → q; q → r; logo p → r | Sim |
| **Silogismo disjuntivo** | p ∨ q; ~p; logo q | Sim |
| **Afirmação do consequente** | p → q; q; logo p | Não (falácia) |
| **Negação do antecedente** | p → q; ~p; logo ~q | Não (falácia) |

> [EXEMPLO] Premissas: (1) Se Ana estuda, então é aprovada. (2) Se Ana é aprovada, então é nomeada. (3) Ana não foi nomeada.
> • Comece pela premissa simples (3): "não nomeada" é V.
> • Em (2), consequente F exige antecedente F: Ana não foi aprovada.
> • Em (1), consequente F exige antecedente F: Ana não estudou.
> • Conclusão válida: "Ana não estudou e não foi aprovada".

> [DICA] Método da conclusão falsa: para testar se um argumento é válido, suponha a conclusão F e tente tornar todas as premissas V. Se conseguir, o argumento é inválido; se surgir contradição, é válido.

### 3.2 Diagramas lógicos (quantificadores)

| Premissa | Diagrama | O que é garantido |
|---|---|---|
| **Todo A é B** | Círculo A inteiro dentro de B | Quem é A é B; nada se sabe de quem é B |
| **Algum A é B** | A e B com interseção marcada | Existe ao menos um elemento comum |
| **Nenhum A é B** | A e B separados | Interseção vazia |
| **Algum A não é B** | Parte de A fora de B (marcada) | Existe A fora de B |

```
  Todo A é B          Algum A é B         Nenhum A é B
 +-----------+        +-----+---+-----+    +-----+   +-----+
 | B  +---+  |        |  A  | x |  B  |    |  A  |   |  B  |
 |    | A |  |        +-----+---+-----+    +-----+   +-----+
 |    +---+  |          x = elemento
 +-----------+          garantido
```

> [EXEMPLO] "Todos os oficiais de justiça são servidores. Alguns servidores são advogados." Conclusão proposta: "Alguns oficiais de justiça são advogados".
> • Desenhe Oficiais dentro de Servidores; Advogados cruza Servidores, mas pode cruzar só a parte fora de Oficiais.
> • Existe desenho com premissas V e conclusão F: argumento INVÁLIDO.

> [PROVA] A FCC usa "pode-se concluir corretamente que" ou "é necessariamente verdadeiro". Só marque o que vale em TODOS os desenhos possíveis. O que vale em apenas alguns desenhos é "possível", não "necessário".

## 4. Estrutura lógica de relações: associação, verdades e mentiras, ordenação

> [SINTESE] Três famílias de problemas.
> • Associação: monte a tabela-gabarito (pessoas × atributos), marque X nas exclusões e ✓ nas certezas; cada linha e cada coluna tem um único ✓.
> • Verdades e mentiras: teste hipóteses (um culpado por vez) ou procure duas afirmações contraditórias.
> • Ordenação: transforme pistas em desigualdades e blocos ("imediatamente depois" = bloco fixo).

### 4.1 Associação com tabela-gabarito

> [EXEMPLO] Ana, Bruno e Carla trabalham, um em cada setor (Protocolo, Secretaria, Gabinete), e moram, um em cada cidade (Belém, Macapá, Santarém). Pistas: (I) Ana não trabalha no Gabinete. (II) Quem trabalha no Protocolo mora em Santarém. (III) Bruno mora em Belém. (IV) Carla não trabalha no Protocolo. (V) Quem mora em Macapá não trabalha na Secretaria.
> • (III) + (II): Bruno mora em Belém, logo não é do Protocolo. (IV): Carla também não. Logo Ana = Protocolo e, por (II), Ana mora em Santarém.
> • Sobra Macapá para Carla. Por (V), Carla não é da Secretaria: Carla = Gabinete; Bruno = Secretaria.

| Pessoa | Protocolo | Secretaria | Gabinete | Belém | Macapá | Santarém |
|---|---|---|---|---|---|---|
| **Ana** | ✓ | X | X | X | X | ✓ |
| **Bruno** | X | ✓ | X | ✓ | X | X |
| **Carla** | X | X | ✓ | X | ✓ | X |

> [DICA] Pistas do tipo "quem faz X tem Y" ligam duas colunas de atributos: use-as para eliminar pessoas que já têm outro valor. Comece sempre pelas pistas afirmativas ("Bruno mora em Belém") e depois cruze com as condicionais.

### 4.2 Verdades e mentiras

| Técnica | Quando usar | Como aplicar |
|---|---|---|
| **Hipótese por culpado** | Poucos suspeitos (3 a 5) | Supõe cada um culpado e conta quantas falas ficam V; fica a hipótese que bate com o enunciado |
| **Par contraditório** | Duas falas que se negam ("Foi o Beto" × "Não fui eu", dito por Beto) | Exatamente uma delas é V; isso fixa o valor das demais |
| **Quem acusa quem mente** | "Fulano está mentindo" | As duas falas têm valores opostos |

> [EXEMPLO] Um vaso foi quebrado por um de três irmãos; apenas um diz a verdade. André: "Foi o Beto." Beto: "Não fui eu." Caio: "Não fui eu."
> • André e Beto dizem coisas contraditórias: exatamente um deles fala a verdade.
> • Como só há uma verdade, Caio mente. "Não fui eu" falso: foi Caio.
> • Conferência: André F, Beto V, Caio F. Uma verdade só. Culpado: Caio.

> [ATENCAO] Sempre confira a hipótese final contando as verdades. A FCC monta alternativas que satisfazem parte das condições ("o culpado certo, mas o sincero errado").

### 4.3 Ordenação e posições

| Pista | Tradução |
|---|---|
| "X chegou antes de Y" | X < Y (não necessariamente vizinhos) |
| "X chegou imediatamente antes de Y" | Bloco XY fixo |
| "Entre X e Y há duas pessoas" | Posições diferem em 3 |
| "X não é o primeiro nem o último" | X em posição intermediária |
| Mesa circular: "à direita de X" | Defina o sentido (horário/anti-horário) e fixe X numa cadeira |

> [EXEMPLO] Cinco processos (A, B, C, D, E) foram protocolados em sequência. C antes de A; A antes de D; B imediatamente depois de D; E foi o último.
> • E ocupa a 5ª posição. Restam 1 a 4 para C < A < D e o bloco DB.
> • D precisa de dois antes de si (C e A) e de B logo após: D = 3, B = 4. Logo C = 1, A = 2.
> • Ordem: C, A, D, B, E (única).

## 5. Raciocínio sequencial: números, letras e figuras

> [SINTESE] Toda sequência esconde uma lei de formação. Roteiro de busca:
> • 1º diferenças entre termos vizinhos (PA, diferenças crescentes);
> • 2º razões (PG, multiplicações);
> • 3º padrão alternado ou duas sequências intercaladas (posições ímpares × pares);
> • 4º ciclos que se repetem (use o resto da divisão);
> • 5º letras: converta em posição no alfabeto.

### 5.1 Tipos de sequência numérica

| Tipo | Exemplo | Lei | Próximo termo |
|---|---|---|---|
| **PA** | 5, 8, 11, 14 | +3 | 17 |
| **PG** | 3, 6, 12, 24 | ×2 | 48 |
| **Diferenças crescentes** | 1, 2, 5, 10, 17, 26 | +1, +3, +5, +7, +9 | 37 (+11) |
| **Alternada** | 3, 7, 6, 10, 9, 13, 12 | +4, −1, +4, −1 | 16 |
| **Intercalada** | 2, 50, 4, 45, 8, 40, 16 | ímpares ×2; pares −5 | 35 |
| **Fibonacci-like** | 1, 1, 2, 3, 5, 8 | soma dos dois anteriores | 13 |
| **Quadrados/cubos** | 1, 4, 9, 16, 25 | n² | 36 |

| Fórmula | Uso |
|---|---|
| PA: aₙ = a₁ + (n − 1) · r | Termo distante sem listar |
| PG: aₙ = a₁ · qⁿ⁻¹ | Termo distante de PG |
| Soma da PA: Sₙ = (a₁ + aₙ) · n ÷ 2 | Total acumulado |

> [EXEMPLO] 100º termo de 5, 8, 11, 14, ...: a₁₀₀ = 5 + 99 · 3 = 302.
> Em 3, 7, 6, 10, 9, 13, ... (alternada +4/−1), a cada par de passos a sequência sobe 3. Os termos ímpares são 3, 6, 9, 12, ... (múltiplos de 3): o 21º termo (11º ímpar) vale 3 · 11 = 33.

> [DICA] Sequência alternada: separe os termos de posição ímpar dos de posição par. Cada subsequência costuma ser uma PA simples, e o termo pedido sai da fórmula da PA aplicada à subsequência certa (posição 2k → k-ésimo termo par).

### 5.2 Sequências de letras

| Letra | A | B | C | D | E | F | G | H | I | J | K | L | M |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Posição** | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |

| Letra | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Posição** | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 |

> [ATENCAO] Questões antigas da FCC usavam o alfabeto de 23 letras (sem K, W e Y). Leia o enunciado: se ele disser "alfabeto oficial" ou "26 letras", inclua K, W e Y; se mandar desconsiderá-las, refaça a tabela. Essa diferença é a pegadinha preferida nas alternativas.

> [EXEMPLO] A, C, F, J, O, ... → posições 1, 3, 6, 10, 15 (+2, +3, +4, +5). Próximo: 15 + 6 = 21 = U.

### 5.3 Ciclos e figuras descritas

Quando um bloco se repete, o n-ésimo elemento é o elemento de posição igual ao **resto** de n dividido pelo tamanho do ciclo (resto zero = último elemento do ciclo).

> [EXEMPLO] A palavra TRTPARA é escrita repetidamente: TRTPARATRTPARA... Qual é a 100ª letra?
> • Ciclo de 7 letras. 100 = 7 · 14 + 2. Resto 2 → 2ª letra do ciclo: R.

| Padrão de figura descrita | Período | Raciocínio |
|---|---|---|
| Seta gira 90° no sentido horário a cada passo | 4 | Posição n → resto de n ÷ 4 |
| Seta gira 45° a cada passo | 8 | Resto de n ÷ 8 |
| Cor alterna preto/branco | 2 | Par ou ímpar |
| Figura ganha um lado a cada passo (triângulo, quadrado...) | Sem ciclo | Nº de lados = 2 + n |

### 5.4 Formação de conceitos e discriminação de elementos

| Tarefa | O que se pede | Estratégia |
|---|---|---|
| **Formação de conceitos** | Descobrir a característica comum de um grupo | Testar categorias: classe gramatical, nº de letras, paridade, primos |
| **Discriminação (intruso)** | Achar o elemento que não pertence | Achar a regra que vale para todos menos um |
| **Analogia** | "A está para B assim como C está para ?" | Descrever a relação A→B em palavras e aplicá-la a C |

> [EXEMPLO] Intruso em 11, 17, 23, 27, 31: todos são primos, exceto 27 (= 3³).

## 6. Orientação temporal e espacial

> [SINTESE] Calendário e dias da semana se resolvem por resto da divisão por 7.
> • Mês de 31 dias desloca o dia da semana em 3; de 30, em 2; fevereiro de 28, em 0; de 29, em 1.
> • Ano comum desloca a mesma data em 1 dia; ano bissexto (passando por 29/2), em 2.
> • Relógio: ângulo entre ponteiros = módulo de (30H − 5,5M).
> • Direções: rotações de 90° em torno de N, L, S, O.

### 6.1 Calendário e dias da semana

| Intervalo | Dias | Resto ÷ 7 | Efeito no dia da semana |
|---|---|---|---|
| Mês de 31 dias | 31 | 3 | Mesmo dia do mês seguinte cai 3 dias à frente |
| Mês de 30 dias | 30 | 2 | 2 dias à frente |
| Fevereiro comum | 28 | 0 | Mesmo dia da semana |
| Fevereiro bissexto | 29 | 1 | 1 dia à frente |
| Ano comum | 365 | 1 | Mesma data no ano seguinte: +1 |
| Ano bissexto | 366 | 2 | +2 |

| Mês | Dias | Mês | Dias |
|---|---|---|---|
| Janeiro | 31 | Julho | 31 |
| Fevereiro | 28 ou 29 | Agosto | 31 |
| Março | 31 | Setembro | 30 |
| Abril | 30 | Outubro | 31 |
| Maio | 31 | Novembro | 30 |
| Junho | 30 | Dezembro | 31 |

> [APROFUNDANDO] Ano bissexto: divisível por 4, exceto os anos de século (terminados em 00), que só são bissextos se divisíveis por 400. Assim, 2000 foi bissexto; 1900 e 2100 não.

> [EXEMPLO] Se 15 de março de certo ano caiu numa quarta-feira, em que dia cai 15 de junho do mesmo ano?
> • De 15/3 a 15/6: 31 (março) + 30 (abril) + 31 (maio) = 92 dias.
> • 92 = 7 · 13 + 1. Resto 1: quarta + 1 = quinta-feira.

> [EXEMPLO] Hoje é sábado. Daqui a 100 dias será: 100 = 7 · 14 + 2 → sábado + 2 = segunda-feira.

> [DICA] Mês de 31 dias tem 4 semanas completas + 3 dias: os três primeiros dias da semana em que o mês começa aparecem 5 vezes. Se um mês de 31 dias começa numa terça, ele terá cinco terças, cinco quartas e cinco quintas.

> [ATENCAO] "Daqui a n dias" conta a partir de amanhã; "do dia 1º ao dia 10" inclui as duas pontas (10 dias), mas a distância entre eles é de 9 dias. Defina se a questão pede distância ou contagem inclusiva.

### 6.2 Relógios

| Fato | Valor |
|---|---|
| Ponteiro das horas | 30° por hora = 0,5° por minuto |
| Ponteiro dos minutos | 6° por minuto = 360° por hora |
| Ângulo entre ponteiros às H horas e M minutos | módulo de (30H − 5,5M); se passar de 180°, use 360° menos o valor |
| Ponteiros sobrepostos | 11 vezes a cada 12 horas |

> [EXEMPLO] Ângulo às 3h40: 30 · 3 = 90; 5,5 · 40 = 220; diferença = 130°.

> [EXEMPLO] Um relógio adianta 3 minutos por hora e foi acertado ao meio-dia. Às 20h do mesmo dia ele marcará: 8 h · 3 min = 24 min de adiantamento → 20h24.

### 6.3 Orientação espacial

| Giro a partir do Norte | Horário (direita) | Anti-horário (esquerda) |
|---|---|---|
| 90° | Leste | Oeste |
| 180° | Sul | Sul |
| 270° | Oeste | Leste |

> [EXEMPLO] Pedro está voltado para o norte, gira 90° à direita e depois 270° à esquerda. Saldo: +90° − 270° = −180°. Ele fica voltado para o sul.

> [DICA] Converta tudo em graus no sentido horário (esquerda = negativo) e some. O resto da divisão por 360° dá a posição final.
