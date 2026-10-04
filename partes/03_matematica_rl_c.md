## Questões comentadas — estilo FCC

### Questão 1 — FCC · Analista Judiciário (estilo TRT)

Considere a afirmação: "Se Tereza termina o relatório, então ela sai mais cedo". Uma afirmação que corresponde à negação lógica da afirmação anterior é:

(A) Se Tereza não termina o relatório, então ela não sai mais cedo.
(B) Tereza termina o relatório e não sai mais cedo.
(C) Tereza não termina o relatório e sai mais cedo.
(D) Se Tereza não sai mais cedo, então ela não termina o relatório.
(E) Tereza não termina o relatório ou não sai mais cedo.

**Gabarito: B**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. É a inversa (~p → ~q), outra condicional; não é negação nem equivalente. Basta ver que ambas podem ser V ao mesmo tempo (Tereza termina e sai cedo). |
| **(B)** | Correta. Passo a passo: p = "termina o relatório"; q = "sai mais cedo". ~(p → q) ≡ p ∧ ~q: mantém o antecedente, troca "se...então" por "e" e nega o consequente. É a única linha que torna a condicional falsa (V → F). |
| **(C)** | Errada. Corresponde a ~p ∧ q, que é exatamente uma linha em que a condicional original é VERDADEIRA (F → V = V). Erro: negar a parte errada. |
| **(D)** | Errada. É a contrapositiva (~q → ~p), EQUIVALENTE à original, e não sua negação. |
| **(E)** | Errada. ~p ∨ ~q é a negação de "p e q" (De Morgan), não de "se p, então q". Erro: aplicar De Morgan à condicional. |

### Questão 2 — FCC · Técnico Judiciário (estilo TRT)

Considere verdadeiras as premissas: "Todo oficial de justiça avaliador é bacharel em Direito" e "Algum servidor do setor X não é bacharel em Direito". A partir delas, é necessariamente verdadeiro que:

(A) Nenhum servidor do setor X é oficial de justiça avaliador.
(B) Algum oficial de justiça avaliador não é servidor do setor X.
(C) Todo bacharel em Direito é oficial de justiça avaliador.
(D) Algum servidor do setor X não é oficial de justiça avaliador.
(E) Algum bacharel em Direito é servidor do setor X.

**Gabarito: D**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Os oficiais estão dentro do círculo dos bacharéis; nada impede que o setor X tenha bacharéis oficiais, desde que tenha também um não bacharel. A frase é possível, não necessária. |
| **(B)** | Errada. As premissas nada dizem sobre os oficiais fora do setor X; pode ser que todos os oficiais sejam do setor X. |
| **(C)** | Errada. É a recíproca da 1ª premissa: "todo A é B" não autoriza "todo B é A". |
| **(D)** | Correta. Diagrama: Oficiais ⊂ Bacharéis. Existe um servidor do setor X fora do círculo dos Bacharéis; logo, está também fora do círculo dos Oficiais (que fica dentro dele). Esse servidor garante "algum servidor do setor X não é oficial". |
| **(E)** | Errada. A 2ª premissa garante um servidor do setor X FORA dos bacharéis; não garante nenhum dentro. Pode não haver interseção entre bacharéis e o setor X. |

### Questão 3 — FCC · Analista Judiciário (estilo TRT)

Considere as afirmações:

I. A negação de "Todo servidor da vara é pontual" é "Algum servidor da vara não é pontual".
II. "Se Bruno é técnico, então Carla é analista" é equivalente a "Se Carla não é analista, então Bruno não é técnico".
III. "Não é verdade que Bruno é técnico e Carla é analista" é equivalente a "Bruno não é técnico e Carla não é analista".

Está correto o que se afirma em

(A) I, apenas.
(B) I e II, apenas.
(C) I e III, apenas.
(D) II e III, apenas.
(E) I, II e III.

**Gabarito: B**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Desconsidera que II também está correta (contrapositiva). |
| **(B)** | Correta. I: a negação de "todo A é B" é "algum A não é B" (basta um contraexemplo). II: p → q ≡ ~q → ~p (contrapositiva). III está errada: pelo De Morgan, ~(p ∧ q) ≡ ~p ∨ ~q; o correto seria "Bruno não é técnico OU Carla não é analista". |
| **(C)** | Errada. III mantém o "e" após negar as partes; teste: com Bruno técnico (V) e Carla não analista, a 1ª frase de III é V e a 2ª é F, logo não são equivalentes. |
| **(D)** | Errada. Exclui I (correta) e inclui III (errada). |
| **(E)** | Errada. III está incorreta pelo motivo exposto em (C). |

### Questão 4 — FCC · Técnico Judiciário (estilo TRT)

Um dos quatro servidores — Ana, Bruno, Carla ou Davi — esqueceu aberta a sala de audiências. Questionados, disseram:
Ana: "Foi o Bruno."
Bruno: "Foi o Davi."
Carla: "Não fui eu."
Davi: "O Bruno está mentindo."
Sabendo que apenas um deles disse a verdade, quem esqueceu a sala aberta e quem disse a verdade são, respectivamente,

(A) Ana e Carla.
(B) Bruno e Ana.
(C) Davi e Bruno.
(D) Carla e Bruno.
(E) Carla e Davi.

**Gabarito: E**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Hipótese culpada = Ana: Ana F, Bruno F, Carla "não fui eu" V, Davi "Bruno mente" V → duas verdades, contrariando o enunciado. |
| **(B)** | Errada. Culpado = Bruno: Ana V, Bruno F, Carla V, Davi V → três verdades. |
| **(C)** | Errada. Culpado = Davi: Ana F, Bruno V, Carla V, Davi F → duas verdades. |
| **(D)** | Errada. A culpada está certa, mas Bruno ("Foi o Davi") mente quando a culpada é Carla. Alternativa que acerta só metade. |
| **(E)** | Correta. Passo a passo: Bruno e Davi formam par contraditório (Davi diz que Bruno mente), então exatamente um deles fala a verdade. Como só há uma verdade, Ana e Carla mentem. Carla mente em "não fui eu" → Carla é a culpada. Conferência: Ana F (não foi Bruno), Bruno F (não foi Davi), Carla F, Davi V. Uma única verdade: Davi. |

### Questão 5 — FCC · Oficial de Justiça Avaliador Federal (estilo TRT)

Três oficiais de justiça — Lúcia, Márcio e Tereza — cumprem mandados, cada um em um bairro diferente (Nazaré, Marco e Umarizal) e cada um usando um meio de transporte diferente (carro, moto e ônibus). Sabe-se que:
I. Lúcia não atua em Nazaré nem no Marco.
II. Quem atua em Nazaré usa ônibus.
III. Tereza usa carro.
Com base nessas informações, é correto afirmar que

(A) Tereza atua no Marco e Lúcia usa moto.
(B) Márcio atua no Marco e usa ônibus.
(C) Lúcia atua no Umarizal e usa carro.
(D) quem atua no Umarizal usa ônibus.
(E) Tereza atua em Nazaré e usa carro.

**Gabarito: A**

| Alternativa | Análise |
|---|---|
| **(A)** | Correta. Passo a passo: (I) Lúcia = Umarizal. (III) Tereza usa carro; por (II), quem atua em Nazaré usa ônibus, logo Tereza não está em Nazaré → Tereza = Marco. Sobra Nazaré para Márcio, que usa ônibus (II). Sobra moto para Lúcia. Gabarito final: Lúcia–Umarizal–moto; Márcio–Nazaré–ônibus; Tereza–Marco–carro. |
| **(B)** | Errada. Márcio usa ônibus, mas atua em Nazaré; o Marco é de Tereza. |
| **(C)** | Errada. Lúcia atua no Umarizal, mas o carro é de Tereza (III). |
| **(D)** | Errada. O ônibus é de quem atua em Nazaré (II); no Umarizal, Lúcia usa moto. |
| **(E)** | Errada. Contradiz (II): quem atua em Nazaré usa ônibus, e Tereza usa carro. |

### Questão 6 — FCC · Técnico Judiciário (estilo TRT)

Considere a sequência de números que obedece a uma lei de formação: (5, 9, 7, 11, 9, 13, 11, ...). O 40º termo dessa sequência é

(A) 43.
(B) 45.
(C) 49.
(D) 47.
(E) 85.

**Gabarito: D**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. 43 é o 39º termo: aplicou a fórmula dos termos de posição ímpar (5, 7, 9, ... → 5 + 2 · 19 = 43) ao termo de posição par. |
| **(B)** | Errada. Raciocinou "a sequência sobe 2 a cada par; 20 pares → 5 + 2 · 20 = 45", que é o 41º termo (erro de contagem de pares). |
| **(C)** | Errada. Usou k em vez de (k − 1) na PA dos pares: 9 + 2 · 20 = 49, que é o 42º termo. |
| **(D)** | Correta. Passo a passo: a lei é +4, −2 alternados. Termos de posição par: 9, 11, 13, ... (PA de razão 2). O 40º termo é o 20º termo par: a₂₀ = 9 + (20 − 1) · 2 = 9 + 38 = 47. |
| **(E)** | Errada. Supôs aumento de 2 a cada termo a partir do 2º: 9 + 38 · 2 = 85. A variação líquida de +2 ocorre a cada DOIS termos. |

### Questão 7 — FCC · Analista Judiciário (estilo TRT)

Considerando o alfabeto oficial de 26 letras, as duas letras que completam corretamente a sequência (B, E, D, G, F, I, H, ..., ...) são, respectivamente,

(A) L e J.
(B) J e I.
(C) K e J.
(D) L e K.
(E) K e M.

**Gabarito: C**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Resulta do alfabeto de 23 letras (sem K): de H, avançando 3 (I, J, L) chega-se a L e, recuando 1, a J. O enunciado manda usar 26 letras. |
| **(B)** | Errada. Aplicou +2 em vez de +3: H(8) + 2 = J(10); J − 1 = I. |
| **(C)** | Correta. Passo a passo: posições 2, 5, 4, 7, 6, 9, 8 → padrão +3, −1. Próximos: 8 + 3 = 11 (K) e 11 − 1 = 10 (J). |
| **(D)** | Errada. Aplicou +4 (8 + 4 = 12 = L) e −1 (11 = K). |
| **(E)** | Errada. Acertou K, mas aplicou +2 em seguida (13 = M), ignorando a alternância com −1. |

### Questão 8 — FCC · Técnico Judiciário (estilo TRT)

Em certo ano não bissexto, o dia 1º de fevereiro caiu numa segunda-feira. Nesse mesmo ano, o dia 1º de maio caiu numa

(A) quarta-feira.
(B) sexta-feira.
(C) domingo.
(D) segunda-feira.
(E) sábado.

**Gabarito: E**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Considerou todos os meses com 31 dias: 93 dias = 7 · 13 + 2 → segunda + 2 = quarta. |
| **(B)** | Errada. Contou só até 30 de abril (88 dias = 7 · 12 + 4) → segunda + 4 = sexta. |
| **(C)** | Errada. Tratou o ano como bissexto (fevereiro com 29): 90 dias = 7 · 12 + 6 → domingo. |
| **(D)** | Errada. Supôs que três meses equivalem a 13 semanas exatas (91 dias, resto 0). |
| **(E)** | Correta. Passo a passo: de 1º/2 a 1º/5 = 28 (fevereiro) + 31 (março) + 30 (abril) = 89 dias. 89 = 7 · 12 + 5. Segunda + 5 = sábado. |

### Questão 9 — FCC · Analista Judiciário (estilo TRT)

No setor de informática de um tribunal, a rotina A de cópia de segurança é executada a cada 8 dias, a rotina B a cada 12 dias e a rotina C a cada 20 dias. As três rotinas foram executadas juntas numa segunda-feira. A próxima vez em que as três serão executadas no mesmo dia cairá numa

(A) terça-feira.
(B) quarta-feira.
(C) sexta-feira.
(D) sábado.
(E) segunda-feira.

**Gabarito: A**

| Alternativa | Análise |
|---|---|
| **(A)** | Correta. Passo a passo: 8 = 2³; 12 = 2² · 3; 20 = 2² · 5. MMC = 2³ · 3 · 5 = 120 dias. 120 = 7 · 17 + 1 → segunda + 1 = terça-feira. |
| **(B)** | Errada. Multiplicou os intervalos (8 · 12 · 20 = 1.920 = 7 · 274 + 2) ou errou o MMC para 240; ambos dão resto 2 → quarta. |
| **(C)** | Errada. Usou o MDC (4 dias) no lugar do MMC: segunda + 4 = sexta. |
| **(D)** | Errada. Somou os intervalos: 8 + 12 + 20 = 40 = 7 · 5 + 5 → sábado. |
| **(E)** | Errada. Supôs, sem calcular, que o ciclo fecharia em semanas completas. 120 não é múltiplo de 7. |

### Questão 10 — FCC · Técnico Judiciário (estilo TRT)

Carla recebeu seu salário e gastou 1/4 com aluguel, 2/5 do restante com alimentação e 1/3 do que sobrou com transporte, restando-lhe R$ 1.800,00. O salário de Carla é de

(A) R$ 4.000,00.
(B) R$ 6.000,00.
(C) R$ 9.000,00.
(D) R$ 12.000,00.
(E) R$ 108.000,00.

**Gabarito: B**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Esqueceu a etapa do transporte: (3/4) · (3/5) = 9/20; 9/20 · x = 1.800 → x = 4.000. |
| **(B)** | Correta. Passo a passo pelas frações que sobram: aluguel → sobra 3/4; alimentação → sobra 3/5 do resto; transporte → sobra 2/3 do resto. Fração final: 3/4 · 3/5 · 2/3 = 18/60 = 3/10. 3/10 · x = 1.800 → x = 1.800 · 10 ÷ 3 = 6.000. Conferência: 6.000 − 1.500 = 4.500; 4.500 − 1.800 = 2.700; 2.700 − 900 = 1.800. |
| **(C)** | Errada. Usou a fração gasta (2/5) como se fosse a que sobra: 3/4 · 2/5 · 2/3 = 1/5 → x = 9.000. |
| **(D)** | Errada. Usou 1/3 (gasto) como sobra na última etapa: 3/4 · 3/5 · 1/3 = 3/20 → x = 12.000. |
| **(E)** | Errada. Somou as frações como se todas incidissem sobre o total: 1/4 + 2/5 + 1/3 = 59/60, sobrando 1/60 → x = 108.000. |

### Questão 11 — FCC · Analista Judiciário (estilo TRT)

Em uma unidade judiciária, 8 servidores, trabalhando 6 horas por dia, digitalizam 3.000 páginas em 10 dias. Mantido o mesmo ritmo individual, 12 servidores, trabalhando 5 horas por dia, digitalizarão 4.500 páginas em

(A) 8 dias.
(B) 10 dias.
(C) 12 dias.
(D) 18 dias.
(E) 27 dias.

**Gabarito: C**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Ignorou o aumento de páginas: 10 · (8/12) · (6/5) = 8. |
| **(B)** | Errada. Ignorou a mudança de horas: 10 · (8/12) · (4.500/3.000) = 10. |
| **(C)** | Correta. Passo a passo: servidores × dias (inversa) → 8/12; horas × dias (inversa) → 6/5; páginas × dias (direta) → 4.500/3.000. x = 10 · (2/3) · (6/5) · (3/2) = 12. Conferência pelo método homem-hora: 8 · 6 · 10 = 480 servidor-hora para 3.000 páginas; 4.500 páginas exigem 720; 12 · 5 = 60 por dia → 720 ÷ 60 = 12 dias. |
| **(D)** | Errada. Ignorou o número de servidores: 10 · (6/5) · (3/2) = 18. |
| **(E)** | Errada. Tratou servidores como grandeza direta (mais servidores, mais dias): 10 · (12/8) · (6/5) · (3/2) = 27. |

### Questão 12 — FCC · Técnico Judiciário (estilo TRT)

O preço de um equipamento sofreu aumento de 25% em janeiro, desconto de 20% em fevereiro e novo aumento de 10% em março. Em relação ao preço vigente antes de janeiro, o preço após março é

(A) 15% maior.
(B) 5% maior.
(C) igual.
(D) 10% maior.
(E) 4,5% maior.

**Gabarito: D**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Somou as taxas: 25 − 20 + 10 = 15. Variações sucessivas se multiplicam. |
| **(B)** | Errada. Somou 25 − 20 = 5 e ainda esqueceu o aumento de março. |
| **(C)** | Errada. Calculou corretamente 1,25 · 0,8 = 1, mas esqueceu o aumento de março. |
| **(D)** | Correta. Passo a passo: fator total = 1,25 · 0,80 · 1,10. 1,25 · 0,80 = 1,00; 1,00 · 1,10 = 1,10 → 10% maior. Exemplo: R$ 100 → 125 → 100 → 110. |
| **(E)** | Errada. Achou que +25% e −20% geram perda de 5% (0,95) e aplicou março: 0,95 · 1,1 = 1,045. |

### Questão 13 — FCC · Analista Judiciário (estilo TRT)

Uma gratificação de R$ 3.900,00 será dividida entre três servidores em partes inversamente proporcionais ao número de faltas de cada um no semestre: 2, 3 e 4 faltas. O servidor que teve 2 faltas receberá

(A) R$ 866,67.
(B) R$ 900,00.
(C) R$ 1.200,00.
(D) R$ 1.300,00.
(E) R$ 1.800,00.

**Gabarito: E**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Fez divisão DIRETA: 3.900 · 2/9 = 866,67. Quem falta menos receberia menos, o oposto do enunciado. |
| **(B)** | Errada. É a parte de quem teve 4 faltas (3 · 300). |
| **(C)** | Errada. É a parte de quem teve 3 faltas (4 · 300). |
| **(D)** | Errada. Dividiu igualmente (3.900 ÷ 3), ignorando a proporcionalidade. |
| **(E)** | Correta. Passo a passo: pesos inversos 1/2, 1/3, 1/4; multiplicando pelo MMC 12 → 6, 4, 3 (soma 13). k = 3.900 ÷ 13 = 300. Partes: 6 · 300 = 1.800 (2 faltas); 4 · 300 = 1.200; 3 · 300 = 900. Soma = 3.900. |

### Questão 14 — FCC · Técnico Judiciário (estilo TRT)

Em um fórum, os 12 servidores do setor A têm média de idade de 30 anos e os 18 servidores do setor B têm média de idade de 40 anos. Se um servidor de 67 anos for lotado no setor B, a média de idade de todos os servidores dos dois setores passará a ser

(A) 37 anos.
(B) 36 anos.
(C) 35 anos.
(D) aproximadamente 38,2 anos.
(E) 51,5 anos.

**Gabarito: A**

| Alternativa | Análise |
|---|---|
| **(A)** | Correta. Passo a passo pelas somas: setor A = 12 · 30 = 360; setor B = 18 · 40 = 720; soma = 1.080 (média 1.080 ÷ 30 = 36). Com o novo servidor: 1.080 + 67 = 1.147; 1.147 ÷ 31 = 37. |
| **(B)** | Errada. É a média dos 30 servidores antes da lotação do novo servidor. |
| **(C)** | Errada. Fez a média das médias, (30 + 40) ÷ 2 = 35, ignorando os tamanhos dos grupos e o novo servidor. |
| **(D)** | Errada. Somou a idade do novo servidor mas não aumentou a quantidade: 1.147 ÷ 30 ≈ 38,2. |
| **(E)** | Errada. Fez a média entre a média antiga e a idade do novo servidor: (36 + 67) ÷ 2 = 51,5, como se ambos tivessem o mesmo peso. |

### Questão 15 — FCC · Analista Judiciário (estilo TRT)

A tabela mostra a distribuição dos 20 servidores de uma vara segundo o número de faltas no mês.

| Faltas | Nº de servidores |
|---|---|
| 0 | 6 |
| 1 | 9 |
| 2 | 3 |
| 3 | 2 |

Considere as afirmações:

I. A moda da distribuição é 1 falta.
II. A mediana da distribuição é 1,5 falta.
III. Em um gráfico de setores, o setor correspondente aos servidores sem faltas teria ângulo central de 108°.

Está correto o que se afirma em

(A) I, apenas.
(B) I e II, apenas.
(C) I e III, apenas.
(D) II e III, apenas.
(E) I, II e III.

**Gabarito: C**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Deixa de fora III, que está correta. |
| **(B)** | Errada. II é falsa: 1,5 é a média dos valores centrais da coluna "faltas" (1 e 2), e não a mediana dos 20 servidores. |
| **(C)** | Correta. I: a maior frequência (9) corresponde a 1 falta → moda 1. II: n = 20; centrais = 10º e 11º; acumuladas: 0 falta ocupa posições 1 a 6, 1 falta ocupa 7 a 15 → 10º e 11º valem 1 → mediana 1 (falsa a afirmação). III: 6 ÷ 20 = 30%; 0,30 · 360° = 108° (verdadeira). Para registro, a média é (0 + 9 + 6 + 6) ÷ 20 = 1,05. |
| **(D)** | Errada. Inclui II (falsa) e exclui I (verdadeira). |
| **(E)** | Errada. II é falsa, pelo erro de calcular a mediana sobre os valores distintos em vez de sobre o rol completo. |
