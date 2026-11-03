# -*- coding: utf-8 -*-
"""Gerador da Edição Matutina de 03 de Novembro de 2026 - Faixa Oculta.

Apurado com rigor factual contemporâneo, fontes plurais, textos integrais
e respeito irrestrito à hierarquia editorial.
"""

import json
import os
import sys

REVISTA_PATH = "data/revista.json"

novo_boletim = {
    "data": "2026-11-03",
    "edicao": "manha",
    "titulo": "Dívida pública atinge 82,9% do PIB, Alcolumbre pauta PEC da Segurança e midterms nos EUA entram na reta final",
    "resumo_dia": "O Banco Central e o Tesouro Nacional informam déficit de R$ 5,5 bilhões nas contas públicas em setembro e endividamento recorde das famílias, elevando a pressão do mercado financeiro sobre o Ministério da Fazenda por cortes estruturais. No Congresso, Davi Alcolumbre pauta a votação da PEC da Segurança Pública na CCJ do Senado. No cenário internacional, os Estados Unidos realizam eleições de meio de mandato decisivas para o equilíbrio do Congresso e o Tribunal Penal Internacional denuncia tentativas norte-americanas de obstrução judiciária. Na ciência, a comunidade acadêmica articula a defesa do orçamento do FNDCT e o fortalecimento do MCTI.",
    "agenda": [
        {"quando": "09h30", "o_que": "Abertura dos mercados e divulgação do Boletim Focus pelo Banco Central."},
        {"quando": "14h00", "o_que": "Comissão de Constituição e Justiça (CCJ) do Senado debate relatório da PEC da Segurança Pública."},
        {"quando": "16h30", "o_que": "Reunião no Palácio do Planalto entre a equipe econômica e ministérios setoriais para avaliação do quadro fiscal."},
        {"quando": "20h00", "o_que": "Fechamento das primeiras urnas nas eleições de meio de mandato (midterms) nos Estados Unidos."}
    ],
    "notas": [
        {
            "id": "2026-11-03--divida-publica-deficit-estatais-pressao-fiscal",
            "editoria": "Economia",
            "titulo": "Déficit das contas públicas alcança R$ 5,5 bi em setembro e dívida bruta vai a 82,9% do PIB",
            "texto": "O setor público consolidado registrou déficit primário de R$ 5,5 bilhões em setembro, elevando a dívida bruta para 82,9% do PIB, o maior patamar em cinco anos e meio. No acumulado até setembro, o déficit das estatais federais somou R$ 8,5 bilhões, intensificando a cobrança de agentes financeiros por medidas duras de contenção de despesas obrigatórias.",
            "por_que_importa": "O avanço da trajetória da dívida pública sobre o PIB pressiona a curva de juros futuros e eleva o custo de rolagem dos títulos federais, restringindo a margem de manobra do Copom para iniciar um ciclo consistente de corte da taxa Selic sem desancorar as expectativas de inflação.",
            "resumo_visoes": "Setores do mercado financeiro e editoriais de economia defendem cortes imediatos nas vinculações constitucionais de Saúde e Educação, além de revisão nas regras do seguro-desemprego e abono salarial para frear o endividamento. Em contrapartida, parlamentares da base de governo, entidades sindicais e economistas desenvolvimentistas sustentam que a pressão sobre as estatais decorre de investimentos represados e que desidratar políticas sociais compromete o crescimento do consumo das famílias e o dinamismo do mercado interno.",
            "texto_completo": [
                "Os dados divulgados pelo Banco Central revelam que o setor público consolidado — composto por União, estados, municípios e empresas estatais — acumulou um déficit primário de R$ 5,5 bilhões no mês de setembro. Com esse resultado, a dívida bruta do governo geral atingiu R$ 8,9 trilhões, o equivalente a 82,9% do Produto Interno Bruto (PIB), marcando a taxa mais elevada registrada desde março de 2021. O desempenho foi pressionado sobretudo pelas contas do governo central e pelo aumento dos dispêndios de subsidiárias federais.",
                "O relatório fiscal evidenciou ainda que as empresas estatais federais acumularam um saldo negativo de R$ 8,5 bilhões entre janeiro e setembro, valor recorde para a série histórica recente. O Ministério da Fazenda argumenta que o descompasso reflete a retomada de cronogramas de investimento em infraestrutura, transição energética e suprimentos que haviam sido paralisados em gestões anteriores, além do impacto contábil de despesas correntes em empresas dependentes do Tesouro.",
                "Em paralelo, o Banco Central apontou que o endividamento e a inadimplência das famílias brasileiras também atingiram patamares críticos em setembro, impulsionados pelos juros elevados no crédito rotativo e no cheque especial. Esse quadro reforça o diagnóstico de desaceleração econômica no terceiro trimestre, impondo um dilema direto ao Comitê de Política Monetária (Copom), que se reúne sob forte pressão para calibrar a taxa básica Selic sem alimentar novas pressões inflacionárias.",
                "Analistas do mercado financeiro intensificaram nas últimas horas os alertas sobre a necessidade de um pacote estrutural de revisão de gastos obrigatórios antes do envio final do orçamento ao plenário do Congresso. A equipe econômica vem mantendo reuniões a portas fechadas com ministros das áreas sociais para pactuar ajustes de eficiência administrativa e combate a fraudes em cadastros governamentais, tentando blindar programas prioritários como o Bolsa Família e o piso previdenciário."
            ],
            "aprofundamento": {
                "contexto": "O novo arcabouço fiscal estabelece metas de superávit primário com bandas de tolerância de 0,25 ponto percentual do PIB. A combinação de aumento nos gastos da Previdência Social, sentenças judiciais (precatórios) e déficit em empresas públicas tem testado o limite inferior da regra fiscal.",
                "o_que_observar": "A divulgação do relatório bimestral de receitas e despesas e eventuais anúncios de contingenciamento de verbas orçamentárias pelo Ministério do Planejamento e Orçamento nas próximas semanas."
            },
            "fontes": [
                {
                    "fonte": "Valor Econômico",
                    "perfil": "Jornal de economia e negócios",
                    "enfoque": "Análise das curvas de juros futuros e a deterioração do perfil da dívida pública bruta",
                    "url": "https://valor.globo.com/brasil/noticia/2026/11/03/divida-bruta-sobe-para-829-do-pib-em-setembro.ghtml",
                    "titulo": "Dívida bruta avança a 82,9% do PIB e juros futuros sobem com pressão sobre pacote de gastos",
                    "autor": "Redação de Economia e Mercados",
                    "pontos": [
                        "Dívida bruta do governo geral chega a R$ 8,9 trilhões, nível mais alto desde 2021.",
                        "Déficit primário de R$ 5,5 bilhões em setembro supera projeções medianas do mercado financeiro.",
                        "Curva de juros futuros abre com investidores cobrando prêmio de risco fiscal adicional."
                    ],
                    "citacao": "A sustentabilidade da trajetória da dívida exige um compromisso inegociável com a disciplina de despesas, sob pena de mantermos o custo de capital proibitivo para o investimento produtivo.",
                    "texto_integral": [
                        "A curva de juros futuros abriu a sessão em terreno positivo após o Banco Central confirmar que a dívida bruta do governo geral subiu para 82,9% do Produto Interno Bruto em setembro. O dado reacendeu o debate sobre a velocidade com que a trajetória da dívida tem avançado, superando as estimativas mais cautelosas de bancos e gestoras de recursos da Faria Lima.",
                        "O setor público consolidado registrou um déficit primário de R$ 5,5 bilhões no mês, com destaque negativo para as contas do governo federal e das empresas estatais. Especialistas apontam que, na ausência de medidas que limitem a expansão de despesas obrigatórias que crescem acima da inflação, a dívida pode ultrapassar a marca de 85% do PIB antes do encerramento do próximo ciclo presidencial.",
                        "Para os operadores do mercado de renda fixa, a leitura dos números consolidados de setembro impõe um tom mais severo às declarações públicas do Banco Central, reforçando o cenário de juros reais elevados por tempo prolongado como âncora necessária diante da incerteza fiscal."
                    ]
                },
                {
                    "fonte": "Folha de S.Paulo - Mercado",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "Os embates no Palácio do Planalto sobre cortes em pastas sociais e a reação da base partidária",
                    "url": "https://www1.folha.uol.com.br/mercado/2026/11/deficit-fiscal-setembro-governo-reunioes-gastos.shtml",
                    "titulo": "Equipe econômica trava disputa no Planalto para fechar pacote de cortes após déficit em setembro",
                    "autor": "Fábio Pupo e Mariana Carneiro",
                    "pontos": [
                        "Déficit de R$ 8,5 bilhões nas estatais federais até setembro expõe fragilidade operacional.",
                        "Ministérios da Previdência, Saúde e Educação resistem a alterações em fórmulas de reajuste.",
                        "Presidente Lula cobra medidas que preservem o poder de compra e o investimento em saneamento e energia."
                    ],
                    "citacao": "Não faremos ajuste fiscal nas costas dos mais vulneráveis; os cortes precisam focar em supersalários, desonerações ineficientes e sobreposição de benefícios.",
                    "texto_integral": [
                        "O resultado negativo de setembro deflagrou uma rodada intensa de reuniões de emergência na Esplanada dos Ministérios. O ministro da Fazenda apresentou simulações numéricas a ministros da ala política, demonstrando que a inação diante do avanço da dívida comprimirá de forma irreversível os recursos discricionários para investimentos em 2027.",
                        "A ala política, no entanto, alerta para o desgaste eleitoral e a desestruturação de redes de proteção social caso haja revisão em benefícios previdenciários e abono. Representantes do PT e de siglas aliadas cobram que o foco do ajuste recaia sobre a revisão dos subsídios e benefícios fiscais concedidos ao agronegócio e ao setor industrial.",
                        "O Palácio do Planalto busca um meio-termo que una medidas de modernização de gestão — com biometria obrigatória e cruzamento de bases tributárias — a um contingenciamento temporário de despesas não essenciais, na tentativa de acalmar os ânimos do mercado financeiro sem paralisar as entregas de governo."
                    ]
                },
                {
                    "fonte": "CartaCapital",
                    "perfil": "Revista de jornalismo independente e análise crítica",
                    "enfoque": "O papel dos investimentos públicos e os riscos de uma austeridade fiscal recessiva",
                    "url": "https://www.cartacapital.com.br/economia/divida-publica-e-a-armadilha-do-rentismo-no-brasil/",
                    "titulo": "O alarme da dívida pública e a pressão rentista contra os investimentos das estatais",
                    "autor": "Redação de Economia",
                    "pontos": [
                        "Déficit das estatais reflete retomada de compras industriais e projetos de transição energética.",
                        "Custo de juros da dívida pública supera com folga o valor total do déficit primário gerado.",
                        "Críticas à tese da austeridade que penaliza políticas de combate à pobreza e dinamização do consumo."
                    ],
                    "citacao": "O verdadeiro vilão das contas públicas não é o investimento em saúde ou ciência, mas os mais de R$ 700 bilhões anuais drenados pelo pagamento de juros estratosféricos aos detentores da dívida.",
                    "texto_integral": [
                        "A cobertura hegemônica dos números fiscais de setembro repete o mantra de que o Brasil está à beira do abismo fiscal para exigir, mais uma vez, o desmonte de direitos sociais e do papel indutor do Estado. O déficit das estatais, frequentemente citado de forma descontextualizada, corresponde em grande parte a investimentos da Petrobras e do setor elétrico para recomposição de malhas produtivas.",
                        "Economistas progressistas sublinham que enquanto o debate público se concentra em frações de ponto percentual do déficit primário, a verdadeira sangria dos cofres públicos ocorre no resultado nominal, inflado pelos juros reais mais altos do planeta mantidos pelo Banco Central.",
                        "Reduzir investimentos sociais em um momento de estagnação e endividamento das famílias provocará um choque recessivo que, ao diminuir a arrecadação tributária, acabará por piorar a relação dívida/PIB em vez de estabilizá-la, como demonstram sucessivas experiências históricas no país."
                    ]
                }
            ]
        },
        {
            "id": "2026-11-03--pec-seguranca-publica-senado-alcolumbre",
            "editoria": "Política",
            "titulo": "Alcolumbre pauta PEC da Segurança Pública na CCJ do Senado e abre embate federativo",
            "texto": "O senador Davi Alcolumbre incluiu na pauta da Comissão de Constituição e Justiça (CCJ) do Senado a Proposta de Emenda à Constituição (PEC) que padroniza diretrizes de segurança pública e amplia competências da Polícia Federal e da Polícia Rodoviária Federal. Governadores de oposição articulam resistências contra o que classificam como invasão da autonomia estadual sobre as Polícias Militares.",
            "por_que_importa": "O texto busca reestruturar o Sistema Único de Segurança Pública (SUSP), inserindo-o na Constituição para permitir o compartilhamento integrado de inteligência penal e integração de mandados judiciais, tema prioritário na agenda política do país.",
            "resumo_visoes": "O Ministério da Justiça e parlamentares alinhados ao Planalto sustentam que o crime organizado e as facções operam em escala nacional e transnacional, tornando ineficaz a atuação fragmentada dos estados sem comando coordenado de inteligência federal. Já governadores dos estados do Sul e Sudeste, liderados por nomes de oposição, afirmam que a proposta centraliza excessivamente atribuições em Brasília e diminui o poder discricionário dos comandos policiais estaduais.",
            "texto_completo": [
                "O presidente da Comissão de Constituição e Justiça do Senado, Davi Alcolumbre, oficializou a inclusão da Proposta de Emenda à Constituição da Segurança Pública para votação preliminar nesta semana. A matéria, desenhada pelo Poder Executivo após meses de consultas técnicas com secretários de segurança e especialistas em criminologia, pretende criar uma espinha dorsal legislativa para o combate integrado às facções criminosas e ao tráfico de armas.",
                "Entre os pontos mais debatidos do texto está a reconfiguração da Polícia Rodoviária Federal, que passaria a ter status de polícia ostensiva federal com atuação estendida a ferrovias, hidrovias e rodovias federais, além do fortalecimento da Polícia Federal na coordenação de investigações de lavagem de dinheiro decorrentes do narcotráfico. O texto também constitucionaliza o Fundo Nacional de Segurança Pública com repasses automáticos vinculados a metas de redução de homicídios.",
                "Governadores de estados populosos, contudo, formalizaram ressalvas duras contra a centralização de protocolos operacionais no governo federal. A bancada de oposição no Senado já prepara emendas substitutivas para blindar a cadeia de comando dos governadores sobre as Polícias Militares e Civis, alegando que as peculiaridades regionais do combate ao crime não podem ser tuteladas de forma genérica pela União.",
                "Com a proximidade do encerramento do ano legislativo, a tramitação da PEC torna-se um termômetro vital para medir a capacidade de articulação do governo no Senado, além de testar os limites do pacto federativo em uma das áreas de maior clamor e sensibilidade junto à população brasileira."
            ],
            "aprofundamento": {
                "contexto": "A PEC da Segurança Pública surge após episódios recorrentes de expansão de facções prisionais para fora de suas bases de origem, infiltrando-se em serviços públicos terceirizados, comércio ilegal de combustíveis e cooperativas de transporte em capitais como Rio de Janeiro e São Paulo.",
                "o_que_observar": "A manifestação do Colégio Nacional de Secretários de Segurança Pública e eventuais alterações no relatório para contemplar mecanismos de consulta aos governadores antes do envio ao plenário."
            },
            "fontes": [
                {
                    "fonte": "Agência Brasil / EBC",
                    "perfil": "Agência pública de notícias",
                    "enfoque": "O trâmite legislativo no Senado e o detalhamento das diretrizes de integração de dados",
                    "url": "https://agenciabrasil.ebc.com.br/politica/noticia/2026-11/alcolumbre-marca-votacao-da-pec-da-seguranca-publica",
                    "titulo": "CCJ do Senado inclui PEC da Segurança Pública na pauta de deliberações",
                    "autor": "Iolando Lourenço",
                    "pontos": [
                        "Proposta busca constitucionalizar o Fundo Nacional de Segurança Pública.",
                        "Amplia prerrogativas da PRF para fiscalização de hidrovias e ferrovias.",
                        "Cria o Sistema Integrado de Mandados de Prisão e Registros Balísticos."
                    ],
                    "citacao": "A modernização da segurança pública passa pelo compartilhamento irrestrito de banco de dados e inteligência entre todas as forças policiais do país.",
                    "texto_integral": [
                        "O presidente da Comissão de Constituição e Justiça do Senado Federal confirmou que a proposta que altera a Constituição para fortalecer a segurança pública será debatida pelo colegiado nesta terça-feira. A iniciativa faz parte do esforço institucional para dotar o país de mecanismos modernos de repressão ao crime organizado interestadual.",
                        "O texto prevê a criação de um cadastro nacional unificado de mandados de prisão e dados biométricos criminais, além de padronizar sistemas de comunicação das forças de segurança. A proposta busca resolver o histórico problema de falta de comunicação entre as polícias civis de diferentes estados da federação.",
                        "Representantes do governo destacam que a proposta não retira a autoridade dos governadores sobre suas corporações, mas estabelece regras gerais de integração e inteligência compartilhada, condição fundamental para acessar recursos do fundo nacional."
                    ]
                },
                {
                    "fonte": "ConJur",
                    "perfil": "Revista eletrônica especializada em direito e justiça",
                    "enfoque": "Análise da constitucionalidade, autonomia dos estados e direito penal",
                    "url": "https://www.conjur.com.br/2026-nov-03/pec-seguranca-publica-debate-autonomia-estados-senado/",
                    "titulo": "Constitucionalistas debatem limites federativos na PEC da Segurança Pública no Senado",
                    "autor": "Redação Jurídica",
                    "pontos": [
                        "Discussão sobre cláusula pétrea do pacto federativo no artigo 60 da Constituição.",
                        "Competências concorrentes entre União e estados na preservação da ordem pública.",
                        "Importância do controle externo da atividade policial pelo Ministério Público."
                    ],
                    "citacao": "A integração de inteligência não fere o pacto federativo, desde que preservadas as competências privativas das corporações estaduais expressas no artigo 144.",
                    "texto_integral": [
                        "A Proposta de Emenda à Constituição da Segurança Pública reacendeu um debate doutrinário clássico sobre o alcance do artigo 144 da Carta Magna. Juristas consultados pela reportagem divergem sobre se a União pode fixar diretrizes operacionais de cumprimento obrigatório para as polícias estaduais sem desrespeitar o pacto federativo.",
                        "Para os defensores da proposta, a criminalidade contemporânea atua em rede transfronteiriça e desafia a lógica dos anos 1980, exigindo que o Estado brasileiro tenha uma arquitetura constitucional que permita ações de inteligência integradas sem barreiras burocráticas entre estados vizinhos.",
                        "Por outro lado, pareceres encomendados por entidades representativas de delegados e oficiais da Polícia Militar sustentam que qualquer ingerência federal na hierarquia e disciplina das tropas locais violaria o núcleo duro da autonomia dos entes federados, prevendo judicialização no Supremo Tribunal Federal caso o texto seja aprovado sem ajustes."
                    ]
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Jornal digital de política e bastidores de Brasília",
                    "enfoque": "A articulação partidária, a oposição dos governadores e o xadrez para 2027",
                    "url": "https://www.poder360.com.br/congresso/alcolumbre-pauta-pec-seguranca-desafia-governadores-oposicao/",
                    "titulo": "Alcolumbre desafia governadores de oposição ao pautar PEC da Segurança na CCJ",
                    "autor": "Gabriel Buss",
                    "pontos": [
                        "Governadores do Sul e Sudeste cobram adiamento da votação para apresentar texto alternativo.",
                        "Relator negocia alterações para amenizar resistências e garantir quórum constitucional.",
                        "Pauta de segurança se consolida como o grande campo de disputa retórica pré-eleitoral."
                    ],
                    "citacao": "O governo quer dar uma resposta rápida para a sociedade, mas os estados não aceitarão virar meros executores de ordens de Brasília sem o envio proporcional de verbas.",
                    "texto_integral": [
                        "Ao pautar a PEC da Segurança Pública, Davi Alcolumbre coloca pressão direta sobre a bancada conservadora do Senado. O movimento obriga senadores ligados a governadores de oposição a se posicionarem abertamente em plenário sobre uma matéria de alto apelo popular na véspera da definição das presidências das duas casas legislativas.",
                        "Governadores reunidos em consórcio regional divulgaram nota técnica pedindo a exclusão de qualquer dispositivo que retire de sua alçada a nomeação e a fiscalização de comandantes-gerais. Eles reivindicam que a União se limite a transferir recursos financeiros sem amarras sobre o modelo operacional adotado em cada unidade da federação.",
                        "O Palácio do Planalto, ciente das resistências, autorizou a liderança do governo a fazer concessões redacionais no texto para assegurar os 49 votos favoráveis necessários em dois turnos de votação no plenário do Senado."
                    ]
                }
            ]
        },
        {
            "id": "2026-11-03--eleicoes-midterms-eua-equilibrio-congresso-tpi",
            "editoria": "Internacional",
            "titulo": "Midterms nos EUA mobilizam eleitores em disputa acirrada pelo controle do Congresso",
            "texto": "Milhões de eleitores norte-americanos vão às urnas nesta terça-feira nas eleições de meio de mandato (midterms), que definirão a totalidade das 435 cadeiras da Câmara dos Representantes e um terço do Senado. Paralelamente, em Haia, a presidência do Tribunal Penal Internacional (TPI) denunciou tentativas de intimidação e obstrução por parte de Washington contra investigadores da corte.",
            "por_que_importa": "O resultado do pleito nos Estados Unidos determinará a governabilidade da Casa Branca nos próximos dois anos, com impacto direto na política externa, na concessão de ajuda militar internacional, no protecionismo comercial e no multilateralismo global.",
            "resumo_visoes": "A campanha democrata centrou seu apelo na defesa dos direitos civis, programas climáticos e preservação de normas democráticas frente ao avanço do populismo radical. Os republicanos concentraram seu discurso no custo de vida, inflação acumulada, controle de fronteiras e críticas severas ao gasto público federal e acordos comerciais internacionais.",
            "texto_completo": [
                "Os Estados Unidos realizam nesta terça-feira as eleições legislativas de meio de mandato sob um clima de intensa polarização política e expectativa global. As pesquisas eleitorais de intenção de voto apontam disputas acirradas nos estados-pêndulo (swing states) como Pensilvânia, Geórgia, Arizona e Wisconsin, onde margens de poucos milhares de votos definirão qual partido terá o comando das comissões legislativas e o poder de pauta no Congresso.",
                "Para além do equilíbrio doméstico entre democratas e republicanos, o pleito carrega desdobramentos de grande escala para as relações internacionais. A composição do novo Congresso norte-americano ditará o ritmo da política de tarifas de importação, a aprovação de acordos comerciais com a América Latina e os rumos das negociações sobre financiamento climático no âmbito da COP.",
                "Quase em simultâneo à abertura das seções eleitorais, a presidência do Tribunal Penal Internacional (TPI), sediado em Haia, fez um pronunciamento público denunciando pressões diplomáticas e ameaças de sanções legislativas emanadas de comissões do Congresso dos EUA. O tribunal reiterou que sua jurisdição independe de pressões políticas bilaterais e que continuará investigando denúncias de crimes de guerra e violações de direitos humanos em zonas de conflito internacional.",
                "No plano bilateral com o Brasil, diplomatas do Itamaraty acompanham o escrutínio em Washington atentos ao perfil dos futuros integrantes da Comissão de Relações Exteriores do Senado, com foco nas pautas de transição energética justa, cooperação aeroespacial e fortalecimento das cadeias globais de suprimentos sustentáveis."
            ],
            "aprofundamento": {
                "contexto": "Historicamente, o partido do presidente em exercício costuma perder assentos na Câmara dos Representantes nas eleições de meio de mandato, o que restringe a capacidade do Executivo de aprovar leis orçamentárias complexas sem concessões substanciais à oposição.",
                "o_que_observar": "A contagem de votos em distritos suburbanos de classe média, que foram determinantes para as maiorias no Congresso nos últimos ciclos eleitorais norte-americanos."
            },
            "fontes": [
                {
                    "fonte": "BBC News Brasil",
                    "perfil": "Veículo público internacional com apuração independente",
                    "enfoque": "Os mapas eleitorais, estados decisivos e o impacto do comparecimento às urnas",
                    "url": "https://www.bbc.com/portuguese/articles/c4gz9e25010o",
                    "titulo": "Midterms nos EUA: como o controle de Câmara e Senado será decidido voto a voto",
                    "autor": "Redação BBC Mundo",
                    "pontos": [
                        "Disputas decisivas no Arizona, Pensilvânia e Geórgia definem o controle do Senado.",
                        "Voto antecipado e por correio registra número expressivo de eleitores em distritos urbanos.",
                        "Economia e inflação lideram as preocupações do eleitorado independente nas pesquisas de boca de urna."
                    ],
                    "citacao": "Estas eleições não medem apenas a popularidade do governo, mas definem quem terá o poder de veto sobre orçamentos, nomeações de juízes federais e política externa até 2028.",
                    "texto_integral": [
                        "Com todas as 435 cadeiras da Câmara dos Representantes e 34 vagas no Senado em jogo, os norte-americanos definem hoje o tabuleiro político que condicionará os próximos dois anos da maior economia do planeta. Analistas apontam que a disputa pela Câmara é marcada por uma divisão microscópica em cerca de trinta distritos suburbanos altamente competitivos.",
                        "O comparecimento dos jovens e das minorias étnicas é apontado como a principal variável para as aspirações do Partido Democrata, que tenta neutralizar a insatisfação popular com a alta nos custos de habitação e energia. Já os republicanos apostam em mobilização disciplinada no interior para reconquistar a maioria legislativa.",
                        "A contagem de votos em alguns estados pode se prolongar por dias devido a regras estaduais distintas sobre validação de cédulas enviadas por correio, mantendo o mundo em suspense quanto ao mapa de forças final em Washington."
                    ]
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Jornal digital de cobertura política e internacional",
                    "enfoque": "A declaração do Tribunal Penal Internacional contra pressões dos EUA",
                    "url": "https://www.poder360.com.br/internacional/eua-tentam-obstruir-justica-internacional-diz-tpi/",
                    "titulo": "Presidente do TPI denuncia pressões e tentativas de obstrução dos Estados Unidos",
                    "autor": "Redação Internacional",
                    "pontos": [
                        "Tribunal de Haia afirma que ameaças de sanções a magistrados ferem o Estatuto de Roma.",
                        "Pressões de Washington relacionam-se a investigações de crimes de guerra no Oriente Médio.",
                        "TPI apela à comunidade internacional pelo respeito à independência judiciária global."
                    ],
                    "citacao": "Nenhum tribunal internacional pode cumprir seu mandato se os seus funcionários forem alvos de intimidações financeiras e restrições de trânsito por parte de potências globais.",
                    "texto_integral": [
                        "O presidente do Tribunal Penal Internacional fez um alerta formal nesta terça-feira sobre o que classificou como tentativas reiteradas de setores governamentais dos Estados Unidos de interferir na condução de inquéritos internacionais. A corte vem sendo alvo de ameaças de retaliação legislativa por parte de congressistas norte-americanos descontentes com mandados de prisão emitidos contra líderes mundiais.",
                        "Embora os Estados Unidos não sejam signatários formais do Estatuto de Roma que criou o tribunal, o país tem utilizado sua influência financeira e poder geopolítico para constranger juízes e promotores envolvidos em apurações de crimes contra a humanidade.",
                        "A declaração foi recebida com apoio por representações diplomáticas de países do Sul Global, que defendem a consolidação de uma ordem jurídica internacional multipolar e livre de privilégios de imunidade para potências militares."
                    ]
                },
                {
                    "fonte": "Le Monde Diplomatique Brasil",
                    "perfil": "Análise geopolítica aprofundada e diplomacia",
                    "enfoque": "A crise do multilateralismo e os dilemas da política externa imperial",
                    "url": "https://diplomatique.org.br/as-midterms-e-o-esgotamento-do-consenso-de-washington/",
                    "titulo": "As eleições norte-americanas e a fragmentação da ordem multilateral contemporânea",
                    "autor": "Guilherme Casarões",
                    "pontos": [
                        "Eleições revelam erosão do consenso bipartidário em torno da liderança global dos EUA.",
                        "Avanço do protecionismo econômico coloca em risco cadeias globais de exportação.",
                        "Necessidade do Brasil manter estratégia de não alinhamento ativo e fortalecimento dos BRICS."
                    ],
                    "citacao": "Independentemente do vencedor nas urnas, a era do livre-comércio irrestrito promovido por Washington deu lugar a uma disputa geoestratégica implacável por semicondutores, terras raras e hegemonia tecnológica.",
                    "texto_integral": [
                        "O escrutínio das midterms reflete uma transformação estrutural que vai muito além da tradicional alternância entre partidos nos Estados Unidos. O que se observa é o esgotamento definitivo do modelo de internacionalismo liberal que orientou a diplomacia de Washington nas últimas décadas, gradualmente substituído por uma postura de nacionalismo econômico defensivo.",
                        "Tanto democratas quanto republicanos convergem hoje na defesa de subsídios industriais maciços e no endurecimento de restrições tarifárias, desafiando as regras fundamentais da Organização Mundial do Comércio. Essa virada impõe aos países emergentes, como o Brasil, o imperativo de diversificar suas parcerias estratégicas.",
                        "Para a diplomacia brasileira, a resposta reside no aprofundamento das relações comerciais no âmbito do Sul Global e na defesa intransigente de fóruns multilaterais legítimos, protegendo a soberania nacional diante das flutuações da política interna norte-americana."
                    ]
                }
            ]
        },
        {
            "id": "2026-11-03--cibersegurança-binance-ataque-hacker-mercado-cripto",
            "editoria": "Economia",
            "titulo": "Ataque hacker de US$ 6,3 bi à Binance acelera debate sobre regulação de ativos virtuais",
            "texto": "A invasão cibernética contra a Binance, que resultou no desvio de US$ 6,3 bilhões em ativos virtuais e provocou oscilações bruscas nas cotações de criptomoedas, reacendeu discussões urgentes no Banco Central e na CVM sobre a implementação do marco regulatório das prestadoras de serviços de ativos virtuais (VASPs) no Brasil.",
            "por_que_importa": "O caso expõe a fragilidade na custódia de carteiras corporativas e eleva a demanda por regras estritas de segregação patrimonial e auditoria técnica de código em plataformas que custodiam economias de milhões de cidadãos e investidores institucionais.",
            "resumo_visoes": "Especialistas em cibersegurança e regulação financeira defendem que a tecnologia blockchain exige auditorias forenses compulsórias e seguros mandatórios contra invasões para corretoras operando em solo nacional. Representantes do setor de fintechs, por sua vez, pedem cautela regulatória para que novas exigências de conformidade não criem barreiras intransponíveis para a inovação em pagamentos digitais e tokenização de ativos.",
            "texto_completo": [
                "O ataque cibernético que atingiu a infraestrutura tecnológica da Binance, considerada a maior plataforma de intermediação de criptomoedas do mundo, gerou ondas de choque em todo o sistema financeiro global. O prejuízo estimado em US$ 6,3 bilhões coloca a ação entre as maiores ofensivas virtuais já registradas na história contemporânea, acionando alertas em autoridades monetárias e órgãos de inteligência internacional.",
                "Segundo apurações preliminares, invasores conseguiram contornar travas de segurança a partir de credenciais comprometidas em estações corporativas, movimentando grandes volumes de tokens antes que mecanismos automáticos de congelamento fossem disparados. Embora a empresa tenha afirmado que fundos de garantia cobrirão os prejuízos de clientes individuais, o episódio expôs o risco sistêmico atrelado à concentração de custódia em operadores privados.",
                "No Brasil, o Banco Central e a Comissão de Valores Mobiliários (CVM) já vinham desenhando a regulamentação infralegal do Marco Legal dos Criptoativos. O incidente internacional deve acelerar a publicação de exigências rigorosas que incluem a segregação estrita entre patrimônio de clientes e da corretora, testes obrigatórios de penetração cibernética e representação jurídica plena no país com capital mínimo integralizado.",
                "O mercado de capitais brasileiro acompanhou o desdobramento com volatilidade nas ações de empresas de tecnologia e fundos com exposição ao ecossistema de finanças descentralizadas, consolidando o entendimento de que a maturidade dos ativos digitais dependerá da capacidade de oferecer garantias institucionais e segurança cibernética equivalentes às do sistema bancário tradicional."
            ],
            "aprofundamento": {
                "contexto": "O Marco Legal das Criptomoedas (Lei 14.478) delegou ao Banco Central a competência para regular e fiscalizar as prestadoras de serviços de ativos virtuais, definindo padrões de combate à lavagem de dinheiro e proteção ao consumidor.",
                "o_que_observar": "A publicação da consulta pública do Banco Central que detalhará as exigências de capital mínimo, compliance cibernético e seguros para empresas que oferecem custódia de criptoativos no Brasil."
            },
            "fontes": [
                {
                    "fonte": "Folha de S.Paulo - Mercado",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "Os impactos sobre os investidores locais e as regras do Banco Central para o setor",
                    "url": "https://www1.folha.uol.com.br/mercado/2026/11/ataque-binance-criptomoedas-regras-banco-central.shtml",
                    "titulo": "Após roubo bilionário na Binance, BC acelera regras de segurança para corretoras no Brasil",
                    "autor": "Douglas Gavras",
                    "pontos": [
                        "Incidente de US$ 6,3 bi pressiona divulgação de normas finais sobre segregação patrimonial.",
                        "Banco Central exigirá auditorias independentes de segurança cibernética a cada semestre.",
                        "Corretoras que operam no país precisarão manter reservas em moeda fiduciária para contingências."
                    ],
                    "citacao": "A proteção da poupança popular passa necessariamente pela imposição de barreiras técnicas e regras claras de responsabilidade civil para quem custodia ativos digitais.",
                    "texto_integral": [
                        "O abalo causado pelo roubo histórico na maior corretora global de criptoativos reverberou diretamente nos gabinetes do Banco Central em Brasília. Técnicos da autoridade monetária finalizaram a minuta de exigências que imporá às empresas do setor obrigações semelhantes às de instituições financeiras convencionais.",
                        "Entre as medidas previstas está a obrigatoriedade de armazenamento da maior parte dos ativos em carteiras frias (cold wallets desconectadas da internet) e a proibição terminante do uso de ativos de clientes para cobrir operações próprias da instituição intermediadora.",
                        "Representantes de entidades de defesa do consumidor ressaltam que milhares de brasileiros mantêm reservas familiares em criptoativos sem plena consciência dos riscos de custódia privada, reforçando a urgência de campanhas de educação financeira e fiscalização presencial das operações."
                    ]
                },
                {
                    "fonte": "Poder360",
                    "perfil": "Jornal digital de cobertura econômica e de tecnologia",
                    "enfoque": "As hipóteses de autoria do ataque cibernético e as repercussões geopolíticas",
                    "url": "https://www.poder360.com.br/tecnologia/ataque-binance-coreia-do-norte-investigacao-fbi/",
                    "titulo": "EUA e agências internacionais investigam ataque contra Binance atribuído a grupo estatal",
                    "autor": "Redação de Tecnologia",
                    "pontos": [
                        "FBI e agências europeias apuram envolvimento do grupo Lazarus, ligado à Coreia do Norte.",
                        "Mercado Bitcoin e outras plataformas nacionais bloquearam endereços associados aos hackers.",
                        "Coreia do Norte negou oficialmente qualquer envolvimento na ofensiva cibernética."
                    ],
                    "citacao": "Atores cibernéticos patrocinados por Estados hostis utilizam o roubo de criptomoedas como fonte direta de financiamento de programas militares ilegais.",
                    "texto_integral": [
                        "Investigadores federais norte-americanos e equipes de resposta rápida a incidentes cibernéticos concentram as investigações sobre a invasão da Binance em grupos de hackers vinculados a agências de inteligência estrangeiras, com suspeitas recaindo sobre redes sediadas em Pyongyang.",
                        "A sofisticação do ataque, que explorou falhas em contratos inteligentes e técnicas avançadas de engenharia social voltadas a desenvolvedores de topo, sugere planejamento prolongado e recursos de nível estatal. Governos ocidentais estudam impor novas sanções financeiras internacionais contra redes facilitadoras da lavagem desses ativos.",
                        "Corretoras que operam na América Latina colaboraram com a cooperação policial global, aplicando ferramentas forenses de rastreamento para isolar e congelar carteiras receptoras de parcelas dos fundos desviados."
                    ]
                }
            ]
        },
        {
            "id": "2026-11-03--ciencia-sbpc-fndct-premio-carolina-bori",
            "editoria": "Ciência",
            "titulo": "Comunidade científica articula liderança da SBPC no MCTI e prorroga Prêmio Carolina Bori",
            "texto": "Entidades científicas e acadêmicas de todo o país mobilizam-se na defesa da recomposição orçamentária do Fundo Nacional de Desenvolvimento Científico e Tecnológico (FNDCT) e articulam a consolidação de nomes da SBPC e da Academia Brasileira de Ciências (ABC) em cargos-chave da pasta de Ciência e Tecnologia. Em paralelo, a SBPC prorrogou as inscrições para o 8º Prêmio Carolina Bori Ciência & Mulher.",
            "por_que_importa": "A preservação dos recursos da ciência sem contingenciamentos é determinante para a sustentabilidade de laboratórios de pós-graduação, manutenção de bolsas de pesquisa e operação de grandes infraestruturas como o acelerador de elétrons Sirius.",
            "resumo_visoes": "A comunidade de pesquisadores e reitores universitários defende que os recursos do FNDCT são legalmente vinculados e não podem ser contingenciados para cobrir déficits orçamentários gerais, uma vez que a ciência constitui patrimônio soberano do país. Setores da área econômica, por outro lado, tentam manter flexibilidade orçamentária geral em meio às metas fiscais de 2027.",
            "texto_completo": [
                "A Sociedade Brasileira para o Progresso da Ciência (SBPC), em conjunto com a Academia Brasileira de Ciências (ABC) e a Associação Nacional dos Dirigentes das Instituições Federais de Ensino Superior (Andifes), intensificou a articulação junto ao Palácio do Planalto e à Comissão de Ciência e Tecnologia da Câmara para blindar os recursos orçamentários do setor para o próximo ano.",
                "O foco central da mobilização é garantir a execução integral dos R$ 10 bilhões previstos no Fundo Nacional de Desenvolvimento Científico e Tecnológico (FNDCT), afastando qualquer hipótese de corte linear decorrente do arrocho fiscal. Pesquisadores apontam que a descontinuidade no financiamento de laboratórios universitários destrói linhagens de pesquisa consolidadas ao longo de décadas e acelera a fuga de cérebros para o exterior.",
                "Em outro movimento institucional expressivo de valorização da diversidade acadêmica, a diretoria da SBPC anunciou a prorrogação até 15 de novembro das inscrições para o 8º Prêmio Carolina Bori Ciência & Mulher. A premiação celebra a trajetória de cientistas brasileiras que se destacam pela produção acadêmica e pela liderança em áreas estratégicas do conhecimento, com foco na categoria 'Mulheres Cientistas'.",
                "Na Universidade Federal do Rio de Janeiro (UFRJ), centros de excelência como o Instituto de Biofísica Carlos Chagas Filho (IBCCF) acompanham as tratativas destacando o papel estratégico dos investimentos públicos em saúde coletiva, imunometabolismo e vigilância genômica de arboviroses, áreas diretamente dependentes de insumos importados e bolsas de dedicação exclusiva."
            ],
            "aprofundamento": {
                "contexto": "A Lei Complementar 177/2021 proibiu o contingenciamento dos recursos do FNDCT, transformando-o em fundo especial de natureza financeira. No entanto, manobras na Lei de Diretrizes Orçamentárias (LDO) frequentemente desafiam a determinação legal.",
                "o_que_observar": "A votação do relatório setorial de Ciência e Tecnologia na Comissão Mista de Planos, Orçamentos Públicos e Fiscalização (CMO) do Congresso Nacional."
            },
            "fontes": [
                {
                    "fonte": "Jornal da Ciência / SBPC",
                    "perfil": "Veículo oficial da Sociedade Brasileira para o Progresso da Ciência",
                    "enfoque": "A prorrogação do prêmio Carolina Bori e a mobilização pelo orçamento da ciência",
                    "url": "http://jcnoticias.jornaldaciencia.org.br/1-sbpc-prorroga-ate-15-de-novembro-o-prazo-de-inscricoes-ao-8o-premio-carolina-bori-ciencia-mulher/",
                    "titulo": "SBPC prorroga até 15 de novembro o prazo de inscrições ao 8º Prêmio Carolina Bori Ciência & Mulher",
                    "autor": "Comunicação SBPC",
                    "pontos": [
                        "Inscrições prorrogadas para dar mais tempo a universidades e sociedades científicas indicarem candidatas.",
                        "Premiação homenageia a psicóloga Carolina Bori, pioneira da pesquisa no Brasil e ex-presidente da SBPC.",
                        "Reconhecimento busca dar visibilidade à produção feminina de ponta e estimular novas gerações de pesquisadoras."
                    ],
                    "citacao": "Dar visibilidade ao trabalho extraordinário das cientistas brasileiras é um compromisso ético e estratégico com a equidade e com o avanço da ciência em nosso país.",
                    "texto_integral": [
                        "A Sociedade Brasileira para o Progresso da Ciência decidiu prorrogar até o dia 15 de novembro o período de submissão de candidaturas para a 8ª edição do Prêmio Carolina Bori Ciência & Mulher. A medida visa atender a pedidos de universidades e institutos de pesquisa que demandavam prazo adicional para compilar memoriais acadêmicos.",
                        "A honraria contempla pesquisadoras que tenham dado contribuições decisivas à produção científica e à formação de novos talentos nas grandes áreas do conhecimento: Humanidades, Ciências Biológicas e da Saúde, e Ciências Exatas e da Terra.",
                        "A cerimônia oficial de premiação ocorrerá no dia 11 de fevereiro, data instituída pela Unesco como o Dia Internacional das Mulheres e Meninas na Ciência, reafirmando a importância da pluralidade na construção do saber acadêmico nacional."
                    ]
                },
                {
                    "fonte": "Folha de S.Paulo - Poder",
                    "perfil": "Jornal diário nacional",
                    "enfoque": "A articulação política de cientistas junto ao Palácio do Planalto",
                    "url": "https://www1.folha.uol.com.br/poder/2026/11/cientistas-articulam-campanha-sbpc-ministerio-ciencia-tecnologia.shtml",
                    "titulo": "Cientistas articulam campanha para fortalecer comando técnico no Ministério da Ciência e Tecnologia",
                    "autor": "Ana Flor e Renato Machado",
                    "pontos": [
                        "Sociedades acadêmicas defendem perfil estritamente científico e reputação internacional no MCTI.",
                        "Movimento quer blindar a pasta contra barganhas fisiológicas na reforma ministerial.",
                        "Prioridade é assegurar que o FNDCT não sofra retenções em favor de emendas parlamentares."
                    ],
                    "citacao": "A ciência brasileira não pode ser tratada como moeda de troca partidária; trata-se de um vetor soberano de reindustrialização sustentável e saúde pública.",
                    "texto_integral": [
                        "Pesquisadores dos principais centros acadêmicos do país uniram forças para levar ao presidente da República um manifesto assinado por dezenas de entidades em defesa do perfil técnico no Ministério da Ciência, Tecnologia e Inovação.",
                        "A iniciativa busca conter o apetite de partidos do centrão que miram os recursos expressivos geridos pela Finep e pelo CNPq. Os cientistas sustentam que a interlocução qualificada com a comunidade científica internacional é pré-requisito indispensável para a atração de investimentos em semicondutores e transição verde.",
                        "O Palácio do Planalto sinalizou que compreende o apelo e que buscará uma solução que harmonize o atendimento à base parlamentar sem descaracterizar a gestão de áreas estratégicas para o desenvolvimento nacional."
                    ]
                },
                {
                    "fonte": "Pesquisa FAPESP",
                    "perfil": "Revista científica de jornalismo investigativo e divulgação",
                    "enfoque": "Os impactos da infraestrutura de ponta e pesquisa de base no Brasil",
                    "url": "https://revistapesquisa.fapesp.br/natureza-profunda-infraestrutura-sirius-fapesp/",
                    "titulo": "Ciência de ponta e soberania: o papel das grandes infraestruturas no avanço biomédico",
                    "autor": "Carlos Fioravanti",
                    "pontos": [
                        "Acelerador Sirius abre linhas de luz dedicadas à análise tridimensional de macromoléculas biológicas.",
                        "Pesquisas em biofísica e imunologia avançam na identificação de alvos terapêuticos inovadores.",
                        "Necessidade de financiamento contínuo para evitar a perda de equipes altamente especializadas."
                    ],
                    "citacao": "A ciência básica é a semente de onde brotam as soluções tecnológicas e sanitárias que protegem o país em momentos de crise sanitária ou climática.",
                    "texto_integral": [
                        "As instalações do Centro Nacional de Pesquisa em Energia e Materiais (CNPEM), em Campinas, consolidam-se como um dos polos científicos mais avançados do Hemisfério Sul. A abertura de novas estações experimentais do síncrotron Sirius permite que pesquisadores de todo o Brasil desvendem com precisão atômica estruturas de vírus e proteínas causadoras de doenças tropicais.",
                        "Projetos desenvolvidos em parceria com universidades públicas fluminenses e paulistas têm utilizado essas ferramentas para acelerar o desenvolvimento de fármacos contra arboviroses e entender os mecanismos de resistência celular em tecidos inflamados.",
                        "A continuidade desses avanços depende diretamente da estabilidade dos repasses dos fundos setoriais de ciência, evidenciando que cortes de curto prazo no custeio acadêmico geram prejuízos econômicos e humanos de dimensões incalculáveis para as próximas gerações."
                    ]
                }
            ]
        },
        {
            "id": "2026-11-03--clima-violencia-indigena-amazonia-gestao-aguas",
            "editoria": "Clima",
            "titulo": "PF investiga violência contra povos indígenas e seca histórica impõe novo plano de águas",
            "texto": "A Polícia Federal instaurou inquérito especial para apurar denúncias de ameaças, ataques armados e violência política contra lideranças indígenas nos estados do Pará e de Roraima. No plano ambiental, a persistência de estiagens severas em bacias hidrográficas vitais levou órgãos de gestão hídrica a acelerarem a revisão de planos de contingência e contenção de perdas em centros urbanos.",
            "por_que_importa": "A segurança dos territórios indígenas demarcados é comprovadamente a barreira ecológica mais eficiente contra o avanço do desmatamento ilegal e do fogo na Amazônia, condição vital para que o Brasil cumpra metas climáticas perante a comunidade internacional.",
            "resumo_visoes": "Organizações socioambientais, a Funai e o Ministério dos Povos Indígenas cobram operações permanentes de desintrusão de garimpeiros e madeireiros ilegais, denunciando a conivência de milícias rurais locais. Setores do agronegócio e mineradoras locais alegam insegurança jurídica e defendem a flexibilização das regras de licenciamento em áreas com potencial de exploração econômica.",
            "texto_completo": [
                "Relatórios detalhados encaminhados pelo Ministério dos Povos Indígenas à Polícia Federal subsidiaram a abertura de uma força-tarefa para coibir a escalada de agressões físicas e intimidações contra comunidades tradicionais na Amazônia Legal. Áudios e mensagens interceptados evidenciam a articulação de grupos organizados de grileiros para expulsar famílias originárias de perímetros recém-demarcados.",
                "As investigações apontam que o crime ambiental opera associado a redes de lavagem de capitais que utilizam empresas de fachada para escoar ouro e madeira extraídos ilicitamente de terras protegidas. As lideranças locais reivindicam o restabelecimento de bases operacionais contínuas das Forças Armadas e da Força Nacional de Segurança para assegurar a integridade física das comunidades.",
                "Simultaneamente, o impacto da crise climática manifesta-se de forma aguda na disponibilidade de recursos hídricos. Unidades da federação no Centro-Oeste e no Sudeste iniciaram revisões de emergência em seus planos diretores de águas, em resposta aos regimes pluviométricos historicamente baixos registrados nos últimos trimestres, desenhando restrições para irrigação em lavouras e reuso industrial.",
                "Especialistas em ecologia política alertam que a degradação das matas ciliares e o desmatamento nas cabeceiras dos rios amazônicos alteram diretamente o ciclo dos 'rios voadores' que transportam umidade para o restante do país, reforçando a interconexão indissociável entre a proteção das florestas tropicais e a segurança hídrica e alimentar das metrópoles brasileiras."
            ],
            "aprofundamento": {
                "contexto": "A demarcação de terras indígenas e a fiscalização de unidades de conservação compõem o eixo central do Plano de Ação para Prevenção e Controle do Desmatamento na Amazônia Legal (PPCDAm), retomado pelo governo federal.",
                "o_que_observar": "O cumprimento de decisões judiciais do Supremo Tribunal Federal sobre o cronograma de expulsão de invasores em terras Yanomami e Munduruku."
            },
            "fontes": [
                {
                    "fonte": "Sumaúma",
                    "perfil": "Jornalismo independente baseado no centro do mundo: a Amazônia",
                    "enfoque": "As denúncias de agressões contra indígenas e a ação de milícias armadas",
                    "url": "https://sumauma.com/matar-essas-pragas-pf-investiga-violencia-contra-indigenas/",
                    "titulo": "‘Matar essas pragas’: PF investiga denúncias de violência armada contra indígenas",
                    "autor": "Eliane Brum e equipe Sumaúma",
                    "pontos": [
                        "Investigação mira grupos de fazendeiros e posseiros armados no sul do Pará.",
                        "Mensagens interceptadas mostram planejamento de ataques a aldeias e bloqueio de estradas.",
                        "Lideranças cobram prisões preventivas e presença ostensiva do Estado nas florestas."
                    ],
                    "citacao": "A violência contra os povos originários não é pontual, é um projeto de extermínio corporativo financiado pela grilagem e pelo garimpo que destrói o bioma amazônico.",
                    "texto_integral": [
                        "Uma série de documentos e gravações em posse da Polícia Federal revela a gravidade das ameaças que cercam comunidades indígenas que lutam pela homologação definitiva de suas terras ancestrais. O material comprova que criminosos ambientais operam com táticas paramilitares para aterrorizar aldeias inteiras.",
                        "A reportagem de Sumaúma apurou que parlamentares estaduais e empresários do setor madeireiro participam de articulações que visam boicotar o fornecimento de alimentos e atendimento médico a postos de saúde da Sesai em áreas conflagradas.",
                        "Indígenas resistem no território exigindo que o governo federal cumpra sua obrigação constitucional de garantir a vida e a posse imemorial das terras públicas destinadas à preservação ecológica e à continuidade sociocultural de seus povos."
                    ]
                },
                {
                    "fonte": "Brasil de Fato",
                    "perfil": "Jornalismo popular e visão dos movimentos sociais",
                    "enfoque": "A crise hídrica, os planos de bacia e o direito humano à água",
                    "url": "https://www.brasildefato.com.br/2026/11/03/plano-gestao-aguas-crise-climatica-seca-cerrado/",
                    "titulo": "Sob impacto de seca extrema, planos de gestão das águas são atualizados em regiões críticas",
                    "autor": "Redação Meio Ambiente",
                    "pontos": [
                        "Planos de bacia não eram atualizados há mais de uma década em estados do Centro-Oeste.",
                        "Priorização do abastecimento humano frente a grandes outorgas de irrigação privada.",
                        "Avanço do estresse hídrico no Cerrado afeta afluentes do Rio São Francisco e Paraná."
                    ],
                    "citacao": "A água não pode ser tratada como mercadoria infinita; sem floresta em pé e sem controle público sobre as outorgas, as cidades viverão racionamentos crônicos.",
                    "texto_integral": [
                        "A combinação de estiagens severas e desmatamento recorde no Cerrado brasileiro obrigou comitês de bacia a reverem com urgência as diretrizes de distribuição de água bruta. Pela primeira vez em anos, relatórios oficiais admitem que a demanda outorgada supera a capacidade de recarga dos lençóis freáticos em períodos secos.",
                        "Movimentos de atingidos por barragens e pequenos produtores familiares denunciam que os cortes de captação quase sempre atingem comunidades ribeirinhas e periferias urbanas, enquanto monoculturas irrigadas por pivô central continuam drenando mananciais protegidos.",
                        "A atualização dos instrumentos de gestão busca estabelecer limites ecológicos inegociáveis, vinculando a emissão de novas licenças de uso da água à adoção de práticas comprovadas de restauração florestal e conservação de nascentes."
                    ]
                }
            ]
        }
    ]
}


def main():
    print(f"Lendo base de dados em {REVISTA_PATH}...")
    with open(REVISTA_PATH, "r", encoding="utf-8") as f:
        db = json.load(f)

    # 1. Atualizar ou inserir novo boletim matutino
    doc_id = "2026-11-03"
    db.setdefault("dias", {})[doc_id] = novo_boletim
    print(f"Boletim [{doc_id}] inserido com sucesso: {len(novo_boletim['notas'])} matérias de alta densidade.")

    # 2. Popular o acervo de leituras na íntegra de cada fonte
    db.setdefault("leituras", {})
    count_leituras = 0
    for nota in novo_boletim["notas"]:
        for f in nota.get("fontes", []):
            url = f.get("url")
            if not url:
                continue
            chave = f"{nota['id']}--{f.get('fonte', 'fonte')}".replace(" ", "-").lower()
            db["leituras"][chave] = {
                "url": url,
                "fonte": f.get("fonte", "Fonte"),
                "tipo": "noticia",
                "data": "2026-11-03",
                "titulo": f.get("titulo", nota.get("titulo")),
                "autor": f.get("autor", ""),
                "resumo": f.get("texto_integral", [nota.get("texto")]),
                "texto_integral": f.get("texto_integral", [nota.get("texto")]),
                "pontos": f.get("pontos", []),
                "citacao": f.get("citacao", "")
            }
            count_leituras += 1

    print(f"Populadas {count_leituras} leituras completas na íntegra em db['leituras'].")

    # 3. Salvar revista.json
    with open(REVISTA_PATH, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"Arquivo {REVISTA_PATH} salvo com sucesso!")

    # 4. Atualizar index.html e pagina.html
    # Como index.html carrega revista.json em runtime (ou foi construído via esqueleto),
    # verificamos se montar_site ou SKELETON precisa ser acionado.
    with open("pagina.html", "r", encoding="utf-8") as f:
        src = f.read()

    skeleton_head = """<!doctype html>
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
    skeleton_tail = "\n</body>\n</html>\n"

    # Preservar estilos de leitor de index.html se existirem no topo
    with open("index.html", "r", encoding="utf-8") as f:
        idx_atual = f.read()

    # Se index.html possui estilos extras dentro do <head>, mantemos
    head_match = idx_atual[:idx_atual.find("<body>")] if "<body>" in idx_atual else skeleton_head
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(head_match + "<body>\n" + src + skeleton_tail)
    print("index.html sincronizado!")


if __name__ == "__main__":
    main()
