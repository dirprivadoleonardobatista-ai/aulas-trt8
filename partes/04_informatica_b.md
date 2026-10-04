## 3. Google Workspace

> [SINTESE] Gmail organiza por **marcadores** (não pastas) e oferece arquivar, filtros, silenciar, programar envio e modo confidencial. Documentos: Sugestão, comentários, histórico de versões, digitação por voz. Planilhas: funções com ";" e referências com "$". Agenda integra convites, anexos do Drive e Meet. Drive: Leitor, Comentarista, Editor e Proprietário; "Restrito" x "Qualquer pessoa com o link".

### 3.1 Gmail

| Configurações rápidas (engrenagem) | Opções |
|---|---|
| **Densidade** | Padrão · Confortável · Compacto |
| **Tipo de Caixa de entrada** | Padrão (guias Principal, Promoções, Social, Atualizações) · Importantes primeiro · Não lidos primeiro · Com estrela primeiro · Prioritária · Várias caixas de entrada |
| **Painel de leitura** | Sem divisão · À direita · Abaixo da Caixa de entrada |
| **Visualização de conversa** | Agrupa (ou não) as respostas no mesmo fio |

| Recurso | Funcionamento | Pegadinha |
|---|---|---|
| **Marcadores** | Uma mensagem pode ter **vários** marcadores, o que pastas não permitem | Excluir o marcador **não** exclui as mensagens |
| **Arquivar** | Tira da Caixa de entrada sem apagar; fica em "Todos os e-mails" | Se alguém responder, a conversa **volta** à Caixa de entrada |
| **Silenciar** | Arquiva e faz as novas respostas não aparecerem na Caixa de entrada | Volta se a nova mensagem for só para você ou o incluir de novo em Para/Cc |
| **Filtros** | Critérios (De, Para, Assunto, palavras, tamanho, anexo) + ações (pular a Caixa de entrada, aplicar marcador, marcar como lida, encaminhar, excluir, nunca enviar para spam) | Podem ser aplicados também às conversas já existentes |
| **Programar envio** | Seta ao lado de "Enviar"; fica em "Programados" | Pode ser cancelado antes do horário |
| **Modo confidencial** | Data de expiração e senha por SMS; bloqueia encaminhar, copiar, imprimir e baixar | **Não** impede captura de tela; o remetente pode revogar o acesso |
| **Excluir** | Vai para a Lixeira, esvaziada após 30 dias | Diferente de arquivar |

> [PROVA] A FCC cobra "marcador x pasta", "arquivar x excluir" e a falsa ideia de que o modo confidencial impede qualquer cópia. Anexos acima de 25 MB viram link do Drive.

### 3.2 Google Documentos

| Recurso | Caminho / atalho | Efeito |
|---|---|---|
| **Modo Sugestão** | Menu Edição · Sugestão · Visualização | Alterações marcadas, que precisam ser **aceitas ou rejeitadas** |
| **Comentários** | Ctrl+Alt+M | Mencionar com "@" permite **atribuir** o comentário; pode ser resolvido |
| **Histórico de versões** | Arquivo › Histórico de versões (Ctrl+Alt+Shift+H) | Mostra autores e alterações; permite **nomear** e **restaurar** versões |
| **Digitação por voz** | Ferramentas › Digitação por voz (Ctrl+Shift+S) | Converte fala em texto, no Chrome |
| **Salvamento** | Automático | Não há botão "Salvar"; download em .docx, .odt, .pdf, .txt |

> [ATENCAO] Restaurar versão anterior **não apaga** as posteriores. Ctrl+Shift+S (voz no Docs) não se confunde com Win+Shift+S (captura do Windows).

### 3.3 Planilhas Google

Fórmulas começam com "=". Na localidade Brasil, argumentos separados por **ponto e vírgula**.

| Função | Sintaxe | O que faz |
|---|---|---|
| **SOMA** | =SOMA(A1:A10) | Soma o intervalo (":" = até; ";" = e) |
| **MÉDIA** | =MÉDIA(B2:B6) | Média; ignora vazias e texto |
| **SE** | =SE(teste; se_verdadeiro; se_falso) | Retorna um de dois valores |
| **CONT.SE** | =CONT.SE(intervalo; critério) | Conta as células que atendem ao critério |
| **SOMASE** | =SOMASE(intervalo; critério; [intervalo_soma]) | Soma os valores correspondentes ao critério |
| **PROCV** | =PROCV(chave; intervalo; índice; [classificado]) | Busca a chave na **1ª coluna** e devolve a coluna "índice"; FALSO = correspondência exata |

> [EXEMPLO] A2:A5 = Ana, Bruno, Ana, Carla; B2:B5 = 100, 200, 300, 400.
> • =SOMA(B2:B5) → 1000 · =MÉDIA(B2:B5) → 250 · =CONT.SE(A2:A5;"Ana") → 2
> • =SOMASE(A2:A5;"Ana";B2:B5) → 400 · =SOMASE(B2:B5;">200") → 700
> • =SE(B3>150;"Alto";"Baixo") → "Alto" · =PROCV("Carla";A2:B5;2;FALSO) → 400

| Referência | Forma | Ao copiar |
|---|---|---|
| **Relativa** | A1 | Coluna e linha se ajustam |
| **Absoluta** | $A$1 | Nada muda |
| **Mista** | $A1 / A$1 | Fixa só a coluna / só a linha |

> [PROVA] =A1*$C$1 em B2, copiada para D5 (+2 colunas, +3 linhas) → **=C4*$C$1**. O "$" trava o elemento à sua direita; F4 alterna os tipos. Erros: #DIV/0! (divisão por zero), #N/D (não encontrado), #REF! (referência inválida), #NOME? (função inexistente), #VALOR! (tipo incompatível).

### 3.4 Apresentações, Agenda, Tarefas e Meet

| Aplicativo | Funcionalidades cobradas |
|---|---|
| **Apresentações** | Temas, layouts, anotações do apresentador, modo Apresentar, edição colaborativa, exportação .pptx/.pdf |
| **Agenda — criar e convidar** | Título, data/hora, dia inteiro, repetição, notificações; "Adicionar convidados", com permissões (modificar evento, convidar outros, ver lista); respostas Sim/Não/Talvez |
| **Agenda — ajustar horários** | "Encontrar um horário" cruza a disponibilidade dos convidados; arrastar o evento altera o horário |
| **Agenda — anexos e Meet** | Clipe na descrição anexa arquivo do Drive; "Adicionar videoconferência do Google Meet" gera o link da reunião |
| **Tarefas** | Listas com data, repetição e subtarefas; painel lateral do Gmail, Agenda e Docs; e-mail pode virar tarefa |
| **Meet** | Reunião por link; apresentar tela, legendas, chat, levantar a mão, enquetes, salas temáticas; gravação conforme o plano |

### 3.5 Google Drive

Conta gratuita: 15 GB compartilhados entre Gmail, Drive e Fotos. Cria-se pelo botão "Novo". A Lixeira do Drive apaga após 30 dias.

| Papel | Pode | Não pode |
|---|---|---|
| **Leitor** | Visualizar (por padrão, baixar e imprimir) | Comentar, editar |
| **Comentarista** | Visualizar, comentar e **sugerir** | Editar diretamente |
| **Editor** | Editar e, por padrão, **compartilhar e alterar permissões** | Transferir a propriedade |
| **Proprietário** | Tudo, inclusive excluir e **transferir a propriedade** | — (único por arquivo) |

| Acesso geral | Efeito |
|---|---|
| **Restrito** | Só as pessoas adicionadas abrem |
| **Organização** | Membros do domínio Workspace com o link |
| **Qualquer pessoa com o link** | Qualquer um com o link, **sem login**, no papel escolhido |

| Critério | Meu Drive | Drive compartilhado |
|---|---|---|
| **Dono** | O usuário | A **equipe/organização** |
| **Saída de membro** | Arquivos saem com ele | Arquivos **permanecem** |
| **Papéis** | Leitor, Comentarista, Editor, Proprietário | Administrador, Administrador de conteúdo, Colaborador, Comentarista, Leitor |

> [PROVA] (1) Comentarista não edita, sugere; (2) Editor compartilha por padrão — o proprietário pode desmarcar "Editores podem alterar permissões e compartilhar"; (3) "Qualquer pessoa com o link" dispensa conta Google; (4) em drive compartilhado, o dono é a equipe.

## 4. Redes e internet

> [SINTESE] Abrangência: PAN, LAN, MAN, WAN. Internet é pública; intranet é privada com tecnologia da internet; extranet abre a intranet a parceiros. Cada serviço tem protocolo e porta padrão.

| Conceito | Definição |
|---|---|
| **LAN / MAN / WAN** | Rede local (prédio) / metropolitana (cidade) / de longa distância (estados, países) |
| **Internet** | Rede mundial pública de redes, baseada em TCP/IP |
| **Intranet** | Rede **privada** que usa as tecnologias da internet (HTTP, navegador), restrita aos usuários internos |
| **Extranet** | Parte da intranet aberta, com controle (login, VPN), a **parceiros externos** |
| **VPN** | **Túnel criptografado** sobre a internet para acesso seguro à rede interna |
| **Wi-Fi** | Rede sem fio IEEE 802.11; usar WPA2/WPA3 (WEP é inseguro) |
| **IP / porta** | IP identifica o dispositivo (IPv4: 32 bits, ex.: 192.168.0.10; IPv6: 128 bits); porta identifica o serviço |

> [ATENCAO] Intranet pode ser acessada de fora por VPN e usa os mesmos protocolos da internet; a diferença é a restrição de acesso.

| Protocolo | Função | Porta |
|---|---|---|
| **TCP / UDP** | Transporte com conexão e confiável / sem conexão e mais rápido (streaming, VoIP) | — |
| **HTTP / HTTPS** | Páginas web / com criptografia TLS e certificado (cadeado) | 80 / 443 |
| **FTP** | Transferência de arquivos | 20 e 21 |
| **SMTP** | **Envio** de e-mail | 25 (587 autenticado) |
| **POP3** | **Recebimento**: baixa as mensagens | 110 (995 seguro) |
| **IMAP** | **Acesso** às mensagens no servidor, sincronizadas | 143 (993 seguro) |
| **DNS** | Traduz nomes (www.trt8.jus.br) em IP | 53 |
| **DHCP** | Atribui IP, máscara, gateway e DNS automaticamente | 67/68 |

| Critério | POP3 | IMAP |
|---|---|---|
| **Mensagens** | Baixadas; por padrão removidas do servidor | Ficam no servidor |
| **Vários dispositivos** | Inadequado | Sincroniza lidas, pastas e excluídas |

> [PROVA] **SMTP envia; POP3 e IMAP recebem.** A FCC troca SMTP por POP3 no envio ou diz que o IMAP remove as mensagens do servidor. No webmail, o acesso é por HTTPS.

## 5. Navegadores: Chrome, Edge e Firefox

> [SINTESE] Atalhos quase idênticos, com uma exceção decisiva: janela privativa do Firefox = **Ctrl+Shift+P**; anônima do Chrome e InPrivate do Edge = **Ctrl+Shift+N**.

| Conceito | Explicação |
|---|---|
| **Navegação privada** | Ao fechar, apaga do dispositivo histórico, cookies e dados de formulário; **mantém** downloads e favoritos |
| **Limite** | Não oculta a navegação do provedor, da rede corporativa nem dos sites; não protege contra malware |
| **Cookies** | Arquivos de texto gravados pelo site (sessão, preferências, rastreamento); de sessão x persistentes; primários x de terceiros |
| **Cache** | Cópia local de páginas e imagens para acelerar o carregamento |
| **Extensões** | Complementos que adicionam funções; risco se de origem duvidosa |

| Atalho | Chrome / Edge | Firefox |
|---|---|---|
| **Ctrl+T / Ctrl+W** | Nova guia / fecha guia | Idem |
| **Ctrl+Shift+T** | Reabre a última guia fechada | Idem |
| **Ctrl+N** | Nova janela | Idem |
| **Ctrl+Shift+N** | Janela anônima / InPrivate | Reabre a última **janela** fechada |
| **Ctrl+Shift+P** | Não é navegação privada | Janela **privativa** |
| **Ctrl+H** | Histórico | Histórico |
| **Ctrl+J** | Downloads | Downloads: Ctrl+Shift+Y no Windows |
| **Ctrl+D** | Adiciona aos favoritos | Idem |
| **Ctrl+Shift+Del** | Limpar dados de navegação | Limpar histórico recente |
| **F5 / Ctrl+F5** | Recarregar / recarregar ignorando o cache | Idem |
| **Ctrl+L ou F6** | Barra de endereços | Idem |

> [PROVA] "Ctrl+Shift+N abre janela privativa em todos os navegadores" e "a navegação anônima esconde os acessos do empregador" — ambas erradas.

## 6. Ferramentas de busca: Google e Bing

> [SINTESE] Operadores refinam a pesquisa: aspas (frase exata), hífen (exclusão), site:, filetype:, OR, asterisco (curinga), intitle: e ".." (intervalo). O Bing aceita quase todos.

| Operador | Efeito | Exemplo |
|---|---|---|
| **Aspas** | Expressão exata | "justa causa" |
| **- (hífen)** | Exclui o termo | férias -coletivas |
| **site:** | Restringe a site ou domínio | assédio site:tst.jus.br |
| **filetype:** | Tipo de arquivo | edital filetype:pdf |
| **OR** | Um termo ou outro (maiúsculas) | jornada OR expediente |
| **\*** | Curinga | "o * é o limite" |
| **intitle:** | Termo no título | intitle:concurso |
| **..** | Intervalo numérico | 2018..2022 |

O **Bing** aceita aspas, site:, filetype: e intitle:, e usa AND, OR e NOT (equivalente ao hífen), além de operadores próprios como inbody: (termo no corpo da página) e ip: (sites em determinado IP).

> [ATENCAO] O "+" do Google foi descontinuado; para obrigar um termo, usam-se aspas.
