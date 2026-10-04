## 7. Números inteiros e racionais, expressões, MMC e MDC

> [SINTESE] Base aritmética de toda a prova.
> • Conjuntos: naturais (N), inteiros (Z), racionais (Q = frações e dízimas periódicas).
> • Ordem das operações: parênteses → potências e raízes → multiplicação e divisão (da esquerda para a direita) → adição e subtração.
> • Divisibilidade e fatoração em primos alimentam MMC, MDC e contagem de divisores.
> • MMC: eventos que se repetem e voltam a coincidir. MDC: dividir em partes iguais, as maiores possíveis.

### 7.1 Conjuntos e regras de sinais

| Conjunto | Elementos | Exemplo de pegadinha |
|---|---|---|
| **N** (naturais) | 0, 1, 2, 3, ... | 0 é natural |
| **Z** (inteiros) | ..., −2, −1, 0, 1, 2, ... | −3 < −1 (mais distante do zero é menor) |
| **Q** (racionais) | a/b, com b ≠ 0; decimais exatos; dízimas periódicas | 0,333... = 1/3 é racional |
| **Irracionais** | Dízimas não periódicas | √2, π |

| Operação | Sinais iguais | Sinais diferentes |
|---|---|---|
| Multiplicação e divisão | Resultado positivo | Resultado negativo |
| Adição | Soma e mantém o sinal | Subtrai e fica o sinal do maior em módulo |
| Potência de base negativa | Expoente par: positivo | Expoente ímpar: negativo |

> [ATENCAO] (−2)² = 4, mas −2² = −4 (o expoente atinge só o 2). A FCC explora essa diferença nas expressões numéricas.

> [EXEMPLO] 18 ÷ 3 · 2 − (5 − 2³) = ?
> • Parênteses: 2³ = 8; 5 − 8 = −3.
> • Divisão e multiplicação da esquerda para a direita: 18 ÷ 3 = 6; 6 · 2 = 12.
> • 12 − (−3) = 15.
> • Erro clássico: fazer 3 · 2 primeiro (18 ÷ 6 = 3) e chegar a 6.

### 7.2 Critérios de divisibilidade

| Divisível por | Critério | Exemplo |
|---|---|---|
| **2** | Termina em algarismo par | 1.354 |
| **3** | Soma dos algarismos divisível por 3 | 1.236 (1+2+3+6 = 12) |
| **4** | Dois últimos algarismos formam múltiplo de 4 (ou 00) | 3.516 (16) |
| **5** | Termina em 0 ou 5 | 2.345 |
| **6** | Divisível por 2 e por 3 | 1.236 |
| **8** | Três últimos algarismos formam múltiplo de 8 | 7.128 (128) |
| **9** | Soma dos algarismos divisível por 9 | 4.536 (4+5+3+6 = 18) |
| **10** | Termina em 0 | 4.370 |
| **11** | Diferença entre soma dos algarismos de ordem ímpar e de ordem par é múltiplo de 11 (inclui 0) | 2.728 (8+7) − (2+2) = 11 |

### 7.3 Múltiplos, divisores e número de divisores

| Conceito | Definição | Exemplo |
|---|---|---|
| **Múltiplo** | a é múltiplo de b se a = b · k, com k inteiro | 35 é múltiplo de 7 |
| **Divisor** | b divide a se a divisão é exata | 7 é divisor de 35 |
| **Primo** | Exatamente dois divisores naturais (1 e ele mesmo) | 2, 3, 5, 7, 11, 13 (2 é o único primo par) |
| **Nº de divisores** | Se n = pᵃ · qᵇ · rᶜ, o nº de divisores positivos é (a+1)(b+1)(c+1) | 360 = 2³ · 3² · 5 → 4 · 3 · 2 = 24 divisores |

> [ATENCAO] 1 não é primo nem composto. Para saber se um número é primo, basta testar divisores primos até a sua raiz quadrada.

### 7.4 MMC e MDC

| Item | MMC | MDC |
|---|---|---|
| **Definição** | Menor múltiplo comum positivo | Maior divisor comum |
| **Pela fatoração** | Todos os fatores primos, cada um com o MAIOR expoente | Só os fatores comuns, cada um com o MENOR expoente |
| **Problema típico** | Eventos periódicos que voltam a coincidir | Cortar, repartir ou agrupar em partes iguais e máximas, sem sobra |
| **Palavras-gatilho** | "novamente juntos", "próxima vez", "coincidir" | "maior tamanho possível", "menor número de pacotes", "sem sobras" |
| **Relação** | MMC(a, b) · MDC(a, b) = a · b (vale para dois números) | — |

> [EXEMPLO] (MMC) Três linhas de ônibus partem juntas do terminal às 6h, com intervalos de 12, 18 e 30 minutos. Quando partirão juntas de novo?
> • 12 = 2² · 3; 18 = 2 · 3²; 30 = 2 · 3 · 5.
> • MMC = 2² · 3² · 5 = 180 min = 3 h. Próxima partida conjunta: 9h.

> [EXEMPLO] (MDC) Duas fitas de 84 cm e 120 cm serão cortadas em pedaços iguais, do maior tamanho possível, sem sobra.
> • 84 = 2² · 3 · 7; 120 = 2³ · 3 · 5. MDC = 2² · 3 = 12 cm.
> • Número de pedaços: 84 ÷ 12 + 120 ÷ 12 = 7 + 10 = 17.

> [PROVA] A FCC gosta de combinar MMC com calendário: "as três rotinas coincidiram numa segunda-feira; a próxima coincidência será em que dia da semana?" Ache o MMC em dias e tire o resto por 7.

> [DICA] Erros que viram alternativas: somar os intervalos (12 + 18 + 30), multiplicá-los (12 · 18 · 30) ou usar o MDC no lugar do MMC. O MMC nunca é menor que o maior dos números, e o MDC nunca é maior que o menor deles.

## 8. Frações e problemas com frações

> [SINTESE] Fração = parte de um todo.
> • Somar/subtrair: igualar denominadores (MMC). Multiplicar: numerador × numerador, denominador × denominador. Dividir: multiplicar pelo inverso.
> • "Fração do restante" se resolve multiplicando as frações que SOBRAM em cada etapa.
> • Dízima periódica vira fração pela regra da geratriz.

### 8.1 Operações e geratriz

| Operação | Regra | Exemplo |
|---|---|---|
| **Soma** | MMC dos denominadores | 1/4 + 2/3 = 3/12 + 8/12 = 11/12 |
| **Multiplicação** | Direta | 2/3 · 9/10 = 18/30 = 3/5 |
| **Divisão** | Conserva a primeira, inverte a segunda | (3/4) ÷ (1/2) = 3/4 · 2 = 3/2 |
| **"Fração de"** | "de" = multiplicação | 2/5 de 300 = 120 |
| **Dízima simples** | Período sobre tantos 9 quantos forem os algarismos do período | 0,333... = 3/9 = 1/3; 0,1515... = 15/99 = 5/33 |
| **Dízima composta** | (parte não periódica seguida do período − parte não periódica) sobre 9s do período seguidos de 0s da parte não periódica | 0,1222... = (12 − 1)/90 = 11/90 |

### 8.2 Fração do total × fração do restante

> [EXEMPLO] Ana gastou 2/5 do que tinha com aluguel e 1/3 do restante com alimentação, ficando com R$ 1.200,00. Quanto tinha?
> • Após o aluguel sobram 3/5. A alimentação consome 1/3 desses 3/5, sobrando 2/3 deles.
> • Fração final que sobra: 3/5 · 2/3 = 6/15 = 2/5 do total.
> • 2/5 · x = 1.200 → x = 1.200 · 5 ÷ 2 = R$ 3.000,00.
> • Erro clássico: somar 2/5 + 1/3 = 11/15 (como se ambas fossem do total), sobrando 4/15 → x = R$ 4.500,00.

| Expressão no enunciado | Tratamento |
|---|---|
| "gastou 1/3 do salário e 1/4 do salário" | Ambas sobre o total: soma 1/3 + 1/4 |
| "gastou 1/3 e depois 1/4 do restante" | Multiplica o que sobra: 2/3 · 3/4 |
| "restaram R$ X" | X corresponde à fração final que sobra |
| "gastou R$ X na 2ª etapa" | X corresponde à fração gasta naquela etapa |

> [DICA] Método rápido: escreva só as frações que SOBRAM em cada etapa e multiplique. Gastou 1/4 → sobra 3/4; gastou 2/5 do resto → sobra 3/5; a fração final é o produto.

### 8.3 Problemas de trabalho conjunto (torneiras, servidores)

| Situação | Fórmula | Exemplo |
|---|---|---|
| Dois agentes juntos | 1/t = 1/a + 1/b, ou t = ab ÷ (a + b) | Torneiras de 3 h e 6 h: t = 18 ÷ 9 = 2 h |
| Um enche, outro esvazia | 1/t = 1/a − 1/b | Enche em 4 h, esvazia em 12 h: 1/t = 3/12 − 1/12 = 1/6 → 6 h |

## 9. Razões, proporções, divisão proporcional e regra de três

> [SINTESE] Razão = quociente a/b. Proporção = igualdade de razões (a/b = c/d ↔ a · d = b · c).
> • Grandezas diretamente proporcionais: uma dobra, a outra dobra (razão constante).
> • Inversamente proporcionais: uma dobra, a outra cai à metade (produto constante).
> • Divisão proporcional: total ÷ soma dos pesos = constante k.
> • Regra de três composta: compare cada grandeza com a incógnita, uma por vez.

### 9.1 Razão e proporção

| Conceito | Definição | Exemplo |
|---|---|---|
| **Razão** | a/b, b ≠ 0 | 15 homens para 10 mulheres = 3/2 |
| **Proporção** | a/b = c/d | 3/4 = 9/12 |
| **Propriedade fundamental** | Produto dos meios = produto dos extremos | 3 · 12 = 4 · 9 |
| **Propriedade da soma** | a/b = c/d = (a + c)/(b + d) | Base da divisão proporcional |
| **Escala** | Desenho ÷ real (mesma unidade) | 1:50.000 → 1 cm = 500 m |
| **Velocidade média** | Distância ÷ tempo | 240 km em 3 h = 80 km/h |

> [EXEMPLO] Numa vara, a razão entre processos físicos e eletrônicos é 2/7 e há 360 processos ao todo. Físicos = 360 · 2/9 = 80; eletrônicos = 280.

### 9.2 Divisão proporcional

| Tipo | Procedimento | Exemplo |
|---|---|---|
| **Direta** | k = total ÷ (soma dos pesos); cada parte = peso · k | R$ 18.000 em partes proporcionais a 2, 3 e 4: k = 18.000 ÷ 9 = 2.000 → 4.000, 6.000, 8.000 |
| **Inversa** | Use os inversos dos números como pesos (multiplique pelo MMC para tirar frações) | R$ 1.300 inversamente a 2, 3 e 4: pesos 1/2, 1/3, 1/4 → ×12 → 6, 4, 3; k = 1.300 ÷ 13 = 100 → 600, 400, 300 |
| **Composta** | Peso = (grandeza direta) ÷ (grandeza inversa) | Ver exemplo abaixo |

> [EXEMPLO] (Composta) Prêmio de R$ 5.400 dividido em partes diretamente proporcionais ao nº de processos baixados e inversamente proporcionais ao nº de faltas. Ana: 30 processos, 2 faltas; Bruno: 40 processos, 4 faltas; Carla: 20 processos, 1 falta.
> • Pesos: 30/2 = 15; 40/4 = 10; 20/1 = 20. Soma = 45.
> • k = 5.400 ÷ 45 = 120 → Ana R$ 1.800; Bruno R$ 1.200; Carla R$ 2.400.

> [ATENCAO] Na divisão inversa, quem tem o MAIOR número recebe a MENOR parte. Se a alternativa dá mais dinheiro a quem teve mais faltas, o candidato fez divisão direta por engano. E nunca some os números originais (2 + 3 + 4) na divisão inversa: some os inversos já ajustados (6 + 4 + 3).

### 9.3 Regra de três simples

| Tipo | Relação | Montagem |
|---|---|---|
| **Direta** | Mais causa → mais efeito (ex.: mais páginas → mais tempo) | Multiplica cruzado |
| **Inversa** | Mais agentes → menos tempo (ex.: mais operários → menos dias) | Multiplica em linha (produto constante) |

> [EXEMPLO] 6 operários fazem uma obra em 20 dias. Com 8 operários (inversa): 6 · 20 = 8 · x → x = 15 dias.

### 9.4 Regra de três composta

Roteiro: (1) monte a tabela com as grandezas em colunas; (2) isole a coluna da incógnita; (3) compare cada outra grandeza com a incógnita, considerando as demais fixas, e marque D (direta) ou I (inversa); (4) multiplique o valor conhecido da incógnita pelas razões, invertendo as inversas.

> [EXEMPLO] 8 operários, trabalhando 6 h por dia, constroem 120 m de muro em 10 dias. Em quantos dias 12 operários, trabalhando 8 h por dia, construirão 360 m?
> • Operários × dias: mais operários, menos dias (I) → fator 8/12.
> • Horas × dias: mais horas por dia, menos dias (I) → fator 6/8.
> • Metros × dias: mais metros, mais dias (D) → fator 360/120.
> • x = 10 · (8/12) · (6/8) · (360/120) = 10 · (2/3) · (3/4) · 3 = 15 dias.

| Operários | Horas/dia | Metros | Dias |
|---|---|---|---|
| 8 | 6 | 120 | 10 |
| 12 | 8 | 360 | x |
| I | I | D | — |

> [DICA] Método "causa ÷ efeito" (homem-hora): o produto das grandezas que TRABALHAM (operários · horas/dia · dias) dividido pelo que é PRODUZIDO (metros, páginas, processos) é constante.
> 8 · 6 · 10 ÷ 120 = 4 e 12 · 8 · x ÷ 360 = 4 → 96x = 1.440 → x = 15. Não exige decidir direta/inversa.

> [PROVA] Na regra de três composta, a FCC monta as alternativas erradas tratando uma grandeza inversa como direta ou ignorando uma das grandezas. Confira o resultado pelo método homem-hora.

## 10. Porcentagem, acréscimos e descontos sucessivos

> [SINTESE] Porcentagem = razão de denominador 100.
> • Trabalhe sempre com o fator multiplicativo: aumento de i% → (1 + i); desconto de i% → (1 − i).
> • Variações sucessivas se MULTIPLICAM, nunca se somam.
> • Variação percentual = (final − inicial) ÷ inicial.
> • Pontos percentuais ≠ porcentagem.

### 10.1 Fator multiplicativo

| Situação | Fator | Exemplo |
|---|---|---|
| Aumento de 15% | 1,15 | R$ 200 → 200 · 1,15 = R$ 230 |
| Desconto de 15% | 0,85 | R$ 200 → 200 · 0,85 = R$ 170 |
| Aumento de 100% | 2 | Dobra |
| Desconto de 100% | 0 | Zera |
| x% de y% | x · y ÷ 100 | 30% de 40% = 12% |

### 10.2 Variações sucessivas

| Sequência | Cálculo | Resultado | Erro típico (alternativa falsa) |
|---|---|---|---|
| +20% e −20% | 1,2 · 0,8 = 0,96 | Perda de 4% | "Volta ao preço original" |
| −10% e −20% | 0,9 · 0,8 = 0,72 | Desconto total de 28% | 30% |
| +10% e +5% | 1,1 · 1,05 = 1,155 | Aumento total de 15,5% | 15% |
| +25% e −20% | 1,25 · 0,8 = 1,00 | Preço inalterado | +5% |
| −20% e quanto para voltar? | 1 ÷ 0,8 = 1,25 | Aumento de 25% | 20% |

> [EXEMPLO] Um salário de R$ 4.000 recebeu reajuste de 10% em março e de 5% em setembro. Valor final: 4.000 · 1,1 · 1,05 = 4.000 · 1,155 = R$ 4.620. Aumento acumulado: 15,5%.

> [EXEMPLO] Preço caiu de R$ 300 para R$ 250: variação = (250 − 300) ÷ 300 = −16,67%. Se subir de R$ 250 para R$ 300: (300 − 250) ÷ 250 = +20%. A base da porcentagem é sempre o valor INICIAL.

> [ATENCAO] Para descobrir o valor original a partir do valor com desconto, DIVIDA pelo fator: produto pago R$ 340 com 15% de desconto → original = 340 ÷ 0,85 = R$ 400. Somar 15% a R$ 340 (= R$ 391) é o erro que vira alternativa.

### 10.3 Lucro, pontos percentuais

| Conceito | Cálculo | Exemplo |
|---|---|---|
| **Lucro sobre o custo** | lucro ÷ custo | Custo 80, venda 100: 20 ÷ 80 = 25% |
| **Lucro sobre a venda** | lucro ÷ venda | Mesmo caso: 20 ÷ 100 = 20% |
| **Pontos percentuais (p.p.)** | Diferença entre duas taxas | Taxa de 10% para 12%: +2 p.p. |
| **Variação relativa da taxa** | (nova − antiga) ÷ antiga | De 10% para 12%: aumento de 20% |

## 11. Estatística descritiva e leitura de gráficos

> [SINTESE] Medidas de posição: média (simples e ponderada), moda, mediana.
> • Medidas de dispersão: amplitude, desvio médio, variância, desvio padrão.
> • Tabelas de frequência: use frequência acumulada para achar a mediana.
> • Gráficos: setor = fração · 360°; histograma = classes contíguas; atenção à escala e à unidade.

### 11.1 Medidas de posição

| Medida | Definição | Observação de prova |
|---|---|---|
| **Média aritmética simples** | Soma dos valores ÷ quantidade | Sensível a valores extremos |
| **Média ponderada** | Soma (valor · peso) ÷ soma dos pesos | Média de grupos com tamanhos diferentes é ponderada |
| **Moda** | Valor mais frequente | Pode haver mais de uma (bimodal) ou nenhuma (amodal) |
| **Mediana** | Valor central do rol ordenado; com n par, média dos dois centrais | Ordene antes; não é afetada por extremos |

> [EXEMPLO] (Média ponderada) Provas com pesos 2, 3 e 5; notas 6, 7 e 8. Média = (2·6 + 3·7 + 5·8) ÷ (2 + 3 + 5) = (12 + 21 + 40) ÷ 10 = 7,3. A média simples seria 7,0.

> [EXEMPLO] (Média de grupos) Turma A: 20 alunos, média 7. Turma B: 30 alunos, média 8. Média geral = (20·7 + 30·8) ÷ 50 = (140 + 240) ÷ 50 = 7,6. A "média das médias" (7,5) está errada porque os grupos têm tamanhos diferentes.

> [EXEMPLO] (Inclusão de elemento) A média de 10 números é 15 (soma 150). Acrescentando 26: (150 + 26) ÷ 11 = 176 ÷ 11 = 16.

> [DICA] Em problemas de média, trabalhe com a SOMA (média · quantidade). Inclusões, exclusões e trocas de valores alteram a soma, e a nova média é a nova soma dividida pela nova quantidade.

### 11.2 Medidas de dispersão

| Medida | Cálculo | Unidade |
|---|---|---|
| **Amplitude** | Maior valor − menor valor | Mesma dos dados |
| **Desvio médio** | Média dos módulos dos desvios em relação à média | Mesma dos dados |
| **Variância (populacional)** | Média dos quadrados dos desvios: soma dos (xᵢ − média)² ÷ n | Unidade ao quadrado |
| **Variância (amostral)** | Soma dos (xᵢ − média)² ÷ (n − 1) | Unidade ao quadrado |
| **Desvio padrão** | Raiz quadrada da variância | Mesma dos dados |

> [EXEMPLO] Dados: 2, 4, 4, 6, 9 (n = 5).
> • Média = 25 ÷ 5 = 5. Moda = 4. Mediana = 4 (3º termo). Amplitude = 9 − 2 = 7.
> • Desvios: −3, −1, −1, 1, 4 (somam zero, sempre).
> • Desvio médio = (3 + 1 + 1 + 1 + 4) ÷ 5 = 10 ÷ 5 = 2.
> • Quadrados: 9, 1, 1, 1, 16 → soma 28. Variância populacional = 28 ÷ 5 = 5,6; desvio padrão ≈ 2,37.
> • Se for amostra: variância = 28 ÷ 4 = 7; desvio padrão ≈ 2,65.

| Transformação nos dados | Média | Desvio padrão | Variância |
|---|---|---|---|
| Somar k a todos | + k | Não muda | Não muda |
| Multiplicar todos por k | · k | · k (em módulo) | · k² |

> [PROVA] Propriedade cobrada: somar uma constante a todos os valores (ex.: "cada servidor recebeu R$ 300 de abono") desloca média, moda e mediana, mas NÃO altera amplitude, desvio padrão nem variância.

### 11.3 Tabelas de frequência

| Faltas no mês | Servidores (fᵢ) | Frequência acumulada | Faltas · fᵢ |
|---|---|---|---|
| 0 | 5 | 5 | 0 |
| 1 | 8 | 13 | 8 |
| 2 | 4 | 17 | 8 |
| 3 | 3 | 20 | 9 |
| **Total** | **20** | — | **25** |

> [EXEMPLO] Na tabela acima: moda = 1 (maior frequência, 8). Mediana: n = 20, centrais são o 10º e o 11º; a acumulada mostra que as posições 6 a 13 valem 1 → mediana = 1. Média = 25 ÷ 20 = 1,25 falta.

> [ATENCAO] A mediana NÃO é o valor central da coluna de valores (0, 1, 2, 3 → 1,5). É o valor central dos 20 servidores ordenados. Esse é o erro mais explorado em tabelas de frequência.

### 11.4 Gráficos e infográficos

| Gráfico | Leitura | Pegadinha |
|---|---|---|
| **Setores (pizza)** | Ângulo = (parte ÷ total) · 360°; 1% = 3,6° | Ângulo de 90° = 25%, não 90% |
| **Barras/colunas** | Altura = valor | Eixo que não começa no zero exagera diferenças |
| **Linhas** | Evolução no tempo | Inclinação maior = variação absoluta maior, não necessariamente percentual |
| **Histograma** | Colunas contíguas para classes de valores; área proporcional à frequência | Classes de amplitudes diferentes: compare áreas, não alturas |
| **Infográfico/tabela** | Combina números, ícones e textos | Unidades (mil, milhões), base da porcentagem, notas de rodapé |

> [EXEMPLO] Num gráfico de setores sobre 400 processos, o setor "Execução" mede 54°. Fração = 54 ÷ 360 = 15% → 0,15 · 400 = 60 processos. Inversamente, uma categoria com 20% dos dados ocupa 0,2 · 360 = 72°.

> [DICA] Antes de calcular, leia título, legenda, unidade e fonte. Grande parte das questões de gráfico se resolve com uma regra de três ou uma porcentagem simples; o difícil é extrair o número certo.
