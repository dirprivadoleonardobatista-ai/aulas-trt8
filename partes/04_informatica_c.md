## 7. Segurança da informação

> [SINTESE] Princípios (confidencialidade, integridade, disponibilidade, autenticidade, não repúdio) · malware: o que distingue cada um é **como se propaga** e **o que faz** (tema campeão) · golpes: phishing, pharming, engenharia social · defesas: antivírus, firewall, antispyware, backup · criptografia, assinatura e certificado digital · autenticação multifator (sabe / tem / é).

### 7.1 Princípios

| Princípio | Significado | Ameaçado por |
|---|---|---|
| **Confidencialidade** | Só autorizados acessam | Vazamento, spyware |
| **Integridade** | Sem alteração indevida | Adulteração, vírus |
| **Disponibilidade** | Acessível quando necessário | Ransomware, DoS/DDoS |
| **Autenticidade** | Origem/autoria verdadeira | Falsificação de remetente (*spoofing*) |
| **Não repúdio** | Autor não pode negar a autoria | Assegurado pela assinatura digital |

### 7.2 Códigos maliciosos

| Malware | Definição | Propaga-se sozinho? |
|---|---|---|
| **Vírus** | Propaga-se **inserindo cópias de si em outros programas ou arquivos**; tipos: de macro, de boot, de script | **Não**: depende da execução do hospedeiro |
| **Worm** | Propaga-se **automaticamente pelas redes**, enviando cópias de si entre computadores e explorando vulnerabilidades; não infecta arquivos; consome recursos | **Sim** |
| **Bot / botnet** | Bot: além de se propagar como o worm, comunica-se com o invasor, que o **controla remotamente** (máquina "zumbi"). Botnet: rede de zumbis usada em DDoS e spam | Sim |
| **Cavalo de Troia (trojan)** | Além das funções aparentes, executa **outras, maliciosas**, sem o conhecimento do usuário | **Não**: a vítima o instala, enganada |
| **Spyware** | **Monitora** as atividades e envia as informações a terceiros | Não |
| **Keylogger** | Spyware que captura as **teclas** digitadas | Não |
| **Screenlogger** | Spyware que captura a **tela** e a posição dos cliques (burla teclados virtuais) | Não |
| **Adware** | Exibe **propaganda**; pode ser legítimo ou malicioso | Não |
| **Backdoor** | Permite o **retorno do invasor** ao computador comprometido | Não |
| **Rootkit** | Conjunto de programas e técnicas para **esconder e assegurar a presença** do invasor ou de outro malware | Não |
| **Ransomware** | Torna dados ou equipamento **inacessíveis** (em regra, por criptografia) e exige **resgate**; tipos *Locker* (bloqueia o equipamento) e *Crypto* (cifra os dados) | Varia |

> [PROVA] Pares que a FCC troca:
> • Vírus x worm: o vírus precisa de **hospedeiro e execução**; o worm se propaga **sozinho pela rede**.
> • Worm x bot: o bot acrescenta o **controle remoto**.
> • Trojan x backdoor: trojan é o **disfarce**; backdoor é o **acesso de retorno**.
> • Keylogger x screenlogger: **teclas** x **tela/cliques**.
> • Rootkit **esconde** — não serve para "obter acesso", mas para manter-se oculto.
> • Ransomware ataca a **disponibilidade**; a defesa decisiva é o **backup** desconectado.

### 7.3 Golpes

| Golpe | Mecanismo |
|---|---|
| **Engenharia social** | Explora confiança, ingenuidade ou medo da vítima (inclusive por telefone); ataca a **pessoa**, não a máquina |
| **Phishing** | Mensagem falsa (e-mail, SMS, rede social) que imita instituição e leva a vítima, **por link**, a página falsa ou a fornecer dados; *spear phishing* = direcionado; *smishing* = SMS; *vishing* = voz |
| **Pharming** | **Redirecionamento** a site falso por adulteração do DNS: a vítima digita o **endereço correto** e mesmo assim cai na fraude |
| **Hoax** | Boato alarmista que pede para ser repassado |

> [EXEMPLO] Bruno clica em link de e-mail que imita seu banco: **phishing**. Bruno digita corretamente o endereço do banco e cai em página falsa porque o DNS foi adulterado: **pharming**.

> [ATENCAO] O cadeado (HTTPS) indica conexão criptografada, **não** que o site seja legítimo: páginas de phishing também usam HTTPS.

### 7.4 Ferramentas de defesa

| Ferramenta | Faz | Não faz |
|---|---|---|
| **Antivírus** | Detecta e remove malware por **assinaturas**, **heurística** e comportamento | Não filtra conexões; não substitui backup |
| **Firewall** | Filtra o tráfego de **entrada e saída** conforme regras | **Não é antivírus**: não remove vírus |
| **Antispyware** | Detecta e remove spywares | Hoje integrado ao antivírus |
| **Antispam / antiphishing** | Separa mensagens indesejadas; alerta sobre sites fraudulentos | Não elimina o fator humano |

### 7.5 Backup

| Tipo | Copia | Marca como copiado? | Restauração exige |
|---|---|---|---|
| **Completo** | Todos os arquivos selecionados | Sim | Só o último completo |
| **Incremental** | O que mudou desde o **último backup de qualquer tipo** | Sim | Completo + **todos** os incrementais seguintes |
| **Diferencial** | O que mudou desde o **último completo** | **Não** (volume cresce a cada dia) | Completo + **o último** diferencial |

> [EXEMPLO] Completo no domingo; segunda altera A e B; terça altera C. Incrementais: seg = A, B; ter = C (restaurar: completo + seg + ter). Diferenciais: seg = A, B; ter = **A, B, C** (restaurar: completo + ter). O incremental é mais rápido de fazer; o diferencial, mais rápido de restaurar.

> [DICA] Regra 3-2-1: 3 cópias, em 2 mídias diferentes, 1 fora do local. Contra ransomware, uma cópia off-line.

### 7.6 Criptografia, assinatura e certificado digital

| Critério | Simétrica | Assimétrica |
|---|---|---|
| **Chaves** | **Uma** chave secreta compartilhada | **Par**: pública (divulgada) e privada (secreta) |
| **Desempenho** | Rápida | Lenta |
| **Problema** | Distribuir a chave com segurança | Custo computacional |
| **Exemplos** | AES, DES, 3DES | RSA, curvas elípticas |

| Objetivo | Cifra com | Decifra/verifica com | Garante |
|---|---|---|---|
| **Sigilo** | Chave **pública do destinatário** | Chave **privada do destinatário** | Confidencialidade |
| **Assinatura digital** | Chave **privada do remetente** (sobre o hash) | Chave **pública do remetente** | Autenticidade, integridade e não repúdio — **não** sigilo |

| Conceito | Explicação |
|---|---|
| **Hash** | Resumo de tamanho fixo, unidirecional; qualquer alteração no conteúdo muda o hash (ex.: SHA-256) |
| **Certificado digital** | Documento eletrônico emitido por **Autoridade Certificadora** que vincula a chave pública ao titular, com validade |
| **ICP-Brasil** | AC Raiz: **ITI** |
| **A1 x A3** | A1: em software, no computador, validade de 1 ano · A3: em token ou cartão, chave privada não exportável |

>> Art. 1º Fica instituída a Infra-Estrutura de Chaves Públicas Brasileira - ICP-Brasil, para garantir a autenticidade, a integridade e a validade jurídica de documentos em forma eletrônica, das aplicações de suporte e das aplicações habilitadas que utilizem certificados digitais, bem como a realização de transações eletrônicas seguras.

Comentário: o art. 1º da MP nº 2.200-2/2001 lista autenticidade, integridade e validade jurídica. A confidencialidade não aparece, porque decorre da cifragem, não da assinatura — a FCC inclui "sigilo" entre as garantias da assinatura para tornar a alternativa errada.

>> Art. 1º (...) § 2º (...) III - assinatura eletrônica as seguintes formas de identificação inequívoca do signatário: a) assinatura digital baseada em certificado digital emitido por Autoridade Certificadora credenciada, na forma de lei específica; b) mediante cadastro de usuário no Poder Judiciário, conforme disciplinado pelos órgãos respectivos.

Comentário: a Lei nº 11.419/2006, base do PJe, admite duas formas de assinatura eletrônica: a digital (certificado ICP-Brasil) e o cadastro no próprio tribunal. Assinatura **digital** é espécie do gênero assinatura **eletrônica**.

> [ATENCAO] Conferir nas normas vigentes da ICP-Brasil o prazo máximo de validade do certificado A3, alterado ao longo do tempo.

### 7.7 Autenticação e boas práticas

| Fator | Exemplos |
|---|---|
| **Algo que você sabe** | Senha, PIN, pergunta secreta |
| **Algo que você tem** | Celular (app autenticador, SMS), token, cartão inteligente |
| **Algo que você é** | Biometria: digital, face, íris, voz |

> [PROVA] 2FA exige fatores de **categorias diferentes**: senha + PIN (ambos "sabe") **não** é 2FA; senha + código no celular, ou cartão + digital, **é**.

| Boa prática | Por quê |
|---|---|
| **Senhas longas (frases-senha) e únicas** | Resistem à força bruta; vazamento de um serviço não compromete os demais |
| **Gerenciador de senhas** | Gera e guarda senhas fortes, protegidas por senha mestra |
| **Atualizar sistema e programas** | Fecha vulnerabilidades exploradas por worms |
| **Desconfiar de links e anexos** | Principal porta de entrada de phishing e trojans |
| **Bloquear a tela (Win+L) e evitar Wi-Fi aberto para transações** | Evita acesso físico e interceptação |
