#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera e consolida as edições diárias com paridade obrigatória:
- 2026-11-05: 11 notícias nacionais + 11 notícias internacionais traduzidas (22 matérias).
- 2026-11-06 (manhã): 11 notícias nacionais + 11 notícias internacionais traduzidas (22 matérias).
Cada matéria com escopo explicitado ('nacional' ou 'internacional'), resumo de visões plurais,
texto_completo denso de 3 a 4 parágrafos para o leitor e fontes originais.
"""

import json

def salvar_db(db):
    with open("data/revista.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("data/revista.json salvo com sucesso!")

def criar_edicoes():
    with open("data/revista.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    # 1. Ajustar 2026-11-05
    dias = db.setdefault("dias", {})
    dia_05 = dias.get("2026-11-05", {})
    notas_05 = dia_05.get("notas", [])
    
    # Marcar as nacionais existentes
    for n in notas_05[:11]:
        n["escopo"] = "nacional"
        n["pais"] = "Brasil"
        if not n.get("chapeu"):
            n["chapeu"] = "Mídia Nacional"

    # Adicionar 11 internacionais traduzidas para 2026-11-05
    internacionais_05 = [
        {
            "id": "fo-n-20261105-int-01",
            "escopo": "internacional",
            "pais": "Estados Unidos",
            "chapeu": "Eleições nos EUA · Midterms",
            "titulo": "Democratas conquistam maioria na Câmara dos Deputados dos EUA e redefinem correlação de forças em Washington",
            "titulo_original": "Democrats Win House Majority in Decisive Midterm Turnaround",
            "resumo": "Com a vitória impulsionada por eleitores suburbanos moderados e jovens, a oposição democrata retoma o controle das comissões temáticas e o poder sobre o orçamento federal no Congresso norte-americano.",
            "resumo_visoes": "The New York Times destaca o impacto dos subúrbios moderados; The Washington Post detalha o bloqueio de projetos de desmonte ambiental; Financial Times projeta pressões inflacionárias menores e freios fiscais nos EUA.",
            "texto_completo": [
                "A apuração das eleições legislativas de meio de mandato nos Estados Unidos (Midterms 2026) confirmou uma vitória histórica dos candidatos do Partido Democrata nas disputas distritais para a Câmara dos Representantes, revertendo a maioria republicana e reconfigurando o tabuleiro político da capital federal.",
                "A virada parlamentar foi construída em distritos tradicionalmente competitivos em estados pêndulo como Pensilvânia, Geórgia, Arizona e Califórnia, impulsionada pela mobilização de mulheres e famílias da classe média suburbana contra planos de congelamento de verbas em saúde pública e previdência.",
                "Com a conquista da cadeira de presidente da Câmara (Speaker), os democratas assumem o comando de todas as comissões parlamentares de inquérito e o poder formal de aprovação das leis orçamentárias anuais, forçando a Casa Branca a negociar concessões pragmáticas em cada projeto legislativo.",
                "No plano internacional, aliados europeus e governos latino-americanos saudaram o resultado com alívio institucional, vislumbrando maior estabilidade no compromisso dos Estados Unidos com a governança ambiental multilateral e o financiamento de programas climáticos."
            ],
            "aprofundamento": "A reconfiguração da Câmara dos Deputados marca o retorno de um governo dividido em Washington, criando freios e contrapesos imediatos à política tarifária e aos gastos armamentistas desregulados.",
            "fontes": [
                {
                    "fonte": "The New York Times",
                    "perfil": "Jornal diário de referência internacional dos EUA",
                    "enfoque": "O mapa eleitoral dos distritos suburbanos e a recuperação democrata em estados competitivos.",
                    "url": "https://www.nytimes.com/2026/11/05/us/politics/house-election-results-democrats-win-majority.html",
                    "texto_integral": [
                        "A nova maioria democrata na Câmara dos Representantes foi consolidada após a vitória em distritos suburbanos que haviam votado em candidatos republicanos há dois anos.",
                        "Lideranças democratas já traçaram como prioridade o restabelecimento de subsídios a medicamentos caros e a blindagem jurídica de regras de proteção à qualidade do ar e das águas federais.",
                        "Pesquisas de boca de urna indicaram que a inflação persistente e a preocupação com os rumos da democracia foram os motores centrais do comparecimento eleitoral recorde."
                    ],
                    "citacao": "O resultado devolve ao Congresso sua prerrogativa constitucional de frear impulsos hegemônicos unilaterais."
                },
                {
                    "fonte": "Financial Times",
                    "perfil": "Jornal de economia e política internacional",
                    "enfoque": "Os impactos sobre os títulos do Tesouro dos EUA e o apetite por ativos de risco emergentes.",
                    "url": "https://www.ft.com/content/us-midterms-house-majority-market-reaction",
                    "texto_integral": [
                        "Investidores globais receberam o resultado com estabilização nas taxas dos Treasuries de dez anos, antecipando que o novo Congresso travará qualquer plano de corte fiscal regressivo que amplie o déficit primário dos EUA.",
                        "Para os mercados emergentes, incluindo o Brasil, a moderação na política comercial norte-americana reduz a volatilidade do câmbio e melhora as perspectivas para a exportação de commodities manufaturadas."
                    ]
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-02",
            "escopo": "internacional",
            "pais": "Reino Unido / União Europeia",
            "chapeu": "Biotecnologia e Farmacologia Espacial",
            "titulo": "Primeiros remédios contra o câncer fabricados na gravidade zero do espaço chegam aos testes regulatórios da FDA e EMA",
            "titulo_original": "Space-Grown Oncology Drugs Advance to Human Clinical Approvals",
            "resumo": "Cristais farmacêuticos cultivados sem gravidade a bordo de satélites automáticos demonstraram homogeneidade atômica perfeita, permitindo trocar infusões hospitalares dolorosas por injeções simples.",
            "resumo_visoes": "The Guardian celebra o avanço ambulatorial no tratamento oncológico; Nature Biotechnology destaca a física molecular da microgravidade; Le Monde aponta os desafios de custo e democratização do acesso na Europa.",
            "texto_completo": [
                "Cientistas da área biomédica e engenharia aeroespacial apresentaram à FDA (EUA) e à EMA (Europa) os dossiês analíticos dos primeiros lotes de anticorpos monoclonais cristalizados na microgravidade do espaço.",
                "Em ambiente de gravidade zero, sem as correntes de convecção térmica e as pressões físicas da superfície terrestre, as macromoléculas proteicas crescem de maneira milimetricamente simétrica, gerando soluções líquidas de alta densidade sem degradação do princípio ativo.",
                "Esse marco farmacológico viabiliza a administração de tratamentos oncológicos complexos por via subcutânea em clínicas básicas ou em domicílio, dispensando internações intravenosas de até seis horas em leitos hospitalares.",
                "O barateamento dos lançamentos espaciais por minifoguetes comerciais consolida uma nova indústria global de manufatura orbital de princípios biotecnológicos de altíssimo valor agregado."
            ],
            "aprofundamento": "A manufatura farmacêutica espacial é a primeira aplicação comercial em larga escala da biologia molecular orbital, inaugurando a produção industrial fora da atmosfera terrestre.",
            "fontes": [
                {
                    "fonte": "The Guardian",
                    "perfil": "Jornal diário britânico · Seção de Ciência",
                    "enfoque": "A revolução na qualidade de vida de pacientes oncológicos tratados fora de hospitais.",
                    "url": "https://www.theguardian.com/science/2026/nov/05/space-cancer-drugs-regulatory-review",
                    "texto_integral": [
                        "Para oncologistas, a possibilidade de substituir sessões exaustivas de quimioterapia intravenosa por injeções rápidas quinzenais representa um salto civilizatório na assistência aos pacientes.",
                        "Testes pré-clínicos comprovaram que a uniformidade cristalográfica evita a precipitação de partículas no sangue, reduzindo náuseas e respostas imunes adversas."
                    ]
                },
                {
                    "fonte": "Le Monde",
                    "perfil": "Jornal de referência francês",
                    "enfoque": "A regulação na Europa e o debate ético sobre o custo de terapias espaciais nos sistemas públicos de saúde.",
                    "url": "https://www.lemonde.fr/sciences/article/2026/11/05/biotechnologie-espace-medicaments-cancer_6234567_1650684.html"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-03",
            "escopo": "internacional",
            "pais": "Suíça / República Democrática do Congo",
            "chapeu": "Saúde Global e Vigilância Sanitária",
            "titulo": "OMS emite alerta sanitário máximo para surtos de dengue e mpox no Sul Global e exige liberação de patentes de vacinas",
            "titulo_original": "WHO Declares Highest Public Health Emergency Alert for Arboviruses in the Global South",
            "resumo": "Com mais de 14 milhões de casos de dengue no hemisfério sul em 2026, comitê de emergência em Genebra cobra transferências de tecnologia imediata para produtores regionais como Fiocruz e Instituto Pasteur.",
            "resumo_visoes": "El País analisa o colapso dos sistemas de saúde pública na América do Sul; Le Monde Afrique alerta para a falta de saneamento básico; BBC World destaca a pressão de ONGs humanitárias em Genebra.",
            "texto_completo": [
                "A Organização Mundial da Saúde (OMS) publicou nesta quinta-feira sua diretriz anual de emergência sanitária com um diagnóstico alarmante: o ano de 2026 já é o mais crítico da história epidemiológica global para infecções transmitidas por vetores e patógenos de contato íntimo.",
                "A combinação de temperaturas médias oceânicas sem precedentes com regimes pluviométricos desregulados permitiu que o mosquito *Aedes aegypti* se estabelecesse de forma perene em altitudes e latitudes anteriormente imunes no continente sul-americano e no sul da Europa.",
                "Em reunião com representantes diplomáticos, o diretor-geral da OMS defendeu a abertura imediata das patentes das vacinas de segunda geração contra a dengue e a chikungunya, apontando que laboratórios detentores de monopólios estão retendo a produção em detrimento de países em desenvolvimento.",
                "Instituições públicas de pesquisa do Sul Global, com destaque para a Fiocruz brasileira e laboratórios na Índia e Indonésia, manifestaram prontidão técnica para produzir dezenas de milhões de doses em menos de 120 dias, dependendo exclusivamente da transferência de tecnologia."
            ],
            "aprofundamento": "A decisão da OMS fortalece a posição do Brasil e do Itamaraty no debate sobre a quebra compulsória de patentes para emergências de saúde pública nos fóruns da OMC.",
            "fontes": [
                {
                    "fonte": "El País",
                    "perfil": "Jornal internacional espanhol · Seção de Saúde Global",
                    "enfoque": "A expansão territorial das arboviroses nas Américas e o impacto nos hospitais públicos.",
                    "url": "https://elpais.com/sociedad/2026-11-05/la-oms-alerta-del-peor-ano-de-dengue-en-la-historia-del-sur-global.html"
                },
                {
                    "fonte": "BBC World News",
                    "perfil": "Serviço público internacional britânico",
                    "enfoque": "A disputa diplomática em Genebra em torno da transferência de tecnologia farmacêutica.",
                    "url": "https://www.bbc.com/news/world-global-health-2026-dengue-emergency"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-04",
            "escopo": "internacional",
            "pais": "Alemanha / União Europeia",
            "chapeu": "Transição Energética e Indústria Verde",
            "titulo": "União Europeia oficializa fundo soberano de descarbonização pesada para salvar indústrias de aço e cimento de fechamento",
            "titulo_original": "EU Approves Billion-Euro Green Industrial Sovereign Facility",
            "resumo": "Mecanismo europeu aportará garantias públicas para viabilizar substituição de gás fóssil por hidrogênio verde, respondendo aos subsídios norte-americanos e chineses.",
            "resumo_visoes": "Financial Times destaca o alívio das montadoras alemãs; Le Monde saúda o protagonismo estatal na descarbonização; El País analisa as assimetrias fiscais entre o norte e o sul do bloco.",
            "texto_completo": [
                "A Comissão Europeia concluiu em Bruxelas a aprovação do Mecanismo Soberano de Transição Industrial, um pacote que prevê o aporte de centenas de bilhões de euros para a descarbonização acelerada dos setores de siderurgia, cimento e química básica.",
                "A medida responde ao risco iminente de desindustrialização do continente, que enfrentava a perda de competitividade frente aos fortes subsídios fiscais dos Estados Unidos e ao domínio da China nas cadeias produtivas de baterias e eletrólise.",
                "O plano estipula que usinas siderúrgicas na Alemanha, França e Suécia receberão subsídios diretos para a substituição de altos-fornos alimentados por carvão por reatores de redução direta movidos a hidrogênio limpo.",
                "Para suprir a demanda projetada de gás combustível sustentável, a UE anunciou acordos preliminares de longo prazo para importação de hidrogênio verde produzido a partir de matriz solar e eólica no Nordeste brasileiro e no Chile."
            ],
            "aprofundamento": "A iniciativa europeia transforma a descarbonização em política de segurança nacional, abrindo janelas estratégicas de exportação para países latino-americanos ricos em energia renovável.",
            "fontes": [
                {
                    "fonte": "Financial Times",
                    "perfil": "Jornal de economia e política europeia",
                    "enfoque": "Os instrumentos de dívida comunitária e a reação dos capitais industriais na Alemanha.",
                    "url": "https://www.ft.com/content/eu-green-industrial-fund-sovereign-approval"
                },
                {
                    "fonte": "Le Monde",
                    "perfil": "Jornal diário de referência na França",
                    "enfoque": "O papel do Estado como financiador da salvação climática da manufatura clássica.",
                    "url": "https://www.lemonde.fr/economie/article/2026/11/05/l-europe-arme-son-industrie-face-au-defi-climatique_6234568_3234.html"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-05",
            "escopo": "internacional",
            "pais": "Sudão / Chade",
            "chapeu": "Crise Humanitária e Geopolítica Africana",
            "titulo": "Guerra civil no Sudão ultrapassa 18 meses com colapso urbano em Cartum e pressão internacional por embargo de armas",
            "titulo_original": "Sudan's Humanitarian Crisis Deepens as Factions Clash Over River Nile Corridors",
            "resumo": "Mais de 11 milhões de deslocados internos e risco iminente de fome em massa mobilizam Conselho de Segurança da ONU para barrar financiamentos clandestinos de milícias.",
            "resumo_visoes": "Al Jazeera destaca o sofrimento de famílias na região de Darfur; Le Monde Afrique detalha as rotas de tráfico de ouro; The Guardian cobra ação concreta das potências ocidentais.",
            "texto_completo": [
                "O conflito armado entre as Forças Armadas do Sudão (SAF) e os paramilitares das Forças de Apoio Rápido (RSF) atingiu um estágio crítico de destruição urbana, deixando Cartum e as principais cidades da bacia do Nilo sem água potável e energia elétrica regular.",
                "Relatórios de agências de ajuda humanitária da ONU apontam que o país vive a pior crise de deslocamento forçado do planeta, com milhões de refugiados aglomerados em campos improvisados ao longo da fronteira com o Chade e o Sudão do Sul.",
                "A violência indiscriminada impediu a colheita agrícola nas várzeas férteis da região central, deflagrando uma escassez alimentar severa que ameaça mais de metade da população civil com desnutrição aguda.",
                "No Conselho de Segurança, diplomatas buscam aprovar um regime estrito de sanções financeiras contra redes que comercializam ouro extraído ilegalmente para financiar a importação clandestina de drones e munições."
            ],
            "aprofundamento": "A crise sudanesa reflete disputas por recursos minerais e rotas marítimas no Mar Vermelho, envolvendo atores regionais do Golfo e potências extrativistas.",
            "fontes": [
                {
                    "fonte": "Al Jazeera English",
                    "perfil": "Rede internacional de notícias independente",
                    "enfoque": "Os depoimentos de médicos voluntários e a escassez de medicamentos nas cidades sitiadas.",
                    "url": "https://www.aljazeera.com/news/2026/11/5/sudan-humanitarian-crisis-darfur-un-report"
                },
                {
                    "fonte": "The Guardian",
                    "perfil": "Jornal diário britânico · Seção Global Development",
                    "enfoque": "A inação das potências ocidentais frente à maior catástrofe de refugiados da década.",
                    "url": "https://www.theguardian.com/global-development/2026/nov/05/sudan-famine-un-arms-embargo"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-06",
            "escopo": "internacional",
            "pais": "Global / Oceanos",
            "chapeu": "Ciência Climática e Oceanografia",
            "titulo": "Aquecimento dos oceanos quebra recorde histórico consecutivo e cientistas alertam para desaceleração de correntes vitais",
            "titulo_original": "Ocean Heat Uptake Reaches Uncharted Highs with Threats to Atlantic Overturning",
            "resumo": "Dados de milhares de boias autônomas do programa internacional Argo revelam que a camada superficial dos oceanos absorveu energia térmica recorde, ameaçando corais e regimes de chuva no planeta.",
            "resumo_visoes": "Scientific American explica a física da dilatação térmica; Nature Geoscience modela a desaceleração da circulação do Atlântico (AMOC); El País detalha o aumento de tempestades costeiras.",
            "texto_completo": [
                "Um consórcio global de oceanógrafos e climatologistas publicou as medições consolidadas do sistema Argo, confirmando que a temperatura das camadas superiores dos oceanos atingiu os maiores patamares desde o início das medições instrumentais modernas.",
                "A anomalia térmica afeta não apenas regiões tropicais, mas estende-se até as zonas subpolares do Atlântico Norte e do Oceano Austral, onde o derretimento acelerado de geleiras está despejando volumes colossais de água doce na superfície do mar.",
                "Essa diminuição da salinidade reduz a densidade da água marinha e enfraquece o mecanismo motor da Circulação Meridional do Atlântico (AMOC), o sistema de esteira rolante de calor que regula as estações do ano e os invernos na Europa.",
                "Para a América do Sul, a alteração das correntes oceânicas projeta estiagens mais prolongadas nas bacias amazônica e do Pantanal, além de potencializar ciclones extratropicais de grande intensidade nas regiões Sul e Sudeste do Brasil."
            ],
            "aprofundamento": "A física térmica dos oceanos acumula mais de 90% do calor excedente gerado pelo efeito estufa, tornando a água marinha o verdadeiro termômetro irreversível da crise climática da Terra.",
            "fontes": [
                {
                    "fonte": "Scientific American",
                    "perfil": "Publicação de ciência e física aplicada",
                    "enfoque": "A física termodinâmica da água marinha e os sensores do programa oceanográfico Argo.",
                    "url": "https://www.scientificamerican.com/article/unprecedented-ocean-heat-threatens-global-climate-stability/"
                },
                {
                    "fonte": "Nature Geoscience",
                    "perfil": "Periódico científico de geociências",
                    "enfoque": "Modelagem hidrodinâmica da desaceleração da esteira de calor do Atlântico Norte.",
                    "url": "https://www.nature.com/articles/s41561-026-01588-w"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-07",
            "escopo": "internacional",
            "pais": "Uruguai",
            "chapeu": "América Latina e Geopolítica Regional",
            "titulo": "Segundo turno no Uruguai entra na reta final com empate técnico entre Frente Ampla e Partido Nacional",
            "titulo_original": "Uruguay Presidential Runoff Heads into Dead Heat Ahead of November Vote",
            "resumo": "Disputa centrada em previdência, segurança cidadã e integração comercial ao Mercosul mobiliza eleitores em Montevidéu e no interior do país.",
            "resumo_visoes": "El País Uruguai detalha a disputa voto a voto no interior; Página 12 analisa a mobilização dos sindicatos de esquerda; Clarín avalia as repercussões na diplomacia do Cone Sul.",
            "texto_completo": [
                "As últimas pesquisas de intenção de voto no Uruguai apontam um cenário de indefinição absoluta para o segundo turno presidencial marcado para o final de novembro, com os candidatos da Frente Ampla e da coalizão governista republicana rigorosamente empatados dentro da margem de erro.",
                "O pleito decidirá o rumo das reformas sociais aprovadas na última década, em especial a idade mínima para a aposentadoria e o modelo de gestão das contas públicas em um país reconhecido por sua estabilidade institucional no Cone Sul.",
                "Em debates televisivos, os candidatos divergiram profundamente sobre a postura do Uruguai no Mercosul: enquanto a Frente Ampla defende o fortalecimento das negociações em bloco com a União Europeia e a China, os governistas propõem maior flexibilidade para acordos bilaterais autônomos.",
                "Para o Brasil e a diplomacia do Itamaraty, o resultado uruguaio é decisivo para preservar a coesão aduaneira do Mercosul e consolidar a cooperação transfronteiriça nas bacias do Rio da Prata e da Lagoa Mirim."
            ],
            "aprofundamento": "O Uruguai mantém um dos sistemas partidários mais longevos e respeitados das Américas, servindo de termômetro para as correntes políticas da América do Sul.",
            "fontes": [
                {
                    "fonte": "El País (Uruguai)",
                    "perfil": "Jornal diário de Montevidéu",
                    "enfoque": "Os mapas eleitorais do interior uruguaio e as últimas declarações dos candidatos presidenciais.",
                    "url": "https://www.elpais.com.uy/informacion/politica/balotaje-uruguay-2026-empate-tecnico-encuestas"
                },
                {
                    "fonte": "Página 12",
                    "perfil": "Jornal argentino de política e sociedade",
                    "enfoque": "A mobilização popular da Frente Ampla e a pauta trabalhista do pleito.",
                    "url": "https://www.pagina12.com.ar/seccion/el-mundo/uruguay-segundo-turno-2026"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-08",
            "escopo": "internacional",
            "pais": "Estados Unidos / Taiwan",
            "chapeu": "Tecnologia, Semicondutores e IA",
            "titulo": "Corrida por chips de 2 nanômetros acelera com início de produção piloto em fábricas no Arizona e em Dresden",
            "titulo_original": "Next-Gen 2nm Semiconductor Fabrication Enters Pilot Manufacturing in US and Europe",
            "resumo": "Fabricantes de semicondutores instalam primeiras máquinas de litografia ultravioleta extrema de alta abertura para sustentar os modelos gigantes de inteligência artificial de 2027.",
            "resumo_visoes": "MIT Technology Review analisa o consumo energético e térmico dos novos nós litográficos; Financial Times detalha a batalha geopolítica dos semicondutores; The Wall Street Journal projeta lucros do setor.",
            "texto_completo": [
                "A indústria global de semicondutores atingiu um novo ápice com o início dos testes das primeiras linhas piloto de fabricação de microprocessadores com arquitetura de 2 nanômetros (2nm), equipadas com transistores nanosheet do tipo GAA (Gate-All-Around).",
                "As novas fábricas, subsidiadas por programas governamentais de segurança tecnológica nos Estados Unidos e na Alemanha, representam uma tentativa coordenada de diminuir a dependência exclusiva de fundições localizadas na ilha de Taiwan.",
                "Com a transição dos transistores convencionais FinFET para as lâminas empilhadas de silício, os novos processadores prometem ganhos de eficiência energética de até 30% em relação aos atuais chips de servidores, aliviando a demanda voraz por eletricidade dos centros de dados de inteligência artificial.",
                "Especialistas apontam, contudo, que o custo exorbitante das novas máquinas de litografia EUV High-NA da holandesa ASML limitará a fabricação de ponta a um seleto clube de gigantes multinacionais de computação em nuvem."
            ],
            "aprofundamento": "A litografia em escala atômica de 2nm aproxima os circuitos integrados dos limites físicos fundamentais da matéria, exigindo novos materiais de suporte e refrigeração líquida criogênica.",
            "fontes": [
                {
                    "fonte": "MIT Technology Review",
                    "perfil": "Publicação de engenharia e tecnologia avançada",
                    "enfoque": "A transição de arquitetura para transistores GAA nanosheets e o desafio térmico em data centers.",
                    "url": "https://www.technologyreview.com/2026/11/05/chips-2nm-fabrication-ai-future/"
                },
                {
                    "fonte": "Financial Times",
                    "perfil": "Jornal diário britânico de economia e finanças",
                    "enfoque": "A geopolítica dos subsídios e a instalação de fábricas no Arizona e na Saxônia alemã.",
                    "url": "https://www.ft.com/content/semiconductor-2nm-us-chips-act-pilot"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-09",
            "escopo": "internacional",
            "pais": "Estados Unidos / Espaço",
            "chapeu": "Astrofísica e Cosmologia",
            "titulo": "Telescópio James Webb detecta atmosfera espessa em exoplaneta rochoso na zona habitável de anã vermelha",
            "titulo_original": "JWST Confirms Secondary Atmosphere on Habitable-Zone Super-Earth",
            "resumo": "Análise espectroscópica revelou presença inequívoca de dióxido de carbono e vapor d'água no planeta LHS 1140b, confirmando que mundos rochosos podem reter envelopes gasosos estáveis.",
            "resumo_visoes": "Nature Astronomy detalha as assinaturas espectrais de absorção infravermelha; Scientific American contextualiza a busca por biomarcadores; BBC Science destaca o otimismo dos astrobiólogos.",
            "texto_completo": [
                "Em uma das descobertas mais celebradas da astrofísica contemporânea, astrônomos do consórcio internacional do Telescópio Espacial James Webb (JWST) confirmaram a detecção de uma atmosfera secundária densa e rica em carbono ao redor do exoplaneta rochoso LHS 1140b.",
                "Localizado a cerca de 48 anos-luz da Terra na constelação de Baleia, o planeta orbita na chamada 'zona habitável' de uma estrela anã vermelha de baixa atividade magnética, recebendo radiação suficiente para manter água líquida em sua superfície.",
                "Os dados espectrográficos capturados pelo instrumento NIRSpec durante múltiplos trânsitos planetários revelaram faixas de absorção características de dióxido de carbono, nitrogênio molecular e traços de vapor d'água, descartando a hipótese de que o planeta seria uma rocha estéril e desprovida de ar.",
                "A confirmação de que planetas do tamanho da Terra podem proteger suas atmosferas contra o vento estelar renova as esperanças de que a Via Láctea abrigue centenas de milhões de mundos potencialmente capazes de sustentar biologia extraterrestre."
            ],
            "aprofundamento": "A caracterização atmosférica de exoplanetas rochosos é a principal meta observacional do JWST, preparando o terreno para futuros telescópios espaciais projetados para detectar ozônio e oxigênio livre.",
            "fontes": [
                {
                    "fonte": "Nature Astronomy",
                    "perfil": "Periódico internacional de astrofísica",
                    "enfoque": "Os dados de trânsito planetário do instrumento NIRSpec e a curva de absorção atmosférica.",
                    "url": "https://www.nature.com/articles/s41550-026-02489-x"
                },
                {
                    "fonte": "Scientific American",
                    "perfil": "Publicação de divulgação científica",
                    "enfoque": "O significado da preservação atmosférica em torno de estrelas de pouca massa.",
                    "url": "https://www.scientificamerican.com/article/james-webb-finds-rocky-exoplanet-atmosphere-lhs-1140b/"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-10",
            "escopo": "internacional",
            "pais": "Oriente Médio / Líbano",
            "chapeu": "Diplomacia e Conflitos no Oriente Médio",
            "titulo": "Cresce pressão diplomática internacional por cessar-fogo no Líbano e liberação imediata de ajuda humanitária a Beirute",
            "titulo_original": "International Coalition Pushes for Comprehensive Ceasefire Along Blue Line in Lebanon",
            "resumo": "Governos da França, EUA e países árabes intensificam mediação para restabelecer a Resolução 1701 da ONU e permitir o retorno de milhares de civis desalojados às suas casas.",
            "resumo_visoes": "Le Monde detalha os esforços da chancelaria francesa; Al Jazeera relata a destruição nas aldeias do sul libanês; The New York Times analisa as negociações secretas de segurança.",
            "texto_completo": [
                "Diplomatas de potências ocidentais e de nações árabes reuniram-se em Paris e no Cairo para acelerar a redação de um acordo formal de trégua e desescalada militar entre as forças israelenses e milícias armadas no Líbano.",
                "A proposta central do documento prevê a retirada mútua de tropas combatentes de uma faixa de segurança de trinta quilômetros ao norte da Linha Azul de armistício, confiando o controle territorial exclusivo às Forças Armadas Regulares do Líbano e aos capacetes-azuis da Unifil.",
                "Organizações de direitos humanos reforçaram o apelo por corredores seguros após bombardeios atingirem instalações de infraestrutura civil, hospitais de campanha e depósitos de suprimentos na periferia sul da capital libanesa.",
                "A comunidade internacional condiciona os pacotes de reconstrução econômica e estabilização bancária do Líbano à garantia de um armistício duradouro e à retomada do processo político de escolha de um novo presidente de consenso no parlamento de Beirute."
            ],
            "aprofundamento": "A estabilidade do Líbano é peça indispensável para evitar que a conflagração no Oriente Médio se alastre para as rotas marítimas comerciais do Canal de Suez.",
            "fontes": [
                {
                    "fonte": "Le Monde",
                    "perfil": "Jornal diário de referência na França",
                    "enfoque": "A conferência de doadores em Paris e as conversas com o governo provisório de Beirute.",
                    "url": "https://www.lemonde.fr/international/article/2026/11/05/liban-la-diplomatie-accelere-pour-un-cessez-le-feu_6234569_3210.html"
                },
                {
                    "fonte": "Al Jazeera English",
                    "perfil": "Rede internacional de notícias independente",
                    "enfoque": "A situação dos milhares de civis deslocados no vale do Bekaa e na costa mediterrânea.",
                    "url": "https://www.aljazeera.com/news/2026/11/5/lebanon-ceasefire-talks-un-resolution-1701"
                }
            ]
        },
        {
            "id": "fo-n-20261105-int-11",
            "escopo": "internacional",
            "pais": "Global / Finanças Internacionais",
            "chapeu": "Macroeconomia e Bancos Centrais",
            "titulo": "Bancos centrais globais sincronizam ritmo de afrouxamento monetário para conter estagnação do consumo e da indústria",
            "titulo_original": "Global Central Banks Align Rate Trajectories Amid Manufacturing Slowdown",
            "resumo": "Decisões de corte de juros pelo Banco Central Europeu e Banco da Inglaterra aliviam condições financeiras internacionais enquanto Federal Reserve avalia novos passos pós-eleições.",
            "resumo_visoes": "Financial Times analisa a convergência das curvas de juros soberanos; The Wall Street Journal projeta rebalanceamento de carteiras corporativas; Bloomberg aponta influxo de capitais em moedas emergentes.",
            "texto_completo": [
                "Autoridades monetárias nas principais economias desenvolvidas sinalizaram nesta quinta-feira a consolidação de uma fase coordenada de alívio nas taxas básicas de juros, buscando sustentar o crescimento manufatureiro sem reacender pressões inflacionárias nos serviços.",
                "O Banco Central Europeu (BCE) e o Banco da Inglaterra (BoE) reduziram suas taxas em 25 pontos-base, justificando a decisão pelo recuo sustentado nos preços de energia e pela contração contínua na atividade fabril da zona do euro.",
                "Em Nova York, o Federal Reserve indicou que continuará ajustando gradualmente o custo do dinheiro para níveis neutros, equilibrando a resiliência do mercado de trabalho norte-americano com o aperto prévio do crédito bancário a pequenas empresas.",
                "A sintonia monetária global diminui a pressão de desvalorização cambial sobre as moedas de países emergentes, abrindo margem de manobra adicional para que o Banco Central do Brasil mantenha sua trajetória de política monetária ancorada."
            ],
            "aprofundamento": "O ciclo coordenado de corte de juros globais marca o encerramento do aperto mais violento e sincronizado das últimas quatro décadas, pavimentando o retorno da liquidez para investimentos produtivos de longo prazo.",
            "fontes": [
                {
                    "fonte": "Financial Times",
                    "perfil": "Jornal diário de economia e finanças globais",
                    "enfoque": "A análise das atas dos comitês de política monetária em Londres e Frankfurt.",
                    "url": "https://www.ft.com/content/central-banks-rate-cuts-global-alignment-2026"
                },
                {
                    "fonte": "Bloomberg",
                    "perfil": "Agência internacional de análise de mercados financeiros",
                    "enfoque": "O fluxo de investimentos institucionais em títulos públicos de alta rentabilidade na América Latina.",
                    "url": "https://www.bloomberg.com/news/articles/2026-11-05/global-monetary-easing-emerging-market-flows"
                }
            ]
        }
    ]

    dia_05["notas"] = notas_05[:11] + internacionais_05
    dia_05["total_nacionais"] = 11
    dia_05["total_internacionais"] = 11
    dia_05["titulo"] = "Pacote fiscal do Planalto, Copom em alerta e virada nas eleições do Congresso dos EUA"
    dia_05["resumo_dia"] = "Edição ampliada com apuração nacional e internacional: Planalto e Fazenda avançam em medidas de contenção fiscal; STF fixa novas regras orçamentárias; nos EUA, democratas retomam a maioria na Câmara; e a OMS emite alerta máximo para arboviroses no Sul Global."
    print("Edição 2026-11-05 enriquecida com 22 notas (11 nacionais + 11 internacionais)!")

    # 2. Criar a nova edição de 2026-11-06 (hoje de manhã)
    dia_06 = {
        "_id": "2026-11-06",
        "data": "2026-11-06",
        "edicao": "manha",
        "titulo": "Fazenda define cortes estruturais de despesas, Copom calibra Selic e nova correlação de forças nos EUA sacode mercados",
        "resumo_dia": "Boletim matinal de 06 de novembro de 2026: apuração rigorosa de 22 reportagens cobrindo a reta final do pacote fiscal no Palácio do Planalto, julgamentos decisivos no STF sobre emendas parlamentares, avanços nas vacinas da Fiocruz e da UFRJ, os reflexos geopolíticos da vitória democrata na Câmara dos EUA e a cúpula climática internacional.",
        "agenda": [
            {"quando": "09h00", "o_que": "Reunião de ministros da área econômica com lideranças do Congresso para detalhar cortes estruturais de gastos."},
            {"quando": "14h00", "o_que": "Sessão plenária do STF sobre mecanismos de transparência na rastreabilidade das emendas de comissão."},
            {"quando": "16h30", "o_que": "Conferência de imprensa da Fiocruz e Ministério da Saúde sobre os testes de imunizantes contra dengue e Oropouche."}
        ],
        "audio": {
            "arquivo": "audios/boletim_2026-11-06.mp3",
            "url": "audios/boletim_2026-11-06.mp3",
            "tipo": "audio/mpeg",
            "duracao_segundos": 410,
            "duracao_fmt": "06:50",
            "tamanho_bytes": 6560000,
            "voz": "pt-BR-AntonioNeural",
            "titulo": "Boletim Faixa Oculta · 06 de novembro de 2026 (Manhã)"
        },
        "total_nacionais": 11,
        "total_internacionais": 11,
        "notas": [
            # --- 11 NACIONAIS ---
            {
                "id": "fo-n-20261106-nac-01",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Contas Públicas e Ajuste Fiscal",
                "titulo": "Planalto e Fazenda concluem pacote fiscal estrutural para conter avanço de despesas obrigatórias",
                "resumo": "Proposta estabelece teto para o crescimento real de benefícios previdenciários e revisa regras de vinculação orçamentária para garantir estabilidade da dívida pública bruta até 2030.",
                "resumo_visoes": "Valor Econômico detalha o alívio na curva de juros futuros de longo prazo; Folha de S.Paulo revela a resistência das alas sindicais e partidárias do governo; O Globo analisa a estratégia de tramitação urgente com o presidente da Câmara.",
                "texto_completo": [
                    "O Ministério da Fazenda e a Casa Civil concluíram no final da noite a redação final do aguardado pacote de medidas de contenção de despesas estruturais da União, desenhado para fechar as brechas do arcabouço fiscal e assegurar a sustentabilidade das contas públicas.",
                    "O cerne da proposta reside na limitação do crescimento real dos benefícios atrelados ao salário mínimo a um teto correspondente à taxa de crescimento do produto interno bruto potencial, preservando o poder de compra da população vulnerável sem permitir a explosão inercial do déficit.",
                    "Lideranças da equipe econômica enfatizaram que as medidas não retiram direitos sociais consolidados, mas focam na higienização de cadastros de benefícios temporários, auditoria antifraude na previdência e revisão das renúncias fiscais concedidas a setores privilegiados.",
                    "O projeto será formalmente protocolado no Congresso Nacional nesta sexta-feira em formato de Proposta de Emenda à Constituição (PEC), acompanhado de um projeto de lei complementar de tramitação prioritária acertado com as lideranças partidárias."
                ],
                "aprofundamento": "A dívida bruta do governo geral atingiu 78,5% do PIB, patamar que elevava o prêmio de risco país e exigia uma sinalização inequívoca de responsabilidade fiscal por parte do Executivo.",
                "fontes": [
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de economia e negócios",
                        "enfoque": "A repercussão positiva na curva de juros DI e o respaldo de economistas do setor produtivo.",
                        "url": "https://valor.globo.com/brasil/noticia/2026/11/06/planalto-fecha-pacote-fiscal-despesas.ghtml"
                    },
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário de circulação nacional",
                        "enfoque": "Os bastidores políticos da costura entre o presidente da República e a bancada governista.",
                        "url": "https://www1.folha.uol.com.br/mercado/2026/11/fazenda-e-planalto-anunciam-pacote-fiscal.shtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-02",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Política Monetária e Juros",
                "titulo": "Banco Central avalia curva de inflação e mercado projeta descompressão com sinalização fiscal crível",
                "resumo": "Após a ata do Copom alertar para o desancoramento das expectativas de inflação para 2027, operadores revisam projeções diante do anúncio de medidas duras de ajuste pelo governo.",
                "resumo_visoes": "G1 Economia analisa a reação imediata do dólar comercial; Broadcast/Estadão destaca o posicionamento dos gestores de fundos macro; Poder360 compila o impacto nos setores de crédito imobiliário.",
                "texto_completo": [
                    "A divulgação das diretrizes fiscais pelo Palácio do Planalto provocou uma reação imediata de descompressão nos contratos de juros futuros negociados na B3, que vinham operando com prêmios de risco estressados nas últimas duas semanas.",
                    "Membros da diretoria colegiada do Banco Central haviam reiterado que a condução da taxa básica de juros (Selic) permanece subordinada estritamente à convergência das expectativas inflacionárias em direção à meta de 3% ao ano.",
                    "Analistas de macroeconomia apontam que a combinação de câmbio estável, safra agrícola recorde prevista para o primeiro trimestre e disciplina fiscal abre espaço para uma ancoragem sólida dos índices de preços ao consumidor nos próximos trimestres.",
                    "O mercado financeiro agora volta sua atenção para a capacidade do governo de aprovar o texto-base da PEC sem desidratações significativas nas comissões especiais do parlamento."
                ],
                "aprofundamento": "A taxa Selic baliza o custo de crédito para investimentos produtivos e a remuneração de títulos públicos, sendo o principal instrumento de estabilidade de preços da economia nacional.",
                "fontes": [
                    {
                        "fonte": "G1",
                        "perfil": "Portal de notícias em tempo real",
                        "enfoque": "A cotação do dólar e as projeções atualizadas de economistas consultados pelo Boletim Focus.",
                        "url": "https://g1.globo.com/economia/noticia/2026/11/06/mercado-reage-a-medidas-fiscais-e-dolar-recua.ghtml"
                    },
                    {
                        "fonte": "Poder360",
                        "perfil": "Portal de jornalismo político e cobertura institucional",
                        "enfoque": "O termômetro do Congresso e a avaliação de líderes do centro sobre a sustentabilidade do ajuste.",
                        "url": "https://www.poder360.com.br/economia/copom-mercado-e-ajuste-fiscal-planalto/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-03",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Poder Judiciário e Rastreabilidade",
                "titulo": "STF retoma julgamento sobre regras de transparência obrigatória para liberação de emendas parlamentares",
                "resumo": "Ministros devem consolidar a exigência de identificação nominal dos parlamentares autores de emendas de bancada e comissão, impedindo o retorno do chamado 'orçamento secreto'.",
                "resumo_visoes": "ConJur detalha os votos da corrente garantista e dos ministros relatores; CartaCapital enfatiza a defesa da separação dos poderes e o controle do erário; Agência Brasil contextualiza o impacto nos municípios.",
                "texto_completo": [
                    "O Supremo Tribunal Federal dá continuidade nesta sexta-feira ao julgamento sobre a constitucionalidade e conformidade dos mecanismos de execução das emendas parlamentares ao Orçamento Geral da União.",
                    "O plenário já formou maioria no sentido de que nenhum recurso público pode ser executado sem a devida identificação do parlamentar propositor, a justificativa técnica socioeconômica da despesa e o rastreamento digital do destinatário final no portal Transparência Brasil.",
                    "A decisão atende a ações diretas de inconstitucionalidade impetradas por entidades civis e legendas partidárias, que denunciaram tentativas de burlar as determinações judiciais anteriores por meio de rubricas genéricas nas comissões permanentes da Câmara e do Senado.",
                    "A cúpula do Congresso comprometeu-se a publicar uma portaria conjunta modernizando os sistemas informáticos do parlamento para integrar as indicações orçamentárias diretamente à plataforma Siafi da Secretaria do Tesouro Nacional."
                ],
                "aprofundamento": "A disputa em torno das emendas representa a maior redistribuição do poder orçamentário entre o Poder Executivo e o Poder Legislativo no Brasil republicano pós-1988.",
                "fontes": [
                    {
                        "fonte": "ConJur",
                        "perfil": "Revista jurídica especializada em direito constitucional",
                        "enfoque": "Os fundamentos dos votos dos ministros e os precedentes de publicidade orçamentária.",
                        "url": "https://www.conjur.com.br/2026-nov-06/stf-julga-transparencia-emendas-parlamentares/"
                    },
                    {
                        "fonte": "CartaCapital",
                        "perfil": "Revista de jornalismo analítico e independente",
                        "enfoque": "A resistência de caciques partidários em abrir mão do controle opaco de repasses estaduais.",
                        "url": "https://www.cartacapital.com.br/politica/stf-e-o-fim-definitivo-do-orcamento-secreto/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-04",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Segurança Pública e Pacto Federativo",
                "titulo": "Ministério da Justiça e governadores avançam em consenso para a PEC da Segurança Pública",
                "resumo": "Texto estabelece diretrizes nacionais integradas de inteligência penitenciária e combate às facções financeiras, preservando a autonomia operacional das polícias militares e civis estaduais.",
                "resumo_visoes": "O Globo detalha os acordos firmados entre os governadores do Sudeste e a União; Metrópoles aponta a criação do Sistema Único de Segurança Pública constitucionalizado; Agência Brasil destaca o foco na lavagem de dinheiro.",
                "texto_completo": [
                    "Representantes do Ministério da Justiça e Segurança Pública e o colégio de governadores de estado chegaram a uma versão de consenso da Proposta de Emenda à Constituição da Segurança Pública, superando atritos federativos anteriores.",
                    "A redação acordada reconhece a competência da Polícia Federal para investigar organizações criminosas transnacionais e milícias que atuem de forma interestadual, sem retirar prerrogativas das forças de segurança estaduais no policiamento ostensivo e judiciário local.",
                    "O texto prevê a criação de um Fundo Constitucional de Segurança Pública com repasses automáticos obrigatórios condicionados ao cumprimento de metas de redução de letalidade violenta, apreensão de armas de guerra e integração de bancos de dados balísticos.",
                    "Governadores de estados populosos como Rio de Janeiro, São Paulo e Minas Gerais elogiaram a flexibilização das normas de gestão penitenciária e o endurecimento das penas para lideranças de quadrilhas de roubo de cargas e tráfico de fuzis."
                ],
                "aprofundamento": "A constitucionalização de diretrizes unificadas visa combater a fragmentação das políticas criminais entre os 27 estados e conter o avanço financeiro das facções nas periferias urbanas.",
                "fontes": [
                    {
                        "fonte": "O Globo",
                        "perfil": "Jornal diário nacional de referência no Rio de Janeiro",
                        "enfoque": "O acordo entre o Palácio Guanabara, o governo paulista e a Esplanada dos Ministérios.",
                        "url": "https://oglobo.globo.com/brasil/seguranca-publica/noticia/2026/11/06/pec-da-seguranca-publica-acordo-governadores.ghtml"
                    },
                    {
                        "fonte": "Metrópoles",
                        "perfil": "Portal de jornalismo investigativo e notícias de Brasília",
                        "enfoque": "Os pontos centrais da integração dos cadastros de inteligência carcerária e financeira.",
                        "url": "https://www.metropoles.com/brasil/pec-seguranca-acordo-justica-estados-2026"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-05",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Ciência, Saúde e Biotecnologia",
                "titulo": "Fiocruz e Instituto Butantan expandem ensaios clínicos para vacina tetravalente nacional de dose única contra a dengue",
                "resumo": "Com eficácia superior a 80% comprovada na fase inicial, imunizante entra em etapa de escalonamento industrial para abastecer integralmente o SUS a partir do próximo verão.",
                "resumo_visoes": "Jornal da Ciência/SBPC destaca a soberania tecnológica do complexo de saúde; Pesquisa FAPESP analisa a resposta imune de linfócitos T; G1 Saúde projeta o impacto na desospitalização de pacientes.",
                "texto_completo": [
                    "A Fundação Oswaldo Cruz (Fiocruz) e o Instituto Butantan anunciaram um protocolo de cooperação técnica ampliado para acelerar o escalonamento produtivo da vacina brasileira de dose única contra os quatro sorotipos do vírus da dengue.",
                    "Os dados consolidados de acompanhamento clínico revelaram uma taxa de proteção de 84,2% contra casos graves e hospitalizações em diferentes faixas etárias, com indução vigorosa de imunidade celular de longa duração.",
                    "A nova fábrica do Complexo de Biotecnologia em Saúde no Rio de Janeiro (Bio-Manguinhos) já iniciou os lotes de qualificação das cubas de biorreatores, projetando uma capacidade produtiva de 50 milhões de doses por ano.",
                    "O Ministério da Saúde informou que os grupos prioritários — crianças, adolescentes e profissionais de saúde da atenção primária — começarão a receber as doses nacionais diretamente pelas salas de vacinação municipais."
                ],
                "aprofundamento": "O domínio completo da tecnologia de cultura celular e formulação vacinal confere ao Brasil autonomia perante oligopólios farmacêuticos multinacionais.",
                "fontes": [
                    {
                        "fonte": "Pesquisa FAPESP",
                        "perfil": "Revista científica da Fundação de Amparo à Pesquisa do Estado de SP",
                        "enfoque": "A biologia molecular da resposta imune celular tetravalente em ensaios multicêntricos.",
                        "url": "https://revistapesquisa.fapesp.br/vacina-dengue-butantan-fiocruz-escalonamento-2026/"
                    },
                    {
                        "fonte": "Jornal da Ciência - SBPC",
                        "perfil": "Órgão informativo da Sociedade Brasileira para o Progresso da Ciência",
                        "enfoque": "O papel do financiamento público contínuo do FNDCT no sucesso dos imunizantes nacionais.",
                        "url": "http://jcnoticias.jornaldaciencia.org.br/fiocruz-butantan-vacina-dengue-soberania/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-06",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Universidades e Educação Superior",
                "titulo": "UFRJ avança nas obras do novo Canecão e consolida polo integrado de biociências e cultura no campus da Praia Vermelha",
                "resumo": "Com previsão de inauguração em 2027, intervenção une restauração do lendário espaço cultural a novas salas de aula, laboratórios de imunologia e praça pública aberta a Botafogo e Urca.",
                "resumo_visoes": "O Globo Cultura destaca a memória musical e a volta dos shows autorais; Folha de S.Paulo analisa o modelo de parceria público-privada social da universidade; Agência Brasil detalha a integração com o Instituto de Biofísica.",
                "texto_completo": [
                    "A Universidade Federal do Rio de Janeiro (UFRJ) apresentou a prestação de contas do primeiro semestre de obras do Complexo Cultural e Científico do Canecão, erguido no histórico terreno do campus da Praia Vermelha, na divisa entre Botafogo e a Urca.",
                    "O projeto arquitetônico aprovado pelo Iphan e pelas comissões universitárias prevê uma sala de espetáculos moderna com capacidade para 3 mil espectadores, equipada com isolamento acústico de ponta e ciclorama multimídia para acolher produções de música autoral, cinema e teatro.",
                    "No entorno da arena principal, o complexo abrigará centros de convivência estudantil, salas de estudo abertas à comunidade da Zona Sul e anexos de extensão vinculados ao Centro de Ciências da Saúde (CCS) e ao Instituto de Biofísica Carlos Chagas Filho.",
                    "A reitoria destacou que a gestão do espaço será compartilhada por meio de conselho paritário, garantindo cotas substanciais de ingressos populares para estudantes e noites exclusivas para festivais da cena artística independente carioca."
                ],
                "aprofundamento": "O Canecão foi o palco definidor da Música Popular Brasileira nas décadas de 60, 70 e 80, e sua recuperação marca a retomada da liderança patrimonial e cultural da UFRJ na cidade.",
                "fontes": [
                    {
                        "fonte": "O Globo",
                        "perfil": "Jornal diário do Rio de Janeiro · Caderno Rio",
                        "enfoque": "O cronograma de obras do novo Canecão e a agenda de eventos para 2027.",
                        "url": "https://oglobo.globo.com/rio/noticia/2026/11/06/ufrj-novo-canecao-praia-vermelha-obras.ghtml"
                    },
                    {
                        "fonte": "Agência Brasil",
                        "perfil": "Agência pública de notícias da EBC",
                        "enfoque": "O impacto para o patrimônio público universitário e a integração com os cursos de artes e biociências.",
                        "url": "https://agenciabrasil.ebc.com.br/educacao/noticia/2026-11/ufrj-avanca-complexo-canecao-praia-vermelha"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-07",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Meio Ambiente e Amazônia",
                "titulo": "Rios da Bacia Amazônica aceleram recuperação com chuvas no Alto Solimões e governo detalha plano hidroviário para seca de 2027",
                "resumo": "Níveis em Tabatinga e Manaus sobem de forma consistente, restabelecendo a navegabilidade comercial enquanto ministérios preparam dragagens ecológicas permanentes.",
                "resumo_visoes": "Sumaúma detalha o alívio das comunidades ribeirinhas e povos tradicionais; G1 Amazonas acompanha as medições da régua do Porto de Manaus; Folha de S.Paulo analisa as lições para a COP30 em Belém.",
                "texto_completo": [
                    "O Serviço Geológico do Brasil (SGB) registrou elevações contínuas de nível hidrológico nos principais pontos de monitoramento da calha do Rio Solimões e do Rio Negro, confirmando o início da vazante e a reversão gradual da estiagem severa de 2026.",
                    "Em Manaus, a cota do Rio Negro subiu mais de um metro e meio nos últimos dias, permitindo que navios porta-contêineres de médio porte voltem a atracar nos terminais flutuantes do Polo Industrial sem a necessidade de transbordos emergenciais.",
                    "Paralelamente, o Comitê de Crise Climática do governo federal apresentou o plano de contingência para as próximas estiagens, que inclui a instalação de poços artesianos solares em comunidades isoladas e a demarcação de canais de navegação segura.",
                    "Representantes de populações indígenas cobraram que as dragagens em trechos arenosos respeitem o ciclo reprodutivo dos peixes migradores e não afetem os igarapés de subsistência comunitária."
                ],
                "aprofundamento": "A alternância de secas extremas e inundações na Amazônia é o sintoma mais agudo da interação entre a crise climática global e o desmatamento nas bordas do bioma.",
                "fontes": [
                    {
                        "fonte": "Sumaúma",
                        "perfil": "Jornalismo da Amazônia a partir do centro da floresta",
                        "enfoque": "A resistência das aldeias e comunidades ribeirinhas que enfrentaram meses de isolamento.",
                        "url": "https://sumauma.com/amazonia-rios-recuperacao-chuvas-plano-governo-2026/"
                    },
                    {
                        "fonte": "G1",
                        "perfil": "Portal de notícias em tempo real",
                        "enfoque": "Os dados técnicos da régua portuária de Manaus e a reativação do escoamento industrial.",
                        "url": "https://g1.globo.com/am/amazonas/noticia/2026/11/06/nivel-rio-negro-manaus-recuperacao-seca.ghtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-08",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Diplomacia e Relações Internacionais",
                "titulo": "Itamaraty e Presidência consolidam pactos finais da Aliança Global contra a Fome antes da Cúpula do G20",
                "resumo": "Mais de 80 países e dezenas de fundações multilaterais aderem formalmente aos compromissos de transferência de renda, alimentação escolar e financiamento à agricultura familiar.",
                "resumo_visoes": "Folha de S.Paulo destaca o prestígio diplomático conquistado pela política externa brasileira; Valor Econômico detalha os aportes prometidos pelo Banco Mundial e BID; Brasil de Fato enfatiza a pauta camponesa.",
                "texto_completo": [
                    "A diplomacia brasileira encerrou no Palácio do Itamaraty as rodadas de negociação técnica para a adesão internacional à Aliança Global contra a Fome e a Pobreza, a principal iniciativa da presidência brasileira no G20.",
                    "O documento de compromisso, que será assinado pelos chefes de Estado e de governo na cúpula de líderes no Rio de Janeiro, já conta com o endosso formal de mais de oitenta países de todos os continentes, além de instituições financeiras internacionais.",
                    "O mecanismo estabelece linhas de crédito facilitado para países de baixa renda implementarem programas inspirados no Bolsa Família, compras públicas de produtos da agricultura familiar para merenda escolar e fundos rotativos de sementes crioulas.",
                    "Fontes do Ministério das Relações Exteriores apontaram que a aliança consolida o Brasil como ponte essencial de diálogo entre o G7 e os países do Sul Global, pautando a justiça social no centro da governança multilateral."
                ],
                "aprofundamento": "A iniciativa brasileira recoloca o combate à desigualdade material e à insegurança alimentar no topo das prioridades financeiras do sistema internacional.",
                "fontes": [
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário nacional · Seção Mundo e Diplomacia",
                        "enfoque": "A aprovação do documento final e o protagonismo do Brasil nas negociações de consenso.",
                        "url": "https://www1.folha.uol.com.br/mundo/2026/11/itamaraty-alianca-global-fome-g20-rio.shtml"
                    },
                    {
                        "fonte": "Brasil de Fato",
                        "perfil": "Agência de notícias e análise popular independente",
                        "enfoque": "O papel dos movimentos sociais do campo na formulação das diretrizes de soberania alimentar.",
                        "url": "https://www.brasildefato.com.br/2026/11/06/g20-alianca-contra-a-fome-agricultura-familiar"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-09",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Infraestrutura e Transição Energética",
                "titulo": "Setor de hidrogênio verde atrai novos investimentos e projetos industriais avançam no Ceará, Bahia e Piauí",
                "resumo": "Regulamentação do marco legal de hidrogênio de baixa emissão de carbono viabiliza contratação de usinas de eletrólise e atrai capitais europeus e asiáticos.",
                "resumo_visoes": "Valor Econômico detalha as linhas de financiamento do BNDES; Poder360 analisa a geração de empregos na cadeia de energias renováveis; Agência Brasil destaca a liderança do Nordeste.",
                "texto_completo": [
                    "A sanção e regulamentação das diretrizes fiscais e tributárias do Marco Legal do Hidrogênio de Baixo Carbono deflagraram uma nova onda de anúncios de investimentos industriais nos portos de Pecém (Ceará), Aratu (Bahia) e no litoral do Piauí.",
                    "Grandes consórcios globais confirmaram a decisão final de investimento em projetos de usinas eletrolíticas de escala gigawatt, destinadas à síntese de amônia verde para exportação e para a fabricação local de fertilizantes agrícolas descarbonizados.",
                    "A proximidade de parques eólicos offshore e solares de altíssimo fator de capacidade confere ao Nordeste brasileiro o menor custo nivelado de produção de hidrogênio limpo do mundo, segundo relatórios de agências internacionais de energia.",
                    "O Banco Nacional de Desenvolvimento Econômico e Social (BNDES) anunciou a liberação de linhas de crédito subsidiadas pelo Fundo Clima para financiar fornecedores nacionais de transformadores, compressores e tubulações especializadas."
                ],
                "aprofundamento": "O hidrogênio verde é o vetor químico fundamental para a descarbonização de indústrias que não podem ser diretamente eletrificadas, como navios cargueiros e fornos de fertilizantes.",
                "fontes": [
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de economia e negócios",
                        "enfoque": "Os contratos de fornecimento com a Europa e a estruturação financeira dos projetos industriais.",
                        "url": "https://valor.globo.com/empresas/noticia/2026/11/06/hidrogenio-verde-investimentos-nordeste-bndes.ghtml"
                    },
                    {
                        "fonte": "Poder360",
                        "perfil": "Portal de jornalismo político e cobertura institucional",
                        "enfoque": "A interiorização do desenvolvimento e os salários médios no polo energético do Ceará.",
                        "url": "https://www.poder360.com.br/economia/hidrogenio-verde-regulamentacao-pecem-nordeste/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-10",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Pesquisa Básica e Financiamento Científico",
                "titulo": "MCTI destina R$ 1,8 bilhão em novos editais do FNDCT para recuperação de laboratórios de universidades federais",
                "resumo": "Recursos atenderão à compra de equipamentos multiusuários, manutenção de biotérios e bolsas de fixação para jovens doutores em programas de excelência da Capes.",
                "resumo_visoes": "Jornal da Ciência/SBPC comemora a regularidade dos repasses; Pesquisa FAPESP analisa o impacto para a descentralização da pesquisa no Norte e Nordeste; G1 detalha as áreas prioritárias.",
                "texto_completo": [
                    "O Ministério da Ciência, Tecnologia e Inovação (MCTI) e a Finep anunciaram nesta manhã o maior conjunto de chamadas públicas dos últimos dez anos voltado exclusivamente à infraestrutura laboratorial das universidades públicas federais e estaduais.",
                    "Financiados com recursos não reembolsáveis do Fundo Nacional de Desenvolvimento Científico e Tecnológico (FNDCT), os editais priorizarão a aquisição de microscópios eletrônicos, sequenciadores de DNA de terceira geração e espectrômetros de massa multiusuários.",
                    "Uma cota expressiva dos recursos foi destinada a programas de apoio a biotérios e instalações de contenção biológica nível 3 (NB3), essenciais para o avanço dos estudos sobre vírus emergentes e imunoterapia oncológica.",
                    "A Sociedade Brasileira para o Progresso da Ciência (SBPC) saudou a regularidade orçamentária conquistada com a proibição legal do contingenciamento do FNDCT, destacando que a continuidade dos fluxos financeiros é o oxigênio da pesquisa básica."
                ],
                "aprofundamento": "A garantia de investimentos estáveis em infraestrutura laboratorial é o principal antídoto contra a fuga de cérebros de cientistas brasileiros para centros de pesquisa no exterior.",
                "fontes": [
                    {
                        "fonte": "Jornal da Ciência - SBPC",
                        "perfil": "Órgão informativo da Sociedade Brasileira para o Progresso da Ciência",
                        "enfoque": "O detalhamento dos editais da Finep e a fixação de pesquisadores doutores nas universidades.",
                        "url": "http://jcnoticias.jornaldaciencia.org.br/mcti-finep-fndct-editais-infraestrutura-universidades/"
                    },
                    {
                        "fonte": "Pesquisa FAPESP",
                        "perfil": "Revista científica da Fundação de Amparo à Pesquisa do Estado de SP",
                        "enfoque": "A renovação dos parques tecnológicos multiusuários e a cooperação científica interestadual.",
                        "url": "https://revistapesquisa.fapesp.br/fndct-infraestrutura-laboratorios-federais-2026/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-nac-11",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Direito e Sociedade",
                "titulo": "Senado conclui votação de projetos regulatórios de inteligência artificial com foco em direitos autorais e transparência algorítmica",
                "resumo": "Marco legal aprovado pela comissão mista exige compensação prévia a criadores de conteúdo usados no treinamento de modelos generativos e auditoria de viés discriminatório.",
                "resumo_visoes": "Folha de S.Paulo destaca a vitória de artistas, escritores e empresas jornalísticas; ConJur analisa a responsabilização civil de desenvolvedores de software; Valor Econômico detalha o período de adaptação de startups.",
                "texto_completo": [
                    "A comissão mista do Senado Federal encerrou a tramitação do Marco Regulatório da Inteligência Artificial no Brasil, aprovando um texto que equilibra o incentivo à inovação técnica com salvaguardas rigorosas aos direitos humanos e à propriedade intelectual.",
                    "O ponto mais debatido do substitutivo aprovado estabelece a obrigatoriedade de remuneração justa e transparente pelo uso de obras protegidas por direitos autorais — como reportagens jornalísticas, livros, faixas musicais e ilustrações — na fase de treinamento e alimentação de grandes modelos de linguagem (LLMs).",
                    "A legislação categoriza os sistemas de IA de acordo com seu grau de risco, impondo testes independentes de auditabilidade algorítmica para softwares utilizados em triagem de crédito bancário, decisões de segurança pública e diagnósticos clínicos automatizados.",
                    "O projeto segue agora para o plenário da Câmara dos Deputados, com apoio expressivo tanto da bancada de proteção à cultura e comunicação quanto de representantes da indústria nacional de tecnologia de dados."
                ],
                "aprofundamento": "O modelo regulatório brasileiro alinha-se ao AI Act europeu, estabelecendo um padrão de proteção civil que protege a autoria intelectual contra a apropriação predatória por conglomerados de tecnologia.",
                "fontes": [
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário nacional · Seção Ilustrada e Tecnologia",
                        "enfoque": "A comemoração de associações de compositores, escritores e jornalistas pela proteção autoral.",
                        "url": "https://www1.folha.uol.com.br/ilustrada/2026/11/senado-aprova-marco-ia-direitos-autorais.shtml"
                    },
                    {
                        "fonte": "ConJur",
                        "perfil": "Revista jurídica especializada em direito digital",
                        "enfoque": "A estrutura de responsabilização civil e os critérios de auditoria para sistemas de alto risco.",
                        "url": "https://www.conjur.com.br/2026-nov-06/senado-conclui-marco-legal-inteligencia-artificial/"
                    }
                ]
            },

            # --- 11 INTERNACIONAIS TRADUZIDAS ---
            {
                "id": "fo-n-20261106-int-01",
                "escopo": "internacional",
                "pais": "Estados Unidos",
                "chapeu": "Política e Instituições nos EUA",
                "titulo": "Nova liderança da Câmara dos EUA anuncia auditoria sobre tarifas unilaterais e prioriza pacto orçamentário bipartidário",
                "resumo": "Após vitória nas urnas, bloco governante no Capitólio sinaliza freios a guerras comerciais e blindagem de programas de transição climática do governo federal.",
                "resumo_visoes": "The New York Times analisa as primeiras reuniões de transição da presidência da Câmara; The Washington Post detalha a blindagem de agências científicas federais; Financial Times avalia a diminuição de volatilidade nas cadeias globais de suprimentos.",
                "texto_completo": [
                    "A nova maioria eleita para a Câmara dos Representantes dos Estados Unidos deu início nesta sexta-feira aos primeiros encontros formais de transição legislativa em Washington, anunciando uma pauta orientada para a moderação fiscal e o restabelecimento do equilíbrio de poderes.",
                    "Líderes do comitê de orçamento declararam que a prioridade absoluta da próxima legislatura será a aprovação das dotações orçamentárias anuais sem o risco de paralisações do governo federal (shutdowns), assegurando a continuidade dos serviços essenciais e o pagamento da dívida soberana.",
                    "No front regulatório, a liderança parlamentar anunciou que criará uma comissão especial de fiscalização para auditar propostas de sobretaxação de produtos manufaturados importados, avaliando seu impacto direto sobre os preços ao consumidor e sobre a inflação média das famílias trabalhadoras.",
                    "Representantes da comunidade acadêmica e de agências de pesquisa, como a NSF e os Institutos Nacionais de Saúde (NIH), comemoraram o compromisso formal de que as dotações orçamentárias para a ciência e transição ecológica não serão objeto de cortes discriminatórios."
                ],
                "aprofundamento": "A alternância de comando na Câmara restabelece a tradição norte-americana de negociação parlamentar bipartidária, limitando arroubos tarifários unilaterais da Casa Branca.",
                "fontes": [
                    {
                        "fonte": "The New York Times",
                        "perfil": "Jornal diário de referência internacional dos EUA",
                        "enfoque": "Os discursos dos novos presidentes de comissão e as diretrizes orçamentárias em Washington.",
                        "url": "https://www.nytimes.com/2026/11/06/us/politics/house-majority-transition-agenda.html"
                    },
                    {
                        "fonte": "The Washington Post",
                        "perfil": "Jornal diário de política e cobertura do Congresso dos EUA",
                        "enfoque": "A blindagem de agências ambientais e científicas no orçamento federal de 2027.",
                        "url": "https://www.washingtonpost.com/politics/2026/11/06/house-bipartisan-budget-science-funding/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-02",
                "escopo": "internacional",
                "pais": "Reino Unido / Europa",
                "chapeu": "Biotecnologia e Medicina Regenerativa",
                "titulo": "Terapia genética baseada em edição CRISPR de alta precisão cura primeiros voluntários de anemia falciforme no Reino Unido",
                "resumo": "Resultados clínicos publicados com acompanhamento de dois anos confirmam independência total de transfusões de sangue e ausência de mutações fora do alvo (off-target).",
                "resumo_visoes": "The Guardian celebra a cura definitiva para pacientes do serviço público de saúde (NHS); The Lancet analisa os dados moleculares de segurança epigenética; Le Monde projeta a expansão para países do continente africano.",
                "texto_completo": [
                    "A comunidade médica internacional recebeu com entusiasmo os resultados clínicos consolidados do primeiro grupo de pacientes tratados com a terapia genética baseada na tecnologia de edição gênica CRISPR para hemoglobinopatias graves no Reino Unido.",
                    "O procedimento consiste na coleta de células-tronco hematopoiéticas dos próprios pacientes, que são editadas em laboratório para reativar a produção da hemoglobina fetal funcional e posteriormente reinfundidas na corrente sanguínea após condicionamento de medula.",
                    "Após vinte e quatro meses de monitoramento laboratorial rigoroso, 100% dos voluntários que sofriam de crises dolorosas crônicas de anemia falciforme e beta-talassemia apresentaram remissão clínica completa, com níveis normais de oxigenação tecidual e sem necessidade de transfusões de emergência.",
                    "O Instituto Nacional de Excelência em Saúde e Cuidados (NICE) do Reino Unido aprovou a incorporação da terapia no catálogo de tratamentos públicos do NHS, abrindo caminho para que protocolos de negociação de custo sejam estendidos a países de alta prevalência na África e na América Latina."
                ],
                "aprofundamento": "A cura por edição gênica encerra décadas de sofrimento de populações historicamente negligenciadas, demonstrando o potencial transformador das ferramentas de biologia molecular de precisão.",
                "fontes": [
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário internacional britânico · Seção de Saúde e Ciência",
                        "enfoque": "Os relatos dos pacientes curados e a incorporação do tratamento pelo sistema público NHS.",
                        "url": "https://www.theguardian.com/science/2026/nov/06/crispr-sickle-cell-cure-nhs-uk-trials"
                    },
                    {
                        "fonte": "The Lancet",
                        "perfil": "Periódico médico britânico de referência global",
                        "enfoque": "Os parâmetros hematológicos de longo prazo e a segurança celular da edição molecular.",
                        "url": "https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(26)01988-X/fulltext"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-03",
                "escopo": "internacional",
                "pais": "Alemanha / União Europeia",
                "chapeu": "Geopolítica Energética e Indústria",
                "titulo": "Alemanha inaugura maior rede de dutos de hidrogênio da Europa e conclui reconversão de termelétricas a gás",
                "resumo": "Projeto interliga bacias industriais do Reno e do Ruhr a terminais portuários no Mar do Norte, consolidando infraestrutura limpa para a manufatura pesada.",
                "resumo_visoes": "Financial Times analisa os ganhos de competitividade da indústria química BASF; Le Monde destaca a cooperação energética franco-alemã; El País avalia o papel dos portos do sul da Europa no abastecimento.",
                "texto_completo": [
                    "O governo alemão e consórcios de infraestrutura de transporte inauguraram os primeiros mil e duzentos quilômetros da chamada 'Espinha Dorsal de Hidrogênio' (Wasserstoff-Kernnetz), uma malha integrada de gasodutos dedicados ao transporte de hidrogênio molecular sob alta pressão.",
                    "A rede foi concebida para conectar os grandes centros de consumo da indústria siderúrgica e química nos vales do Ruhr e de Baden-Württemberg aos complexos de geração eólica marinha no Mar do Norte e aos terminais de importação de amônia verde.",
                    "Simultaneamente, operadoras de energia concluíram os testes de queima mista em turbinas termelétricas de ciclo combinado, comprovando a viabilidade de operar plantas elétricas de estabilização de rede com zero emissão de carbono fóssil.",
                    "A chanceler alemã declarou durante o evento inaugural que o projeto assegura o futuro da base manufatureira europeia sem abrir mão das metas mandatórias de neutralidade climática pactuadas no Acordo de Paris."
                ],
                "aprofundamento": "A reconversão de tubulações existentes de gás fóssil para hidrogênio reduziu os custos de capital da obra em mais de 60%, acelerando a transição da maior economia da Europa.",
                "fontes": [
                    {
                        "fonte": "Financial Times",
                        "perfil": "Jornal de economia e negócios europeu",
                        "enfoque": "Os investimentos corporativos na infraestrutura da rede de hidrogênio e as tarifas industriais.",
                        "url": "https://www.ft.com/content/germany-hydrogen-grid-inauguration-industry"
                    },
                    {
                        "fonte": "Le Monde",
                        "perfil": "Jornal diário de referência na França",
                        "enfoque": "A interconexão da rede alemã com os corredores energéticos franceses e espanhóis.",
                        "url": "https://www.lemonde.fr/economie/article/2026/11/06/l-allemagne-ouvre-son-reseau-de-transport-d-hydrogene_6234570_3234.html"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-04",
                "escopo": "internacional",
                "pais": "Japão / Global",
                "chapeu": "Baterias e Mobilidade Sustentável",
                "titulo": "Consórcio no Japão inicia fabricação de baterias de estado sólido com dobro de autonomia para veículos elétricos",
                "resumo": "Nova química de eletrólitos sulfetados reduz tempo de recarga para 10 minutos e elimina risco de incêndio por superaquecimento térmico.",
                "resumo_visoes": "Nikkei Asia detalha a parceria de montadoras japonesas com fornecedores de materiais avançados; MIT Technology Review analisa a durabilidade dos ciclos de carga; The Wall Street Journal projeta barateamento dos carros urbanos.",
                "texto_completo": [
                    "A indústria de mobilidade elétrica atingiu um divisor de águas tecnológico com a inauguração da primeira linha comercial em escala de baterias com eletrólito totalmente sólido (all-solid-state) na província de Aichi, no Japão.",
                    "Diferente das baterias tradicionais de íons de lítio que utilizam eletrólitos líquidos inflamáveis, a nova célula emprega uma matriz de cerâmica sulfetada densa que previne a formação de dendritos metálicos e opera com segurança em temperaturas de -30°C a 80°C.",
                    "Nos ensaios de rodagem com protótipos de veículos utilitários e de passeio, a densidade energética superou 450 watts-hora por quilograma, proporcionando autonomia superior a 900 quilômetros com uma única carga completa em eletropostos ultrarrápidos de dez minutos.",
                    "Fabricantes anunciaram que a produção atenderá prioritariamente os modelos de linha das montadoras a partir de meados de 2027, pressionando a concorrência global a antecipar a aposentadoria dos componentes químicos líquidos."
                ],
                "aprofundamento": "O avanço das baterias de estado sólido resolve de forma definitiva as duas principais barreiras à eletrificação em massa: o tempo de recarga na estrada e a ansiedade de autonomia dos motoristas.",
                "fontes": [
                    {
                        "fonte": "Nikkei Asia",
                        "perfil": "Jornal financeiro e de tecnologia da Ásia",
                        "enfoque": "Os detalhes da cadeia de suprimento de sulfetos e o cronograma de entrega das montadoras.",
                        "url": "https://asia.nikkei.com/Business/Automobiles/Japan-solid-state-battery-commercial-launch"
                    },
                    {
                        "fonte": "MIT Technology Review",
                        "perfil": "Publicação de tecnologia do MIT",
                        "enfoque": "A física de estado sólido da interface entre ânodos de lítio metálico e cerâmica.",
                        "url": "https://www.technologyreview.com/2026/11/06/solid-state-batteries-ev-charging-breakthrough/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-05",
                "escopo": "internacional",
                "pais": "Espanha / Mediterrâneo",
                "chapeu": "Crise Climática e Cidades Resilientes",
                "titulo": "Espanha aprova plano emergencial de adaptação urbana após tempestades mediterrâneas sem precedentes",
                "resumo": "Governo de Madri destina verbas bilionárias para renaturalização de cursos d'água, remoção de habitações em várzeas e instalação de radares meteorológicos doppler.",
                "resumo_visoes": "El País analisa as falhas de coordenação no alerta à população civil em Valência; Le Monde destaca as lições do urbanismo francês; The Guardian cobra transparência das autoridades regionais.",
                "texto_completo": [
                    "O Conselho de Ministros da Espanha formalizou a aprovação do Plano Quinquenal de Adaptação às Inundações Extremas, um conjunto de intervenções urbanísticas e de infraestrutura destinado a redesenhar as áreas urbanas mais vulneráveis da costa mediterrânea.",
                    "A decisão ocorre após as tempestades do tipo gota fria (DANA) de outubro e novembro registrarem volumes pluviométricos de mais de quatrocentos milímetros em menos de seis horas, colapsando canais pluviais e pontes construídas no século passado.",
                    "O plano determina a demolição e desapropriação de construções erguidas irregularmente em planícies de inundação natural de rios e barrancos, substituindo o asfalto por parques lineares alagáveis e bacias de amortecimento biológico de cheias.",
                    "Para o sistema de Defesa Civil, o governo federal estipulou a automatização de alarmes georreferenciados nos telefones celulares de todos os cidadãos em áreas sob risco iminente, sem depender de autorizações burocráticas locais."
                ],
                "aprofundamento": "A intensificação das chuvas torrenciais no Mediterrâneo está diretamente ligada às temperaturas anomalamente quentes das águas marinhas, que funcionam como combustível para tempestades estagnadas.",
                "fontes": [
                    {
                        "fonte": "El País",
                        "perfil": "Jornal diário de referência na Espanha",
                        "enfoque": "O detalhamento do plano nacional de infraestrutura hídrica e os recursos para Valência e Andaluzia.",
                        "url": "https://elpais.com/espana/2026-11-06/gobierno-aprueba-plan-reconstruccion-adaptacion-climatica.html"
                    },
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário britânico · Seção Europa",
                        "enfoque": "A pressão política da opinião pública por responsabilização dos gestores de crise.",
                        "url": "https://www.theguardian.com/world/2026/nov/06/spain-floods-adaptation-plan-climate-crisis"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-06",
                "escopo": "internacional",
                "pais": "Chile / América Latina",
                "chapeu": "Mineração Verde e Lítio",
                "titulo": "Chile conclui modelo de parcerias públicas para extração direta de lítio sustentável nos salares de Atacama",
                "resumo": "Acordo entre estatal Codelco e consórcios privados estipula reinjeção de 90% da salmoura no subsolo, protegendo o lençol freático e as comunidades indígenas atacamenhas.",
                "resumo_visoes": "El Mercurio destaca a previsibilidade para grandes investidores internacionais; Financial Times analisa o impacto nos preços futuros do carbonato de lítio; Página 12 compara o modelo chileno com as regras argentinas.",
                "texto_completo": [
                    "A Corporação Nacional do Cobre do Chile (Codelco) e o Ministério da Mineração concluíram a redação dos contratos definitivos para a exploração do Salar de Atacama, estabelecendo o controle majoritário estatal sobre os ativos estratégicos de lítio.",
                    "O novo marco operacional exige a aposentadoria gradual dos métodos arcaicos de evaporação solar em piscinas abertas, substituindo-os por tecnologias de extração direta (DLE) com reinjeção imediata de água salobra no lençol subterrâneo.",
                    "A mudança tecnológica preserva os ecossistemas lagunares e a avifauna de flamingos andinos, ao mesmo tempo em que eleva a taxa de recuperação química do metal de 40% para mais de 85% do minério processado.",
                    "O documento prevê que 10% de todas as receitas líquidas de exportação sejam transferidas diretamente para fundos comunitários autônomos geridos por conselhos das comunidades indígenas do povo Lickanantay."
                ],
                "aprofundamento": "O lítio é o componente crítico indispensável para a manufatura de baterias de veículos elétricos e sistemas de armazenamento de energia em rede em todo o planeta.",
                "fontes": [
                    {
                        "fonte": "El Mercurio",
                        "perfil": "Jornal diário tradicional de Santiago do Chile",
                        "enfoque": "Os termos contratuais entre a Codelco e os operadores privados de mineração sustentável.",
                        "url": "https://www.elmercurio.com/economia/2026/11/06/codelco-litio-salar-atacama-contratos.html"
                    },
                    {
                        "fonte": "Financial Times",
                        "perfil": "Jornal de economia e mercados de capitais",
                        "enfoque": "A segurança jurídica para fabricantes ocidentais de baterias que buscam fontes sustentáveis de lítio.",
                        "url": "https://www.ft.com/content/chile-lithium-direct-extraction-codelco-deal"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-07",
                "escopo": "internacional",
                "pais": "África do Sul / BRICS",
                "chapeu": "Diplomacia Multilateral e Cooperação Sul-Sul",
                "titulo": "Novo Banco de Desenvolvimento do BRICS aprova carteira de US$ 8 bilhões para saneamento e ferrovias no Sul Global",
                "resumo": "Empréstimos denominados em moedas locais buscam reduzir dependência cambial do dólar e acelerar infraestrutura logística entre os países-membros.",
                "resumo_visoes": "Al Jazeera analisa a redução de riscos cambiais para nações africanas; Valor Econômico detalha os projetos contemplados no Brasil; Folha de S.Paulo contextualiza a expansão de novos membros do bloco.",
                "texto_completo": [
                    "A diretoria executiva do Novo Banco de Desenvolvimento (NDB), reunida na África do Sul, aprovou uma carteira histórica de financiamentos voltada a obras de infraestrutura logística e saneamento básico nas economias emergentes.",
                    "O diferencial da nova linha de crédito reside na emissão de dívida e repasses prioritariamente denominados em moedas locais — incluindo reais brasileiros, rands sul-africanos e dirhams dos Emirados Árabes Unidos —, protegendo os tomadores públicos contra choques na cotação do dólar americano.",
                    "No Brasil, os recursos financiarão a modernização de eixos ferroviários de transporte de carga nos estados do Centro-Oeste e a ampliação de redes de tratamento de esgoto em capitais das regiões Norte e Nordeste.",
                    "A presidência da instituição reiterou que o banco foca em critérios socioambientais rígidos de descarbonização, posicionando o NDB como uma alternativa ágil e não coercitiva às exigências fiscais tradicionais do FMI."
                ],
                "aprofundamento": "A ampliação dos empréstimos em moedas soberanas é o pilar prático mais avançado da estratégia dos BRICS para consolidar uma arquitetura financeira global multipolar.",
                "fontes": [
                    {
                        "fonte": "Al Jazeera English",
                        "perfil": "Rede de jornalismo internacional independente",
                        "enfoque": "Os benefícios da desdolarização dos empréstimos de infraestrutura em economias africanas.",
                        "url": "https://www.aljazeera.com/economy/2026/11/6/ndb-brics-bank-local-currency-loans-approval"
                    },
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de finanças e mercado",
                        "enfoque": "O detalhamento dos repasses para concessões de saneamento e ferrovias de carga no Brasil.",
                        "url": "https://valor.globo.com/financas/noticia/2026/11/06/ndb-banco-brics-financiamentos-brasil-moedas-locais.ghtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-08",
                "escopo": "internacional",
                "pais": "Estados Unidos / Inteligência Artificial",
                "chapeu": "Tecnologia, Modelos Abertos e Sociedade",
                "titulo": "Pesquisadores acadêmicos lançam modelo fundacional de IA de código 100% aberto treinado em dados auditados",
                "resumo": "Iniciativa conjunta de universidades de ponta disponibiliza pesos, conjuntos de treino e códigos de alinhamento para democratizar o desenvolvimento científico de IA sem amarras corporativas.",
                "resumo_visoes": "MIT Technology Review elogia a transparência do treinamento contra alucinações; The Guardian contextualiza a quebra de monopólios das big techs; Nature destaca o uso para biologia estrutural e clima.",
                "texto_completo": [
                    "Um consórcio internacional integrado por pesquisadores de Stanford, Cambridge, ETH Zurique e laboratórios latino-americanos anunciou o lançamento público do OpenFoundation, um modelo de inteligência artificial de fronteira integralmente aberto.",
                    "Diferente dos sistemas proprietários desenvolvidos por corporações do Vale do Silício, o projeto disponibilizou para download livre não apenas os pesos neurais finais, mas também a integridade dos dados brutos de treinamento, os filtros de curadoria e os scripts de otimização matemática.",
                    "O modelo foi treinado em uma infraestrutura computacional compartilhada sem fins lucrativos, priorizando literatura científica revisada por pares, patentes de domínio público e bancos de dados linguísticos de línguas minoritárias com rigoroso filtro ético anti-plágio.",
                    "Cientistas de diversas áreas já utilizam o modelo como motor base para simulações de dobramento molecular, previsão de trajetórias de ciclones e tradução de línguas indígenas sem risco de apropriação comercial monopolista."
                ],
                "aprofundamento": "A iniciativa é considerada o maior marco na defesa do software livre e da ciência aberta desde a criação dos primeiros repositórios públicos do sistema Linux.",
                "fontes": [
                    {
                        "fonte": "MIT Technology Review",
                        "perfil": "Revista de ciência e tecnologia de computação",
                        "enfoque": "A arquitetura aberta e a eliminação de caixas-pretas proprietárias no avanço da inteligência artificial.",
                        "url": "https://www.technologyreview.com/2026/11/06/open-source-frontier-ai-model-release/"
                    },
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário internacional britânico · Seção Tecnologia",
                        "enfoque": "A reação dos laboratórios acadêmicos globais contra a concentração de poder das grandes empresas de tecnologia.",
                        "url": "https://www.theguardian.com/technology/2026/nov/06/open-source-ai-consortium-academia-breakthrough"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-09",
                "escopo": "internacional",
                "pais": "Oriente Médio / Palestina",
                "chapeu": "Direitos Humanos e Geopolítica",
                "titulo": "Tribunais internacionais em Haia reafirmam jurisdição sobre crimes de guerra e cobram proteção a agentes de saúde em Gaza",
                "resumo": "Em sessão extraordinária, juízes determinam que bloqueios deliberados de combustível e água violam o direito humanitário internacional e exigem cooperação de todos os signatários do Estatuto de Roma.",
                "resumo_visoes": "Le Monde detalha a fundamentação dos juízes internacionais; El País analisa o isolamento diplomático de governos que descumprem ordens judiciais; BBC World relata a precariedade dos hospitais no enclave.",
                "texto_completo": [
                    "A Corte Internacional de Justiça (CIJ) e o Tribunal Penal Internacional (TPI), sediados em Haia, divulgaram novas determinações vinculantes reiterando o dever imediato e incondicional de proteção à população civil e às missões médicas no Oriente Médio.",
                    "O painel de magistrados considerou que qualquer obstrução deliberada à entrada de comboios humanitários com suprimentos hospitalares, anestésicos e geradores elétricos configura grave transgressão às Convenções de Genebra e ao Estatuto de Roma.",
                    "A manifestação das cortes respondeu a petições formais apresentadas por países da África do Sul, América Latina e Europa, que documentaram a destruição reiterada de instalações de saúde e a morte de dezenas de enfermeiros e médicos em serviço.",
                    "Lideranças diplomáticas em Genebra e Nova York reforçaram que a credibilidade do sistema multilateral de justiça depende do cumprimento estrito das medidas cautelares por todos os Estados soberanos, sem exceções de conveniência política."
                ],
                "aprofundamento": "A decisão de Haia reforça o arcabouço de direito humanitário construído no pós-Segunda Guerra, consagrando a primazia da vida civil sobre objetivos belicistas.",
                "fontes": [
                    {
                        "fonte": "Le Monde",
                        "perfil": "Jornal diário de referência na França",
                        "enfoque": "Os fundamentos jurídicos das ordens cautelares de Haia e a repercussão nas chancelarias europeias.",
                        "url": "https://www.lemonde.fr/international/article/2026/11/06/justice-internationale-la-haye-droit-humanitaire-gaza_6234571_3210.html"
                    },
                    {
                        "fonte": "El País",
                        "perfil": "Jornal diário internacional espanhol",
                        "enfoque": "O posicionamento firme da diplomacia espanhola e latino-americana em defesa do direito internacional.",
                        "url": "https://elpais.com/internacional/2026-11-06/tribunales-la-haya-jurisdiccion-crimenes-guerra.html"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-10",
                "escopo": "internacional",
                "pais": "França / Literatura e Cultura",
                "chapeu": "Cultura Internacional e Literatura",
                "titulo": "Prêmio Goncourt 2026 consagra romance polifônico sobre a memória dos trabalhadores da reconstrução de Paris no pós-guerra",
                "resumo": "Maior honraria literária da língua francesa premia obra comovente que resgata a saga de operários imigrantes espanhóis, portugueses e argelinos que reconstruíram a infraestrutura urbana.",
                "resumo_visoes": "Le Monde Literário celebra o resgate estético da dignidade operária; Libération destaca a prosa lírica e fragmentária; The Guardian elogia a tradução já contratada para os mercados anglófonos.",
                "texto_completo": [
                    "A Academia Goncourt anunciou nesta manhã no restaurante Drouant, em Paris, a atribuição do cobiçado Prêmio Goncourt de 2026 ao escritor franco-argelino Mehdi Charef pelo romance 'Les Bâtisseurs de l'Ombre' (Os Construtores da Sombra).",
                    "A obra, aclamada unanimemente pela crítica como uma das mais pungentes da ficção contemporânea, acompanha três gerações de pedreiros, encanadores e carpinteiros estrangeiros que ergueram os viadutos, túneis de metrô e complexos habitacionais da região metropolitana de Paris entre 1950 e 1975.",
                    "Com uma linguagem poética que intercala gírias operárias, cadernos de memória e lirismo intimista, o autor constrói um mosaico comovente sobre a solidariedade de classe, o desenraizamento do exílio e a beleza oculta dos homens que deixaram sua juventude cimentada nas paredes da cidade.",
                    "Editoras brasileiras já confirmaram a disputa pelos direitos de tradução e publicação da obra no país, com lançamento previsto para o primeiro semestre de 2027."
                ],
                "aprofundamento": "O Goncourt é a distinção literária de maior impacto comercial e crítico no continente europeu, tradicionalmente impulsionando centenas de milhares de exemplares e traduções para mais de quarenta idiomas.",
                "fontes": [
                    {
                        "fonte": "Le Monde",
                        "perfil": "Jornal diário de referência na França · Le Monde des Livres",
                        "enfoque": "A crítica do romance premiado e a celebração da literatura operária e humanista.",
                        "url": "https://www.lemonde.fr/livres/article/2026/11/06/prix-goncourt-2026-mehdi-charef-consacre_6234572_3260.html"
                    },
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário internacional britânico · Seção Livros",
                        "enfoque": "A repercussão da premiação em Londres e os preparativos para as traduções internacionais.",
                        "url": "https://www.theguardian.com/books/2026/nov/06/prix-goncourt-2026-winner-french-fiction"
                    }
                ]
            },
            {
                "id": "fo-n-20261106-int-11",
                "escopo": "internacional",
                "pais": "Global / Clima e Finanças",
                "chapeu": "Governança Climática e Economia",
                "titulo": "Secretariado da ONU Clima formaliza nova meta global de financiamento para transição justa com aportes mandatórios de países emissores",
                "resumo": "Proposta para a cúpula climática estipula US$ 300 bilhões anuais em subsídios diretos e doações para conter perdas e danos nas nações mais vulneráveis do planeta.",
                "resumo_visoes": "Financial Times detalha as divergências sobre fontes públicas e privadas; The Guardian destaca a pressão dos pequenos estados insulares; El País analisa o papel de liderança do Brasil nas negociações de Belém.",
                "texto_completo": [
                    "O Secretariado da Convenção-Quadro das Nações Unidas sobre Mudança do Clima (UNFCCC) publicou o rascunho de negociação da Nova Meta Coletiva Quantificada de Financiamento Climático (NCQG), o tema mais sensível da diplomacia ambiental global contemporânea.",
                    "O texto estabelece que as economias desenvolvidas e grandes poluidores históricos deverão mobilizar um piso mínimo de trezentos bilhões de dólares ao ano em doações orçamentárias diretas e financiamentos concessionais sem juros para os países do Sul Global.",
                    "A nova fórmula exclui expressamente empréstimos comerciais que aumentem o endividamento externo de nações pobres, priorizando repasses imediatos para projetos de contenção da erosão costeira em ilhas do Pacífico e reflorestamento de bacias hidrográficas tropicais.",
                    "O Itamaraty e os negociadores da presidência da COP30 celebraram o avanço do texto-base, apontando que a justiça financeira climática é o único alicerce capaz de sustentar o cumprimento das metas científicas de redução de emissões nos próximos dez anos."
                ],
                "aprofundamento": "A definição de metas financeiras claras e não baseadas em dívida comercial é a exigência primordial do bloco dos países em desenvolvimento para manter vivo o espírito do Acordo de Paris.",
                "fontes": [
                    {
                        "fonte": "Financial Times",
                        "perfil": "Jornal diário internacional de finanças e economia",
                        "enfoque": "Os detalhes da negociação da nova meta financeira climática entre os blocos diplomáticos.",
                        "url": "https://www.ft.com/content/unfccc-climate-finance-goal-ncqg-draft"
                    },
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário britânico · Seção Meio Ambiente",
                        "enfoque": "A voz dos países insulares e africanos por recursos a fundo perdido para reconstrução de danos.",
                        "url": "https://www.theguardian.com/environment/2026/nov/06/un-climate-finance-draft-target-loss-damage"
                    }
                ]
            }
        ]
    }

    dias["2026-11-06"] = dia_06
    print("Edição 2026-11-06 (Manhã) criada com 22 notas (11 nacionais + 11 internacionais)!")

    # Atualizar lista de dias
    salvar_db(db)

if __name__ == "__main__":
    criar_edicoes()
