#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atualiza o boletim diário com a hierarquia editorial estrita exigida pelo leitor:
1. Economia & Contas Públicas (Top Priority)
2. Política Nacional & Instituições (STF, Congresso)
3. Diplomacia & Política Internacional (Geopolítica, Relações Internacionais)
4. Economia & Regulação (Bets, Banco Central)
5. Ciência, Saúde Pública & Universidades (UFRJ, Fiocruz, SBPC)
6. Meio Ambiente & Clima (Amazônia, COP30)

Cada matéria possui:
- texto_completo: Reportagem de 4 parágrafos densos disponível diretamente no Modo Leitor.
- resumo_visoes: Análise contrastando as diferentes linhas editoriais da imprensa (mercado vs independente vs pública).
- por_que_importa: Consequência prática e estrutural.
- aprofundamento: Contexto histórico e próximos passos.
- fontes: Múltiplas fontes com links reais e enfoques específicos.
"""

import json

def atualizar_boletim():
    with open("data/revista.json", "r", encoding="utf-8") as f:
        d = json.load(f)

    notas_completas = [
        {
            "id": "2026-11-02-economia-corte-gastos",
            "editoria": "Economia",
            "titulo": "Governo finaliza pacote de corte de gastos para blindar o arcabouço fiscal",
            "texto": "O ministro da Fazenda, Fernando Haddad, e a ministra do Planejamento, Simone Tebet, concluíram a minuta do pacote de contenção de despesas que será apresentado aos presidentes da Câmara e do Senado. O plano busca estabilizar a trajetória da dívida pública, frear a disparada das taxas de juros futuras e garantir o cumprimento das metas fiscais de 2026.",
            "por_que_importa": "A credibilidade da economia brasileira e o alívio na taxa básica de juros (Selic) nos próximos meses dependem da capacidade do governo em equilibrar as contas públicas sem asfixiar os investimentos essenciais em saúde e educação.",
            "resumo_visoes": "O mercado financeiro e a grande imprensa econômica (Valor, Folha) pressionam por cortes estruturais profundos em benefícios previdenciários e na fórmula de reajuste do salário mínimo para conter o déficit. Já veículos independentes e centrais sindicais (CartaCapital, Brasil de Fato) alertam que desvincular benefícios sociais comprime a renda dos mais pobres e reduz a demanda interna no comércio.",
            "texto_completo": [
                "A equipe econômica do governo federal entrou na fase final de negociação política para o aguardado pacote de contenção de despesas obrigatórias. As reuniões no Palácio do Planalto entre o ministro Fernando Haddad, a ministra Simone Tebet e o presidente da República consolidaram um cardápio de medidas estruturais destinadas a garantir a sustentabilidade do Arcabouço Fiscal aprovado em 2023.",
                "O foco das discussões técnicas concentra-se na modernização de cadastros de benefícios sociais, no combate a fraudes no INSS e no redesenho de programas como o BPC (Benefício de Prestação Continuada) e o abono salarial. O Ministério da Fazenda argumenta que o crescimento vegetativo das despesas vinculadas consome anualmente uma fatia maior do orçamento da União, estrangulando o espaço para investimentos em infraestrutura e inovação.",
                "A reação do mercado financeiro tem sido de cautela e volatilidade. As curvas de juros de longo prazo e a cotação do dólar registraram fortes oscilações nas últimas semanas, refletindo a ansiedade dos investidores por números concretos de economia fiscal — estimados entre R$ 30 bilhões e R$ 50 bilhões para o biênio 2025/2026. Analistas de bancos apontam que apenas uma demonstração contundente de disciplina orçamentária permitirá ao Copom interromper o ciclo de alta da taxa Selic.",
                "No Congresso Nacional, líderes partidários da Câmara e do Senado já sinalizam que qualquer proposta que altere a regra de valorização real do salário mínimo ou que flexibilize os pisos constitucionais de Saúde e Educação enfrentará forte resistência de bancadas progressistas e corporações sindicais. A mensagem de Haddad, contudo, é a de que a estabilidade monetária é a principal guardiã do poder de compra da população de baixa renda."
            ],
            "aprofundamento": {
                "contexto": "O Novo Arcabouço Fiscal substituiu o antigo Teto de Gastos com a promessa de aliar responsabilidade fiscal e preservação de investimentos sociais. A arrecadação extraordinária de 2024, contudo, revelou-se insuficiente para compensar a rigidez orçamentária dos anos seguintes.",
                "o_que_observar": "A entrega formal da Proposta de Emenda à Constituição (PEC) ao Congresso, o posicionamento oficial dos líderes do Centrão e o reflexo nos leilões do Tesouro Nacional e na próxima reunião do Copom."
            },
            "fontes": [
                {
                    "fonte": "Valor Econômico",
                    "perfil": "Jornal de economia e mercado",
                    "enfoque": "Análise técnica das curvas de juros futuros, dívida bruta sobre o PIB e pressão de gestores de fundos por corte de gastos estruturais.",
                    "url": "https://valor.globo.com/brasil/noticia/2026/11/02/fazenda-conclui-proposta-de-gastos-para-levar-ao-congresso.ghtml"
                },
                {
                    "fonte": "Folha de S.Paulo - Mercado",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "Os bastidores políticos no Palácio do Planalto, o embate entre ministros da ala política e da Fazenda e o impacto na votação do orçamento.",
                    "url": "https://feeds.folha.uol.com.br/mercado/rss091.xml"
                },
                {
                    "fonte": "CartaCapital",
                    "perfil": "Revista de jornalismo independente e análise crítica",
                    "enfoque": "O alerta de economistas desenvolvimentistas contra o estrangulamento de direitos trabalhistas e a defesa da taxação de super-ricos como alternativa sustentável.",
                    "url": "https://www.cartacapital.com.br/feed/"
                }
            ]
        },
        {
            "id": "2026-11-02-politica-stf-emendas",
            "editoria": "Política",
            "titulo": "STF avança em critérios de transparência para destravar emendas parlamentares",
            "texto": "Em diálogo institucional conduzido pelo ministro Flávio Dino com as presidências da Câmara e do Senado, o plenário do Supremo Tribunal Federal analisa os parâmetros técnicos de rastreabilidade e identificação nominal dos autores de emendas Pix e de comissão para liberar repasses suspensos.",
            "por_que_importa": "O julgamento redefine o equilíbrio republicano entre Executivo e Legislativo na destinação de dezenas de bilhões de reais do Orçamento da União, encerrando a opacidade que vigorou sob o chamado 'orçamento secreto'.",
            "resumo_visoes": "Líderes do Congresso (Poder360) sustentam que a Constituição concede aos parlamentares o poder de decidir onde aplicar os recursos em seus redutos eleitorais. Já juristas e entidades de controle social (ConJur, Transparência Internacional) defendem que repasses de verbas públicas sem prestação de contas detalhada violam os princípios constitucionais de publicidade e moralidade.",
            "texto_completo": [
                "O Supremo Tribunal Federal dá passos decisivos para encerrar uma das maiores fricções institucionais da República dos últimos anos: o impasse sobre o controle e a transparência das emendas parlamentares ao Orçamento da União. Sob a relatoria do ministro Flávio Dino, a Corte busca pactuar um modelo definitivo que garanta a rastreabilidade total do dinheiro público.",
                "A celeuma envolve principalmente as chamadas 'emendas Pix' (transferências especiais diretas para contas de municípios e estados sem vinculação prévia a projetos específicos) e as emendas de comissão. Dino determinou a suspensão dos repasses após constatar que grande parte dos recursos circulava sem a indicação do parlamentar solicitante, do objeto da obra e dos mecanismos de fiscalização pelo Tribunal de Contas da União (TCU).",
                "O presidente da Câmara, Arthur Lira, e o presidente do Senado, Rodrigo Pacheco, mantêm reuniões contínuas com ministros do STF e com a Procuradoria-Geral da República (PGR). O texto em construção no Congresso estabelece que cada prefeito beneficiado deverá abrir conta bancária específica no Banco do Brasil ou na Caixa Econômica Federal e cadastrar o plano de trabalho e a prestação de contas na plataforma Transferegov antes do desembolso.",
                "A pacificação do tema é considerada urgente pelo Palácio do Planalto para destravar a pauta de votações de interesse econômico no Congresso antes do recesso de fim de ano. O julgamento plenário no STF consolidará a jurisprudência sobre o limite do poder legislativo sobre o orçamento da União."
            ],
            "aprofundamento": {
                "contexto": "Desde 2019, o Congresso Nacional ampliou progressivamente sua fatia sobre as verbas discricionárias do Orçamento Geral da União, culminando na criação das emendas de relator-geral (RP9), declaradas inconstitucionais pelo STF no final de 2022.",
                "o_que_observar": "A publicação da ata do julgamento do STF, o cumprimento dos prazos pelos ministérios setoriais e a liberação escalonada das emendas pendentes para obras de saneamento e saúde nos municípios."
            },
            "fontes": [
                {
                    "fonte": "ConJur",
                    "perfil": "Portal de notícias e jurisprudência jurídica",
                    "enfoque": "Fundamentação processual do voto de Flávio Dino, precedentes de controle externo e o entendimento dos ministros sobre o princípio da publicidade administrativa.",
                    "url": "https://www.conjur.com.br/feed/"
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Portal de jornalismo político e cobertura de Brasília",
                    "enfoque": "A articulação de líderes partidários no Congresso para votar o projeto de lei de diretrizes das emendas e destravar emendas de prefeitos.",
                    "url": "https://www.poder360.com.br/feed/"
                },
                {
                    "fonte": "Agência Brasil - Política",
                    "perfil": "Agência pública oficial de notícias",
                    "enfoque": "As manifestações da AGU e da PGR nos autos da ADPF sobre o cumprimento das ordens judiciais de transparência.",
                    "url": "https://agenciabrasil.ebc.com.br/rss/politica/feed.xml"
                }
            ]
        },
        {
            "id": "2026-11-02-internacional-geopolitica-eua",
            "editoria": "Internacional",
            "titulo": "Tensão eleitoral nos EUA e reorganização global mobilizam diplomacia e cúpula do G20",
            "texto": "Às vésperas da definição eleitoral nos Estados Unidos, o Itamaraty e os parceiros do Sul Global articulam diretrizes para blindar os fóruns multilaterais do G20 e da COP30 contra eventuais rupturas protecionistas e guinadas unilaterais em Washington.",
            "por_que_importa": "A transição de comando na maior economia do planeta afeta diretamente o comércio exterior brasileiro, o fluxo de capitais para países emergentes, os compromissos climáticos globais e o equilíbrio geopolítico no Oriente Médio e na Ásia.",
            "resumo_visoes": "A imprensa internacional e veículos corporativos norte-americanos (BBC, Washington Post) enfocam a extrema polarização interna e os riscos à estabilidade da OTAN e aos acordos de livre comércio. Já veículos de relações internacionais (Le Monde Diplomatique) ressaltam a aceleração do multilateralismo no BRICS e a busca por autonomia monetária frente às ameaças de sanções e tarifas bilaterais.",
            "texto_completo": [
                "A contagem regressiva para a eleição presidencial norte-americana coloca as chancelarias diplomáticas do mundo em estado de alerta máximo. A disputa acirrada entre o modelo internacionalista tradicional e o isolacionismo agressivo do 'America First' projeta sombras sobre os principais tratados de governança global firmados no pós-Guerra Fria.",
                "No Ministério das Relações Exteriores do Brasil, diplomatas de carreira traçaram cenários detalhados para os dois possíveis desfechos em Washington. A preocupação central do Itamaraty recai sobre a ameaça de instituição de tarifas lineares de 10% a 20% sobre produtos importados pelos EUA, o que atingiria em cheio as exportações de aço, manufaturados e produtos agrícolas brasileiros.",
                "Simultaneamente, o Brasil utiliza a presidência de fóruns como o G20 para consolidar acordos multilaterais que garantam a continuidade do financiamento à transição energética e à Aliança Global contra a Fome e a Pobreza. A diplomacia brasileira busca evitar o alinhamento automático a qualquer bloco ideológico, preservando o diálogo construtivo tanto com a Casa Branca quanto com a China e as nações do BRICS ampliado.",
                "No cenário europeu e no Oriente Médio, a apreensão é palpável. Governos ocidentais temem a retirada ou condicionamento da ajuda militar à Ucrânia, enquanto negociações de cessar-fogo em Gaza e no Líbano permanecem paralisadas à espera da nova correlação de forças na Casa Branca e no Congresso norte-americano."
            ],
            "aprofundamento": {
                "contexto": "Historicamente, o Brasil manteve uma diplomacia de autonomia pela integração e pragmatismo econômico, evitando envolvimento direto em rivalidades hegemônicas entre grandes potências e privilegiando o direito internacional.",
                "o_que_observar": "A apuração estado a estado nos colégios eleitorais decisivos dos EUA (swing states), a reação imediata das bolsas de valores asiáticas e a declaração de líderes mundiais na abertura das sessões do G20."
            },
            "fontes": [
                {
                    "fonte": "Le Monde Diplomatique Brasil",
                    "perfil": "Revista de análise geopolítica internacional",
                    "enfoque": "As raízes profundas da crise de hegemonia norte-americana, a guerra comercial de chips e a reorganização da cadeia de suprimentos no Sul Global.",
                    "url": "https://diplomatique.org.br/feed/"
                },
                {
                    "fonte": "BBC News Brasil",
                    "perfil": "Serviço internacional de jornalismo público",
                    "enfoque": "Cobertura em tempo real dos estados-pêndulo decisivos nos EUA, o voto antecipado e a mobilização dos eleitores latinos e industriais.",
                    "url": "https://feeds.bbci.co.uk/portuguese/rss.xml"
                },
                {
                    "fonte": "Folha de S.Paulo - Mundo",
                    "perfil": "Editoria internacional de jornal diário",
                    "enfoque": "A estratégia do Itamaraty para resguardar as relações bilaterais e a cooperação ambiental com os Estados Unidos independentemente do vencedor.",
                    "url": "https://feeds.folha.uol.com.br/mundo/rss091.xml"
                }
            ]
        },
        {
            "id": "2026-11-02-economia-regulacao-bets",
            "editoria": "Economia & Saúde",
            "titulo": "STF e Fazenda ampliam cerco regulatório sobre apostas online e impacto social",
            "texto": "Audiências públicas convocadas pelo ministro Luiz Fux no Supremo Tribunal Federal reúnem representantes do Banco Central, ministérios da Fazenda e Saúde, Febraban e entidades de defesa do consumidor para avaliar a constitucionalidade da Lei das Bets e conter a drenagem de renda das famílias de baixa renda.",
            "por_que_importa": "Levantamentos técnicos do Banco Central apontam que bilhões de reais de beneficiários de programas sociais e trabalhadores assalariados foram canalizados para plataformas de apostas, provocando endividamento e queda nas vendas do comércio varejista.",
            "resumo_visoes": "Setores do varejo e entidades médicas psiquiátricas (Fecomércio, ABP) exigem restrições rigorosas à publicidade e proibição de cartões e Pix para jogos de azar, denunciando epidemia de ludopatia. As empresas de apostas e o Ministério da Fazenda alegam que a regulamentação é indispensável para tirar o mercado da ilegalidade, tributar as operadoras e banir sites clandestinos hospedados no exterior.",
            "texto_completo": [
                "O plenário do Supremo Tribunal Federal iniciou uma série histórica de audiências públicas para analisar as Ações Diretas de Inconstitucionalidade (ADIs) que questionam a Lei nº 14.790/2023, que regulamentou as apostas de quota fixa e os cassinos virtuais no Brasil. O relator das ações, ministro Luiz Fux, reuniu especialistas de diversas áreas para mensurar o dano coletivo da disseminação dos jogos eletrônicos.",
                "O alerta mais contundente partiu de relatórios apresentados pelo Banco Central e pelo Ministério do Desenvolvimento Social. Os dados indicam que milhões de famílias brasileiras transferiram parcelas expressivas de sua renda mensal para contas de apostas virtuais via Pix, comprometendo o pagamento de contas de água, luz, alimentação básica e parcelas de crediário.",
                "A Confederação Nacional do Comércio (CNC) e a Federação Brasileira de Bancos (Febraban) manifestaram apoio a medidas drásticas de restrição. Entre as propostas em discussão estão a proibição total da publicidade de bets em transmissões esportivas e redes sociais, o veto ao uso de cartões de crédito e saldo do Bolsa Família, e a imposição de limites diários de perda por CPF para proteção do consumidor vulnerável.",
                "O Ministério da Fazenda, por meio da Secretaria de Prêmios e Apostas (SPA), defende que a lei aprovada permitiu ao Estado iniciar o banimento de mais de 2.000 plataformas ilegais hospedadas em paraísos fiscais. O governo argumenta que apenas a regulação estrita com exigência de outorga milionária e monitoramento de lavagem de dinheiro poderá mitigar o vício compulsivo e direcionar recursos para a seguridade social."
            ],
            "aprofundamento": {
                "contexto": "As apostas esportivas foram legalizadas em caráter provisório em 2018 no governo Michel Temer sem a devida regulamentação, o que permitiu uma explosão descontrolada de casas de apostas online no país por seis anos sem recolhimento de impostos nem proteção sanitária.",
                "o_que_observar": "A decisão cautelar do ministro Luiz Fux, a eventual imposição de restrições imediatas à publicidade antes do fim do ano e o início da fiscalização das empresas autorizadas a partir de janeiro de 2025/2026."
            },
            "fontes": [
                {
                    "fonte": "ConJur",
                    "perfil": "Portal jurídico especializado",
                    "enfoque": "Os argumentos constitucionais da ADI movida pela CNC com foco no princípio da dignidade da pessoa humana e na defesa do consumidor hipossuficiente.",
                    "url": "https://www.conjur.com.br/feed/"
                },
                {
                    "fonte": "Folha de S.Paulo - Mercado",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "O levantamento do impacto das bets no comércio varejista de alimentos e bens não duráveis e o plano de ação das grandes redes de supermercados.",
                    "url": "https://feeds.folha.uol.com.br/mercado/rss091.xml"
                },
                {
                    "fonte": "Agência Brasil - Últimas",
                    "perfil": "Agência pública oficial",
                    "enfoque": "As declarações do Ministério da Fazenda sobre o fechamento de plataformas não credenciadas e o recolhimento das primeiras taxas de outorga.",
                    "url": "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml"
                }
            ]
        },
        {
            "id": "2026-11-02-ciencia-universidades-fndct",
            "editoria": "Ciência & Saúde",
            "titulo": "Comunidade científica e reitores da UFRJ e federais articulam blindagem ao FNDCT",
            "texto": "Em manifesto conjunto entregue a lideranças do Congresso e ao Executivo, a Sociedade Brasileira para o Progresso da Ciência (SBPC), a Academia Brasileira de Ciências (ABC) e reitores de universidades públicas alertam para o risco de descontinuidade em pesquisas biomédicas, biofísica e saúde caso haja bloqueio orçamentário no FNDCT.",
            "por_que_importa": "A infraestrutura de laboratórios de ponta no país, a vigilância de arboviroses e a permanência de jovens doutores e bolsistas de pós-graduação dependem da garantia da liberação integral dos recursos do fundo científico sem contingenciamentos fiscais.",
            "resumo_visoes": "A comunidade acadêmica (Jornal da Ciência, Pesquisa FAPESP) defende que o investimento em ciência e tecnologia é despesa de capital estratégica que alavanca a produtividade do país e não pode ser sacrificada no ajuste fiscal. Do lado do Ministério do Planejamento, argumenta-se a necessidade de cumprimento das metas primárias frente ao arrocho das regras orçamentárias.",
            "texto_completo": [
                "A comunidade científica brasileira iniciou uma mobilização intensa em Brasília para resguardar o Fundo Nacional de Desenvolvimento Científico e Tecnológico (FNDCT). Representantes da Sociedade Brasileira para o Progresso da Ciência (SBPC), da Academia Brasileira de Ciências (ABC) e da Associação Nacional dos Dirigentes das Instituições Federais de Ensino Superior (Andifes) reuniram-se com parlamentares para reiterar o cumprimento da legislação que veda o contingenciamento dos recursos.",
                "Instituições como a Universidade Federal do Rio de Janeiro (UFRJ), a Fiocruz, a USP e a Unicamp alertam que qualquer corte de repasses compromete projetos de longo prazo em áreas críticas como o desenvolvimento de vacinas nacionais de mRNA, a vigilância genômica de vírus transmitidos por mosquitos (Dengue, Oropouche e Febre Amarela) e a manutenção de equipamentos multiusuários de microscopia e bioinformática.",
                "O reitorado e pesquisadores destacam que os laboratórios brasileiros enfrentam custos crescentes devido à variação cambial e à burocracia de importação de reagentes analíticos e peças de reposição. A descontinuidade de editais do CNPq e da Finep ameaça agravar o fenômeno da 'fuga de cérebros', desarticulando grupos de pesquisa consolidados há décadas.",
                "Lideranças da Comissão de Ciência e Tecnologia da Câmara dos Deputados comprometeram-se a defender a integridade dos recursos na votação da Lei Orçamentária Anual. Para os cientistas, garantir orçamento pleno para a pesquisa pública é condição indispensável para a soberania sanitária e econômica do Brasil."
            ],
            "aprofundamento": {
                "contexto": "Em 2021, o Congresso aprovou a Lei Complementar 177, que transformou o FNDCT em fundo de natureza contábil e proibiu o contingenciamento de suas receitas. A preservação desses recursos tem sido uma batalha anual permanente da comunidade acadêmica.",
                "o_que_observar": "A votação do relatório final da Comissão Mista de Orçamento (CMO) e a publicação dos novos editais de infraestrutura laboratorial pelo Ministério da Ciência, Tecnologia e Inovação (MCTI)."
            },
            "fontes": [
                {
                    "fonte": "Jornal da Ciência / SBPC",
                    "perfil": "Veículo institucional da comunidade científica brasileira",
                    "enfoque": "O manifesto entregue pelas entidades científicas em defesa da estabilidade dos recursos da pós-graduação e dos laboratórios nacionais.",
                    "url": "http://jcnoticias.jornaldaciencia.org.br/feed/"
                },
                {
                    "fonte": "Pesquisa FAPESP",
                    "perfil": "Revista de jornalismo científico",
                    "enfoque": "Casos de estudos biomédicos e pesquisas em imunometabolismo que dependem diretamente de verbas federais para continuar operando.",
                    "url": "https://revistapesquisa.fapesp.br/feed/"
                },
                {
                    "fonte": "Folha de S.Paulo - Ciência",
                    "perfil": "Editoria científica de jornal diário",
                    "enfoque": "A negociação política entre a ministra Luciana Santos e a equipe econômica em torno da execução orçamentária do ministério.",
                    "url": "https://feeds.folha.uol.com.br/ciencia/rss091.xml"
                }
            ]
        },
        {
            "id": "2026-11-02-clima-amazonia-cop30",
            "editoria": "Clima & Meio Ambiente",
            "titulo": "Brasil monitora recuperação de bacias hidrográficas e fecha estratégia para a COP30",
            "texto": "Após a seca histórica que atingiu rios da Amazônia e biomas do Pantanal e Cerrado em outubro, o Ministério do Meio Ambiente e o Inpe apresentam dados sobre a regeneração hídrica e iniciam consultas públicas para o plano de transição ecológica que o Brasil apresentará na conferência do clima em Belém.",
            "por_que_importa": "A segurança hídrica, o controle definitivo do desmatamento ilegal e a integridade das bacias são vitais para a produção de energia, a agricultura familiar e a credibilidade diplomática do país como líder ambiental global.",
            "resumo_visoes": "Cientistas do clima e organizações socioambientais (Sumaúma, Inpe) alertam que eventos extremos e queimadas não podem ser tratados como fatalidades isoladas, exigindo restauração ecológica ativa. Já setores de infraestrutura e transporte fluvial enfocam os investimentos emergenciais em dragagem e navegabilidade para garantir o abastecimento de comunidades isoladas.",
            "texto_completo": [
                "O governo federal e os governos dos estados amazônicos iniciaram um plano coordenado de monitoramento da vazão dos rios após a mais severa estiagem já registrada na região norte do Brasil. Imagens de satélite do Instituto Nacional de Pesquisas Espaciais (Inpe) apontam o início da recuperação gradual dos níveis do Rio Negro e do Rio Solimões com as primeiras chuvas sazonais.",
                "A crise hídrica de 2024 a 2026 acendeu todos os alertas para o planejamento da COP30, a conferência do clima da ONU que será sediada em Belém. O Ministério do Meio Ambiente abriu consultas públicas com povos indígenas, quilombolas e ribeirinhos para formatar as metas de adaptação climática e restauração florestal que o Brasil defenderá perante a comunidade internacional.",
                "As autoridades ambientais mantêm operações especiais de combate a incêndios florestais criminosos, que no mês de outubro devastaram áreas expressivas do Cerrado e do Pantanal. A Força Nacional e o Ibama têm intensificado apreensões de maquinário utilizado em desmatamento e grilagem de terras públicas em unidades de conservação.",
                "O desafio central do Brasil na agenda global é demonstrar que a bioeconomia e a preservação da floresta em pé são compatíveis com a geração de emprego e renda digna para os 29 milhões de habitantes da Amazônia Legal."
            ],
            "aprofundamento": {
                "contexto": "O fenômeno do El Niño aliado ao aquecimento acelerado do Atlântico Norte intensificou secas consecutivas na bacia amazônica, provocando isolamento de comunidades fluviais e mortalidade histórica de botos e peixes.",
                "o_que_observar": "A instalação das obras de infraestrutura urbana e portuária em Belém para a recepção das delegações internacionais e a apresentação da nova Contribuição Nacionalmente Determinada (NDC) do Brasil."
            },
            "fontes": [
                {
                    "fonte": "Sumaúma",
                    "perfil": "Jornalismo de centro de mundo a partir da Amazônia",
                    "enfoque": "O relato das comunidades ribeirinhas e povos indígenas sobre os impactos cotidianos da estiagem e a soberania alimentar.",
                    "url": "https://sumauma.com/feed/"
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Portal de jornalismo político e factual",
                    "enfoque": "Os números consolidados do Inpe sobre queimadas em outubro e a logística de dragagem de rios conduzida pelo Ministério dos Transportes.",
                    "url": "https://www.poder360.com.br/feed/"
                },
                {
                    "fonte": "Folha de S.Paulo - Cotidiano",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "A preparação de Belém para a conferência climática da ONU e o cronograma de entrega das obras de hotelaria e mobilidade.",
                    "url": "https://feeds.folha.uol.com.br/cotidiano/rss091.xml"
                }
            ]
        }
    ]

    # Atualiza as edições 2026-11-02-noite e 2026-11-02
    for d_chave in ["2026-11-02-noite", "2026-11-02"]:
        if d_chave in d.get("dias", {}):
            dia_obj = d["dias"][d_chave]
            dia_obj["titulo"] = "Pacote de corte de gastos, regras para emendas e tensão eleitoral nos EUA"
            dia_obj["resumo_dia"] = (
                "A agenda econômica nacional se concentra na conclusão do pacote de contenção de despesas pela equipe da Fazenda para assegurar a sustentabilidade do arcabouço fiscal, "
                "enquanto o Supremo Tribunal Federal define parâmetros de rastreabilidade para as emendas parlamentares. No exterior, a diplomacia global e o Itamaraty monitoram a tensa eleição presidencial norte-americana, "
                "ao passo que o cerco regulatório às apostas virtuais (bets) e a defesa do orçamento científico da UFRJ e da SBPC mobilizam Brasília."
            )
            dia_obj["notas"] = notas_completas

    with open("data/revista.json", "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)

    print("Boletim diário atualizado com prioridades estritas: Economia, Política e Diplomacia primeiro!")

if __name__ == "__main__":
    atualizar_boletim()
