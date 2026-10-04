## 4. Planejamento de segurança, segurança física e equipamentos

> [SINTESE] Plano em três níveis (estratégico, tático, operacional), modular e implantado em fases. Segurança física em camadas: dissuadir, detectar, retardar, responder. Eletrônica: sensores + alarme + biometria + CFTV com analíticos, sempre sob a LGPD.

| Nível | Quem / horizonte | Produto |
|---|---|---|
| **Estratégico** | Alta administração; longo prazo | Política e diretrizes de segurança |
| **Tático** | Gestores setoriais; médio prazo | Planos por área (instalações, pessoas, informação) |
| **Operacional** | Equipes de execução; curto prazo | Procedimentos operacionais padrão (POP), escalas, postos |

| Ideia | Explicação |
|---|---|
| **Metodologia** | Diagnóstico → análise de riscos → definição de medidas → plano → implantação → avaliação e revisão (ciclo contínuo) |
| **Modularidade** | Plano dividido em módulos autônomos e integrados (acesso, CFTV, brigada, transporte), que podem ser revistos isoladamente |
| **Faseamento** | Implantação por etapas, segundo prioridade de risco e orçamento |
| **Princípios** | Objetividade, flexibilidade, continuidade, integração, proporcionalidade custo-benefício e sigilo |

| Segurança física | Conteúdo |
|---|---|
| **Camadas (defesa em profundidade)** | Perímetro externo → área → edificação → setor → ativo crítico; cada camada retarda o invasor |
| **Barreiras** | Naturais (rios, relevo) e físicas (muros, grades, portões, cancelas, blindagens) |
| **Controle de acesso** | Pessoas, veículos e materiais: identificação, credencial, pórtico detector, raio X, catraca, livro/sistema de registro |
| **Iluminação** | Contínua, de emergência, de reserva e portátil; ilumina o perímetro e ofusca o invasor, não o vigilante |

### 4.1 Sensores, alarmes e biometria

| Sensor | Princípio | Observação |
|---|---|---|
| **IVP (infravermelho passivo)** | Detecta variação de calor de corpo em movimento | Não emite energia |
| **Micro-ondas** | Ativo; emite ondas e capta alteração (efeito Doppler) | Atravessa materiais finos: mais falso alarme |
| **Dupla tecnologia** | IVP + micro-ondas; dispara só com os dois | Reduz falsos alarmes |
| **Magnético** | Ímã e contato em porta/janela | Detecta abertura |
| **Vibração (sísmico)** | Capta impacto em parede, cofre, vidro | Arrombamento |
| **Quebra de vidro** | Reconhece a frequência sonora do vidro partido | Acústico |
| **Cerca (perimetral)** | Cabo sensor, cerca eletrificada ou barreira de feixe | Primeira camada |

Alarme: **central** (processa sinais), **zonas** (setorização que indica o local do disparo; zona 24 h para pânico), **monitoramento** remoto 24 h com resposta.

| Biometria | Nota |
|---|---|
| **Digital** | Barata e difundida; sofre com dedo sujo ou desgastado |
| **Facial** | Sem contato; sensível a luz e ângulo |
| **Íris** | Alta precisão, custo maior |
| **Voz** | Remota; vulnerável a ruído e gravação |

> [PROVA] ★ **FAR** (taxa de falsa aceitação) = impostor aceito, o erro mais grave para a segurança. **FRR** (taxa de falsa rejeição) = usuário legítimo barrado, erro de conveniência. Tornar o sistema mais rigoroso reduz a FAR e eleva a FRR; o ponto de equilíbrio é a taxa de erro igual (EER/CER).

### 4.2 CFTV e inteligência artificial

| CFTV | Característica |
|---|---|
| **Fixa** | Campo de visão único |
| **PTZ** | Movimento horizontal, vertical e zoom remotos |
| **Analógica** | Cabo coaxial; grava em **DVR** |
| **IP** | Digital, em rede (alimentação PoE); grava em **NVR** |
| **Analíticos/IA** | Cerca virtual, objeto abandonado ou removido, contagem, leitura de placas (LPR), reconhecimento facial |

> [ATENCAO] Dado biométrico é **dado pessoal sensível** (LGPD, art. 5º, II). O uso pelo tribunal para controle de acesso exige finalidade definida, necessidade, transparência, segurança e, conforme o risco, relatório de impacto. A exclusão do art. 4º, III, da LGPD alcança apenas tratamento para fins exclusivos de segurança pública, defesa e persecução penal.

## 5. Prevenção e combate a incêndio

> [SINTESE] Fogo = tetraedro (combustível, comburente, calor, reação em cadeia). Extinguir = retirar um elemento. O agente certo depende da classe (A, B, C, D, K). A NR-23 foi enxugada em 2022.

| NR-23 (Portaria MTP 2.769/2022) | Paráfrase |
|---|---|
| Medidas de prevenção | O empregador adota as medidas exigidas pela legislação estadual e pelas normas técnicas |
| Informação | Trabalhadores informados sobre uso de equipamentos, evacuação e alarme |
| Saídas | Em número suficiente, sinalizadas e desobstruídas, permitindo abandono rápido e seguro |
| Portas | Não podem ficar trancadas a ponto de impedir a saída durante a jornada |

> [ATENCAO] A NR-23 vigente não traz mais o detalhamento de extintores por classe: esse conteúdo vem das normas técnicas e dos regulamentos dos Corpos de Bombeiros. Conferir redação vigente.

| Classe ★ | Material | Agentes adequados | Proibido |
|---|---|---|---|
| **A** | Sólidos que queimam em superfície e profundidade, deixando brasa (papel, madeira, tecido) | Água, espuma, pó ABC | — |
| **B** | Líquidos e gases inflamáveis (queimam só na superfície) | Espuma, pó BC/ABC, CO₂ | Jato d'água |
| **C** | Equipamentos **energizados** | CO₂, pó químico | Água e espuma (conduzem eletricidade) |
| **D** | Metais pirofóricos (magnésio, titânio, sódio) | Pó especial classe D | Água |
| **K** | Óleos e gorduras de cozinha | Agente saponificante (classe K) | Água |

> [DICA] Desligada a energia, o fogo de classe C passa a ser tratado conforme o material que queima (em geral, A).

| Método de extinção | Elemento retirado |
|---|---|
| **Resfriamento** | Calor (água) |
| **Abafamento** | Comburente/oxigênio (espuma, CO₂, cobertor) |
| **Isolamento (retirada)** | Combustível |
| **Extinção química** | Quebra da reação em cadeia (pó químico) |

Propagação: **condução** (por contato com material sólido), **convecção** (massas de ar e gases quentes, sobe andares) e **irradiação** (ondas de calor à distância). Brigada de incêndio: grupo treinado para prevenção, primeiro combate, abandono de área e primeiros socorros.
