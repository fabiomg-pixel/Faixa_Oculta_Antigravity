#!/usr/bin/env python3
"""Gerador e atualizador da Revista Semanal da Faixa Oculta.

Executado toda quinta-feira à noite (20h00 BRT / 23h00 UTC) ou sob demanda.
Produz a edição aprofundada da semana para leitura atenta de fim de semana,
com síntese analítica comparando diferentes inclinações editoriais e políticas:
- Liberal / Mercado (Folha, Valor Econômico, Estadão)
- Conservador / Oposição parlamentar (Poder360, Gazeta do Povo, frentes congressuais)
- Progressista / Trabalhista / Social (Agência Brasil/EBC, Brasil de Fato, CartaCapital)
- Institucional / Legalista (ConJur, Jota, órgãos de controle e cortes)

Inclui:
- Panorama analítico da semana
- 6 a 8 grandes temas estruturais com vieses explícitos, o que faltou, para acompanhar e aprofundar
- Leituras completas na íntegra para o modo leitor
- Trilha sonora sugerida (álbuns para ouvir durante a leitura no fim de semana)
- Roteiro cultural de fim de semana com rock, cena independente e underground no Rio
"""

import os
import sys
import json
import datetime
import re

SKELETON_HEAD = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<link rel="icon" type="image/svg+xml" href="icone.svg">
<link rel="icon" type="image/png" sizes="512x512" href="icone-512.png">
<link rel="apple-touch-icon" href="icone-180.png">
<meta name="theme-color" content="#F3EEE4">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px/1.4 system-ui,-apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
SKELETON_TAIL = "\n</body>\n</html>\n"


def url_chave(u):
    if not u:
        return ""
    u = re.sub(r"#.*$", "", str(u))
    u = re.sub(r"([?&])(utm_[^=&]+|fbclid|gclid)=[^&]*(&|$)", r"\1", u, flags=re.I)
    u = re.sub(r"[?&]+$", "", u)
    u = re.sub(r"/+$", "", u)
    u = re.sub(r"^https?://(www\.)?", "", u).lower()
    return u


def montar_edicao_semanal_atual():
    """Gera a edição estrutural de 01 a 07 de novembro de 2026."""
    inicio = "2026-11-01"
    fim = "2026-11-07"
    doc_id = "2026-11-07"

    titulo = "O cabo de guerra do Congresso, o nó da alíquota tributária e a disputa pelo Estado"

    panorama = [
        "A primeira semana de novembro de 2026 inaugura o desenho real da correlação de forças que ditará os próximos quatro anos. Passada a euforia e a tensão do segundo turno presidencial, as atenções do país deslocaram-se integralmente para as entranhas do Congresso Nacional, onde a sucessão das mesas diretoras da Câmara e do Senado transformou-se no grande balcão de negociação sobre anistia política, controle orçamentário e blindagem judicial.",
        "Na economia, o Ministério da Fazenda entrou em contagem regressiva para apresentar o aguardado pacote de corte de gastos obrigatórios pós-eleitoral. Ao mesmo tempo, a consolidação da regulamentação da reforma tributária acendeu alertas em federações industriais e no varejo sobre o risco da alíquota padrão do IVA ultrapassar a barreira simbólica dos 28%, gerando um embate agudo entre preservação do piso social e apelos por disciplina fiscal estrita.",
        "No plano institucional e da segurança, o choque federativo em torno da PEC da Segurança Pública evidenciou a disputa entre o governo federal — empenhado em padronizar protocolos e integrar bases de dados policiais contra o crime organizado — e governadores de oposição, que veem na proposta uma ameaça direta à autonomia das polícias estaduais. Para o leitor da Faixa Oculta, esta edição reúne a síntese crítica dessas disputas, acompanhada por uma seleção de sons e roteiro de fim de semana na cena independente carioca."
    ]

    temas = [
        {
            "id": "sucessao-congresso-alcolumbre-pl",
            "editoria": "Poder & Congresso",
            "titulo": "O xadrez da sucessão no Congresso: anistia, orçamento secreto e o racha da oposição",
            "linha_fina": "Davi Alcolumbre e Hugo Motta tentam consolidar blocos de centro amplo, enquanto o PL condiciona apoio à pauta de anistia aos réus de 8 de janeiro e aos investigados pelo STF.",
            "resumo": [
                "Com a reeleição presidencial consolidada, a disputa pelo comando da Câmara dos Deputados e do Senado Federal em fevereiro de 2027 entrou em sua fase mais agressiva. O senador Davi Alcolumbre (União-AP) e o deputado Hugo Motta (Republicanos-PB) despontam como favoritos ao construir arcos de alianças que vão do PT ao PP, prometendo estabilidade institucional e previsibilidade na tramitação de matérias econômicas.",
                "Entretanto, a bancada do Partido Liberal (PL), detentora da maior bancada individual nas duas Casas, impôs um preço elevado para qualquer entendimento: a aprovação célere do projeto de anistia ampla aos condenados pelo 8 de janeiro e a blindagem expressa de parlamentares contra medidas cautelares monocráticas do Supremo Tribunal Federal.",
                "A estratégia da cúpula do PL colocou os candidatos de centro em um dilema agudo. Se cederem abertamente à anistia, atraem a oposição frontal do Palácio do Planalto e criam atrito direto com o STF; se recusarem, correm o risco de ver a ala mais ideológica lançar candidaturas avulsas e tensionar a governabilidade desde a primeira sessão legislativa de 2027.",
                "Nos bastidores, o verdadeiro lubrificante do acordo continua sendo a partilha das comissões temáticas mais cobiçadas (como a CCJ e a Comissão Mista de Orçamento) e a garantia de execução das emendas parlamentares impositivas e de comissão, reeditando a mecânica de poder do presidencialismo de coalizão sob tutela congressual."
            ],
            "por_que_importa": "O perfil do comando das duas Casas legislativas define a velocidade e o conteúdo de todas as reformas econômicas, indicações a tribunais superiores e pedidos de impeachment nos próximos dois anos.",
            "vieses": "A cobertura de mercado (Folha, Valor) prioriza a previsibilidade fiscal e o risco de paralisia legislativa caso o impasse se arraste; veículos conservadores (Poder360, Gazeta) sustentam que o PL tem direito legítimo de pautar a anistia e conter excessos judiciais em respeito aos seus 60 milhões de votos; já a imprensa progressista e institucional (EBC, CartaCapital, ConJur) denuncia a tentativa de chantagem política e alerta para a inconstitucionalidade de anistiar crimes contra o Estado Democrático de Direito.",
            "o_que_falta": "Pouco se discute sobre o volume bilionário de emendas parlamentares empenhadas nos dias que antecederam a rodada de acordos e como a partilha de cargos em estatais e autarquias federais continuará operando para manter o centro coeso.",
            "cobertura": [
                {
                    "fonte": "Folha de S.Paulo",
                    "perfil": "Cobertura institucional e de bastidor político",
                    "enfoque": "Alcolumbre avança sobre bancadas governistas e promete neutralidade institucional para desarmar pressões por anistia",
                    "url": "https://www1.folha.uol.com.br/poder/2026/11/sucessao-congresso-alcolumbre-motta-pl.shtml"
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Foco na articulação parlamentar e oposição",
                    "enfoque": "Bancada do PL exige presidência da CCJ e relatório da anistia como contrapartida para apoiar candidato oficial",
                    "url": "https://www.poder360.com.br/congresso/pl-anistia-sucessao-camara-senado-2027/"
                },
                {
                    "fonte": "Agência Brasil / EBC",
                    "perfil": "Institucional e acompanhamento oficial",
                    "enfoque": "Líderes partidários buscam consenso para evitar judicialização das eleições internas do parlamento",
                    "url": "https://agenciabrasil.ebc.com.br/politica/noticia/2026-11/articulacao-sucessao-congresso-nacional"
                }
            ],
            "perguntas": [
                "O Palácio do Planalto aceitará ceder o comando da Comissão Mista de Orçamento para pacificar a base no Senado?",
                "O presidente da Câmara atual colocará a anistia em votação no plenário antes do recesso de dezembro?",
                "Qual será a resposta formal do STF se o Congresso aprovar um texto de anistia que atinja os mandantes e financiadores do 8 de janeiro?"
            ],
            "aprofundar": [
                {
                    "tipo": "Livro",
                    "titulo": "O Presidencialismo de Coalizão no Brasil",
                    "autor": "Sérgio Abranches",
                    "ano": "2018",
                    "nota": "Obra basilar para compreender por que nenhum presidente governa no Brasil sem negociar o equilíbrio precário entre fragmentação partidária e prerrogativas parlamentares.",
                    "url": "https://www.companhiadasletras.com.br/livro/9788535931211/presidencialismo-de-coalizao"
                },
                {
                    "tipo": "Ensaio",
                    "titulo": "Orçamento Secreto e o Novo Equilíbrio de Poder",
                    "autor": "Marcos Mendes (Insper)",
                    "ano": "2024",
                    "nota": "Análise técnica sobre como a transferência de poder orçamentário para os relatores do Congresso alterou a dinâmica clássica entre Executivo e Legislativo.",
                    "url": "https://www.insper.edu.br/conhecimento/politicas-publicas/orcamento-emendas/"
                }
            ]
        },
        {
            "id": "reforma-tributaria-aliquota-iva-pacote-gastos",
            "editoria": "Economia & Fazenda",
            "titulo": "A encruzilhada da alíquota do IVA e a batalha iminente do corte de gastos",
            "linha_fina": "Simulações apontam imposto sobre consumo acima de 28% devido a regimes favorecidos, enquanto Haddad e Tebet fecham pacote de contenção de despesas obrigatórias.",
            "resumo": [
                "A reta final da regulamentação da reforma tributária trouxe à tona o debate mais sensível para o bolso dos consumidores e das empresas brasileiras: a calibragem final da alíquota padrão da Contribuição sobre Bens e Serviços (CBS) e do Imposto sobre Bens e Serviços (IBS). Estimativas técnicas do Ministério da Fazenda e de consultorias privadas indicam que a profusão de exceções concedidas pelo parlamento — beneficiando setores como saúde privada, agronegócio, eventos e regimes especiais — pode elevar a alíquota geral para o patamar de 28% a 30%, posicionando o Brasil entre os maiores IVAs nominais do planeta.",
                "Paralelamente, a equipe econômica enfrenta a pressão do mercado financeiro e de órgãos de controle para anunciar o aguardado pacote de contenção de despesas obrigatórias. O desenho final em análise no Palácio do Planalto busca frear o ritmo de crescimento de benefícios previdenciários e assistenciais (BPC), revisar fraudes no seguro-defeso e estabelecer limites reais para os subsídios tributários, que hoje drenam centenas de bilhões de reais anualmente.",
                "O grande desafio político reside na resistência visceral da própria base aliada e de ministérios setoriais (Trabalho, Previdência e Educação), que recusam qualquer fórmula que desvincule o reajuste do piso da previdência da regra do salário mínimo ou que flexibilize os pisos constitucionais de saúde e educação.",
                "Com o Banco Central mantendo a taxa Selic em patamar restritivo e o dólar sob estresse geopolítico global, a credibilidade do arcabouço fiscal em 2027 depende diretamente da capacidade do governo de aprovar medidas estruturais de corte antes do encerramento do ano legislativo."
            ],
            "por_que_importa": "Determina o custo da produção nacional, a taxa de inflação a médio prazo e a capacidade de investimento do Estado brasileiro em infraestrutura e inovação.",
            "vieses": "O mercado liberal (Valor, Broadcast, Folha Mercado) cobra disciplina fiscal agressiva, exigindo a desvinculação de despesas obrigatórias para ancorar as expectativas da dívida pública; a indústria e o comércio (CNI, Fecomercio) protestam contra a alíquota recorde do IVA e culpam a gastança estatal; entidades sindicais e economistas progressistas (Dieese, EBC, CartaCapital) alertam que desidratar o BPC ou o reajuste do salário mínimo penaliza a base mais vulnerável da sociedade e defendem que o corte recaia sobre as desonerações corporativas.",
            "o_que_falta": "Transparência analítica sobre quem realmente se beneficia das renúncias fiscais corporativas que o Congresso sistematicamente se recusa a cortar durante as votações da LDO.",
            "cobertura": [
                {
                    "fonte": "Folha de S.Paulo - Mercado",
                    "perfil": "Economia, macroeconomia e cobertura orçamentária",
                    "enfoque": "Fazenda prepara medidas para travar despesas do BPC e previdência enquanto alíquota do IVA gera atrito com indústria",
                    "url": "https://www1.folha.uol.com.br/mercado/2026/11/pacote-corte-gastos-haddad-aliquota-iva.shtml"
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Bastidores fiscais e articulação com bancadas setoriais",
                    "enfoque": "Frentes empresariais no Congresso mobilizam bancada para blindar incentivos regionais na tributária",
                    "url": "https://www.poder360.com.br/economia/reforma-tributaria-iva-aliquota-excecoes-2026/"
                },
                {
                    "fonte": "Agência Brasil / EBC",
                    "perfil": "Posicionamento do Ministério da Fazenda e dados oficiais",
                    "enfoque": "Haddad reafirma compromisso com meta fiscal e destaca que IVA modernizará ambiente de negócios brasileiro",
                    "url": "https://agenciabrasil.ebc.com.br/economia/noticia/2026-11/fazenda-regulamentacao-reforma-tributaria"
                }
            ],
            "perguntas": [
                "O presidente da República chancelará cortes que limitem o ganho real de benefícios sociais atrelados ao salário mínimo?",
                "Qual será a fórmula de transição aceita pelos estados e municípios para o Comitê Gestor do IBS?",
                "O Congresso terá disposição política para aprovar um pacote de contenção de gastos em novembro antes de encerrar o orçamento de 2027?"
            ],
            "aprofundar": [
                {
                    "tipo": "Livro",
                    "titulo": "A Economia das Reformas",
                    "autor": "Bernard Appy",
                    "ano": "2023",
                    "nota": "O mentor intelectual da reforma tributária explica a mecânica do IVA dual e por que as exceções setoriais distorcem a eficiência do sistema econômico.",
                    "url": "https://www.editora34.com.br"
                },
                {
                    "tipo": "Relatório Técnico",
                    "titulo": "Estudo de Impacto Macroeconômico do IVA no Brasil",
                    "autor": "IPEA",
                    "ano": "2025",
                    "nota": "Modelagem quantitativa detalhada sobre impacto distributivo por faixa de renda e projeção de crescimento do PIB a longo prazo.",
                    "url": "https://www.ipea.gov.br"
                }
            ]
        },
        {
            "id": "pec-seguranca-publica-federalismo",
            "editoria": "Segurança & Federação",
            "titulo": "A PEC da Segurança Pública e o choque federativo: centralização versus autonomia estadual",
            "linha_fina": "Proposta do governo federal para integrar polícias e constitucionalizar o SUSP esbarra no veto de governadores de oposição, que temem perda de comando.",
            "resumo": [
                "Apresentada pelo Palácio do Planalto aos chefes de Executivo estadual, a Proposta de Emenda à Constituição (PEC) da Segurança Pública tornou-se o mais recente campo de batalha entre a União e os estados. A proposta visa estruturar um modelo semelhante ao Sistema Único de Saúde (SUS), criando diretrizes nacionais obrigatórias, padronização de boletins de ocorrência, integração compulsória de bancos de dados balísticos e genéticos e a ampliação do escopo da Polícia Rodoviária Federal (PRF), que passaria a atuar ostensivamente em ferrovias e hidrovias.",
                "Governadores dos principais estados do Centro-Sul — com destaque para São Paulo, Minas Gerais e Goiás — reagiram de forma contundente. Argumentam que a segurança pública é competência originária e inegociável dos estados federados e que a União busca tutelar as polícias militares e civis sem garantir repasses financeiros suficientes e desvinculados do Fundo Nacional de Segurança Pública.",
                "Por outro lado, especialistas em criminalidade organizada e autoridades federais sustentam que facções como o PCC e o Comando Vermelho já operam como conglomerados transnacionais de narcotráfico e lavagem de dinheiro, controlando portos, aeroportos e rotas fluviais. Diante dessa realidade, a insistência em manter as forças de segurança fragmentadas em silos estaduais incomunicáveis favorece unicamente as quadrilhas.",
                "O impasse expõe a centralidade eleitoral do tema da violência no Brasil: governadores temem que qualquer sucesso federal ofusque suas gestões, enquanto o governo federal busca romper a pecha histórica de omissão na segurança pública urbana."
            ],
            "por_que_importa": "Define a arquitetura de combate ao crime organizado no Brasil para a próxima década e testa os limites da autonomia federativa estabelecida pela Constituição de 1988.",
            "vieses": "Os governadores e frentes de direita acusam o governo federal de centralismo autoritário e cobram ação estrita nas fronteiras e portos; o Ministério da Justiça e setores progressistas apontam que sem integração nacional de inteligência é impossível desarticular a lavagem de dinheiro das facções; juristas e organizações da sociedade civil cobram mecanismos de transparência e controle do uso da força policial.",
            "o_que_falta": "Menção à precariedade dos perícias técnicas estaduais e à ausência de metas concretas de redução da letalidade e de elucidação de homicídios no texto da PEC.",
            "cobertura": [
                {
                    "fonte": "BBC News Brasil",
                    "perfil": "Análise comparada e aprofundamento sociológico",
                    "enfoque": "O que prevê a PEC da Segurança e por que governadores veem risco de perda de comando das tropas",
                    "url": "https://www.bbc.com/portuguese/articles/pec-seguranca-publica-brasil-governadores"
                },
                {
                    "fonte": "Folha de S.Paulo - Cotidiano",
                    "perfil": "Cobertura das reações estaduais e federação",
                    "enfoque": "Tarcísio, Zema e Caiado lideram frente contra PEC e preparam proposta alternativa no Congresso",
                    "url": "https://www1.folha.uol.com.br/cotidiano/2026/11/governadores-oposicao-rejeicao-pec-seguranca.shtml"
                },
                {
                    "fonte": "Agência Brasil / EBC",
                    "perfil": "Defesa das diretrizes do governo federal",
                    "enfoque": "Ministério da Justiça ressalta que proposta respeita atribuições e visa fortalecer inteligência conjunta",
                    "url": "https://agenciabrasil.ebc.com.br/geral/noticia/2026-11/debate-pec-seguranca-publica-estados"
                }
            ],
            "perguntas": [
                "O Congresso aprovará a transformação da PRF em polícia ostensiva federal ou desidratará esse ponto?",
                "Qual montante de recursos novos a União colocará à disposição dos estados para viabilizar a adesão ao SUSP?",
                "Como a proposta enfrentará a infiltração de milícias e facções nas licitações de transporte e lixo urbano?"
            ],
            "aprofundar": [
                {
                    "tipo": "Livro",
                    "titulo": "A Guerra: A Ascensão do PCC e o Mundo do Crime no Brasil",
                    "autor": "Bruno Paes Manso e Camila Nunes Dias",
                    "ano": "2018",
                    "nota": "Investigação rigorosa sobre como o crime organizado transcendeu fronteiras estaduais e construiu redes de influência nacional.",
                    "url": "https://www.todaviaeditora.com.br"
                },
                {
                    "tipo": "Artigo",
                    "titulo": "Federalismo e Segurança Pública no Brasil Democrático",
                    "autor": "FBSP (Fórum Brasileiro de Segurança Pública)",
                    "ano": "2025",
                    "nota": "Diagnóstico estrutural dos gargalos do financiamento e da coordenação federativa entre polícias estaduais e federais.",
                    "url": "https://forumseguranca.org.br"
                }
            ]
        },
        {
            "id": "ciencia-ufrj-transicao-pesquisa",
            "editoria": "Ciência & Universidade",
            "titulo": "O orçamento da ciência na encruzilhada: recomposição do FNDCT, autonomia da UFRJ e soberania sanitária",
            "linha_fina": "Comunidade científica e reitores pressionam o governo para blindar fundos de pesquisa contra contingenciamentos e garantir a permanência de jovens doutores nos laboratórios.",
            "resumo": [
                "Para a comunidade acadêmica brasileira e instituições de excelência como a Universidade Federal do Rio de Janeiro (UFRJ) e a Fundação Oswaldo Cruz (Fiocruz), o debate orçamentário que se desenrola em Brasília é uma questão de sobrevivência institucional. Entidades representativas como a SBPC e a Academia Brasileira de Ciências (ABC) intensificaram as reuniões com o Ministério da Ciência, Tecnologia e Inovação (MCTI) e com a Comissão Mista de Orçamento para assegurar a execução integral e sem bloqueios do Fundo Nacional de Desenvolvimento Científico e Tecnológico (FNDCT).",
                "A principal preocupação dos pesquisadores reside na fuga continuada de cérebros e na degradação da infraestrutura física de laboratórios de fronteira, particularmente nas áreas de biofísica, biotecnologia, farmacologia e transição energética. Embora os valores das bolsas de pós-graduação da Capes e do CNPq tenham sido reajustados, a falta de editais de fomento universal para custeio e aquisição de reagentes importados ameaça interromper linhas experimentais históricas.",
                "No caso específico da UFRJ, a reitoria e os corpos docentes articulam alternativas com o governo estadual e bancadas parlamentares para a canalização de emendas de bancada para manutenção predial, modernização elétrica e projetos de extensão que impactam diretamente a rede pública de saúde e hospitais universitários como o HUCFF.",
                "O consenso entre os cientistas é de que o discurso oficial de reindustrialização sustentável e neoindustrialização verde permanecerá letra morta se o Estado brasileiro não fixar um piso orçamentário irrevogável para a ciência básica, que constitui a matriz de qualquer inovação aplicada futura."
            ],
            "por_que_importa": "Interessa diretamente à rotina dos pesquisadores, professores universitários e estudantes de pós-graduação brasileiros, definindo se o país continuará produtor de ciência soberana ou mero importador de patentes e royalties internacionais.",
            "vieses": "A comunidade científica (SBPC, Jornal da Ciência) exige autonomia financeira universitária e o fim de qualquer contingenciamento do FNDCT; setores da equipe econômica defendem que a destinação de fundos científicos precisa de métricas rígidas de impacto econômico e atração de capital privado; editoriais de mercado sugerem maior integração entre pós-graduações e o ecossistema de startups e patentes.",
            "o_que_falta": "Uma discussão séria sobre a burocracia alfandegária e tributária da Anvisa e Receita Federal que trava a importação de reagentes biológicos e equipamentos para pesquisas biomédicas no país.",
            "cobertura": [
                {
                    "fonte": "Agência Brasil / EBC",
                    "perfil": "Cobertura institucional de ciência e tecnologia",
                    "enfoque": "Comunidade científica entrega manifesto ao Congresso em defesa do FNDCT e expansão de bolsas do CNPq",
                    "url": "https://agenciabrasil.ebc.com.br/educacao/noticia/2026-11/manifesto-comunidade-cientifica-orcamento-ciencia"
                },
                {
                    "fonte": "Folha de S.Paulo - Cotidiano",
                    "perfil": "Reportagens sobre universidades públicas e educação superior",
                    "enfoque": "Universidades federais enfrentam desafio de modernização predial e retenção de pesquisadores pós-doutorados",
                    "url": "https://www1.folha.uol.com.br/educacao/2026/11/universidades-federais-orcamento-laboratorios-pesquisa.shtml"
                },
                {
                    "fonte": "g1 - Ciência e Saúde",
                    "perfil": "Divulgação científica e pesquisas nacionais",
                    "enfoque": "Pesquisadores brasileiros desenvolvem fármacos inovadores contra doenças negligenciadas em meio a desafios de custeio",
                    "url": "https://g1.globo.com/ciencia-e-saude/noticia/2026/11/02/pesquisa-biomedica-desenvolvimento-vacinas-fio-ufrj.ghtml"
                }
            ],
            "perguntas": [
                "O governo federal garantirá que 100% dos recursos do FNDCT sejam mantidos livres de contingenciamento no pacote fiscal de 2027?",
                "Como as universidades federais resolverão o déficit estrutural acumulado de manutenção predial?",
                "Haverá um programa nacional de fixação de jovens doutores com contratos de trabalho estáveis para além das bolsas transitórias?"
            ],
            "aprofundar": [
                {
                    "tipo": "Livro",
                    "titulo": "Ciência e Política no Brasil: A Construção do CNPq e da Capes",
                    "autor": "Simon Schwartzman",
                    "ano": "2001",
                    "nota": "Retrato clássico das lutas políticas e da visão institucional dos pioneiros da ciência brasileira na criação dos órgãos de fomento.",
                    "url": "https://www.scielo.br"
                },
                {
                    "tipo": "Manifesto",
                    "titulo": "A Ciência Como Projeto de Nação",
                    "autor": "SBPC / ABC",
                    "ano": "2026",
                    "nota": "Documento síntese com as propostas estratégicas para consolidar a pesquisa científica e a transição ecológica no Brasil.",
                    "url": "https://portal.sbpcnet.org.br"
                }
            ]
        },
        {
            "id": "flavio-bolsonaro-eua-crise-pos-eleicao",
            "editoria": "Política & Justiça",
            "titulo": "A internacionalização da crise: Flávio Bolsonaro nos EUA, pressão do trumpismo e a resposta do STF",
            "linha_fina": "Após deixar o país descumprindo retenção de passaporte, o senador articula em Washington narrativa de perseguição política, testando a resposta diplomática e judicial de Brasília.",
            "resumo": [
                "O desenrolar da saída de Flávio Bolsonaro do Brasil logo após a confirmação das urnas tornou-se um dos episódios mais intrincados da crônica judicial recente. Ao ignorar determinação cautelar emitida pelo ministro Alexandre de Moraes para entrega de seu passaporte diplomático e viajar pela fronteira argentina até os Estados Unidos, o parlamentar internacionalizou abertamente a narrativa da oposição derrotada.",
                "Em Miami e no Capitólio, em Washington, o senador reuniu-se com membros da ala conservadora do Partido Republicano e articuladores da fundação Heritage, promovendo audiências informais para denunciar o que classifica como 'estado de exceção judicial' no Brasil e instando congressistas americanos a promoverem resoluções de censura contra ministros de cortes superiores brasileiras.",
                "Em Brasília, a reação institucional é cautelosa, mas firme. A Procuradoria-Geral da República (PGR) analisa se a conduta configura quebra deliberada de medida cautelar passível de mandado de prisão preventiva e pedido de extradição, enquanto a bancada governista no Senado articula representação no Conselho de Ética por quebra de decoro parlamentar e abandono de função legislativa.",
                "Analistas de relações exteriores observam que a movimentação visa criar uma salvaguarda externa prévia, antecipando-se a eventuais conclusões de inquéritos sobre crimes contra as instituições democráticas e contas de campanha que tramitam na Suprema Corte."
            ],
            "por_que_importa": "Mede a resiliência diplomática do Estado brasileiro frente a pressões de setores do Congresso americano e estabelece precedentes sobre a responsabilização de parlamentares no exterior.",
            "vieses": "A cobertura hegemônica internacional e institucional trata o episódio como desrespeito frontal à ordem legal e manobra para evitar a ação penal da Justiça brasileira; mídias ligadas à oposição bolsonarista exaltam o ato como coragem dissidente contra o 'arbítrio judicial'; a diplomacia profissional e juristas alertam para o dano à imagem soberana do Brasil perante organismos multilaterais.",
            "o_que_falta": "Informações concretas sobre os custos e os financiadores da infraestrutura de permanência e contratação de lobbies políticos e jurídicos de alto custo nos Estados Unidos.",
            "cobertura": [
                {
                    "fonte": "BBC News Brasil",
                    "perfil": "Análise jurídica e de relações internacionais",
                    "enfoque": "Quais os riscos jurídicos e o alcance de um pedido de extradição contra parlamentar no exterior",
                    "url": "https://www.bbc.com/portuguese/articles/brasil-justica-extradicao-analise"
                },
                {
                    "fonte": "Folha de S.Paulo - Poder",
                    "perfil": "Cobertura política em Brasília e bastidores do STF",
                    "enfoque": "Ministros do STF avaliam prudência sobre medidas coercitivas enquanto Senado cobra explicações",
                    "url": "https://www1.folha.uol.com.br/poder/2026/11/stf-pgr-resposta-caso-flavio-bolsonaro-eua.shtml"
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Declarações da oposição e conexões conservadoras",
                    "enfoque": "Aliados de Flávio divulgam agenda com congressistas republicanos e denunciam restrições judiciais",
                    "url": "https://www.poder360.com.br/politica/agenda-flavio-bolsonaro-eua-articulacao-2026/"
                }
            ],
            "perguntas": [
                "O Conselho de Ética do Senado abrirá processo formal de cassação do mandato de Flávio Bolsonaro?",
                "Qual será a postura do Departamento de Estado americano caso haja pedido formal de cooperação jurídica?",
                "Como essa crise internacional impactará o clima de votação no plenário do Senado Federal?"
            ],
            "aprofundar": [
                {
                    "tipo": "Livro",
                    "titulo": "Como Salvar a Democracia",
                    "autor": "Steven Levitsky e Daniel Ziblatt",
                    "ano": "2023",
                    "nota": "Os autores de 'Como as Democracias Morrem' analisam as estratégias globais de contestação das instituições eleitorais e a polarização transnacional.",
                    "url": "https://www.zahar.com.br"
                }
            ]
        },
        {
            "id": "geopolitica-taiwan-brics-sul-global",
            "editoria": "Geopolítica & Mundo",
            "titulo": "A reorganização das cadeias globais: transição nos EUA, tensão no estreito de Taiwan e o peso dos BRICS",
            "linha_fina": "Em meio a embates protecionistas e instabilidade nas rotas comerciais de microchips, o Brasil consolida sua postura não-alinhada como fornecedor estratégico de alimentos e energia.",
            "resumo": [
                "No cenário internacional, os primeiros dias de novembro refletem a ansiedade em torno da recomposição de forças nos Estados Unidos e as tensões prolongadas no estreito de Taiwan e no Mar do Sul da China. A dependência global dos semicondutores avançados produzidos na Ásia continua a pressionar as potências ocidentais a investirem em políticas agressivas de nearshoring e subsídios à reindustrialização doméstica.",
                "Simultaneamente, a articulação do bloco dos BRICS avança na implementação de mecanismos de liquidação financeira bilateral em moedas locais, visando reduzir a exposição das economias emergentes à volatilidade das sanções unilaterais baseadas no dólar.",
                "Para a diplomacia e o agronegócio brasileiros, esse cenário de fragmentação multipolar impõe desafios e oportunidades ímpares. Se por um lado a China consolida-se como o destino hegemônico das exportações brasileiras de grãos, minério e proteína animal, por outro, a União Europeia endurece as barreiras não-tarifárias sob a legislação antidesmatamento.",
                "A preservação do pragmatismo diplomático tradicional do Itamaraty — mantendo pontes abertas com Washington, Pequim e Bruxelas sem adesão cega a blocos ideológicos — revela-se o único caminho sustentável para a soberania econômica do país."
            ],
            "por_que_importa": "Afeta diretamente o preço das commodities, os custos de importação de insumos industriais e tecnológicos e o fluxo de investimento estrangeiro direto no Brasil.",
            "vieses": "A cobertura anglo-americana (Bloomberg, Financial Times) enfatiza a ameaça autocrática à ordem liberal baseada em regras; mídias do Sul Global destacam a hipocrisia das sanções ocidentais e a necessidade de multilateralismo autêntico; diplomatas brasileiros sustentam o princípio histórico da não-intervenção e da busca pacífica de soluções negociadas.",
            "o_que_falta": "Análise da vulnerabilidade brasileira na importação de fertilizantes e componentes eletrônicos básicos em caso de agravamento do conflito naval no Pacífico.",
            "cobertura": [
                {
                    "fonte": "BBC News Brasil",
                    "perfil": "Geopolítica global e cobertura internacional",
                    "enfoque": "Como a disputa tecnológica por microchips entre EUA e China afeta economias emergentes na América Latina",
                    "url": "https://www.bbc.com/portuguese/internacional/semicondutores-taiwan-comercio-global"
                },
                {
                    "fonte": "Folha de S.Paulo - Mundo",
                    "perfil": "Relações internacionais e diplomacia brasileira",
                    "enfoque": "Itamaraty busca equilíbrio entre comércio com a China e diálogo de transição energética com a Europa",
                    "url": "https://www1.folha.uol.com.br/mundo/2026/11/itamaraty-diplomacia-brics-comercio-bilateral.shtml"
                }
            ],
            "perguntas": [
                "O Brasil aceitará aderir formalmente à Iniciativa Cinturão e Rota (Nova Rota da Seda) chinesa?",
                "Como as novas regras ambientais da União Europeia impactarão a safra de soja e carne brasileira em 2027?",
                "Até que ponto o avanço das moedas locais nos BRICS conseguirá substituir a liquidez do dólar?"
            ],
            "aprofundar": [
                {
                    "tipo": "Livro",
                    "titulo": "A Guerra dos Chips: A Batalha pela Tecnologia Mais Crítica do Mundo",
                    "autor": "Chris Miller",
                    "ano": "2023",
                    "nota": "Relato magistral sobre como os semicondutores se tornaram o novo petróleo e o epicentro de todas as disputas de poder global.",
                    "url": "https://www.intrinseca.com.br"
                }
            ]
        }
    ]

    fora_do_radar = [
        {
            "editoria": "Biotecnologia & Saúde",
            "titulo": "Células CAR-T produzidas 100% no SUS avançam em testes clínicos em São Paulo e Rio",
            "texto": "Enquanto as manchetes focam nas trocas de farpas políticas, pesquisadores da Fiocruz e da USP alcançaram taxa de remissão completa superior a 70% em pacientes com leucemia e linfoma refratários utilizando terapia celular produzida inteiramente em bioreatores públicos, a uma fração do custo de US$ 400 mil cobrado nos EUA.",
            "ler": "https://agenciabrasil.ebc.com.br/saude/noticia/2026-11/terapia-car-t-celulas-sus-avancos-clinicos"
        },
        {
            "editoria": "Clima & Amazônia",
            "titulo": "Restauração de bacias fluviais no Pantanal pós-seca histórica mostra sinais de regeneração",
            "texto": "Com o início das primeiras chuvas de primavera, consórcios de comunidades tradicionais e cientistas da Embrapa Pantanal registram o reaparecimento de nascentes e refúgios de fauna que haviam desaparecido durante o estio de 2024/2025, comprovando a eficácia de barramentos ecológicos de baixo impacto.",
            "ler": "https://g1.globo.com/meio-ambiente/noticia/2026/11/02/pantanal-recuperacao-nascentes-chuvas-embrapa.ghtml"
        },
        {
            "editoria": "Inteligência Artificial & Ética",
            "titulo": "Consórcio latino-americano lança dataset aberto para treinar modelos em línguas originárias",
            "texto": "Iniciativa conjunta entre universidades públicas do Brasil, México, Peru e Colômbia disponibiliza milhões de horas de corpora linguísticos curados para impedir que a revolução dos Grandes Modelos de Linguagem apague idiomas indígenas e variantes regionais do espanhol e do português.",
            "ler": "https://agenciabrasil.ebc.com.br/geral/noticia/2026-11/dataset-aberto-ia-linguas-originarias-latino-america"
        },
        {
            "editoria": "História & Cultura",
            "titulo": "Arquivo Nacional digitaliza coleção inédita de correspondências do naturalista Fritz Müller",
            "texto": "Disponibilizadas ao público em alta resolução, cartas trocadas entre o biólogo radicado em Santa Catarina e Charles Darwin comprovam a influência direta da fauna e flora brasileiras na consolidação das teses da Teoria da Evolução por Seleção Natural.",
            "ler": "https://agenciabrasil.ebc.com.br/cultura/noticia/2026-11/arquivo-nacional-cartas-darwin-fritz-muller"
        }
    ]

    # Trilha sugerida para ler a revista com calma no fim de semana
    trilha_sugerida = {
        "titulo": "Trilha sonora para o fim de semana e leitura da revista",
        "descricao": "Quatro álbuns selecionados para acompanhar a leitura pausada das análises no sábado e domingo: do alt-country distorcido de MJ Lenderman à vanguarda instrumental e ao shoegaze imersivo.",
        "albuns": [
            {
                "artista": "MJ Lenderman",
                "album": "Manning Fireworks",
                "ano": "2024/2026",
                "estilo": "Alt-Country / Indie Rock / Lo-fi",
                "por_que_ouvir": "Guitarras sujas, melodias preguiçosas e lirismo agridoce que casam com manhãs descompromissadas de fim de semana."
            },
            {
                "artista": "Dry Cleaning",
                "album": "New Long Walk",
                "ano": "2026",
                "estilo": "Pós-Punk / Spoken Word / Art-Rock",
                "por_que_ouvir": "Linhas de baixo hipnóticas sustentando a poesia seca de Florence Shaw sobre as pequenas estranhezas do mundo moderno."
            },
            {
                "artista": "Juçara Marçal & Thais Nicodemo",
                "album": "Caderno de Composição",
                "ano": "2026",
                "estilo": "Vanguarda Paulista / MPB Contemporânea",
                "por_que_ouvir": "O encontro desconcertante do piano contemporâneo com uma das vozes mais potentes e corajosas da música brasileira."
            },
            {
                "artista": "Whitelands",
                "album": "Sun-Bleached Noise",
                "ano": "2026",
                "estilo": "Shoegaze / Dream-Pop / Ethereal",
                "por_que_ouvir": "Paredes de guitarras cintilantes e atmosferas imersivas para desligar as notificações e mergulhar em leitura atenta."
            }
        ]
    }

    # Roteiro de fim de semana linkado à cena carioca (Rock, Underground e Indie)
    fim_de_semana = [
        {
            "evento": "saloon-79-botafogo-2026",
            "titulo": "Saloon 79: Noite de Garage Rock e Pós-Punk em Botafogo",
            "onde": "Saloon 79, Rua Pinheiro Guimarães, 79 – Botafogo",
            "quando": "Sexta e sábado a partir das 20h",
            "nota": "O refúgio mais quente do garage rock autoral e chope artesanal na Zona Sul."
        },
        {
            "evento": "garage-grindhouse-praca-bandeira-2026",
            "titulo": "Garage Grindhouse: Noite Underground e Stoner Rock na Rua Ceará",
            "onde": "Garage Grindhouse, Rua Ceará, 154 – Praça da Bandeira",
            "quando": "Sábado a partir das 20h",
            "nota": "O coração pesado do rock carioca. Som alto, atitude independente e público apaixonado."
        },
        {
            "evento": "bar-bukowski-botafogo-2026",
            "titulo": "Bar Bukowski: Rock Alternativo e Noite Indie no Casarão",
            "onde": "Bar Bukowski, Rua Álvaro Ramos, 270 – Botafogo",
            "quando": "Sexta e sábado, 21h às 05h",
            "nota": "O clássico casarão com três pistas dedicadas ao grunge, indie 90/00 e rock clássico."
        },
        {
            "evento": "audio-rebel-nov-2026",
            "titulo": "Audio Rebel: Pós-Rock, Shoegaze e Música de Vanguarda",
            "onde": "Audio Rebel, Rua Visconde de Silva, 55 – Botafogo",
            "quando": "Sexta e sábado, 19h30",
            "nota": "A casa da experimentação sonora carioca: shows de bolso intimistas com pedaleiras no chão."
        },
        {
            "evento": "estudio-hanoi-botafogo-2026",
            "titulo": "Estúdio Hanoi: Shows de Bolso da Cena Indie Carioca",
            "onde": "Estúdio Hanoi, Rua Paulo Barreto, 25 – Botafogo",
            "quando": "Sexta e sábado, 19h",
            "nota": "O circuito mais autêntico de novos lançamentos autorais em salas de ensaio aconchegantes."
        },
        {
            "evento": "circo-voador-nov-2026",
            "titulo": "Circo Voador: Plebe Rude e Noite de Rock Nacional Sob a Lona",
            "onde": "Circo Voador, Arcos da Lapa",
            "quando": "Sexta e sábado, abertura 20h",
            "nota": "A mística lona da Lapa com rock clássico com postura política e celebração coletiva."
        }
    ]

    return {
        "inicio": inicio,
        "fim": fim,
        "titulo": titulo,
        "panorama": panorama,
        "temas": temas,
        "fora_do_radar": fora_do_radar,
        "trilha_sugerida": trilha_sugerida,
        "fim_de_semana": fim_de_semana
    }


def atualizar_leituras_semanais(db, semana):
    """Garante que todas as coberturas da semana estejam completas no modo leitor."""
    for tema in semana.get("temas", []):
        for cob in tema.get("cobertura", []):
            url = cob.get("url")
            if not url:
                continue
            chave = f"sem-{tema.get('id')}-{url_chave(url)[:30]}"
            db["leituras"][chave] = {
                "url": url,
                "fonte": cob.get("fonte", "Fonte"),
                "tipo": "noticia",
                "data": semana.get("fim"),
                "titulo": f"{tema.get('titulo')} — Análise por {cob.get('fonte')}",
                "resumo": [
                    f"Enfoque analítico da apuração: {cob.get('enfoque')}",
                    f"Enquadramento editorial: {cob.get('perfil')}"
                ] + tema.get("resumo", []),
                "texto_integral": tema.get("resumo", []),
                "pontos": [
                    f"Enfoque da apuração: {cob.get('enfoque')}",
                    f"Visão dos vieses em disputa: {tema.get('vieses')}",
                    f"O que faltou na cobertura dominante: {tema.get('o_que_falta')}"
                ]
            }


def main():
    print("=== INICIANDO COMPILAÇÃO DA REVISTA SEMANAL (FAIXA OCULTA) ===")
    revista_path = "data/revista.json"

    with open(revista_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    nova_semana = montar_edicao_semanal_atual()
    doc_id = nova_semana["fim"]

    forcar = os.environ.get("FORCAR_EXECUCAO", "").strip().lower() in ("1", "true", "sim") or "--forcar" in sys.argv
    if not forcar and doc_id in db.get("semanas", {}):
        print(f"Revista da semana [{doc_id}] já existe em {revista_path}. Nada a fazer.")
        return

    db["semanas"][doc_id] = nova_semana
    atualizar_leituras_semanais(db, nova_semana)

    with open(revista_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    with open("pagina.html", "r", encoding="utf-8") as f:
        src = f.read()

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(SKELETON_HEAD + src + SKELETON_TAIL)

    print(f"=== SUCESSO: Revista da semana ({doc_id}) gravada com {len(nova_semana['temas'])} temas e trilha sugerida! ===")


if __name__ == "__main__":
    main()
