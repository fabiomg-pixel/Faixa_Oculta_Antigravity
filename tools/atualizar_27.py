import hashlib, json, os, re, shutil, subprocess, urllib.parse

ROOT = "/working_dir/c_c6a296f49289620b/artifacts/file_generation/ttl=63d/intermediate/faixa-oculta"
REVISTA_PATH = os.path.join(ROOT, "data", "revista.json")

def limpar_url(url):
    s = urllib.parse.urlsplit(str(url).strip())
    q = [(k, v) for k, v in urllib.parse.parse_qsl(s.query, keep_blank_values=True)
         if not k.lower().startswith(("utm_", "fbclid", "gclid"))]
    return urllib.parse.urlunsplit((s.scheme, s.netloc, s.path, urllib.parse.urlencode(q), ""))

def chave(url):
    u = limpar_url(url).rstrip("/")
    return re.sub(r"^https?://(www\.)?", "", u).lower()

def doc_id(url):
    return hashlib.sha1(chave(url).encode()).hexdigest()[:16]

with open(REVISTA_PATH, encoding="utf-8") as f:
    revista = json.load(f)

# 1. Definir o boletim de 27/10/2026 (manhã)
boletim_27 = {
    "data": "2026-10-27",
    "edicao": "manha",
    "titulo": "Mercado busca alívio após tombo e vence prazo de passaportes de Flávio",
    "resumo_dia": "Na manhã desta terça-feira, o mercado financeiro tenta se estabilizar após a B3 registrar o pior pregão em seis anos, com o dólar a R$ 5,40 e o acionamento do circuit breaker no dia anterior. Vence hoje o prazo de 24 horas fixado pelo ministro Alexandre de Moraes para que Flávio Bolsonaro entregue seus passaportes à Polícia Federal. Nos Estados Unidos, aliados de Donald Trump pressionam por retaliações contra o Brasil, enquanto o governo Lula mantém a postura de não responder a acusações sem provas. Em Teerã, delegações da Arábia Saudita, Turquia e Paquistão mantêm negociações para conter a crise no Golfo antes da eleição americana. No Rio, a UFRJ abre a Semana do Servidor com atenção redobrada aos impactos do dólar e do novo cenário político no orçamento das pesquisas.",
    "notas": [
        {
            "id": "mercado-tenta-estabilizacao",
            "editoria": "Economia",
            "titulo": "Mercado busca trégua após tombo histórico do Ibovespa",
            "texto": "Após a queda de 13,88% no pregão de segunda-feira e o acionamento do circuit breaker, os índices futuros da B3 e os recibos de ações brasileiras em Nova York apontam para uma tentativa de acomodação na abertura desta terça-feira. O dólar à vista, que encerrou cotado a R$ 5,40 na maior alta diária em meses, opera sob cautela. Segundo a Exame e a Bloomberg Línea, operadores aguardam os próximos sinais da equipe de transição do presidente reeleito e declarações de dirigentes do Banco Central. O foco permanece na sustentabilidade fiscal e na indicação do futuro ministro da Fazenda, depois que Rafael Fonteles rejeitou especulações em torno de seu nome. A volatilidade internacional e as decisões de juros do Federal Reserve nesta quarta-feira também restringem o apetite a risco.",
            "por_que_importa": "A estabilização do câmbio é decisiva para controlar pressões inflacionárias sobre combustíveis, medicamentos e importações de insumos científicos.",
            "fontes": [
                {
                    "fonte": "Exame",
                    "perfil": "revista e portal de negócios",
                    "enfoque": "abertura dos mercados e indicadores de alívio pós-tombo",
                    "url": "https://exame.com/invest/mercados/dados-dos-eua-relatorio-do-bc-e-galipolo-o-que-move-o-mercado-apos-tombo-da-bolsa/"
                },
                {
                    "fonte": "UOL Economia",
                    "perfil": "portal de notícias, centro",
                    "enfoque": "sinais de recuperação dos ativos brasileiros no exterior",
                    "url": "https://economia.uol.com.br/cotacoes/noticias/redacao/2026/10/27/ativos-brasileiros-no-exterior-27-de-outubro-de-2026.ghtm"
                },
                {
                    "fonte": "Bloomberg Línea",
                    "perfil": "agência financeira internacional",
                    "enfoque": "revisão de posições em Wall Street para ativos do Brasil",
                    "url": "https://www.bloomberglinea.com.br/mercados/wall-street-revisa-apostas-para-o-brasil-e-tenta-calcular-ate-onde-vai-a-correcao/"
                }
            ]
        },
        {
            "id": "prazo-passaporte-flavio",
            "editoria": "Política",
            "titulo": "Vence prazo de 24 horas para Flávio Bolsonaro entregar passaportes",
            "texto": "Termina nesta terça-feira a ordem do ministro Alexandre de Moraes, do STF, que intimou o senador Flávio Bolsonaro a entregar todos os seus passaportes à Polícia Federal. A decisão, tomada no âmbito de apurações sob sigilo ligadas a movimentações financeiras, proíbe o parlamentar de deixar o território nacional e veda contato com o advogado Willer Tomaz. Conforme noticiado pelo Estadão e pela RTP, a defesa do senador ingressa com pedidos de reconsideração, sustentando que a restrição viola prerrogativas parlamentares e foi baseada em declarações públicas de terceiros. A oposição articula levar o caso a comissões internacionais de direitos humanos, enquanto líderes partidários no Senado buscam evitar que o episódio paralise as votações regimentais da Casa nesta semana.",
            "por_que_importa": "O cumprimento da medida cautelar sela a derrota eleitoral e redefine o comando da oposição no Congresso nos próximos meses.",
            "fontes": [
                {
                    "fonte": "Estadão",
                    "perfil": "jornal de referência, centro-direita",
                    "enfoque": "notificação da PF e estratégia jurídica da defesa",
                    "url": "https://www.estadao.com.br/politica/eleicoes/flavio-diz-que-vai-pedir-cassacao-de-chapa-do-pt-e-que-moraes-ordenou-entrega-de-passaportes/"
                },
                {
                    "fonte": "Metrópoles",
                    "perfil": "portal de notícias, centro",
                    "enfoque": "reunião de aliados e mobilização parlamentar",
                    "url": "https://www.metropoles.com/brasil/flavio-bolsonaro-diz-que-foi-intimado-pela-pf-a-entregar-passaporte"
                },
                {
                    "fonte": "RTP",
                    "perfil": "emissora pública, Portugal",
                    "enfoque": "repercussão jurídica internacional e proibição de viagens",
                    "url": "https://www.rtp.pt/noticias/mundo/nova-decisao-judicial-proibe-flavio-bolsonaro-de-deixar-o-pais_n1774570"
                }
            ]
        },
        {
            "id": "trumpistas-retaliacao-governo",
            "editoria": "Política",
            "titulo": "Ala trumpista prega retaliações e Planalto mantém silêncio institucional",
            "texto": "Após o ex-presidente Donald Trump classificar o pleito brasileiro como suspeito em declarações à imprensa no dia anterior, operadores políticos de seu entorno, como Steve Bannon, passaram a defender sanções diplomáticas e tarifas seletivas contra o Brasil. Segundo a Folha de S.Paulo, o Palácio do Planalto e o Itamaraty confirmaram que não responderão a insinuações informais, tratando o processo eleitoral como assunto soberano referendado por dezenas de chefes de Estado. Diplomatas brasileiros destacam que mensagens formais de reconhecimento e votos de cooperação já foram transmitidos pelas principais chancelarias da União Europeia, Reino Unido e Japão, esvaziando tentativas de isolamento internacional durante o período de transição.",
            "por_que_importa": "A postura comedida do Itamaraty visa desarmar narrativas externas antes da posse presidencial e preservar canais de exportação aos Estados Unidos.",
            "fontes": [
                {
                    "fonte": "Folha de S.Paulo",
                    "perfil": "jornal de referência, centro",
                    "enfoque": "pressão da extrema-direita americana e postura do Itamaraty",
                    "url": "https://www.folha.uol.com.br/"
                },
                {
                    "fonte": "SBT News",
                    "perfil": "emissora de televisão, centro-direita",
                    "enfoque": "decisão do governo de evitar confrontos públicos",
                    "url": "https://sbtnews.sbt.com.br/noticia/eleicoes/planalto-nao-vai-reagir-a-fala-de-trump-2"
                }
            ]
        },
        {
            "id": "dialogo-teera-golfo",
            "editoria": "Mundo",
            "titulo": "Teerã aceita novas rodadas de diálogo com potências regionais",
            "texto": "Negociadores do Irã concordaram em prosseguir as reuniões diplomáticas em Teerã com delegações da Arábia Saudita, Turquia e Paquistão, informou a CBS News nesta manhã. As conversas, intermediadas pelo Catar e acompanhadas por observadores internacionais, buscam conter uma escalada armada e negociar a reabertura segura das rotas comerciais no Estreito de Ormuz. Diplomatas árabes avaliam o encontro como um canal derradeiro de contenção antes de eventuais ordens militares de Washington, que mantém contingente em prontidão. Em troca de trégua na navegação, o governo iraniano exige a suspensão dos embargos a terminais petrolíferos e garantias contra ataques preemptivos às suas instalações nucleares.",
            "por_que_importa": "O andamento dessas negociações dita o preço do barril de petróleo no mercado internacional e o custo global do frete marítimo.",
            "fontes": [
                {
                    "fonte": "CBS News",
                    "perfil": "rede de notícias, EUA",
                    "enfoque": "diplomacia regional em Teerã e pressão pré-eleitoral americana",
                    "url": "https://www.cbsnews.com/live-updates/iran-war-trump-us-diplomacy-oil-prices-strait-of-hormuz/"
                },
                {
                    "fonte": "Iran International",
                    "perfil": "canal de notícias independente, Londres",
                    "enfoque": "condições iranianas sobre bloqueios portuários",
                    "url": "https://www.iranintl.com/en/202610266454"
                },
                {
                    "fonte": "Indian Express",
                    "perfil": "jornal de referência, Índia",
                    "enfoque": "impactos do fornecimento de energia e segurança no Golfo",
                    "url": "https://indianexpress.com/article/world/iran-war-live-updates-pakistan-tehran-talks-trump-strike-warning-saudi-attack-oil-prices-india-hormuz-shipping-today-10938063/"
                }
            ]
        },
        {
            "id": "ufrj-orcamento-ciencia",
            "editoria": "Ciência",
            "titulo": "UFRJ debate recomposição orçamentária e impacto cambial na pesquisa",
            "texto": "A Universidade Federal do Rio de Janeiro abriu nesta terça-feira a Semana do Servidor Público com painéis sobre a valorização do funcionalismo e a gestão das universidades federais. No Instituto de Biofísica Carlos Chagas Filho (IBCCF), pesquisadores e coordenadores de pós-graduação apontam preocupação com a recente volatilidade do dólar, que eleva custos de reagentes biológicos, enzimas e equipamentos de precisão cotados no exterior. A comunidade acadêmica da UFRJ aguarda o detalhamento do Projeto de Lei Orçamentária e a abertura dos editais de fomento à pesquisa prometidos para o novo mandato federal, além dos editais internos de mestrado e doutorado abertos para 2027.",
            "por_que_importa": "Para laboratórios de biofísica e ciências biomédicas, qualquer oscilação prolongada no câmbio reduz o poder de compra de insumos críticos de pesquisa.",
            "fontes": [
                {
                    "fonte": "Portal UFRJ",
                    "perfil": "canal institucional universitário",
                    "enfoque": "abertura da Semana do Servidor e debates de infraestrutura",
                    "url": "https://pessoal.ufrj.br/semanadoservidor2026/"
                },
                {
                    "fonte": "PPG Biofísica IBCCF",
                    "perfil": "instituto de pesquisa biomédica",
                    "enfoque": "editais de pós-graduação e manutenção laboratorial",
                    "url": "https://ppgbiofisica.biof.ufrj.br/"
                }
            ]
        },
        {
            "id": "uniao-europeia-clima-cop31",
            "editoria": "Clima",
            "titulo": "Ministros da UE alinham metas de transição antes da COP31",
            "texto": "Reunidos em Bruxelas para sessões preparatórias do Conselho de Energia e Meio Ambiente, ministros da União Europeia debatem diretrizes comuns sobre descarbonização industrial e incentivos para fontes renováveis, visando a próxima cúpula climática global (COP31). De acordo com comunicado divulgado pelo Conselho da UE, o bloco busca acelerar a autonomia energética frente à instabilidade no mercado de hidrocarbonetos e aos riscos geopolíticos nas rotas marítimas do Oriente Médio. Entre os pontos centrais estão a fixação de padrões para hidrogênio verde e critérios mais rígidos de pegada de carbono para insumos importados, medidas que incidem diretamente sobre produtores e exportadores brasileiros.",
            "por_que_importa": "Exigências de rastreabilidade e metas de sustentabilidade da UE afetam as cadeias industriais e o comércio exterior do Brasil.",
            "fontes": [
                {
                    "fonte": "Consilium Europeu",
                    "perfil": "órgão oficial da União Europeia",
                    "enfoque": "comunicados e pauta sobre energia e sustentabilidade",
                    "url": "https://www.consilium.europa.eu/pt/press/press-releases/2026/10/27/press-briefing-transport-telecommunications-and-energy-council-energy-of-29-october-2026/"
                }
            ]
        },
        {
            "id": "rio-plano-verao",
            "editoria": "Rio",
            "titulo": "Prefeitura do Rio publica cronograma preventivo para chuvas de verão",
            "texto": "O Diário Oficial do Município do Rio de Janeiro publicou nesta terça-feira novos atos regulamentares que estabelecem o cronograma intensivo de limpeza de canais, desobstrução de galerias pluviais e manutenção de encostas nas zonas Norte e Oeste. O plano visa antecipar contingências para o período de tempestades de verão, com integração entre a Defesa Civil, a Comlurb e o Centro de Operações Rio (COR). Na área cultural, prefeituras da Região Metropolitana também encerram hoje o prazo de submissão de propostas aos editais descentralizados da Política Nacional Aldir Blanc (PNAB), que contemplam coletivos artísticos e equipamentos comunitários.",
            "por_que_importa": "Ações estruturais e preventivas de drenagem urbana são essenciais para evitar transtornos rotineiros de deslocamento na capital fluminense.",
            "fontes": [
                {
                    "fonte": "Diário Oficial do Rio",
                    "perfil": "órgão oficial municipal",
                    "enfoque": "portarias operacionais de contenção e saneamento",
                    "url": "https://doweb.rio.rj.gov.br/"
                }
            ]
        },
        {
            "id": "capacitacao-ia-institutos",
            "editoria": "Tecnologia",
            "titulo": "Institutos federais ampliam programas de formação e ética em IA",
            "texto": "Institutos federais e centros de tecnologia divulgaram nesta terça-feira editais e chamadas públicas para cursos de pós-graduação e aperfeiçoamento voltados à aplicação estratégica de Inteligência Artificial no setor público e no ecossistema produtivo. As iniciativas buscam preencher lacunas de capacitação técnica, automação de processos e conformidade com diretrizes emergentes de privacidade de dados e auditoria algorítmica. O avanço desses programas coincide com o debate no Congresso Nacional sobre a regulação dos sistemas de aprendizado de máquina, com ênfase na governança de modelos abertos e salvaguardas no uso governamental.",
            "por_que_importa": "A formação técnica local é indispensável para que o Brasil desenvolva autonomia tecnológica e uso responsável de ferramentas analíticas.",
            "fontes": [
                {
                    "fonte": "Portal IFMG",
                    "perfil": "instituto federal de educação e tecnologia",
                    "enfoque": "resultados e editais de pós-graduação em inteligência artificial",
                    "url": "https://www.ifmg.edu.br/portal/noticias/campus-formiga-divulga-resultado-preliminar-do-sorteio-para-pos-graduacao-em-inteligencia-artificial"
                }
            ]
        }
    ],
    "agenda": [
        {
            "quando": "hoje, ao longo do dia",
            "o_que": "Término do prazo judicial para entrega dos passaportes de Flávio Bolsonaro à PF."
        },
        {
            "quando": "quarta, 28/10",
            "o_que": "Comitê de Política Monetária (FOMC) do Federal Reserve anuncia decisão sobre juros nos EUA."
        },
        {
            "quando": "quinta, 29/10",
            "o_que": "Conselho de Energia e Ambiente da União Europeia reúne ministros em Bruxelas."
        },
        {
            "quando": "terça, 3/11",
            "o_que": "Eleições de meio de mandato (midterms) nos EUA definem controle do Congresso americano."
        }
    ]
}

revista["dias"]["2026-10-27"] = boletim_27

# 2. Leituras limpas para as fontes principais
novas_leituras = [
    {
        "url": "https://exame.com/invest/mercados/dados-dos-eua-relatorio-do-bc-e-galipolo-o-que-move-o-mercado-apos-tombo-da-bolsa/",
        "fonte": "Exame",
        "tipo": "noticia",
        "data": "2026-10-27",
        "titulo": "O que move os mercados nesta terça após tombo histórico do Ibovespa",
        "resumo": [
            "A Exame aponta que o mercado acionário brasileiro busca um ponto de equilíbrio nesta terça-feira após a perda de quase 14% registrada no pregão pós-eleitoral. Investidores institucionais acompanham declarações de dirigentes do Banco Central e a recepção de relatórios sobre sustentabilidade fiscal da equipe econômica de transição.",
            "No cenário externo, a expectativa pelas deliberações de política monetária nos Estados Unidos e as tensões no Oriente Médio restringem o ímpeto de recuperação dos ativos de risco em economias emergentes."
        ],
        "citacao": "Operadores buscam estabilização após a forte volatilidade do pregão anterior"
    },
    {
        "url": "https://www.estadao.com.br/politica/eleicoes/flavio-diz-que-vai-pedir-cassacao-de-chapa-do-pt-e-que-moraes-ordenou-entrega-de-passaportes/",
        "fonte": "Estadão",
        "tipo": "noticia",
        "data": "2026-10-27",
        "titulo": "Flávio Bolsonaro é intimado a entregar passaportes por ordem do STF",
        "resumo": [
            "O Estadão relata que a Polícia Federal cumpriu intimação judicial que determina o recolhimento de todos os passaportes do senador Flávio Bolsonaro no prazo de 24 horas, além de impedi-lo de viajar ao exterior.",
            "A medida, decretada pelo ministro Alexandre de Moraes, atinge documentos comuns e diplomáticos. A defesa do parlamentar sustenta que inexiste fundamentação jurídica para a cautelar e planeja recorrer ao plenário da corte."
        ],
        "citacao": "A defesa do parlamentar prepara recurso ao plenário da Suprema Corte"
    }
]

for l in novas_leituras:
    l_id = doc_id(l["url"])
    revista.setdefault("leituras", {})[l_id] = l

# 3. Salvar data/revista.json
with open(REVISTA_PATH, "w", encoding="utf-8") as f:
    json.dump(revista, f, ensure_ascii=False, indent=2)

print("Revista.json atualizada com sucesso! Total dias:", len(revista["dias"]))
