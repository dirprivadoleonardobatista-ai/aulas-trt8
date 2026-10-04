## Questões comentadas — estilo FCC

### Questão 1 — FCC · Técnico Judiciário – Agente da Polícia Judicial (estilo TRT)

A equipe de suporte de um Tribunal identificou um código malicioso que se propagava automaticamente pela rede interna, explorando uma vulnerabilidade do sistema operacional e enviando cópias de si mesmo de computador para computador, sem infectar arquivos e sem depender de que algum usuário o executasse. Esse código malicioso é classificado como

(A) vírus de macro.
(B) cavalo de troia.
(C) worm.
(D) rootkit.
(E) spyware.

**Gabarito: C**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. O vírus precisa de hospedeiro (no caso do vírus de macro, um documento) e depende da execução do arquivo infectado. |
| **(B)** | Errada. O cavalo de troia não se autopropaga: é instalado pela própria vítima, enganada por um programa aparentemente útil. |
| **(C)** | Correta. Propagação automática pela rede, envio de cópias de si mesmo, exploração de vulnerabilidade e ausência de hospedeiro são as notas do worm. |
| **(D)** | Errada. O rootkit serve para esconder e assegurar a presença do invasor, não para se propagar. |
| **(E)** | Errada. O spyware monitora atividades e envia informações a terceiros; não tem propagação automática. |

### Questão 2 — FCC · Analista Judiciário (estilo TRT)

Em uma Vara do Trabalho, adota-se a seguinte rotina: backup completo aos domingos e backup diferencial de segunda a sábado, sempre ao fim do expediente. Na quinta-feira pela manhã, antes do expediente, um ransomware tornou inacessíveis os arquivos do servidor. Para restaurar os dados na situação mais recente possível, será necessário utilizar

(A) somente o backup diferencial de quarta-feira, pois ele contém todos os arquivos do servidor.
(B) o backup completo de domingo e os diferenciais de segunda, terça e quarta-feira, aplicados nessa ordem.
(C) apenas os diferenciais de segunda, terça e quarta-feira, dispensado o completo.
(D) o backup completo de domingo e todos os backups incrementais da semana.
(E) o backup completo de domingo e o diferencial de quarta-feira.

**Gabarito: E**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. O diferencial contém apenas o que mudou desde o último completo, não todos os arquivos. |
| **(B)** | Errada. Como cada diferencial acumula todas as alterações desde o completo, os de segunda e terça são desnecessários; essa sequência descreve a lógica do incremental. |
| **(C)** | Errada. Sem o backup completo, falta a base sobre a qual as alterações se aplicam. |
| **(D)** | Errada. A rotina descrita não gera backups incrementais. |
| **(E)** | Correta. Restauração com diferencial = último completo + último diferencial. |

### Questão 3 — FCC · Analista Judiciário – Oficial de Justiça Avaliador Federal (estilo TRT)

Considere as afirmações sobre protocolos de correio eletrônico:

I. O SMTP é o protocolo utilizado no envio de mensagens, tanto do programa cliente para o servidor quanto entre servidores de e-mail.
II. O POP3 é o protocolo indicado para quem acessa a mesma caixa postal em vários dispositivos, pois mantém as mensagens e pastas sincronizadas no servidor.
III. O IMAP permite que o usuário acesse e organize as mensagens mantidas no servidor, refletindo as alterações em todos os dispositivos conectados à conta.

Está correto o que se afirma em

(A) I, apenas.
(B) I e III, apenas.
(C) II e III, apenas.
(D) I, II e III.
(E) II, apenas.

**Gabarito: B**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. A afirmação III também está correta. |
| **(B)** | Correta. I descreve o SMTP (envio); III descreve o IMAP (mensagens no servidor, sincronizadas). |
| **(C)** | Errada. A afirmação II atribui ao POP3 a característica do IMAP: o POP3 baixa as mensagens e, por padrão, remove-as do servidor. |
| **(D)** | Errada. A II está incorreta. |
| **(E)** | Errada. A II é justamente a incorreta. |

### Questão 4 — FCC · Técnico Judiciário – Agente da Polícia Judicial (estilo TRT)

Um servidor, utilizando o Windows 11 em português com configurações padrão e o histórico da área de transferência já ativado, deseja, nesta ordem: criar uma nova área de trabalho virtual; voltar para a área de trabalho virtual anterior; e visualizar os itens recentemente copiados para escolher um deles. Para isso, deverá utilizar, respectivamente, as combinações de teclas

(A) Win+D; Win+Tab; Ctrl+V.
(B) Win+Ctrl+N; Alt+Tab; Win+V.
(C) Win+Ctrl+D; Win+Ctrl+F4; Ctrl+Shift+V.
(D) Win+Ctrl+D; Win+Ctrl+seta para a esquerda; Win+V.
(E) Win+Tab; Win+M; Win+C.

**Gabarito: D**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Win+D mostra a área de trabalho (não cria área virtual); Ctrl+V cola apenas o último item copiado. |
| **(B)** | Errada. Win+Ctrl+N não cria área virtual; Alt+Tab alterna janelas, não áreas de trabalho. |
| **(C)** | Errada. Win+Ctrl+F4 **fecha** a área virtual atual; Ctrl+Shift+V não abre o histórico da área de transferência do Windows. |
| **(D)** | Correta. Win+Ctrl+D cria; Win+Ctrl+setas alternam; Win+V abre o histórico. |
| **(E)** | Errada. Win+Tab abre a Visão de Tarefas (de onde se pode criar a área, mas não a cria diretamente); Win+M minimiza janelas; Win+C não abre o histórico da área de transferência. |

### Questão 5 — FCC · Analista Judiciário (estilo TRT)

Ana, proprietária de um documento no Google Drive, compartilhou-o com Bruno, no papel de Comentarista, e com Carla, no papel de Editora, mantendo as configurações padrão de compartilhamento. Nessa situação,

(A) Carla poderá compartilhar o documento com outras pessoas, e Bruno poderá fazer sugestões de alteração, sem modificar diretamente o texto.
(B) Bruno poderá editar diretamente o texto, desde que o faça no modo Sugestão, cabendo a Ana aceitar as alterações.
(C) Carla poderá transferir a propriedade do documento para si, por ter o papel de Editora.
(D) somente Ana poderá adicionar novas pessoas ao documento, pois o papel de Editor nunca permite o compartilhamento.
(E) se Ana alterar o acesso geral para "Qualquer pessoa com o link", no papel de Leitor, somente quem tiver conta Google e tiver sido adicionado nominalmente poderá abrir o arquivo.

**Gabarito: A**

| Alternativa | Análise |
|---|---|
| **(A)** | Correta. Por padrão, editores podem compartilhar e alterar permissões; o comentarista comenta e sugere, sem editar. |
| **(B)** | Errada. Sugestão não é edição direta: fica pendente de aceite por quem tem papel de Editor ou de Proprietário, não necessariamente de Ana. |
| **(C)** | Errada. Só o proprietário transfere a propriedade. |
| **(D)** | Errada. Troca "por padrão pode" por "nunca pode"; o proprietário é que pode desativar a opção "Editores podem alterar permissões e compartilhar". |
| **(E)** | Errada. Descreve o acesso "Restrito". "Qualquer pessoa com o link" dispensa inclusão nominal e login. |

### Questão 6 — FCC · Analista Judiciário – Oficial de Justiça Avaliador Federal (estilo TRT)

Considere as afirmações sobre o Gmail e o Google Agenda, em suas versões web em português:

I. Ao arquivar uma conversa no Gmail, ela é excluída e enviada para a Lixeira, onde permanece por 30 dias.
II. No Gmail, uma mesma mensagem pode receber mais de um marcador, diferentemente do que ocorre com a organização em pastas tradicionais.
III. Ao criar um evento no Google Agenda, é possível convidar participantes, adicionar videoconferência do Google Meet e anexar arquivos do Google Drive ao próprio evento.
IV. O modo confidencial do Gmail impede que o destinatário encaminhe, copie, imprima ou faça captura de tela do conteúdo da mensagem.

Está correto o que se afirma em

(A) I e II, apenas.
(B) I e IV, apenas.
(C) II e III, apenas.
(D) III e IV, apenas.
(E) II, III e IV, apenas.

**Gabarito: C**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. A I está incorreta: arquivar retira a conversa da Caixa de entrada sem excluí-la; ela permanece em "Todos os e-mails". |
| **(B)** | Errada. I e IV estão incorretas. |
| **(C)** | Correta. II (vários marcadores) e III (convidados, Meet e anexos do Drive no evento) estão corretas. |
| **(D)** | Errada. A IV está incorreta: o modo confidencial bloqueia encaminhar, copiar, imprimir e baixar, mas **não** impede captura de tela ou foto. |
| **(E)** | Errada. Inclui a IV, incorreta. |

### Questão 7 — FCC · Técnico Judiciário – Agente da Polícia Judicial (estilo TRT)

Em uma planilha do Planilhas Google, a célula C3 contém a fórmula =A3*$B$1+B$2. Essa célula foi copiada e colada na célula E6. A fórmula resultante em E6 será

(A) =A6*$B$1+B$2
(B) =C6*$D$4+D$5
(C) =C3*$B$1+B$5
(D) =C6*$B$1+D$5
(E) =C6*$B$1+D$2

**Gabarito: E**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Ignora o deslocamento de colunas na referência relativa A3 e o de coluna em B$2. |
| **(B)** | Errada. Trata $B$1 e B$2 como relativas; o "$" trava o elemento imediatamente à sua direita, impedindo seu ajuste. |
| **(C)** | Errada. Em A3 desloca só a coluna (A → C), esquecendo as linhas; em B$2 ajusta justamente a linha travada e mantém a coluna livre. |
| **(D)** | Errada. Em B$2 a linha está fixa; só a coluna se ajusta (B → D), mantendo a linha 2. |
| **(E)** | Correta. Deslocamento de C3 para E6: +2 colunas e +3 linhas. A3 → C6 (relativa); $B$1 inalterada (absoluta); B$2 → D$2 (coluna livre, linha fixa). |

### Questão 8 — FCC · Analista Judiciário (estilo TRT)

Em uma planilha do Planilhas Google, configurada com a localidade Brasil, as células A2 a A6 contêm, respectivamente, os textos Vara 1, Vara 2, Vara 1, Vara 3 e Vara 1, e as células B2 a B6 contêm, respectivamente, os números 10, 20, 30, 40 e 50. Na célula D1 foi digitada a fórmula =SOMASE(A2:A6;"Vara 1";B2:B6)/CONT.SE(A2:A6;"Vara 1") e, na célula D2, a fórmula =SE(MÉDIA(B2:B6)>25;"Acima";"Abaixo"). Os resultados exibidos em D1 e D2 serão, respectivamente,

(A) 90 e Acima.
(B) 30 e Acima.
(C) 30 e Abaixo.
(D) 3 e Acima.
(E) 90 e Abaixo.

**Gabarito: B**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. 90 é apenas o resultado do SOMASE (10 + 30 + 50), sem a divisão pelo CONT.SE. |
| **(B)** | Correta. SOMASE = 90; CONT.SE = 3; 90/3 = 30. MÉDIA(B2:B6) = 150/5 = 30, que é maior que 25 → "Acima". |
| **(C)** | Errada. A média é 30, superior a 25, logo o SE retorna o valor_se_verdadeiro. |
| **(D)** | Errada. 3 é apenas o resultado do CONT.SE. |
| **(E)** | Errada. Erra as duas células. |

### Questão 9 — FCC · Analista Judiciário – Oficial de Justiça Avaliador Federal (estilo TRT)

Sobre os navegadores Google Chrome e Mozilla Firefox, em suas versões atuais para Windows e em português, é correto afirmar:

(A) A navegação anônima do Chrome impede que o provedor de internet e o administrador da rede do órgão identifiquem os sites acessados.
(B) Ao encerrar uma janela privativa do Firefox, os arquivos baixados durante a sessão são automaticamente apagados do computador.
(C) No Chrome, Ctrl+J exibe o histórico de navegação e Ctrl+H exibe a lista de downloads.
(D) A combinação Ctrl+Shift+P abre uma janela privativa no Firefox, enquanto Ctrl+Shift+N abre uma janela anônima no Chrome; em ambos, Ctrl+Shift+T reabre a última guia fechada.
(E) Em ambos os navegadores, Ctrl+D fecha a guia atual e Ctrl+T reabre a guia fechada por último.

**Gabarito: D**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. A navegação privada só evita registros no próprio dispositivo; provedor, rede corporativa e sites continuam vendo o acesso. |
| **(B)** | Errada. Downloads e favoritos criados na sessão privada permanecem. |
| **(C)** | Errada. Inverte os atalhos: Ctrl+H = histórico; Ctrl+J = downloads. |
| **(D)** | Correta. Reproduz exatamente a diferença entre os navegadores e o atalho comum de reabrir guia. |
| **(E)** | Errada. Ctrl+D adiciona aos favoritos; Ctrl+T abre nova guia; quem reabre a guia fechada é Ctrl+Shift+T. |

### Questão 10 — FCC · Técnico Judiciário – Agente da Polícia Judicial (estilo TRT)

Um servidor deseja localizar, pelo Google, somente arquivos em formato PDF hospedados no domínio tst.jus.br que contenham a expressão exata horas extras e que não contenham a palavra bancário. A pesquisa adequada é

(A) "horas extras" -bancário site:tst.jus.br filetype:pdf
(B) horas extras +bancário site:tst.jus.br filetype:pdf
(C) "horas extras" NOT site:tst.jus.br pdf
(D) "horas extras" -bancário inurl:pdf tst.jus.br
(E) "horas extras" OR bancário site:tst.jus.br filetype:pdf

**Gabarito: A**

| Alternativa | Análise |
|---|---|
| **(A)** | Correta. Aspas = expressão exata; hífen = exclusão; site: = domínio; filetype: = tipo de arquivo. |
| **(B)** | Errada. Sem aspas não há expressão exata, e "+" não exclui termo (operador, aliás, descontinuado). |
| **(C)** | Errada. Exclui o domínio desejado e não restringe o tipo de arquivo. |
| **(D)** | Errada. inurl:pdf apenas procura "pdf" no endereço, e "tst.jus.br" sem site: vira termo comum de busca. |
| **(E)** | Errada. OR amplia a busca para páginas com "bancário", em vez de excluí-las. |

### Questão 11 — FCC · Analista Judiciário (estilo TRT)

No processo de assinatura digital de um documento eletrônico com base em criptografia assimétrica e certificado digital da ICP-Brasil,

(A) o signatário utiliza a chave pública do destinatário, o que assegura a confidencialidade do conteúdo assinado.
(B) a assinatura garante, simultaneamente, sigilo, integridade e autenticidade, já que o documento assinado fica cifrado.
(C) o signatário utiliza a sua chave privada sobre o resumo (hash) do documento, e qualquer pessoa que disponha da chave pública correspondente pode verificar a assinatura, o que assegura autenticidade, integridade e não repúdio.
(D) utiliza-se uma única chave secreta, compartilhada entre signatário e destinatário, o que caracteriza a criptografia assimétrica.
(E) o certificado digital é emitido pelo próprio titular, dispensando-se a participação de Autoridade Certificadora.

**Gabarito: C**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. Cifrar com a chave pública do destinatário é o procedimento do sigilo, não da assinatura. |
| **(B)** | Errada. A assinatura digital não garante sigilo; o documento assinado pode ser lido por qualquer um. |
| **(C)** | Correta. Hash cifrado com a chave privada do signatário; verificação com a pública; garantias de autenticidade, integridade e não repúdio (art. 1º da MP 2.200-2/2001). |
| **(D)** | Errada. Chave única compartilhada caracteriza a criptografia **simétrica**. |
| **(E)** | Errada. O certificado é emitido por Autoridade Certificadora credenciada, que vincula a chave pública ao titular. |

### Questão 12 — FCC · Analista Judiciário – Oficial de Justiça Avaliador Federal (estilo TRT)

Considere as afirmações sobre segurança da informação:

I. No pharming, o usuário pode ser direcionado a uma página falsa mesmo digitando corretamente o endereço do site legítimo, em razão de alterações no serviço de DNS.
II. Exigir do usuário uma senha e, em seguida, um PIN numérico caracteriza autenticação de dois fatores, por serem duas informações distintas.
III. O keylogger captura as teclas digitadas, enquanto o screenlogger captura a tela e a posição do cursor, técnica desenvolvida para contornar os teclados virtuais.
IV. O firewall pessoal dispensa o uso de antivírus, pois detecta e remove os vírus presentes nos arquivos do computador.
V. Na engenharia social, o atacante explora a confiança ou a ingenuidade da vítima para obter informações sigilosas, podendo atuar inclusive por telefone, sem empregar código malicioso.

Está correto o que se afirma em

(A) I e II, apenas.
(B) II e IV, apenas.
(C) I, II e III, apenas.
(D) III, IV e V, apenas.
(E) I, III e V, apenas.

**Gabarito: E**

| Alternativa | Análise |
|---|---|
| **(A)** | Errada. A II é incorreta. |
| **(B)** | Errada. II e IV são as duas incorretas. |
| **(C)** | Errada. Inclui a II: senha e PIN pertencem à mesma categoria ("algo que você sabe"); 2FA exige fatores de categorias diferentes. |
| **(D)** | Errada. Inclui a IV: firewall filtra tráfego de rede e não remove vírus — não substitui o antivírus. |
| **(E)** | Correta. I (pharming), III (keylogger x screenlogger) e V (engenharia social) estão corretas. |
