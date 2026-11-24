#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/curadoria_revistas_semanais.py
------------------------------------
Curadoria e estruturação rica das Revistas Semanais do Beeper para o Modo Leitor na aba Semana:
- The Economist (Reino Unido / Global): Diplomacia, Geopolítica Global, Leaders e Relações Internacionais
- CartaCapital (Brasil): Política Nacional, Economia e Análise Institucional
- Revista Veja (Brasil): Poder, Sociedade e Conjuntura
- The New York Times Magazine (Estados Unidos): Ensaios de Fôlego, Diplomacia Cultural e Geopolítica
"""

import os
import json
import hashlib
from datetime import datetime

def obter_revistas_semanais(imagens_mapa):
    hoje_iso = "2026-11-07"
    
    return {
        "data_edicao": hoje_iso,
        "resumo": "Panorama aprofundado das principais revistas de análise política, geopolítica e diplomacia internacional da semana. Clique em qualquer publicação para acessar seus ensaios, editoriais e grandes reportagens no Modo Leitor.",
        "contraste": "Confronto entre a visão liberal-global do The Economist, os ensaios geopolíticos do NYT Magazine e as análises políticas nacionais da CartaCapital e da Veja.",
        "publicacoes": [
            {
                "revista": "The Economist",
                "pais": "Reino Unido / Global",
                "escopo": "internacional",
                "imagem": imagens_mapa.get("The Economist", "capas/cf1dd44af367e7cb9c6582406ab77d50.jpg"),
                "site": "https://www.economist.com",
                "manchete": "The New Geopolitics of Order: Diplomacia, Multipolaridade e o Futuro das Alianças Ocidentais",
                "manchete_original": "The New Geopolitics of Order: Diplomacy, Multipolarity and the Future of Western Alliances",
                "nota": "Análise editorial de fôlego sobre os impasses da governança global, o desgaste do multilateralismo tradicional e os movimentos diplomáticos nas cúpulas de líderes.",
                "resumo_edicao": [
                    "A edição semanal do The Economist destaca a reconfiguração dos eixos diplomáticos mundiais em meio à transição política nos Estados Unidos e ao avanço das potências médias na Ásia e no Oriente Médio.",
                    "O periódico dedica seus cadernos de Leaders, International e Briefing a esmiuçar os impactos das novas diretrizes comerciais e de defesa nas chancelarias europeias e no Sul Global."
                ],
                "editorial": {
                    "titulo": "The Test of Statecraft: A Arte da Diplomacia em Tempos de Ruptura",
                    "texto": [
                        "A ordem internacional construída no pós-guerra enfrenta seu momento de maior fragilidade conceitual. Não se trata apenas da contestação de fronteiras ou de rotas marítimas, mas da erosão do consenso diplomático sobre como gerir conflitos e transições energéticas compartilhadas.",
                        "Para os formuladores de política externa e para as economias abertas, a prudência estratégica exige menos retórica maniqueísta e maior capacidade pragmática de construir coalizões temáticas sobre comércio, segurança de cadeias produtivas e governança digital."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Leaders · Diplomacia e Ordem Global",
                        "pagina": "11",
                        "autor": "Redação The Economist",
                        "titulo": "A diplomacia das potências médias: como Índia, Brasil e Turquia arbitram o tabuleiro global",
                        "titulo_original": "Middle-Power Diplomacy: How Non-Aligned Giants Arbitrate Global Strategy",
                        "lide": "Com as superpotências travadas em disputas bilaterais assimétricas, os polos regionais consolidam protagonismo diplomático indispensável nas grandes negociações multilaterais.",
                        "texto": [
                            "Nas últimas duas décadas, o conceito de não-alinhamento evoluiu de uma postura defensiva para uma diplomacia ativa de múltiplos vetores. Países como Brasil, Índia, Turquia e África do Sul recusam adesão automática a blocos fechados e operam como articuladores indispensáveis em fóruns que vão da transição climática à segurança alimentar.",
                            "Essa flexibilidade diplomática permite negociar acordos de infraestrutura com Pequim ao mesmo tempo em que aprofundam parcerias de alta tecnologia com Washington e capitais europeias. O resultado é um tabuleiro mais fragmentado, mas também menos vulnerável a ultimatos hegemônicos.",
                            "Para a diplomacia ocidental, a lição central consiste em abandonar a exigência de alinhamentos binários e valorizar compromissos pragmáticos que gerem estabilidade nas rotas comerciais do Sul Global."
                        ],
                        "texto_integral": [
                            "Nas últimas duas décadas, o conceito de não-alinhamento evoluiu de uma postura defensiva para uma diplomacia ativa de múltiplos vetores. Países como Brasil, Índia, Turquia e África do Sul recusam adesão automática a blocos fechados e operam como articuladores indispensáveis em fóruns que vão da transição climática à segurança alimentar.",
                            "Essa flexibilidade diplomática permite negociar acordos de infraestrutura com Pequim ao mesmo tempo em que aprofundam parcerias de alta tecnologia com Washington e capitais europeias. O resultado é um tabuleiro mais fragmentado, mas também menos vulnerável a ultimatos hegemônicos.",
                            "Para a diplomacia ocidental, a lição central consiste em abandonar a exigência de alinhamentos binários e valorizar compromissos pragmáticos que gerem estabilidade nas rotas comerciais do Sul Global."
                        ],
                        "pontos": [
                            "Superação do alinhamento binário em favor de diplomacia multipolar pragmática.",
                            "Atuação decisiva de potências médias em fóruns climáticos e acordos de comércio multilateral."
                        ]
                    },
                    {
                        "caderno": "International · Cúpulas e Negociações",
                        "pagina": "23",
                        "autor": "Equipe de Correspondentes Internacionais",
                        "titulo": "Cimeira da Commonwealth e a diplomacia caribenha: reparações, clima e soberania",
                        "titulo_original": "The Commonwealth Summit: Climate Resilience and Sovereign Debt Diplomacy",
                        "lide": "Reunião de chefes de Estado em Antígua e Barbuda coloca a justiça climática e o financiamento de desastres naturais no centro da agenda das antigas colônias britânicas.",
                        "texto": [
                            "A participação do rei Charles III e do primeiro-ministro britânico Andy Burnham na Cimeira da Commonwealth revelou uma mudança de tom significativa nos debates entre Londres e os governos insulares do Caribe e do Pacífico.",
                            "Em vez de formalismos cerimoniais, os líderes locais impuseram discussões concretas sobre mecanismos de renegociação de dívida soberana após eventos climáticos extremos e fundos de compensação direta por danos ambientais históricos.",
                            "A iniciativa reflete uma tendência diplomática mais ampla: pequenas nações vulneráveis a desastres utilizam a diplomacia multilateral como alavanca de sobrevivência econômica e jurídica perante as maiores emissoras de carbono."
                        ],
                        "texto_integral": [
                            "A participação do rei Charles III e do primeiro-ministro britânico Andy Burnham na Cimeira da Commonwealth revelou uma mudança de tom significativa nos debates entre Londres e os governos insulares do Caribe e do Pacífico.",
                            "Em vez de formalismos cerimoniais, os líderes locais impuseram discussões concretas sobre mecanismos de renegociação de dívida soberana após eventos climáticos extremos e fundos de compensação direta por danos ambientais históricos.",
                            "A iniciativa reflete uma tendência diplomática mais ampla: pequenas nações vulneráveis a desastres utilizam a diplomacia multilateral como alavanca de sobrevivência econômica e jurídica perante as maiores emissoras de carbono."
                        ],
                        "pontos": [
                            "Pequenas nações insulares usam o direito internacional para exigir compensações climáticas.",
                            "Resistência a cláusulas de austeridade em cenários pós-desastres climáticos."
                        ]
                    },
                    {
                        "caderno": "United States · Eleições e Poder",
                        "pagina": "35",
                        "autor": "Bureau de Washington",
                        "titulo": "O novo mapa do Congresso americano e os limites da política externa unilateral",
                        "titulo_original": "Congress, Partisanship and the Constraints on Foreign Policy",
                        "lide": "A nova configuração de maiorias no Senado e na Câmara de Representantes exigirá concessões orçamentárias duras para a manutenção da ajuda externa e defesa.",
                        "texto": [
                            "As eleições parlamentares nos Estados Unidos demonstraram que o eleitorado priorizou temas domésticos de custo de vida e segurança de fronteira sobre os grandes compromissos de segurança internacional da Casa Branca.",
                            "Com maiorias estreitas e bancadas ideológicas intransigentes, o envio de fundos adicionais para a defesa europeia e para o Indo-Pacífico enfrentará um crivo fiscal sem precedentes no Capitólio.",
                            "Diplomatas estrangeiros em Washington já adaptam seus canais de interlocução, cientes de que a aprovação de tratados e a nomeação de embaixadores dependerão de barganhas prolongadas com comissões do Senado."
                        ],
                        "texto_integral": [
                            "As eleições parlamentares nos Estados Unidos demonstraram que o eleitorado priorizou temas domésticos de custo de vida e segurança de fronteira sobre os grandes compromissos de segurança internacional da Casa Branca.",
                            "Com maiorias estreitas e bancadas ideológicas intransigentes, o envio de fundos adicionais para a defesa europeia e para o Indo-Pacífico enfrentará um crivo fiscal sem precedentes no Capitólio.",
                            "Diplomatas estrangeiros em Washington já adaptam seus canais de interlocução, cientes de que a aprovação de tratados e a nomeação de embaixadores dependerão de barganhas prolongadas com comissões do Senado."
                        ],
                        "pontos": [
                            "Eleições americanas impõem freios fiscais aos pacotes de defesa internacional.",
                            "Canalização das negociações diplomáticas diretamente com comissões parlamentares no Capitólio."
                        ]
                    },
                    {
                        "caderno": "Asia · Geopolítica Regional",
                        "pagina": "42",
                        "autor": "Correspondente em Tóquio",
                        "titulo": "Japão reformula defesa civil e estratégia marítima no Leste Asiático",
                        "titulo_original": "Japan Reorganises Disaster Response and Regional Deterrence",
                        "lide": "A criação de uma agência nacional centralizada e a renovação dos laços de segurança com Seul e Taipé buscam blindar o arquipélago contra crises simultâneas.",
                        "texto": [
                            "O governo japonês deu início à unificação operacional das diretrizes de resposta a catástrofes naturais e segurança cibernética em uma única estrutura ministerial, espelhando a crescente complexidade das ameaças híbridas na região.",
                            "Paralelamente, a diplomacia japonesa acelerou a cooperação naval com a Coreia do Sul e parceiros do Sudeste Asiático, priorizando a segurança de rotas de navegação vitais para o abastecimento de semicondutores e energia.",
                            "Essa postura mais proativa sinaliza o fim definitivo do isolamento defensivo japonês, reposicionando Tóquio como um ator central da estabilidade geopolítica do Pacífico Ocidental."
                        ],
                        "texto_integral": [
                            "O governo japonês deu início à unificação operacional das diretrizes de resposta a catástrofes naturais e segurança cibernética em uma única estrutura ministerial, espelhando a crescente complexidade das ameaças híbridas na região.",
                            "Paralelamente, a diplomacia japonesa acelerou a cooperação naval com a Coreia do Sul e parceiros do Sudeste Asiático, priorizando a segurança de rotas de navegação vitais para o abastecimento de semicondutores e energia.",
                            "Essa postura mais proativa sinaliza o fim definitivo do isolamento defensivo japonês, reposicionando Tóquio como um ator central da estabilidade geopolítica do Pacífico Ocidental."
                        ],
                        "pontos": [
                            "Integração entre resiliência climática e segurança cibernética nacional.",
                            "Aproximação estratégica entre Japão e Coreia do Sul para vigilância de rotas marítimas."
                        ]
                    }
                ]
            },
            {
                "revista": "CartaCapital",
                "pais": "Brasil",
                "escopo": "nacional",
                "imagem": imagens_mapa.get("CartaCapital", "capas/1a0fd788fd6df433f8c0df1d89914a9e.jpg"),
                "site": "https://www.cartacapital.com.br",
                "manchete": "O Nó da Escala 6x1 e a Pressão Fiscal sobre o Trabalho: STF e Congresso no Centro do Debate",
                "manchete_original": None,
                "nota": "Matéria de capa examina o avanço da mobilização popular pelo fim da jornada 6x1 e as reações do empresariado industrial junto às cortes superiores.",
                "resumo_edicao": [
                    "A CartaCapital analisa as tensões entre as reivindicações da classe trabalhadora pela redução da jornada sem redução salarial e a contraofensiva da CNI e CNC no Supremo Tribunal Federal.",
                    "A edição aprofunda ainda o debate sobre o pacote de corte de gastos do Ministério da Fazenda e as implicações políticas da blindagem do orçamento social."
                ],
                "editorial": {
                    "titulo": "Carta ao Leitor · A Dignidade Humana e a Regulação do Trabalho",
                    "texto": [
                        "O debate sobre a escala 6x1 toca no coração do pacto social brasileiro. A insistência de setores do patronato em barrar a discussão por vias judiciais revela a histórica resistência à modernização das relações trabalhistas no país.",
                        "Um projeto de nação democrático não pode subordinar a saúde física e mental de milhões de trabalhadores a modelos de rentabilidade que não encontram paralelo sequer nos países de capitalismo avançado."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Capa · Sociedade e Trabalho",
                        "pagina": "16",
                        "autor": "Redação Política e Economia",
                        "titulo": "O levante contra a escala 6x1: mobilização das bases populares encurrala o parlamento",
                        "titulo_original": None,
                        "lide": "A adesão massiva de jovens trabalhadores às redes e manifestações de rua transformou a PEC do descanso semanal na pauta central da agenda política nacional.",
                        "texto": [
                            "O movimento que ganhou força espontânea entre trabalhadores do comércio e serviços rompeu a barreira da desmobilização tradicional e colocou deputados de diferentes espectros partidários sob pressão direta de seus eleitorados.",
                            "Diante da repercussão popular, bancadas do centro e até parlamentares da oposição viram-se constrangidos a assinar a proposição legislativa, gerando forte desconforto entre federações empresariais que contavam com o silêncio da pauta.",
                            "O embate agora se desloca para as comissões temáticas da Câmara, onde entidades sindicais e movimentos cívicos prometem vigília permanente para evitar desidratações no texto original."
                        ],
                        "texto_integral": [
                            "O movimento que ganhou força espontânea entre trabalhadores do comércio e serviços rompeu a barreira da desmobilização tradicional e colocou deputados de diferentes espectros partidários sob pressão direta de seus eleitorados.",
                            "Diante da repercussão popular, bancadas do centro e até parlamentares da oposição viram-se constrangidos a assinar a proposição legislativa, gerando forte desconforto entre federações empresariais que contavam com o silêncio da pauta.",
                            "O embate agora se desloca para as comissões temáticas da Câmara, onde entidades sindicais e movimentos cívicos prometem vigília permanente para evitar desidratações no texto original."
                        ],
                        "pontos": [
                            "Pressão digital e de rua força deputados do centro a apoiarem a tramitação da PEC.",
                            "Batalha jurídica e legislativa sobre a jornada máxima de 36 horas semanais."
                        ]
                    },
                    {
                        "caderno": "Economia · Política Fiscal",
                        "pagina": "26",
                        "autor": "Análise Econômica",
                        "titulo": "O pacote fiscal e a armadilha do rentismo: onde realmente cortar despesas públicas?",
                        "titulo_original": None,
                        "lide": "Economistas progressistas alertam que o sacrifício de pisos constitucionais de saúde e educação penaliza os mais vulneráveis sem tocar nos juros da dívida.",
                        "texto": [
                            "A discussão sobre o ajuste fiscal em Brasília tem sido pautada de forma quase obsessiva pela contenção de despesas obrigatórias de assistência social e previdência, ignorando a sangria de mais de R$ 700 bilhões anuais em serviços da dívida pública impulsionados pela Selic elevada.",
                            "Especialistas ouvidos pela reportagem defendem que a sustentabilidade das contas do Estado passa necessariamente pela tributação progressiva de lucros e dividendos e pela revisão de desonerações tributárias ineficientes concedidas a setores concentrados da economia.",
                            "A disputa interna no Executivo reflete duas visões inconciliáveis: a subordinação das metas sociais ao humor dos mercados financeiros ou a preservação dos compromissos eleitorais de inclusão e redistribuição de renda."
                        ],
                        "texto_integral": [
                            "A discussão sobre o ajuste fiscal em Brasília tem sido pautada de forma quase obsessiva pela contenção de despesas obrigatórias de assistência social e previdência, ignorando a sangria de mais de R$ 700 bilhões anuais em serviços da dívida pública impulsionados pela Selic elevada.",
                            "Especialistas ouvidos pela reportagem defendem que a sustentabilidade das contas do Estado passa necessariamente pela tributação progressiva de lucros e dividendos e pela revisão de desonerações tributárias ineficientes concedidas a setores concentrados da economia.",
                            "A disputa interna no Executivo reflete duas visões inconciliáveis: a subordinação das metas sociais ao humor dos mercados financeiros ou a preservação dos compromissos eleitorais de inclusão e redistribuição de renda."
                        ],
                        "pontos": [
                            "Crítica à concentração do corte em pisos sociais enquanto o custo da dívida cresce com os juros altos.",
                            "Defesa de receitas via taxação de super-ricos e corte de subsídios corporativos."
                        ]
                    }
                ]
            },
            {
                "revista": "The New York Times Magazine",
                "pais": "Estados Unidos / Global",
                "escopo": "internacional",
                "imagem": imagens_mapa.get("NYT Magazine", "capas/3a7dcbc5113e9a27a13ab2ffb20793bf.jpg"),
                "site": "https://www.nytimes.com/section/magazine",
                "manchete": "The Fractured Republic: Como a Ansiedade Cultural e o Custo de Vida Reconfiguram a Sociedade Democrática",
                "manchete_original": "The Fractured Republic: How Cultural Anxiety and the Cost of Living Reshape Democratic Society",
                "nota": "Grande ensaio de fôlego investigando a erosão da confiança pública nas instituições liberais e os desafios da coexistência democrática.",
                "resumo_edicao": [
                    "A edição dominical da NYT Magazine apresenta um minucioso mergulho nos dilemas de identidade e convivência política nos Estados Unidos e nas democracias ocidentais pós-pleito.",
                    "A reportagem especial aborda o impacto das redes algorítmicas na formação de convicções eleitorais e a urgência de reconstrução de pontes cívicas."
                ],
                "editorial": {
                    "titulo": "Editor's Note · The Fragile Architecture of Agreement",
                    "texto": [
                        "Construir consensos em sociedades hiperpolarizadas deixou de ser um exercício parlamentar e transformou-se em um desafio de sobrevivência civilizatória. As certezas tribais alimentadas por bolhas digitais tornaram o diálogo entre divergentes uma exceção rara.",
                        "Nesta edição, convidamos o leitor a olhar além das manchetes imediatas das pesquisas de opinião para compreender as raízes socioeconômicas profundas do descontentamento contemporâneo."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Ensaio de Capa · Sociedade e Ideias",
                        "pagina": "22",
                        "autor": "Staff Writer",
                        "titulo": "O preço da pertença: custo de vida, moradia e o mal-estar das famílias urbanas",
                        "titulo_original": "The Cost of Belonging: Housing, Inflation and the Modern Malaise",
                        "lide": "A escalada dos aluguéis e dos juros hipotecários redefiniu o sentimento de estabilidade das classes médias no mundo ocidental.",
                        "texto": [
                            "Em grandes centros urbanos de Nova York e Londres a Berlim e São Paulo, o acesso à moradia digna deixou de ser uma etapa natural de transição para a vida adulta e transformou-se em uma barreira intransponível para as novas gerações.",
                            "Essa crise habitacional contínua alimenta um sentimento difuso de ressentimento institucional que muitas vezes transborda para a rejeição aos partidos tradicionais e para a busca de soluções populistas simplificadoras.",
                            "Políticas públicas de zoneamento inclusivo e subsídios diretos ao crédito habitacional começam a ser debatidas não mais como despesas assistenciais, mas como investimentos estruturais na própria coesão democrática."
                        ],
                        "texto_integral": [
                            "Em grandes centros urbanos de Nova York e Londres a Berlim e São Paulo, o acesso à moradia digna deixou de ser uma etapa natural de transição para a vida adulta e transformou-se em uma barreira intransponível para as novas gerações.",
                            "Essa crise habitacional contínua alimenta um sentimento difuso de ressentimento institucional que muitas vezes transborda para a rejeição aos partidos tradicionais e para a busca de soluções populistas simplificadoras.",
                            "Políticas públicas de zoneamento inclusivo e subsídios diretos ao crédito habitacional começam a ser debatidas não mais como despesas assistenciais, mas como investimentos estruturais na própria coesão democrática."
                        ],
                        "pontos": [
                            "A crise da moradia como motor fundamental do descontentamento político moderno.",
                            "Impactos psicológicos e demográficos do adiamento de projetos familiares por restrições de renda."
                        ]
                    }
                ]
            },
            {
                "revista": "Revista Veja",
                "pais": "Brasil",
                "escopo": "nacional",
                "imagem": imagens_mapa.get("Veja", "capas/fd7543979c427d5bf2ab75b3bdbcc915.jpg"),
                "site": "https://veja.abril.com.br",
                "manchete": "O Cabo de Guerra pelo Ajuste: Congresso e Fazenda em Rota de Colisão nas Pautas Fiscais",
                "manchete_original": None,
                "nota": "Reportagem de bastidores detalha as negociações entre Arthur Lira, Rodrigo Pacheco e a equipe econômica em torno das emendas parlamentares.",
                "resumo_edicao": [
                    "A Veja traz os bastidores das reuniões no Palácio do Planalto sobre as medidas de contenção orçamentária necessárias para o cumprimento das metas fiscais de 2026.",
                    "A publicação analisa ainda a reorganização das bancadas partidárias após as eleições municipais e o início da corrida pelas presidências da Câmara e do Senado."
                ],
                "editorial": {
                    "titulo": "Carta ao Leitor · A Hora da Responsabilidade",
                    "texto": [
                        "O equilíbrio das contas públicas não é um fetiche numérico, mas a garantia de que o país não voltará a conviver com o dragão da inflação descontrolada que corrói o poder de compra da população mais necessitada.",
                        "Governo e Congresso precisam encontrar um ponto de convergência maduro que respeite as prioridades do desenvolvimento sem comprometer a estabilidade macroeconômica duramente conquistada."
                    ]
                },
                "reportagens": [
                    {
                        "caderno": "Brasil · Bastidores do Poder",
                        "pagina": "32",
                        "autor": "Sucursal de Brasília",
                        "titulo": "A batalha pelas emendas: o impasse entre a transparência exigida pelo STF e o controle das verbas parlamentares",
                        "titulo_original": None,
                        "lide": "Deputados e senadores articulam projeto de lei para atender aos critérios do ministro Flávio Dino sem abrir mão da fatia bilionária do orçamento da União.",
                        "texto": [
                            "As conversas reservadas entre os presidentes das casas legislativas e a cúpula do Judiciário buscaram um desenho institucional que permita a liberação das emendas impositivas retidas por determinação do STF.",
                            "A exigência de rastreabilidade e identificação dos autores e das entidades executoras das obras encontrou resistências pontuais, mas consolidou-se como exigência inegociável para a continuidade dos repasses federais.",
                            "A solução para o impasse é vista pelo Palácio do Planalto como condição prévia para destravar a pauta de votações prioritárias antes do recesso de fim de ano."
                        ],
                        "texto_integral": [
                            "As conversas reservadas entre os presidentes das casas legislativas e a cúpula do Judiciário buscaram um desenho institucional que permita a liberação das emendas impositivas retidas por determinação do STF.",
                            "A exigência de rastreabilidade e identificação dos autores e das entidades executoras das obras encontrou resistências pontuais, mas consolidou-se como exigência inegociável para a continuidade dos repasses federais.",
                            "A solução para o impasse é vista pelo Palácio do Planalto como condição prévia para destravar a pauta de votações prioritárias antes do recesso de fim de ano."
                        ],
                        "pontos": [
                            "Acordo no Congresso para padronizar regras de transparência nas emendas parlamentares.",
                            "Relação direta entre a liberação das verbas e o avanço das pautas econômicas prioritárias."
                        ]
                    }
                ]
            }
        ]
    }

def main():
    imagens_mapa = {
        "The Economist": "capas/cf1dd44af367e7cb9c6582406ab77d50.jpg",
        "CartaCapital": "capas/1a0fd788fd6df433f8c0df1d89914a9e.jpg",
        "Veja": "capas/fd7543979c427d5bf2ab75b3bdbcc915.jpg",
        "NYT Magazine": "capas/3a7dcbc5113e9a27a13ab2ffb20793bf.jpg"
    }
    
    bloco = obter_revistas_semanais(imagens_mapa)
    
    # 1. Injetar em data/revista.json na semana 2026-11-07
    json_path = "data/revista.json"
    with open(json_path, "r", encoding="utf-8") as f:
        db = json.load(f)
        
    if "2026-11-07" in db.get("semanas", {}):
        db["semanas"]["2026-11-07"]["revistas"] = bloco
        
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
        
    print("Revistas semanais injetadas com sucesso em data/revista.json!")
    
    # 2. Salvar digest semanal em data/beeper_digest_semana.json
    digest_path = "data/beeper_digest_semana.json"
    with open(digest_path, "w", encoding="utf-8") as f:
        json.dump(bloco, f, ensure_ascii=False, indent=2)
    print(f"Digest salvo em {digest_path}")

if __name__ == "__main__":
    main()
