# NOÇÕES DE INFORMÁTICA

## 1. Windows 10 e Windows 11

> [SINTESE] Windows 11 = evolução do 10 (barra centralizada, Layouts de Ajuste, Configurações redesenhadas), com requisitos mais rígidos (TPM 2.0, Inicialização Segura, só 64 bits). Explorador de Arquivos, atalhos, Win+V, Snap e áreas virtuais organizam o trabalho; o aplicativo Segurança do Windows (Defender) protege.

### 1.1 Diferenças Windows 10 x Windows 11

| Critério | Windows 10 | Windows 11 |
|---|---|---|
| **Barra de tarefas** | À esquerda; pode ir para qualquer borda | Ícones centralizados (pode alinhar à esquerda); fixa embaixo |
| **Menu Iniciar** | Blocos dinâmicos (*Live Tiles*) | "Fixados" e "Recomendado"; sem blocos dinâmicos |
| **Janelas** | Snap Assist | Snap + **Layouts de Ajuste** (Win+Z) e Grupos de Ajuste |
| **Win+A** | Central de Ações (notificações + ações rápidas) | Configurações rápidas; notificações em Win+N |
| **Explorador** | Faixa de opções (*ribbon*) | Barra de comandos simplificada e abas |
| **Requisitos** | 32 ou 64 bits | Só 64 bits; TPM 2.0; UEFI com Inicialização Segura |
| **Suporte** | Encerrado em 14/10/2025 | Em suporte |

> [ATENCAO] O Windows 11 **não** eliminou o Painel de Controle; apenas parte das opções migrou para **Configurações** (Win+I), organizado em Sistema, Bluetooth e dispositivos, Rede e Internet, Personalização, Aplicativos, Contas, Hora e idioma, Acessibilidade, Privacidade e segurança e Windows Update.

### 1.2 Explorador de Arquivos (Win+E)

| Elemento | Função |
|---|---|
| **Acesso rápido / Página Inicial** | Pastas fixadas e arquivos recentes (Página Inicial no 11) |
| **Painel de visualização (Alt+P)** | Exibe o conteúdo do arquivo sem abri-lo |
| **Painel de detalhes (Alt+Shift+P)** | Exibe propriedades do item |
| **Modos de exibição** | Ícones (quatro tamanhos), Lista, Detalhes, Blocos, Conteúdo |
| **Extensões e itens ocultos** | Ocultos por padrão; exibidos pelo menu Exibir |

| Arrastar com o mouse | Mesma unidade | Unidade diferente |
|---|---|---|
| **Sem tecla** | Move | Copia |
| **Ctrl** | Copia | Copia |
| **Shift** | Move | Move |
| **Alt** | Cria atalho | Cria atalho |

> [PROVA] "Arrastar um arquivo para outra pasta sempre o move" — falso: de C: para um pendrive, arrastar **copia**.

### 1.3 Quadro de atalhos do Windows

| Atalho | Efeito |
|---|---|
| **Win+E** | Explorador de Arquivos |
| **Win+D** | Mostra/oculta a área de trabalho |
| **Win+M** | Minimiza todas as janelas |
| **Win+L** | Bloqueia o computador |
| **Win+I** | Configurações |
| **Win+R** | Executar |
| **Win+S** | Pesquisa |
| **Win+X** | Menu de Link Rápido |
| **Win+V** | Histórico da área de transferência |
| **Win+Shift+S** | Ferramenta de Captura (recorte) |
| **Win+PrtScn** | Salva a tela em Imagens › Capturas de Tela |
| **Win+Tab** | Visão de Tarefas |
| **Win+Ctrl+D** | Nova área de trabalho virtual |
| **Win+Ctrl+← / →** | Alterna entre áreas virtuais |
| **Win+Ctrl+F4** | Fecha a área virtual atual |
| **Win+setas** | Snap: encaixa, maximiza ou minimiza a janela |
| **Win+Z** | Layouts de Ajuste (11) |
| **Win+A / Win+N** | Configurações rápidas / notificações (11) |
| **Win+.** | Painel de emojis |
| **Win+número** | Abre o programa na posição correspondente da barra |
| **Alt+Tab / Alt+F4** | Alterna janelas / fecha a janela ativa |
| **Ctrl+Shift+Esc** | Gerenciador de Tarefas, diretamente |
| **Ctrl+Alt+Del** | Tela de segurança |
| **F2 / F5** | Renomear / atualizar |
| **Delete** | Envia para a Lixeira |
| **Shift+Delete** | Exclui definitivamente, sem Lixeira |
| **Ctrl+Shift+N** | Nova pasta (no Explorador) |
| **Alt+Enter** | Propriedades |
| **Alt+↑** | Sobe um nível de pasta |
| **Shift+F10** | Menu de contexto |

> [PROVA] Trocas preferidas: Win+D x Win+M · Win+L x Win+I · Ctrl+Shift+Esc (Gerenciador direto) x Ctrl+Alt+Del (tela de segurança) · Delete x Shift+Delete · Ctrl+Shift+N no Explorador (nova pasta) x no Chrome (janela anônima).

### 1.4 Lixeira e OneDrive

| Lixeira | Regra |
|---|---|
| **Exclusão comum** | Itens de unidade local vão para a Lixeira e podem ser restaurados ao local original |
| **Não passam pela Lixeira** | Shift+Delete; itens de pendrive/cartão e de pastas de rede; itens maiores que a capacidade da Lixeira (com aviso) |
| **Capacidade** | Configurável por unidade |

| OneDrive | Explicação |
|---|---|
| **Natureza** | Nuvem da Microsoft integrada ao Explorador (5 GB gratuitos) |
| **Arquivos sob demanda** | Nuvem = só on-line · visto em círculo vazado = disponível localmente · círculo verde preenchido = "Sempre manter neste dispositivo" |
| **Backup de pastas** | Sincroniza Área de Trabalho, Documentos e Imagens |

> [ATENCAO] Sincronizar não é fazer backup: exclusões e arquivos criptografados por ransomware são replicados na nuvem. O que socorre é o histórico de versões e a Lixeira do OneDrive.

### 1.5 Win+V, Snap e áreas de trabalho virtuais

| Recurso | Pontos cobrados |
|---|---|
| **Histórico da área de transferência (Win+V)** | Precisa ser **ativado** (Configurações › Sistema › Área de transferência); guarda até 25 itens; itens **fixados** sobrevivem à reinicialização; pode sincronizar entre dispositivos |
| **Snap (Ajustar)** | Arrastar a janela à borda ou Win+setas; o Snap Assist sugere janelas para o espaço restante |
| **Áreas de trabalho virtuais** | Criadas em Win+Tab ou Win+Ctrl+D; ao fechar uma área, as janelas **migram** para a área vizinha, não são fechadas |

### 1.6 Segurança do Windows

| Área | Função |
|---|---|
| **Proteção contra vírus e ameaças** | Microsoft Defender Antivírus (tempo real; verificação rápida, completa, personalizada, off-line); **Acesso controlado a pastas** contra ransomware |
| **Firewall e proteção de rede** | Firewall por perfil (domínio, privada, pública) |
| **Controle de aplicativos e do navegador** | SmartScreen: alerta sobre arquivos e sites maliciosos |
| **Segurança do dispositivo** | Isolamento de núcleo, TPM, inicialização segura |

> [DICA] O Defender é antivírus nativo e se desativa sozinho quando outro antivírus é instalado. Firewall e antivírus são ferramentas distintas.

## 2. Organização da informação: arquivos, pastas e programas

> [SINTESE] Arquivo = nome + extensão; pasta = contêiner hierárquico; caminho = endereço na árvore; programa = executável associado a extensões.

| Conceito | Explicação |
|---|---|
| **Caminho absoluto** | A partir da raiz: C:\Users\Ana\Documentos\ata.pdf |
| **Caminho relativo** | A partir da pasta atual: ..\Imagens\foto.jpg (".." = pasta acima) |
| **Atalho (.lnk)** | Aponta para outro arquivo; apagá-lo não apaga o original |
| **Associação** | Vínculo entre extensão e programa padrão |

Nomes de arquivo no Windows não diferenciam maiúsculas de minúsculas e **não podem conter** barra invertida, barra, dois-pontos, asterisco, interrogação, aspas, menor, maior e barra vertical.

| Extensões | Tipo |
|---|---|
| **.docx .odt .rtf .txt** | Texto |
| **.xlsx .ods .csv** | Planilha |
| **.pptx .odp** | Apresentação |
| **.jpg .png .gif .svg** | Imagem (.svg vetorial; .png sem perda) |
| **.mp3 .wav / .mp4 .avi** | Áudio / vídeo |
| **.zip .rar .7z** | Compactados |
| **.exe .msi .bat .dll** | Executáveis, instaladores, scripts, bibliotecas |

> [ATENCAO] Como o Windows oculta extensões conhecidas, "boleto.pdf.exe" aparece como "boleto.pdf". Exibir extensões é boa prática de segurança.
