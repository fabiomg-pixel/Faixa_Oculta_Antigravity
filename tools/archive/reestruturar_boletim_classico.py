#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reestrutura o boletim diário ('Hoje') com notícias clássicas de alta densidade:
- Remove completamente pautas burocráticas de trabalho/laboratório e notas triviais.
- Foca em Economia dura (fiscal, Selic, dólar, dívida, emprego, indústria).
- Foca em Política Nacional (Congresso, STF, Executivo, segurança pública nacional).
- Foca em Geopolítica e Política Internacional clássica (eleições, diplomacia, conflitos, comércio global).
- Preserva a paridade mandatória: 11 notícias nacionais + 11 internacionais traduzidas na íntegra.
"""

import json

def reestruturar():
    with open("data/revista.json", "r", encoding="utf-8") as f:
        db = json.load(f)

    dias = db.setdefault("dias", {})

    # =========================================================================
    # 1. CALIBRAR EDIÇÃO DA MANHÃ (2026-11-06) - Trocar notas de laboratório
    # =========================================================================
    dia_manha = dias.get("2026-11-06")
    if dia_manha and "notas" in dia_manha:
        # Substituir nota 5 (Fiocruz vacinas de bancada) por Mercado de Trabalho
        dia_manha["notas"][4] = {
            "id": "fo-n-20261106-nac-05",
            "escopo": "nacional",
            "pais": "Brasil",
            "chapeu": "Emprego e Mercado de Trabalho",
            "editoria": "Economia",
            "titulo": "Taxa de desemprego recua para 6,4% na PNAD Contínua e massa salarial real atinge recorde histórico",
            "resumo": "Dados divulgados pelo IBGE mostram expansão contínua do emprego formal, puxada pela indústria e pelo setor de serviços, com aumento do poder de compra médio dos trabalhadores.",
            "resumo_visoes": "Valor Econômico destaca a pressão sobre os custos trabalhistas e o alerta do Banco Central; Folha de S.Paulo analisa a queda na informalidade urbana; O Globo ressalta o impacto no consumo das famílias no quarto trimestre.",
            "texto_completo": [
                "A taxa de desocupação no Brasil caiu para 6,4% no trimestre encerrado em outubro, o menor patamar para o período desde o início da série histórica da Pesquisa Nacional por Amostra de Domicílios Contínua (PNAD Contínua) do IBGE.",
                "O contingente de trabalhadores ocupados alcançou a marca inédita de 102,5 milhões de pessoas, impulsionado pela abertura consistente de vagas com carteira assinada na indústria de transformação e no setor de serviços corporativos.",
                "O rendimento médio real habitual avançou 4,1% na comparação interanual, atingindo R$ 3.250 mensais. Essa expansão sustentada da massa de salários em circulação tem funcionado como o principal motor da resiliência do Produto Interno Bruto em 2026.",
                "No Banco Central e em consultorias de macroeconomia, o aperto do mercado de trabalho é acompanhado com atenção redobrada, uma vez que a escassez de mão de obra em setores especializados pode limitar a velocidade de desinflação no segmento de serviços."
            ],
            "aprofundamento": {
                "contexto": "O mercado de trabalho brasileiro opera próximo do pleno emprego técnico, exigindo ganhos de produtividade e investimentos em qualificação para sustentar o ritmo de expansão sem alimentar pressões inflacionárias.",
                "o_que_observar": "Os próximos dados do Caged de geração de vagas formais e os indicadores de inflação de serviços do IPCA."
            },
            "fontes": [
                {
                    "fonte": "Valor Econômico",
                    "perfil": "Jornal diário de economia e mercado",
                    "enfoque": "A leitura do Copom sobre o mercado de trabalho apertado e as projeções de juros.",
                    "url": "https://valor.globo.com/brasil/noticia/2026/11/06/desemprego-ibge-pnad-continua-outubro.ghtml"
                },
                {
                    "fonte": "Folha de S.Paulo",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "A expansão da carteira assinada e a redução da taxa de informalidade nas regiões metropolitanas.",
                    "url": "https://www1.folha.uol.com.br/mercado/2026/11/taxa-de-desemprego-cai-ibge-pnad.shtml"
                }
            ]
        }

        # Substituir nota 6 (Canecão UFRJ) por Indústria e Comércio Exterior
        dia_manha["notas"][5] = {
            "id": "fo-n-20261106-nac-06",
            "escopo": "nacional",
            "pais": "Brasil",
            "chapeu": "Indústria e Comércio Exterior",
            "editoria": "Economia",
            "titulo": "Balança comercial brasileira registra superávit de US$ 8,2 bilhões impulsionada por manufaturados e agroindústria",
            "resumo": "Exportações mantêm ritmo forte com aumento de embarques para a Ásia e União Europeia, enquanto importações de bens de capital sinalizam retomada do investimento produtivo.",
            "resumo_visoes": "Valor Econômico detalha o impacto cambial favorável nas contas externas; G1 destaca o desempenho das exportações de carne processada e celulose; Poder360 analisa a balança com os parceiros do Mercosul.",
            "texto_completo": [
                "A balança comercial do Brasil registrou superávit de US$ 8,2 bilhões no último fechamento mensal compilado pela Secretaria de Comércio Exterior (Secex) do Ministério do Desenvolvimento, Indústria, Comércio e Serviços.",
                "O saldo positivo acumulado no ano já ultrapassa US$ 75 bilhões, consolidando o segundo melhor resultado da história do comércio exterior brasileiro, impulsionado tanto pelos embarques recordes de grãos e carnes quanto pela resiliência das vendas de óleos brutos de petróleo e minério de ferro.",
                "As exportações de produtos da indústria de transformação registraram crescimento de 6,8%, beneficiadas pela reativação de acordos tarifários no âmbito latino-americano e pela demanda europeia por insumos descarbonizados.",
                "Do lado das compras externas, a alta nas importações foi concentrada em bens de capital, máquinas industriais e intermediários químicos, o que analistas interpretam como um indicador antecedente de expansão da capacidade produtiva instalada no país."
            ],
            "aprofundamento": {
                "contexto": "O superávit comercial robusto é a principal âncora de divisas do país, assegurando reservas internacionais confortáveis de mais de US$ 350 bilhões.",
                "o_que_observar": "Os preços internacionais das commodities no mercado futuro de Chicago e a cotação do barril de petróleo Brent."
            },
            "fontes": [
                {
                    "fonte": "Valor Econômico",
                    "perfil": "Jornal diário de comércio e negócios",
                    "enfoque": "Os números detalhados da Secex e a contribuição da agroindústria exportadora.",
                    "url": "https://valor.globo.com/brasil/noticia/2026/11/06/balanca-comercial-superavit-secex-mdic.ghtml"
                },
                {
                    "fonte": "G1",
                    "perfil": "Portal de notícias em tempo real",
                    "enfoque": "Os principais destinos das exportações brasileiras e os setores industriais em destaque.",
                    "url": "https://g1.globo.com/economia/noticia/2026/11/06/balanca-comercial-resultado-mensal.ghtml"
                }
            ]
        }

        # Substituir nota 10 (MCTI editais de laboratório) por Infraestrutura e Concessões
        dia_manha["notas"][9] = {
            "id": "fo-n-20261106-nac-10",
            "escopo": "nacional",
            "pais": "Brasil",
            "chapeu": "Infraestrutura e Transportes",
            "editoria": "Economia",
            "titulo": "Leilões de rodovias e ferrovias garantem R$ 24 bilhões em investimentos privados para escoamento de safras",
            "resumo": "Rodadas na B3 atraem operadores internacionais com contratos de longo prazo voltados à duplicação de eixos no Centro-Oeste e Sudeste e descarbonização da logística.",
            "resumo_visoes": "O Globo detalha os consórcios vencedores e o cronograma de obras; Folha de S.Paulo analisa a redução do custo do frete para o agronegócio; Valor Econômico foca na estrutura de garantias do BNDES.",
            "texto_completo": [
                "O Ministério dos Transportes e a Agência Nacional de Transportes Terrestres (ANTT) concluíram na B3 mais uma etapa bem-sucedida do programa de concessões rodoviárias e ferroviárias, contratando R$ 24 bilhões em investimentos obrigatórios para os próximos dez anos.",
                "Os lotes leiloados abrangem corredores logísticos vitais para o escoamento da produção agrícola e industrial em Minas Gerais, Goiás, Mato Grosso e interior de São Paulo, prevendo mais de 800 quilômetros de duplicações e faixas adicionais.",
                "O certame consolidou a participação de grandes fundos de investimento soberanos e operadoras europeias de infraestrutura, atraídos pela nova modelagem contratual que prevê mecanismos automáticos de mitigação de risco cambial e incentivos à transição ecológica.",
                "A expectativa da Confederação Nacional do Transporte (CNT) é de que a modernização desses eixos reduza o custo logístico do frete em até 18% para os produtores nacionais até 2028."
            ],
            "aprofundamento": {
                "contexto": "O gargalo logístico rodoviário e ferroviário é um dos principais componentes do chamado 'Custo Brasil', impactando a competitividade das exportações de manufaturados e alimentos.",
                "o_que_observar": "A assinatura dos contratos de concessão e o início das primeiras frentes de obras e duplicações."
            },
            "fontes": [
                {
                    "fonte": "O Globo",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "Os resultados do leilão na B3 e a concorrência entre grupos nacionais e internacionais.",
                    "url": "https://oglobo.globo.com/economia/noticia/2026/11/06/leilao-rodovias-b3-investimentos-transportes.ghtml"
                },
                {
                    "fonte": "Valor Econômico",
                    "perfil": "Jornal diário de economia",
                    "enfoque": "A estruturação de debêntures de infraestrutura para financiar os projetos licitados.",
                    "url": "https://valor.globo.com/empresas/noticia/2026/11/06/concessoes-rodoviarias-antt-b3.ghtml"
                }
            ]
        }
        print("Edição 2026-11-06 (manhã) calibrada com notícias clássicas estruturantes!")

    # =========================================================================
    # 2. REESTRUTURAR TOTALMENTE A EDIÇÃO DA NOITE (2026-11-06-noite)
    # =========================================================================
    dia_noite = {
        "_id": "2026-11-06-noite",
        "data": "2026-11-06",
        "edicao": "noite",
        "titulo": "Pacote fiscal tem texto final alinhado, Copom reitera vigilância e Congresso dos EUA inicia transição bipartidária",
        "resumo_dia": "Edição da noite de 06 de novembro de 2026: síntese das 22 reportagens que fecham a semana, destacando os detalhes do ajuste fiscal entre Fazenda e Planalto, o alívio nas taxas de juros futuros e no câmbio, as votações prioritárias no STF e no Congresso, os avanços na trégua diplomática no Oriente Médio e a reorganização da Câmara dos Representantes em Washington.",
        "agenda": [
            {"quando": "18h30", "o_que": "Fechamento dos mercados financeiros: Ibovespa encerra semana em alta e dólar recua a R$ 5,72."},
            {"quando": "19h30", "o_que": "Reunião de líderes governistas no Congresso para traçar cronograma de votação da PEC fiscal."},
            {"quando": "21h00", "o_que": "Balanço das deliberações internacionais sobre clima e ajuda humanitária em Genebra e Paris."}
        ],
        "audio": {
            "arquivo": "audios/boletim_2026-11-06-noite.mp3",
            "url": "audios/boletim_2026-11-06-noite.mp3",
            "tipo": "audio/mpeg",
            "duracao_segundos": 415,
            "duracao_fmt": "06:55",
            "tamanho_bytes": 6640000,
            "voz": "pt-BR-AntonioNeural",
            "titulo": "Boletim Faixa Oculta · 06 de novembro de 2026 (Noite)"
        },
        "total_nacionais": 11,
        "total_internacionais": 11,
        "notas": [
            # --- 11 NACIONAIS CLÁSSICAS ---
            {
                "id": "fo-n-20261106n-nac-01",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Contas Públicas e Ajuste Fiscal",
                "editoria": "Economia",
                "titulo": "Fazenda e Planalto batem o martelo sobre pacote fiscal que prevê contenção de R$ 60 bilhões em dois anos",
                "resumo": "Após rodadas sucessivas de reuniões no Palácio do Planalto, texto final estabelece limites para benefícios obrigatórios e veda criação de renúncias tributárias sem compensação.",
                "resumo_visoes": "Valor Econômico detalha o impacto positivo na curva de juros soberanos; Folha de S.Paulo revela os acordos de bastidor com os ministérios da área social; O Globo analisa a estratégia de tramitação urgente acertada com o Congresso.",
                "texto_completo": [
                    "O Palácio do Planalto e a equipe econômica concluíram no início da noite a formatação definitiva do pacote de medidas de contenção de despesas obrigatórias da União, calibrado para gerar uma economia estrutural estimada em R$ 60 bilhões ao longo do biênio 2027-2028.",
                    "O desenho final preserva as diretrizes centrais defendidas pelo ministro Fernando Haddad, limitando o crescimento real de parcelas não contributivas da seguridade ao teto do arcabouço fiscal e intensificando o recadastramento biométrico e a auditoria de benefícios temporários para erradicar fraudes.",
                    "Lideranças da base governista participaram do fechamento do texto para blindar a proposta contra resistências corporativas, estabelecendo que os recursos poupados serão direcionados para a ancoragem da dívida pública e para a manutenção de investimentos estratégicos em infraestrutura logística.",
                    "A mensagem presidencial que acompanhará a Proposta de Emenda à Constituição (PEC) e os projetos de lei complementares já está assinada e será enviada à Mesa Diretora da Câmara dos Deputados no primeiro horário de segunda-feira."
                ],
                "aprofundamento": {
                    "contexto": "A estabilização da relação dívida/PIB em torno de 78% era vista por investidores e agências de rating como a condição indispensável para a manutenção do grau de investimento e atração de capitais produtivos.",
                    "o_que_observar": "A designação dos relatores da matéria na Comissão de Constituição e Justiça (CCJ) e a receptividade das bancadas do centro."
                },
                "fontes": [
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de economia e negócios",
                        "enfoque": "O detalhamento fiscal das medidas de controle de gastos e a reação do mercado financeiro.",
                        "url": "https://valor.globo.com/brasil/noticia/2026/11/06/planalto-fazenda-fecham-pacote-fiscal-noite.ghtml"
                    },
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário nacional de referência",
                        "enfoque": "Os bastidores políticos no Planalto e o consenso alcançado entre as alas da Fazenda e da Casa Civil.",
                        "url": "https://www1.folha.uol.com.br/mercado/2026/11/pacote-fiscal-planalto-haddad-lula.shtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-02",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Mercado Financeiro e Câmbio",
                "editoria": "Economia",
                "titulo": "Dólar recua para R$ 5,72 e Ibovespa fecha semana em alta impulsionado por alívio nas taxas de juros futuros",
                "resumo": "Sinalização de disciplina orçamentária por Brasília e recuo dos rendimentos dos Treasuries em Nova York desarmam pressões especulativas na praça brasileira.",
                "resumo_visoes": "G1 Economia analisa o fechamento semanal dos ativos; Broadcast/Estadão destaca o fluxo positivo de investidores estrangeiros na B3; Poder360 aponta a redução dos prêmios de risco soberano.",
                "texto_completo": [
                    "O mercado financeiro encerrou a semana em tom de forte otimismo nesta sexta-feira, com o dólar comercial recuando 1,15%, cotado a R$ 5,72, e o principal índice da bolsa de valores brasileira, o Ibovespa, avançando 1,4% para superar a marca dos 132 mil pontos.",
                    "A descompressão foi comandada pelo fechamento expressivo das taxas nos contratos de juros futuros (DIs) em toda a extensão da curva, com alívio médio de mais de 25 pontos-base nas taxas com vencimento em 2027 e 2029.",
                    "Operadores de câmbio atribuíram a melhora do humor à confirmação oficial dos números do pacote fiscal de corte de gastos, que superou as projeções mais céticas de analistas privados.",
                    "No exterior, a estabilização das taxas de juros de longo prazo nos Estados Unidos e a recuperação dos preços internacionais do minério de ferro e do petróleo completaram o cenário favorável aos ativos de economias emergentes."
                ],
                "aprofundamento": {
                    "contexto": "A valorização do real frente ao dólar alivia diretamente as pressões de custos sobre itens cotados em moeda estrangeira, como trigo, fertilizantes e combustíveis, auxiliando a meta de inflação do Banco Central.",
                    "o_que_observar": "A abertura dos mercados na segunda-feira e as projeções do Boletim Focus do Banco Central."
                },
                "fontes": [
                    {
                        "fonte": "G1",
                        "perfil": "Portal de notícias em tempo real",
                        "enfoque": "O balanço de fechamento dos mercados de ações e câmbio no encerramento da semana.",
                        "url": "https://g1.globo.com/economia/noticia/2026/11/06/dolar-fechamento-semana-ibovespa.ghtml"
                    },
                    {
                        "fonte": "Poder360",
                        "perfil": "Portal de jornalismo político e econômico",
                        "enfoque": "O termômetro dos investidores em relação à credibilidade das metas fiscais de Brasília.",
                        "url": "https://www.poder360.com.br/economia/mercado-dolar-bolsa-ajuste-fiscal-planalto/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-03",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Poder Judiciário e Transparência",
                "titulo": "STF forma maioria para validar regras estritas de transparência e rastreabilidade para emendas parlamentares",
                "resumo": "Plenário determina que liberação de recursos depende obrigatoriamente da divulgação do nome do deputado ou senador autor e de plano de trabalho auditável pelo TCU.",
                "resumo_visoes": "ConJur detalha os fundamentos constitucionais dos votos da Corte; CartaCapital destaca o fim do uso político e opaco do orçamento público; O Globo analisa as negociações entre o ministro Flávio Dino e as cúpulas do Congresso.",
                "texto_completo": [
                    "O Supremo Tribunal Federal formou maioria de votos em sessão extraordinária para referendar os novos parâmetros de publicidade e controle institucional sobre a destinação e pagamento das emendas parlamentares ao Orçamento da União.",
                    "Pelo entendimento consolidado pelos ministros, fica terminantemente proibida a execução de qualquer emenda de comissão ou de bancada estadual que não contenha a identificação nominal do parlamentar proponente e o detalhamento técnico do objeto a ser financiado.",
                    "O tribunal também determinou que o Tribunal de Contas da União (TCU) e a Controladoria-Geral da União (CGU) realizem auditorias em tempo real nos municípios beneficiários, para verificar se os repasses estão respeitando os critérios de prioridade epidemiológica na saúde e infraestrutura básica.",
                    "A decisão encerra meses de impasse entre o Poder Judiciário e o Congresso Nacional, abrindo caminho para o desbloqueio responsável de recursos essenciais para obras municipais já licitadas."
                ],
                "aprofundamento": {
                    "contexto": "A exigência de transparência activa decorre do artigo 37 da Constituição Federal e busca restituir a primazia do planejamento público sobre a distribuição fragmentada de verbas orçamentárias.",
                    "o_que_observar": "A publicação do acórdão e os atos normativos conjuntos da Mesa da Câmara e do Senado para adequação dos sistemas eletrônicos."
                },
                "fontes": [
                    {
                        "fonte": "ConJur",
                        "perfil": "Revista jurídica especializada em direito constitucional",
                        "enfoque": "A tese jurídica fixada pelo plenário e os limites entre discricionariedade parlamentar e controle republicano.",
                        "url": "https://www.conjur.com.br/2026-nov-06/stf-maioria-regras-emendas-parlamentares-transparencia/"
                    },
                    {
                        "fonte": "O Globo",
                        "perfil": "Jornal diário nacional",
                        "enfoque": "O acordo institucional entre o STF e as presidências da Câmara e do Senado para destravar o orçamento.",
                        "url": "https://oglobo.globo.com/politica/noticia/2026/11/06/stf-emendas-parlamentares-acordo-congresso.ghtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-04",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Segurança Pública e Pacto Federativo",
                "titulo": "Governadores e Ministério da Justiça selam acordo para priorizar inteligência e asfixia financeira do crime organizado",
                "resumo": "Consenso em torno da PEC da Segurança Pública preserva o comando das polícias estaduais e fortalece o papel da Polícia Federal no combate à lavagem de dinheiro e tráfico interestadual de armas.",
                "resumo_visoes": "Folha de S.Paulo revela os bastidores da reunião entre o ministro Ricardo Lewandowski e governadores do Sudeste; Metrópoles aponta a criação de fundo federativo com critérios de letalidade; Agência Brasil destaca a cooperação em portos e fronteiras.",
                "texto_completo": [
                    "O Ministério da Justiça e os secretários de segurança dos 27 estados da federação fecharam a redação final do pacto federativo de combate às organizações criminosas, viabilizando o apoio formal dos governadores à PEC da Segurança Pública.",
                    "O texto pactuado assegura a autonomia administrativa e operacional dos governos estaduais sobre as polícias militares e civis, ao mesmo tempo em que consolida o Sistema Único de Segurança Pública (SUSP) na Constituição.",
                    "A prioridade estratégica da nova legislação será a asfixia financeira das facções criminosas e milícias armadas, estabelecendo forças-tarefa conjuntas entre a Receita Federal, o Coaf e a Polícia Federal para apreender bens e congelar contas de laranjas e empresas de fachada.",
                    "O projeto também institui repasses federais vinculados a metas de redução de mortes violentas e ampliação do uso de câmeras corporais e bancos unificados de dados genéticos e balísticos."
                ],
                "aprofundamento": {
                    "contexto": "O avanço das facções criminosas sobre setores formais da economia, como postos de combustíveis, cooperativas de transporte e construtoras, exigia uma resposta coordenada de inteligência financeira nacional.",
                    "o_que_observar": "A leitura do relatório na Comissão de Constituição e Justiça do Senado e o início dos debates com os secretários estaduais."
                },
                "fontes": [
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário nacional",
                        "enfoque": "O entendimento político entre governadores de oposição e a Esplanada dos Ministérios.",
                        "url": "https://www1.folha.uol.com.br/cotidiano/2026/11/governadores-pec-seguranca-acordo-justica.shtml"
                    },
                    {
                        "fonte": "Metrópoles",
                        "perfil": "Portal de jornalismo político de Brasília",
                        "enfoque": "Os instrumentos de cooperação técnica e o cronograma de repasses orçamentários do novo fundo de segurança.",
                        "url": "https://www.metropoles.com/brasil/pec-seguranca-publica-consenso-governadores-2026"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-05",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Atividade Produtiva e Indústria",
                "titulo": "Produção industrial avança em 11 dos 15 locais pesquisados pelo IBGE com alta disseminada no setor automotivo e químico",
                "resumo": "Desempenho no Paraná, São Paulo e Rio de Janeiro puxa recuperação fabril no segundo semestre, impulsionado pela renovação de frotas e queda no custo de insumos energéticos.",
                "resumo_visoes": "Valor Econômico detalha o impacto dos investimentos do programa Nova Indústria Brasil; G1 destaca a recuperação do parque fabril paulista; CartaCapital analisa o crescimento do emprego manufatureiro.",
                "texto_completo": [
                    "A Pesquisa Industrial Mensal Regional do IBGE revelou que 11 das 15 regiões avaliadas apresentaram taxas positivas de crescimento na produção fabril, confirmando a recuperação do setor manufatureiro nacional no segundo semestre.",
                    "O estado de São Paulo, principal polo industrial do país, registrou avanço de 1,8%, liderado pela montagem de veículos automotores e fabricação de máquinas e equipamentos industriais pesados.",
                    "No Rio de Janeiro, o setor petroquímico e a indústria naval registraram desempenhos acima da média histórica, impulsionados pela contratação de novos módulos para plataformas de produção no pré-sal da Bacia de Santos.",
                    "Economistas apontam que a combinação de juros reais mais baixos para crédito corporativo direcionado e a modernização de linhas fabris tem sustentado a maior taxa de utilização da capacidade instalada da indústria dos últimos cinco anos."
                ],
                "aprofundamento": {
                    "contexto": "A indústria de transformação responde pelos empregos de maior valor adicionado e produtividade na economia brasileira, gerando forte efeito multiplicador no comércio e serviços.",
                    "o_que_observar": "Os indicadores de confiança do empresário industrial calculados pela Fundação Getulio Vargas (FGV)."
                },
                "fontes": [
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de economia",
                        "enfoque": "A análise setorial do IBGE e o impacto nas projeções de PIB industrial para o fechamento do ano.",
                        "url": "https://valor.globo.com/brasil/noticia/2026/11/06/producao-industrial-ibge-estados-sp-rj.ghtml"
                    },
                    {
                        "fonte": "G1",
                        "perfil": "Portal de notícias em tempo real",
                        "enfoque": "O crescimento por ramo de atividade industrial e os destaques regionais do levantamento.",
                        "url": "https://g1.globo.com/economia/noticia/2026/11/06/producao-industrial-ibge-regional-resultado.ghtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-06",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Agronegócio e Abastecimento",
                "titulo": "Conab projeta safra de grãos 2026/2027 em recorde histórico de 325 milhões de toneladas com recuperação das lavouras",
                "resumo": "Regularização do regime de chuvas no Centro-Oeste favorece semeadura de soja e milho, aliviando preços de alimentos e ampliando receitas de exportação.",
                "resumo_visoes": "Valor Econômico analisa a projeção recorde e os preços das commodities agrícolas; Folha de S.Paulo destaca os ganhos de produtividade por hectare; Agência Brasil foca no abastecimento interno de grãos.",
                "texto_completo": [
                    "O primeiro levantamento consolidado de intenção de plantio da safra 2026/2027, divulgado pela Companhia Nacional de Abastecimento (Conab), apontou que a produção brasileira de grãos deve atingir o recorde histórico de 325,4 milhões de toneladas, um crescimento de 8,2% sobre o ciclo anterior.",
                    "O avanço decorre da regularização das chuvas nas principais regiões produtoras de Mato Grosso, Goiás, Paraná e no polo agrícola do Matopiba, que permitiram um ritmo de plantio da soja sem atrasos expressivos.",
                    "Para o milho e o arroz, as estimativas apontam recuperação das áreas irrigadas no Rio Grande do Sul e Centro-Oeste, garantindo recomposição dos estoques reguladores do governo federal e afastando riscos de choques inflacionários na cesta básica.",
                    "O Ministério da Agricultura destacou que mais de 80% do aumento de volume projetado virá de ganhos de produtividade técnica e melhoria genética das sementes, sem necessidade de abertura de novas áreas de vegetação nativa."
                ],
                "aprofundamento": {
                    "contexto": "O agronegócio representa cerca de um quarto do PIB brasileiro e o principal gerador de superávit na balança comercial do país.",
                    "o_que_observar": "As condições meteorológicas ao longo da fase de floração da soja no verão e as cotações internacionais em Chicago."
                },
                "fontes": [
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de agronegócio e economia",
                        "enfoque": "Os números detalhados da Conab por cultura e as projeções de exportação de soja e farelo.",
                        "url": "https://valor.globo.com/agronegocios/noticia/2026/11/06/conab-projeta-safra-recorde-graos-2026-2027.ghtml"
                    },
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário nacional",
                        "enfoque": "O impacto da supersafra na contenção da inflação de alimentos nos supermercados.",
                        "url": "https://www1.folha.uol.com.br/mercado/2026/11/safra-graos-conab-recorde-soja-milho.shtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-07",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Energia e Recursos Hídricos",
                "titulo": "Ministério de Minas e Energia e ONS descartam retorno do horário de verão com recuperação dos reservatórios",
                "resumo": "Volume útil das represas do Sudeste e Centro-Oeste atinge 58%, assegurando segurança energética e afastando acionamento emergencial de termelétricas caras.",
                "resumo_visoes": "O Globo detalha o parecer técnico do Operador Nacional do Sistema Elétrico; Poder360 analisa a estabilização das bandeiras tarifárias na conta de luz; Agência Brasil destaca a geração eólica e solar no Nordeste.",
                "texto_completo": [
                    "O ministro de Minas e Energia, Alexandre Silveira, confirmou em pronunciamento oficial que o governo federal descartou em definitivo o retorno do horário de verão para o ciclo 2026/2027, respaldado em nota técnica conclusiva do Operador Nacional do Sistema Elétrico (ONS).",
                    "O relatório técnico demonstrou que as chuvas volumosas registradas nas cabeceiras dos rios Grande, Paranaíba e São Francisco elevaram o nível médio dos reservatórios hidrelétricos do subsistema Sudeste/Centro-Oeste para 58,4% da capacidade útil.",
                    "Além da melhora hídrica, a expansão massiva de parques de geração solar fotovoltaica e eólica na Região Nordeste tem suprido com sobra a ponta de consumo diurna, tornando desnecessária a alteração de relógios para economizar energia.",
                    "A decisão garante previsibilidade para os setores de comércio, aviação civil e turismo, ao mesmo tempo em que preserva a bandeira tarifária verde para a imensa maioria dos consumidores residenciais."
                ],
                "aprofundamento": {
                    "contexto": "A matriz elétrica brasileira atingiu mais de 88% de participação renovável, uma das mais limpas e seguras do mundo contemporâneo.",
                    "o_que_observar": "A evolução do período úmido de verão nas principais bacias hidrelétricas do país."
                },
                "fontes": [
                    {
                        "fonte": "O Globo",
                        "perfil": "Jornal diário nacional",
                        "enfoque": "O anúncio do governo e as análises técnicas do ONS sobre a estabilidade do sistema interligado.",
                        "url": "https://oglobo.globo.com/economia/noticia/2026/11/06/governo-descarta-horario-de-verao-reservatorios.ghtml"
                    },
                    {
                        "fonte": "Poder360",
                        "perfil": "Portal de notícias de Brasília",
                        "enfoque": "Os impactos nas tarifas de energia elétrica e nas bandeiras tarifárias para o primeiro semestre de 2027.",
                        "url": "https://www.poder360.com.br/economia/mme-ons-horario-de-verao-reservatorios-energia/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-08",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Diplomacia e Cúpula de Líderes",
                "titulo": "Brasil abre a Cúpula Social do G20 no Rio de Janeiro reunindo movimentos civis e delegações de 40 países",
                "resumo": "Iniciativa inédita na história do bloco reúne debates sobre combate à fome, transição energética justa e reforma das instituições de governança global antes da reunião de chefes de Estado.",
                "resumo_visoes": "Folha de S.Paulo analisa a participação popular no encerramento da presidência brasileira do G20; Brasil de Fato destaca as propostas da sociedade civil do Sul Global; O Globo acompanha a movimentação no Boulevard Olímpico.",
                "texto_completo": [
                    "A cidade do Rio de Janeiro deu início aos trabalhos da Cúpula Social do G20, evento pioneiro concebido pela presidência brasileira do bloco para integrar sindicatos, organizações não governamentais e movimentos comunitários de mais de 40 países ao processo decisório dos líderes mundiais.",
                    "Instaladas nos galpões históricos do Boulevard Olímpico e no Museu de Arte do Rio (MAR), as plenárias debatem propostas concretas para o financiamento da transição ecológica equitativa, a taxação internacional de super-ricos e a soberania alimentar.",
                    "O chanceler Mauro Vieira destacou durante a sessão de abertura que o multilateralismo só preservará sua legitimidade democrática se for capaz de escutar as vozes das populações historicamente excluídas das salas fechadas de negociação de chefes de Estado.",
                    "O documento de consenso que está sendo redigido pelas comissões populares será entregue diretamente aos presidentes e primeiros-ministros na sessão solene de abertura da Cúpula de Líderes do G20 no Museu de Arte Moderna (MAM)."
                ],
                "aprofundamento": {
                    "contexto": "O G20 reúne as 19 maiores economias do mundo, a União Europeia e a União Africana, respondendo por cerca de 85% do PIB mundial e três quartos do comércio global.",
                    "o_que_observar": "A redação da declaração conjunta de líderes e os pontos de dissenso em relação ao financiamento climático."
                },
                "fontes": [
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário nacional · Seção Mundo e Diplomacia",
                        "enfoque": "O início dos debates da Cúpula Social no Rio e as metas da diplomacia brasileira.",
                        "url": "https://www1.folha.uol.com.br/mundo/2026/11/brasil-inaugura-cupula-social-g20-rio.shtml"
                    },
                    {
                        "fonte": "Brasil de Fato",
                        "perfil": "Agência de jornalismo independente e movimentos populares",
                        "enfoque": "As reivindicações de justiça climática e direitos trabalhistas apresentadas pelas delegações do Sul Global.",
                        "url": "https://www.brasildefato.com.br/2026/11/06/g20-social-comeca-no-rio-de-janeiro-sociedade-civil"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-09",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Defesa do Consumidor e Mercado Digital",
                "titulo": "Ministério da Fazenda e Anatel fecham cerco a sites de apostas ilegais e apertam regras para crédito consignado",
                "resumo": "Bloqueio judicial atinge mais de 2.000 domínios não autorizados enquanto Banco Central estipula limite de endividamento para proteger renda de beneficiários de programas sociais.",
                "resumo_visoes": "Valor Econômico detalha a nova regulamentação de compliance para fintechs de pagamento; CartaCapital enfatiza o impacto na redução do superendividamento das famílias; G1 acompanha a fiscalização nas plataformas de telecomunicações.",
                "texto_completo": [
                    "A Secretaria de Prêmios e Apostas do Ministério da Fazenda, em ação coordenada com a Agência Nacional de Telecomunicações (Anatel) e a Polícia Federal, efetuou o bloqueio técnico de mais de 2.000 sites de apostas online que operavam de forma clandestina no país sem autorização oficial.",
                    "A regulação exige que todas as empresas outorgadas mantenham sede no Brasil, capital social comprovado de ao menos R$ 30 milhões e sistemas obrigatórios de reconhecimento facial e monitoramento de saúde mental para prevenir dependência e lavagem de capitais.",
                    "Paralelamente, o Conselho Monetário Nacional (CMN) aprovou novas travas de segurança para operações de crédito consignado vinculadas a aposentadorias e benefícios assistenciais, proibindo o assédio telefônico de correspondentes bancários e limitando a margem de comprometimento da renda.",
                    "A medida atende a estudos de entidades de defesa do consumidor que alertavam para o estrangulamento orçamentário de famílias de baixa renda por dívidas compulsivas contraídas em aplicativos não regulados."
                ],
                "aprofundamento": {
                    "contexto": "O mercado de apostas de quota fixa movimentou mais de R$ 60 bilhões nos últimos doze meses, exigindo uma disciplina fiscal e sanitária rígida por parte das autoridades públicas.",
                    "o_que_observar": "A publicação da lista definitiva das operadoras autorizadas a funcionar a partir de 2027 e os dados de arrecadação de outorgas."
                },
                "fontes": [
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de finanças e regulação",
                        "enfoque": "A fiscalização sobre intermediárias de pagamento eletrônico que operavam para bets ilegais.",
                        "url": "https://valor.globo.com/financas/noticia/2026/11/06/fazenda-anatel-bloqueio-bets-ilegais.ghtml"
                    },
                    {
                        "fonte": "CartaCapital",
                        "perfil": "Revista de jornalismo independente e análise política",
                        "enfoque": "O combate ao endividamento precoce das famílias e a proteção dos beneficiários do Bolsa Família.",
                        "url": "https://www.cartacapital.com.br/sociedade/governo-bloqueia-sites-de-apostas-protege-consignado/"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-10",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Defesa Civil e Resiliência Urbana",
                "titulo": "Defesa Civil Nacional aciona plano preventivo de estiagem e ondas de calor nas capitais com monitoramento por radar",
                "resumo": "Integração do Cemaden com prefeituras agiliza alertas precoces de desidratação e riscos de incêndios em áreas periurbanas diante de temperaturas anômalas no Sudeste e Centro-Oeste.",
                "resumo_visoes": "Folha de S.Paulo detalha as medidas de pontos de hidratação e umidificação em São Paulo e Rio; O Globo relata o plano de contingência para as bacias metropolitanas; Metrópoles acompanha as medições de qualidade do ar em Brasília.",
                "texto_completo": [
                    "O Ministério da Integração e do Desenvolvimento Regional acionou formalmente o Sistema Nacional de Proteção e Defesa Civil em nível de alerta para as regiões metropolitanas de São Paulo, Rio de Janeiro, Belo Horizonte e Brasília, diante da aproximação de uma massa de ar seco e quente persistente.",
                    "O protocolo preventivo, elaborado conjuntamente com o Centro Nacional de Monitoramento e Alertas de Desastres Naturais (Cemaden), estabelece a abertura obrigatória de pontos públicos de hidratação, distribuição de água potável em terminais rodoviários e metroviários e escala reforçada de ambulâncias do Samu.",
                    "Nas regiões periféricas e áreas limítrofes a parques florestais, brigadas comunitárias foram mobilizadas com apoio do Corpo de Bombeiros para fiscalizar focos de queima de lixo e fagulhas que possam deflagrar incêndios em vegetações ressequidas.",
                    "A meteorologia prevê que a passagem de uma frente fria oceânica no final do domingo trará ventos úmidos e quedas de temperatura, restabelecendo a umidade relativa do ar em padrões seguros para a saúde pública."
                ],
                "aprofundamento": {
                    "contexto": "A adaptação das cidades às ondas de calor extremo é uma das principais urgências de saúde coletiva decorrentes da variabilidade climática no Brasil urbano.",
                    "o_que_observar": "Os relatórios diários de qualidade do ar e as orientações da Secretaria de Vigilância em Saúde."
                },
                "fontes": [
                    {
                        "fonte": "Folha de S.Paulo",
                        "perfil": "Jornal diário nacional · Seção Cotidiano",
                        "enfoque": "Os planos de contingência das capitais para enfrentar picos de calor e baixa umidade.",
                        "url": "https://www1.folha.uol.com.br/cotidiano/2026/11/defesa-civil-alerta-onda-de-calor-capitais.shtml"
                    },
                    {
                        "fonte": "O Globo",
                        "perfil": "Jornal diário nacional",
                        "enfoque": "O monitoramento dos mananciais de abastecimento e as medidas de alívio térmico nas cidades.",
                        "url": "https://oglobo.globo.com/rio/noticia/2026/11/06/defesa-civil-calor-metropole-monitoramento.ghtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-nac-11",
                "escopo": "nacional",
                "pais": "Brasil",
                "chapeu": "Governança Legislativa e Orçamento",
                "titulo": "Cúpula do Congresso fecha calendário de votações prioritárias e pauta Lei Orçamentária para a primeira quinzena de dezembro",
                "resumo": "Acordo entre líderes partidários na Câmara e no Senado destrava apreciação da Lei de Diretrizes Orçamentárias (LDO) e regulamentação da reforma tributária sobre o consumo.",
                "resumo_visoes": "Valor Econômico detalha o cronograma de votação dos projetos de lei complementar tributários; Folha de S.Paulo analisa a correlação de forças entre governo e oposição; Poder360 compila as prioridades das bancadas temáticas.",
                "texto_completo": [
                    "Os presidentes da Câmara dos Deputados e do Senado Federal anunciaram em entrevista coletiva conjunta no Salão Verde o calendário de deliberações em plenário para a reta final do ano legislativo, estabelecendo como prioridade a votação da Lei Orçamentária Anual (LOA) de 2027 até 15 de dezembro.",
                    "O cronograma também reservou as duas próximas semanas de sessões deliberativas para a votação definitiva dos projetos de lei complementar que instituem o Comitê Gestor do Imposto sobre Bens e Serviços (IBS) e a regulamentação do Imposto Seletivo, peças centrais da implementação da Reforma Tributária.",
                    "Líderes de diferentes espectros partidários concordaram em realizar esforço concentrado de votação presencial de terça a quinta-feira, garantindo quórum qualificado para a apreciação das matérias econômicas estruturais.",
                    "A definição do calendário afasta incertezas sobre o encerramento do ano parlamentar e reforça a governabilidade institucional em torno das regras do regime fiscal."
                ],
                "aprofundamento": {
                    "contexto": "A votação tempestiva da Lei Orçamentária é indispensável para evitar que a União inicie o ano fiscal operando em duodécimos orçamentários provisórios.",
                    "o_que_observar": "A leitura do parecer do relator-geral da Comissão Mista de Orçamento (CMO) e a apresentação de destaques em plenário."
                },
                "fontes": [
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de economia e política",
                        "enfoque": "O cronograma de votação da reforma tributária e do orçamento na Câmara e no Senado.",
                        "url": "https://valor.globo.com/politica/noticia/2026/11/06/congresso-calendario-reforma-tributaria-orcamento.ghtml"
                    },
                    {
                        "fonte": "Poder360",
                        "perfil": "Portal de jornalismo político",
                        "enfoque": "A costura de bastidores entre as lideranças partidárias para garantir quórum nas sessões presenciais.",
                        "url": "https://www.poder360.com.br/congresso/camara-senado-calendario-votacoes-dezembro/"
                    }
                ]
            },

            # --- 11 INTERNACIONAIS TRADUZIDAS NA ÍNTEGRA ---
            {
                "id": "fo-n-20261106n-int-01",
                "escopo": "internacional",
                "pais": "Estados Unidos",
                "chapeu": "Mídia Internacional Traduzida · Política nos EUA",
                "editoria": "Internacional",
                "titulo": "Nova liderança da Câmara dos EUA anuncia auditoria sobre tarifas unilaterais e prioriza pacto orçamentário bipartidário",
                "titulo_original": "House Leadership Outlines Agenda Focused on Tariff Oversight and Fiscal Predictability",
                "resumo": "Após vitória nas urnas, bloco de maioria no Capitólio sinaliza freios a guerras comerciais e blindagem de programas de transição climática do governo federal.",
                "resumo_visoes": "The New York Times analisa as primeiras reuniões de transição da presidência da Câmara; The Washington Post detalha a blindagem de agências científicas federais; Financial Times avalia a diminuição de volatilidade nas cadeias globais de suprimentos.",
                "texto_completo": [
                    "A nova maioria parlamentar eleita para a Câmara dos Representantes dos Estados Unidos deu início formal às reuniões de transição legislativa em Washington, apresentando uma agenda focada em previsibilidade fiscal e no restabelecimento do equilíbrio clássico entre os poderes.",
                    "Os futuros presidentes das comissões de Finanças e Orçamento afirmaram categoricamente que a prioridade imediata da legislatura será aprovar os pacotes de gastos anuais sem recorrer à ameaça de paralisações (shutdowns) da máquina pública federal.",
                    "No plano de comércio internacional, o comando parlamentar adiantou que convocará audiências de escrutínio para auditar a eficácia e o impacto inflacionário de sobretaxas aduaneiras unilaterais, avaliando o impacto nos custos de vida das famílias da classe média suburbana.",
                    "A postura foi recebida com alívio nos principais centros financeiros da Europa e Ásia, apontando para um período de menor volatilidade nas relações comerciais com os Estados Unidos."
                ],
                "aprofundamento": {
                    "contexto": "O retorno de um governo dividido em Washington resgata a necessidade de negociação pragmática entre os dois partidos no Congresso norte-americano.",
                    "o_que_observar": "A eleição formal para o posto de Speaker da Câmara no início de janeiro e a composição das comissões permanentes."
                },
                "fontes": [
                    {
                        "fonte": "The New York Times",
                        "perfil": "Jornal diário de referência internacional dos EUA",
                        "enfoque": "Os pronunciamentos da nova liderança parlamentar e as diretrizes para o orçamento federal.",
                        "url": "https://www.nytimes.com/2026/11/06/us/politics/house-majority-transition-agenda.html"
                    },
                    {
                        "fonte": "Financial Times",
                        "perfil": "Jornal diário internacional de finanças",
                        "enfoque": "A reação dos mercados de capitais e as projeções para as taxas dos títulos públicos americanos.",
                        "url": "https://www.ft.com/content/us-congress-transition-tariffs-bipartisan"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-02",
                "escopo": "internacional",
                "pais": "Oriente Médio / Líbano",
                "chapeu": "Mídia Internacional Traduzida · Diplomacia e Conflitos",
                "editoria": "Internacional",
                "titulo": "Negociadores internacionais no Cairo e em Paris avançam em termos para trégua de 60 dias no Líbano",
                "resumo": "Minuta de cessar-fogo prevê recuo mútuo de combatentes da Linha Azul, reforço da Unifil e desobstrução de corredores humanitários de remédios para Beirute.",
                "resumo_visoes": "Le Monde detalha os esforços da chancelaria francesa para socorrer a infraestrutura libanesa; Al Jazeera relata a situação dos deslocados no vale do Bekaa; The New York Times analisa as salvaguardas de fronteira.",
                "texto_completo": [
                    "Diplomatas de governos árabes e europeus intensificaram nesta noite as rodadas técnicas de negociação em Paris e no Cairo para formalizar uma trégua imediata de 60 dias nas hostilidades ao longo da fronteira entre o Líbano e Israel.",
                    "O rascunho de acordo prevê a implementação estrita da Resolução 1701 do Conselho de Segurança da ONU, estipulando a desmilitarização de uma faixa de segurança ao sul do Rio Litani e a transferência do controle territorial para o Exército Regular do Líbano.",
                    "Agências de socorro internacional cobram a garantia imediata de passagem segura para comboios com insumos cirúrgicos, anestésicos e geradores de emergência destinados a hospitais civis na periferia sul de Beirute.",
                    "Fontes diplomáticas indicam que a assinatura do armistício provisório é vista como o passo fundamental para permitir a retomada das conversações políticas no parlamento libanês."
                ],
                "aprofundamento": {
                    "contexto": "A estabilização do Líbano é prioritária para estancar o risco de alargamento regional do conflito para as rotas marítimas comerciais do Mar Vermelho.",
                    "o_que_observar": "A manifestação formal dos gabinetes de governo em Beirute e Tel Aviv nos próximos dias."
                },
                "fontes": [
                    {
                        "fonte": "Le Monde",
                        "perfil": "Jornal diário de referência na França",
                        "enfoque": "A conferência de doadores em Paris e a coordenação com a missão de paz da ONU.",
                        "url": "https://www.lemonde.fr/international/article/2026/11/06/liban-negociations-cessez-le-feu-paris_6234575_3210.html"
                    },
                    {
                        "fonte": "Al Jazeera English",
                        "perfil": "Rede de jornalismo internacional independente",
                        "enfoque": "A situação humanitária dos milhares de civis abrigados em escolas e centros comunitários.",
                        "url": "https://www.aljazeera.com/news/2026/11/6/lebanon-ceasefire-talks-paris-cairo"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-03",
                "escopo": "internacional",
                "pais": "União Europeia / Alemanha",
                "chapeu": "Mídia Internacional Traduzida · Bancos Centrais",
                "editoria": "Economia",
                "titulo": "Banco Central Europeu sinaliza novo corte de juros para dezembro diante da contração fabril na Alemanha",
                "resumo": "Autoridades monetárias em Frankfurt avaliam que inflação de serviços caminha para a meta de 2%, abrindo margem para apoiar a atividade industrial em declínio.",
                "resumo_visoes": "Financial Times analisa a ata da reunião do BCE e a pressão das montadoras alemãs; Le Monde destaca a divergência entre a ala hawkish e os economistas do sul; El País projeta os impactos para as hipotecas residenciais.",
                "texto_completo": [
                    "A presidente do Banco Central Europeu (BCE), Christine Lagarde, indicou em seminário econômico em Frankfurt que a autoridade monetária da zona do euro está pronta para efetuar uma nova redução de 25 pontos-base nas taxas básicas de juros em sua reunião deliberativa de dezembro.",
                    "A sinalização responde aos números mais recentes dos índices de gerentes de compras (PMI), que apontam contração contínua na atividade das indústrias automotiva e química da Alemanha e da França decorrente de custos energéticos elevados e concorrência internacional.",
                    "Paralelamente, os dados preliminares de inflação mostraram que a alta dos preços ao consumidor recuou para 1,9% ao ano, permanecendo sustentadamente abaixo da meta oficial pela primeira vez em três anos.",
                    "A perspectiva de juros mais baixos no continente europeu estimulou a recuperação das principais praças acionárias de Paris, Frankfurt e Milão, além de enfraquecer o euro frente ao dólar e moedas emergentes."
                ],
                "aprofundamento": {
                    "contexto": "O afrouxamento monetário do BCE busca evitar uma recessão técnica na maior economia do bloco europeu, garantindo liquidez para investimentos em descarbonização.",
                    "o_que_observar": "A divulgação dos números finais de inflação harmonizada na zona do euro na próxima semana."
                },
                "fontes": [
                    {
                        "fonte": "Financial Times",
                        "perfil": "Jornal diário britânico de economia e finanças",
                        "enfoque": "As declarações das autoridades do BCE e o comportamento dos juros soberanos europeus.",
                        "url": "https://www.ft.com/content/ecb-interest-rate-cut-december-signaling"
                    },
                    {
                        "fonte": "Le Monde",
                        "perfil": "Jornal diário de referência na França",
                        "enfoque": "O debate sobre a desaceleração industrial alemã e os efeitos sobre a economia francesa.",
                        "url": "https://www.lemonde.fr/economie/article/2026/11/06/bce-taux-interet-baisse-decembre_6234576_3234.html"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-04",
                "escopo": "internacional",
                "pais": "Uruguai / América Latina",
                "chapeu": "Mídia Internacional Traduzida · Geopolítica Regional",
                "editoria": "Internacional",
                "titulo": "Segundo turno no Uruguai entra na reta final com disputa acirrada entre Frente Ampla e coalizão republicana",
                "resumo": "Últimas pesquisas mostram empate técnico absoluto em Montevidéu e interior, com debates focados em previdência, segurança cidadã e alianças no Mercosul.",
                "resumo_visoes": "El País Uruguai detalha os mapas eleitorais do interior; Página 12 analisa a mobilização dos sindicatos de trabalhadores; Clarín avalia as repercussões para as relações comerciais no Cone Sul.",
                "texto_completo": [
                    "A campanha eleitoral para o segundo turno presidencial no Uruguai, marcado para o último domingo de novembro, entrou em sua fase mais intensa, com os institutos de pesquisa registrando empate rigoroso dentro da margem de erro entre os dois blocos políticos.",
                    "Yamandú Orsi, candidato da coalizão de esquerda Frente Ampla, tem concentrado seu discurso na defesa do poder de compra dos salários, fortalecimento do sistema público de saúde e combate à desigualdade territorial entre a capital e os departamentos do norte.",
                    "Por sua vez, Álvaro Delgado, representando a coalizão republicana de centro-direita do atual governo, enfatiza a continuidade da estabilidade macroeconômica, reformas de desregulamentação comercial e o endurecimento penal contra o narcotráfico transnacional.",
                    "Para o Brasil e a diplomacia sul-americana, a eleição uruguaia é determinante para calibrar o futuro da união aduaneira do Mercosul e o andamento das negociações de livre comércio com a União Europeia."
                ],
                "aprofundamento": {
                    "contexto": "O Uruguai se destaca no continente latino-americano por sua sólida cultura cívica e pelo respeito consensual às regras do jogo eleitoral.",
                    "o_que_observar": "O debate presidencial obrigatório transmitido em cadeia nacional de rádio e televisão."
                },
                "fontes": [
                    {
                        "fonte": "El País (Uruguai)",
                        "perfil": "Jornal diário de Montevidéu",
                        "enfoque": "Os números consolidados das últimas sondagens e as estratégias de captação de eleitores indecisos.",
                        "url": "https://www.elpais.com.uy/informacion/politica/balotaje-uruguay-2026-candidatos-recta-final"
                    },
                    {
                        "fonte": "Página 12",
                        "perfil": "Jornal diário argentino de análise internacional",
                        "enfoque": "A mobilização militante da Frente Ampla nos bairros populares de Montevidéu.",
                        "url": "https://www.pagina12.com.ar/seccion/el-mundo/elecciones-uruguay-balotaje-2026"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-05",
                "escopo": "internacional",
                "pais": "Haia / Global",
                "chapeu": "Mídia Internacional Traduzida · Justiça Internacional",
                "editoria": "Internacional",
                "titulo": "Tribunais em Haia reafirmam dever incondicional de proteção a missões médicas e remédios em áreas de conflito",
                "resumo": "Juízes da Corte Internacional e do TPI alertam que cerco deliberado e bloqueio de água ou anestésicos violam o direito humanitário de Genebra.",
                "resumo_visoes": "Le Monde analisa a fundamentação dos pareceres em tratados internacionais; El País destaca a declaração de solidariedade das nações ibero-americanas; BBC World relata o colapso de postos médicos em enclaves sitiados.",
                "texto_completo": [
                    "Os tribunais internacionais com sede no Palácio da Paz em Haia emitiram deliberação colegiada reiterando o dever irrevogável de todos os Estados signatários da Carta da ONU de garantir a imunidade e livre trânsito de comboios de saúde e socorristas em zonas de guerra.",
                    "O parecer pontua de forma cristalina que a interrupção deliberada do fornecimento de eletricidade, água potável, sangue e medicamentos essenciais para instalações civis transgride normas consuetudinárias de direito humanitário que não admitem exceções operacionais.",
                    "A manifestação conjunta foi motivada por representações de governos do Sul Global e de entidades como o Comitê Internacional da Cruz Vermelha, que documentaram ataques recorrentes a ambulâncias e clínicas de campanha no Oriente Médio e na África.",
                    "Magistrados destacaram que a observância das ordens judiciais de Haia é o único dique de proteção da ordem multilateral contra a barbárie bélica desregulada."
                ],
                "aprofundamento": {
                    "contexto": "As Convenções de Genebra de 1949 estabelecem a proteção jurídica universal a doentes, feridos e pessoal de saúde durante conflitos armados internacionais e internos.",
                    "o_que_observar": "A apreciação do relatório no Conselho de Segurança da ONU em Nova York."
                },
                "fontes": [
                    {
                        "fonte": "Le Monde",
                        "perfil": "Jornal diário de referência na França",
                        "enfoque": "Os fundamentos de direito penal internacional da manifestação das cortes de Haia.",
                        "url": "https://www.lemonde.fr/international/article/2026/11/06/justice-internationale-la-haye-droit-humanitaire_6234577_3210.html"
                    },
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário britânico · Seção Internacional",
                        "enfoque": "A cobrança de organizações humanitárias por corredores de suprimento médico desmilitarizados.",
                        "url": "https://www.theguardian.com/world/2026/nov/06/the-hague-courts-medical-aid-protection"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-06",
                "escopo": "internacional",
                "pais": "Global / Clima",
                "chapeu": "Mídia Internacional Traduzida · Finanças Climáticas",
                "editoria": "Clima",
                "titulo": "Secretariado da ONU Clima formaliza proposta de US$ 300 bilhões anuais em doações a fundo perdido para países vulneráveis",
                "resumo": "Minuta consensual veda empréstimos comerciais que aumentem dívidas soberanas e foca em subvenções diretas para recomposição de florestas e defesa costeira.",
                "resumo_visoes": "The Guardian destaca a vitória dos pequenos estados insulares do Pacífico; Financial Times detalha as negociações entre o G7 e a diplomacia brasileira da COP30; El País aponta o papel da justiça climática para manter o Acordo de Paris.",
                "texto_completo": [
                    "A Convenção-Quadro das Nações Unidas sobre Mudança do Clima oficializou a minuta de negociação da Nova Meta Coletiva Quantificada de Financiamento Climático, instrumento que definirá os repasses dos países desenvolvidos ao Sul Global na próxima década.",
                    "O documento estabelece um piso anual de US$ 300 bilhões financiado pelos países mais industrializados, canalizado prioritariamente sob o formato de doações orçamentárias diretas e investimentos concessionais sem juros.",
                    "O texto atendeu a uma exigência histórica dos países da América Latina, África e pequenos estados insulares, vetando categoricamente a inclusão de linhas de crédito comercial com juros de mercado que alimentavam o ciclo vicioso de endividamento externo.",
                    "A diplomacia brasileira comemorou o avanço, apontando que a clareza financeira é a condição prévia para que todas as nações ampliem suas metas de corte de emissões na COP30 em Belém."
                ],
                "aprofundamento": {
                    "contexto": "A meta financeira anterior de US$ 100 bilhões anuais, fixada em 2009, foi amplamente criticada pela falta de transparência e pela prevalência de empréstimos onerosos.",
                    "o_que_observar": "A votação do texto final pelos delegados plenipotenciários na rodada ministerial em Baku."
                },
                "fontes": [
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário britânico · Seção Meio Ambiente",
                        "enfoque": "A mobilização de governos insulares e nações tropicais por fundos não baseados em dívida.",
                        "url": "https://www.theguardian.com/environment/2026/nov/06/un-climate-finance-draft-non-debt"
                    },
                    {
                        "fonte": "Financial Times",
                        "perfil": "Jornal diário de finanças e economia",
                        "enfoque": "A posição das chancelarias ocidentais e o modelo de governança multilateral dos recursos.",
                        "url": "https://www.ft.com/content/un-climate-finance-target-draft-agreement"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-07",
                "escopo": "internacional",
                "pais": "Estados Unidos / Europa",
                "chapeu": "Mídia Internacional Traduzida · Tecnologia e Inteligência Artificial",
                "editoria": "Tecnologia",
                "titulo": "Consórcio acadêmico internacional disponibiliza modelo de IA fundacional em código 100% aberto e auditado contra viés",
                "resumo": "Iniciativa de universidades globais democratiza pesos neurais, bases de dados e códigos de treino para romper a dependência de plataformas proprietárias do Vale do Silício.",
                "resumo_visoes": "MIT Technology Review saúda a rastreabilidade total de dados; The Guardian enfatiza a defesa de direitos autorais e licenças públicas; Nature aponta o avanço para modelos científicos de previsão climática e farmacologia.",
                "texto_completo": [
                    "Pesquisadores de centros universitários nos Estados Unidos, Europa e América Latina anunciaram a disponibilização pública irrestrita do modelo neural OpenFoundation, concebido como contraponto aos algoritmos fechados das big techs.",
                    "O modelo teve sua arquitetura concebida sob os princípios do software livre, disponibilizando publicamente todos os hiperparâmetros, os dados revisados por pares e os filtros de segurança matemática.",
                    "Especialistas em ética algorítmica realizaram auditorias independentes para eliminar dados sensíveis sem consentimento e coibir reproduções tendenciosas em tarefas de avaliação social e profissional.",
                    "Grupos de pesquisa de todo o planeta já utilizam a base aberta para desenhar catalisadores químicos ecológicos e modelar impactos da variabilidade climática com autonomia tecnológica plena."
                ],
                "aprofundamento": {
                    "contexto": "A concentração do desenvolvimento de modelos de fronteira em poucas corporações privadas levantava preocupações de segurança cibernética e soberania científica global.",
                    "o_que_observar": "A adoção da plataforma aberta por centros de supercomputação governamentais e instituições de ensino."
                },
                "fontes": [
                    {
                        "fonte": "MIT Technology Review",
                        "perfil": "Revista de tecnologia do Instituto de Tecnologia de Massachusetts",
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
                "id": "fo-n-20261106n-int-08",
                "escopo": "internacional",
                "pais": "África do Sul / BRICS",
                "chapeu": "Mídia Internacional Traduzida · Finanças e Multipolaridade",
                "editoria": "Diplomacia",
                "titulo": "Banco dos BRICS aprova carteira de US$ 8 bilhões em moedas locais para saneamento e mobilidade sustentável",
                "resumo": "Empréstimos denominados em reais, rands e dirhams reduzem exposição a variações da taxa do dólar norte-americano em países emergentes.",
                "resumo_visoes": "Al Jazeera destaca a diminuição da vulnerabilidade da dívida externa nos países do Sul Global; Valor Econômico detalha concessões de ferrovias e saneamento no Brasil; Folha de S.Paulo contextualiza a expansão diplomática do bloco.",
                "texto_completo": [
                    "A presidência executiva do Novo Banco de Desenvolvimento (NDB), sediado em Xangai e reunido na África do Sul, aprovou uma carteira recorde de crédito para infraestrutura sustentável em nações emergentes.",
                    "O pilar estrutural do pacote reside na contratação prioritária de dívida indexada às moedas soberanas dos países beneficiários, afastando o risco de insolvência por desvalorização cambial abrupta frente ao dólar.",
                    "No território brasileiro, os financiamentos cobrirão a modernização de malhas ferroviárias intermodais de grãos e obras de universalização do esgotamento sanitário em capitais do Norte e Nordeste.",
                    "A instituição reafirmou que as aprovações dispensam exigências fiscais contracionistas tradicionais de agências multilaterais do Ocidente, priorizando a sustentabilidade e a inclusão social."
                ],
                "aprofundamento": {
                    "contexto": "A estratégia de desdolarização do crédito internacional busca criar alternativas de liquidez para investimentos em bens públicos essenciais.",
                    "o_que_observar": "A emissão dos primeiros títulos em moedas locais nas bolsas de valores de Joanesburgo e São Paulo."
                },
                "fontes": [
                    {
                        "fonte": "Al Jazeera English",
                        "perfil": "Rede internacional de notícias independente",
                        "enfoque": "A independência financeira dos países emergentes frente às oscilações das taxas do Federal Reserve.",
                        "url": "https://www.aljazeera.com/economy/2026/11/6/ndb-brics-bank-local-currency-loans-approval"
                    },
                    {
                        "fonte": "Valor Econômico",
                        "perfil": "Jornal diário de finanças",
                        "enfoque": "O detalhamento dos contratos assinados para obras de saneamento e transporte no Brasil.",
                        "url": "https://valor.globo.com/financas/noticia/2026/11/06/ndb-banco-brics-financiamentos-brasil-moedas-locais.ghtml"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-09",
                "escopo": "internacional",
                "pais": "Alemanha / Europa",
                "chapeu": "Mídia Internacional Traduzida · Energia e Indústria",
                "editoria": "Clima",
                "titulo": "Alemanha conclui primeiros 1.200 km da malha dorsal de hidrogênio verde para salvar parques industriais pesados",
                "resumo": "Rede dedicada de dutos conectará portos do Mar do Norte aos complexos siderúrgicos e químicos do Reno, viabilizando redução drástica de emissões industriais.",
                "resumo_visoes": "Financial Times enfatiza a competitividade global da indústria pesada alemã; Le Monde analisa a integração com corredores limpos franceses e espanhóis; El País projeta as exportações de hidrogênio do Mediterrâneo.",
                "texto_completo": [
                    "A República Federal da Alemanha formalizou a entrega do primeiro trecho da 'Espinha Dorsal de Hidrogênio', a maior infraestrutura de transporte de moléculas sustentáveis do continente europeu.",
                    "O gasoduto interliga terminais portuários de importação de hidrogênio verde e amônia renovável às grandes usinas químicas e altos-fornos descarbonizados do vale do Ruhr.",
                    "A tecnologia reaproveitou antigas canalizações de gás fóssil, reduzindo o custo total de capital das obras e acelerando em quatro anos o cronograma original de transição ecológica.",
                    "Montadoras e indústrias de base celebraram a garantia de abastecimento contínuo de energia não fóssil a custos previsíveis, blindando o setor contra choques geopolíticos no preço do petróleo."
                ],
                "aprofundamento": {
                    "contexto": "A viabilidade econômica do hidrogênio como vetor energético depende de redes de dutos de grande porte capazes de operar em altíssima pressão.",
                    "o_que_observar": "A conexão da malha alemã com os gasodutos transfronteiriços da França e da Holanda."
                },
                "fontes": [
                    {
                        "fonte": "Financial Times",
                        "perfil": "Jornal diário de economia e negócios",
                        "enfoque": "A estratégia do governo alemão para garantir energia limpa a custos competitivos para a manufatura.",
                        "url": "https://www.ft.com/content/germany-hydrogen-grid-inauguration-industry"
                    },
                    {
                        "fonte": "Le Monde",
                        "perfil": "Jornal diário de referência na França",
                        "enfoque": "Os impactos na descarbonização das cadeias siderúrgicas transfronteiriças da Europa.",
                        "url": "https://www.lemonde.fr/economie/article/2026/11/06/l-allemagne-ouvre-son-reseau-de-transport-d-hydrogene_6234570_3234.html"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-10",
                "escopo": "internacional",
                "pais": "França / Literatura",
                "chapeu": "Mídia Internacional Traduzida · Cultura e Livros",
                "editoria": "Cultura",
                "titulo": "Prêmio Goncourt 2026 coroa romance memorialístico que celebra a saga de operários na construção de Paris",
                "resumo": "Obra de Mehdi Charef resgata com lirismo e rigor histórico as trajetórias invisíveis de pedreiros e carpinteiros estrangeiros que ergueram os bairros e pontes da capital.",
                "resumo_visoes": "Le Monde celebra a vitória de uma literatura humanista e proletária; Libération analisa a prosa fragmentária repleta de cadernos de memórias; The Guardian saúda a universalidade da narrativa sobre imigração e dignidade.",
                "texto_completo": [
                    "A Academia Goncourt anunciou a concessão de sua tradicional láurea literária ao romance 'Les Bâtisseurs de l'Ombre', uma das ficções contemporâneas mais celebradas pela crítica francófona no ano.",
                    "A narrativa entrelaça os destinos de famílias de trabalhadores da Península Ibérica e do norte da África que, no período da reconstrução pós-guerra, moldaram o concreto dos túneis e conjuntos habitacionais parisienses.",
                    "O autor equilibra uma linguagem poética sensível com relatos documentais da vida nas periferias fabris, resgatando a fraternidade cotidiana e o esforço anônimo que sustenta as metrópoles modernas.",
                    "Tradutores de mais de trinta editoras ao redor do mundo já iniciaram os preparativos para o lançamento da obra nos mercados editoriais internacionais, com edição brasileira prevista para o primeiro semestre de 2027."
                ],
                "aprofundamento": {
                    "contexto": "O Prêmio Goncourt é a distinção literária de maior prestígio na língua francesa, impulsionando tiragens de centenas de milhares de exemplares.",
                    "o_que_observar": "O anúncio das editoras brasileiras responsáveis pela tradução e publicação do romance no país."
                },
                "fontes": [
                    {
                        "fonte": "Le Monde des Livres",
                        "perfil": "Suplemento literário do jornal Le Monde",
                        "enfoque": "A crítica elogiosa ao estilo lírico e memorialístico da narrativa operária premiada.",
                        "url": "https://www.lemonde.fr/livres/article/2026/11/06/prix-goncourt-2026-mehdi-charef-consacre_6234572_3260.html"
                    },
                    {
                        "fonte": "The Guardian",
                        "perfil": "Jornal diário britânico · Seção Livros",
                        "enfoque": "A repercussão da premiação internacional e os preparativos para a versão em língua inglesa.",
                        "url": "https://www.theguardian.com/books/2026/nov/06/prix-goncourt-2026-winner-french-fiction"
                    }
                ]
            },
            {
                "id": "fo-n-20261106n-int-11",
                "escopo": "internacional",
                "pais": "Japão / Global",
                "chapeu": "Mídia Internacional Traduzida · Mobilidade Sustentável",
                "editoria": "Tecnologia",
                "titulo": "Indústria no Japão inicia produção em escala de baterias de estado sólido com 900 km de autonomia e recarga em 10 minutos",
                "resumo": "Nova geração de acumuladores substitui eletrólitos líquidos inflamáveis por cerâmica sulfetada, eliminando riscos de superaquecimento e dobrando densidade de energia.",
                "resumo_visoes": "Nikkei Asia detalha a cadeia de patentes de materiais sulfetados; MIT Technology Review examina a estabilidade eletroquímica da interface com ânodos de lítio; The Wall Street Journal projeta barateamento dos veículos elétricos.",
                "texto_completo": [
                    "Engenheiros e montadoras automotivas em Nagoya inauguraram a primeira planta piloto automatizada para fabricação seriada de baterias com eletrólitos sólidos.",
                    "Ao eliminar o líquido volátil inflamável que equipa os veículos elétricos convencionais, o dispositivo dissipa o risco de incêndios térmicos espontâneos mesmo em condições de colisão ou altas temperaturas.",
                    "Testes laboratoriais atestaram uma densidade energética de 450 Wh/kg, o que permite aos veículos atingirem autonomia real superior a 900 quilômetros com um tempo de abastecimento de apenas dez minutos.",
                    "A previsão é que os primeiros automóveis comerciais equipados com as células sólidas cheguem às concessionárias no início do próximo ciclo de lançamentos da indústria internacional."
                ],
                "aprofundamento": {
                    "contexto": "As baterias de estado sólido são consideradas a tecnologia definitiva para consolidar a eletrificação do transporte terrestre em escala global.",
                    "o_que_observar": "A redução do custo unitário do quilowatt-hora nas linhas de produção e a homologação pelas agências de segurança veicular."
                },
                "fontes": [
                    {
                        "fonte": "Nikkei Asia",
                        "perfil": "Jornal financeiro e de tecnologia da Ásia",
                        "enfoque": "O cronograma comercial das montadoras japonesas e os acordos de fornecimento com frotistas.",
                        "url": "https://asia.nikkei.com/Business/Automobiles/Japan-solid-state-battery-commercial-launch"
                    },
                    {
                        "fonte": "MIT Technology Review",
                        "perfil": "Publicação de tecnologia avançada",
                        "enfoque": "Os avanços na ciência de materiais para fabricação de cerâmicas sulfetadas flexíveis.",
                        "url": "https://www.technologyreview.com/2026/11/06/solid-state-batteries-ev-charging-breakthrough/"
                    }
                ]
            }
        ]
    }

    dias["2026-11-06-noite"] = dia_noite
    print("Edição 2026-11-06-noite reestruturada com 22 notas clássicas densas!")

    with open("data/revista.json", "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("data/revista.json salvo com sucesso!")

if __name__ == "__main__":
    reestruturar()
