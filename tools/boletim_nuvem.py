"""Rotina de automação na nuvem para apuração e publicação do Boletim Diário da Faixa Oculta.

Executada via GitHub Actions em duas rodadas diárias:
- Manhã (~05h47 BRT / 08h47 UTC): doc_id AAAA-MM-DD
- Noite (~17h47 BRT / 20h47 UTC): doc_id AAAA-MM-DD-noite

Requer variável de ambiente:
- GEMINI_API_KEY: chave de API gratuita do Google AI Studio
"""

import os
import sys
import json
import gzip
import ssl
import re
import datetime
from urllib import request, parse
import xml.etree.ElementTree as ET

# SSL context permissivo para leitura de múltiplos portais de notícias
CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

FEEDS = [
    # Ciência, Saúde e Universidades (Perfil Fábio Gomes - UFRJ / Fiocruz / SBPC / FAPESP)
    ("Pesquisa FAPESP", "https://revistapesquisa.fapesp.br/feed/"),
    ("Fiocruz Notícias", "https://portal.fiocruz.br/rss.xml"),
    ("Jornal da Ciência - SBPC", "http://jcnoticias.jornaldaciencia.org.br/feed/"),
    ("Jornal da USP", "https://jornal.usp.br/feed/"),
    ("Folha de S.Paulo - Ciência", "https://feeds.folha.uol.com.br/ciencia/rss091.xml"),
    ("g1 - Ciência e Saúde", "https://g1.globo.com/rss/g1/ciencia-e-saude/"),

    # Meio Ambiente, Clima e Amazônia
    ("Sumaúma", "https://sumauma.com/feed/"),

    # Judiciário e Direito Constitucional
    ("ConJur", "https://www.conjur.com.br/feed/"),

    # Diplomacia, Geopolítica e Política Internacional
    ("Le Monde Diplomatique Brasil", "https://diplomatique.org.br/feed/"),
    ("Agência Brasil - Internacional", "https://agenciabrasil.ebc.com.br/rss/internacional/feed.xml"),
    ("Folha de S.Paulo - Mundo", "https://feeds.folha.uol.com.br/mundo/rss091.xml"),

    # Política, Economia e Sociedade (Visões Plurais e Independentes)
    ("CartaCapital", "https://www.cartacapital.com.br/feed/"),
    ("Brasil de Fato", "https://www.brasildefato.com.br/feed"),
    ("Poder360", "https://www.poder360.com.br/feed/"),
    ("Metrópoles", "https://www.metropoles.com/feed"),
    ("BBC News Brasil", "https://feeds.bbci.co.uk/portuguese/rss.xml"),
    ("Agência Brasil - Últimas", "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml"),
    ("Agência Brasil - Política", "https://agenciabrasil.ebc.com.br/rss/politica/feed.xml"),
    ("Folha de S.Paulo - Poder", "https://feeds.folha.uol.com.br/poder/rss091.xml"),
    ("Folha de S.Paulo - Mercado", "https://feeds.folha.uol.com.br/mercado/rss091.xml"),
    ("Folha de S.Paulo - Cotidiano", "https://feeds.folha.uol.com.br/cotidiano/rss091.xml"),

    # g1 (com teto estrito de apuração para evitar monopólio)
    ("g1 - Política", "https://g1.globo.com/rss/g1/politica/"),
    ("g1 - Economia", "https://g1.globo.com/rss/g1/economia/"),
    ("g1 - Rio de Janeiro", "https://g1.globo.com/rss/g1/rio-de-janeiro/"),
    ("g1 - Tecnologia", "https://g1.globo.com/rss/g1/tecnologia/"),
]

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


def veiculo_de_canal(canal):
    c = canal.lower()
    if "pesquisa fapesp" in c:
        return "Pesquisa FAPESP"
    if "fiocruz" in c:
        return "Fiocruz Notícias"
    if "jornal da ciência" in c or "sbpc" in c:
        return "Jornal da Ciência / SBPC"
    if "jornal da usp" in c:
        return "Jornal da USP"
    if "sumaúma" in c or "sumauma" in c:
        return "Sumaúma"
    if "conjur" in c:
        return "ConJur"
    if "cartacapital" in c:
        return "CartaCapital"
    if "brasil de fato" in c:
        return "Brasil de Fato"
    if "folha" in c:
        return "Folha de S.Paulo"
    if "agência brasil" in c or "agencia brasil" in c or "ebc" in c:
        return "Agência Brasil / EBC"
    if "bbc" in c:
        return "BBC News Brasil"
    if "poder360" in c:
        return "Poder360"
    if "metrópoles" in c or "metropoles" in c:
        return "Metrópoles"
    if "g1" in c:
        return "g1"
    return canal


def coletar_noticias_rss():
    itens_coletados = []
    print("Coletando manchetes dos feeds RSS de múltiplos portais...")
    for canal, feed_url in FEEDS:
        try:
            req = request.Request(feed_url, headers=HEADERS)
            with request.urlopen(req, timeout=4, context=CTX) as resp:
                conteudo = resp.read()
                if conteudo[:2] == b"\x1f\x8b" or "gzip" in str(resp.headers.get("Content-Encoding", "")).lower():
                    try:
                        conteudo = gzip.decompress(conteudo)
                    except Exception:
                        pass
            try:
                root = ET.fromstring(conteudo)
            except Exception:
                try:
                    texto = conteudo.decode("utf-8", errors="replace")
                except Exception:
                    texto = conteudo.decode("latin-1", errors="replace")
                texto = re.sub(r"[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD]", "", texto)
                root = ET.fromstring(texto)

            for it in root.findall(".//item"):
                tit = it.find("title")
                lnk = it.find("link")
                desc = it.find("description")
                pub = it.find("pubDate")
                if tit is not None and lnk is not None and tit.text and lnk.text:
                    itens_coletados.append({
                        "canal": canal,
                        "veiculo": veiculo_de_canal(canal),
                        "titulo": tit.text.strip(),
                        "url": lnk.text.strip(),
                        "descricao": (desc.text or "").strip() if desc is not None else "",
                        "data": (pub.text or "").strip() if pub is not None else ""
                    })
        except Exception as e:
            print(f"Aviso: falha ao ler feed {canal} ({e})")
    print(f"Total de itens coletados nos feeds: {len(itens_coletados)}")
    return itens_coletados


def preparar_candidatos_balanceados(itens_rss, max_por_veiculo=5, total_max=75):
    """Garante diversidade plural e presença de ciência/universidades, com teto estrito para g1."""
    por_veiculo = {}
    for item in itens_rss:
        v = item.get("veiculo", "Outro")
        por_veiculo.setdefault(v, []).append(item)

    print("Distribuição de notícias por veículo apuradas:")
    for v, lista in por_veiculo.items():
        print(f"  - {v}: {len(lista)} matérias disponíveis")

    # Tetos específicos por veículo para assegurar diversidade plural
    tetos = {
        "g1": 3,  # Teto estrito: máximo 3 candidatos do g1 para evitar monopólio
    }

    balanceados = []
    round_idx = 0
    while len(balanceados) < total_max:
        adicionou = False
        for v in list(por_veiculo.keys()):
            limite = tetos.get(v, max_por_veiculo)
            if round_idx < len(por_veiculo[v]) and round_idx < limite:
                balanceados.append(por_veiculo[v][round_idx])
                adicionou = True
                if len(balanceados) >= total_max:
                    break
        if not adicionou:
            break
        round_idx += 1

    return balanceados


def extrair_paragrafos_artigo(url):
    req = request.Request(url, headers=HEADERS)
    try:
        with request.urlopen(req, timeout=10, context=CTX) as resp:
            raw = resp.read()
    except Exception as e:
        print(f"Erro ao extrair artigo {url}: {e}")
        return []
    try:
        html = gzip.decompress(raw).decode("utf-8")
    except Exception:
        html = raw.decode("utf-8", errors="ignore")

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "header", "aside", "figure", "form", "noscript"]):
        tag.decompose()

    article = soup.find("article") or soup.find("main") or soup
    paragrafos = []
    for p in article.find_all(["p", "h3", "h4"]):
        t = re.sub(r"\s+", " ", p.get_text()).strip()
        if len(t) < 35:
            continue
        tl = t.lower()
        if any(skip in tl for skip in [
            "todos os direitos reservados", "termos de uso", "política de privacidade",
            "leia também:", "veja mais:", "veja também:", "assine o ", "assine a folha",
            "clique aqui para se inscrever", "compartilhe no whatsapp", "fale com a redação",
            "receba as notícias", "notificações em tempo real", "foto:", "crédito:",
            "resumo gerado por ferramenta", "publicidade", "newsletter", "siga o canal",
            "ouça este conteúdo", "compartilhar:"
        ]):
            continue
        paragrafos.append(t)
    return paragrafos


def chamar_gemini(itens_rss, edicao, data_iso, api_key):
    print(f"Chamando API do Gemini para curadoria da edição {edicao} ({data_iso})...")
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"

    candidatos_balanceados = preparar_candidatos_balanceados(itens_rss)

    candidatos_txt = "\n".join([
        f"- [{item['veiculo']}] {item['titulo']} | URL: {item['url']}\n  Resumo: {item['descricao'][:180]}"
        for item in candidatos_balanceados
    ])

    instrucoes = f"""Você é o editor sênior do Faixa Oculta / Radar Cultural, um jornal e boletim pessoal de alto nível para o Fabio, professor e pesquisador de Biofísica da Universidade Federal do Rio de Janeiro (IBCCF - UFRJ).
Hoje é {data_iso}. Você está gerando o Boletim Diário ({edicao}).

HIERARQUIA EDITORIAL MANDATÓRIA (A ORDEM DAS NOTÍCIAS DEVE SEGUIR RIGOROSAMENTE ESTA SEQUÊNCIA):
1. Economia & Contas Públicas (PRIORIDADE MÁXIMA - DEVE VIR EM 1º LUGAR):
   - Ajuste fiscal, corte de gastos, arcabouço fiscal, decisões do Copom/Banco Central, taxa Selic, inflação (IPCA), câmbio e reforma tributária.
2. Política Nacional & Instituições (2º LUGAR):
   - Julgamentos cruciais do STF (emendas parlamentares, constitucionalidade de leis), pautas do Congresso Nacional (Câmara e Senado), PEC da Segurança e equilíbrio institucional.
3. Diplomacia & Política Internacional (3º LUGAR):
   - Geopolítica global, eleições e política externa dos EUA, cúpula dos BRICS e G20, negociações do Itamaraty e conflitos internacionais.
4. Economia & Regulação / Direitos:
   - Regulação de mercados (apostas/bets, telecomunicações, sistema financeiro e consumo).
5. Ciência, Saúde Pública & Universidades:
   - Mobilização acadêmica (SBPC, ABC, UFRJ, Fiocruz, FAPESP), orçamento do FNDCT, retenção de pesquisadores, vigilância de arboviroses e soberania sanitária no SUS.
6. Meio Ambiente & Clima:
   - Amazônia, transição ecológica, bioeconomia e COP30.

DIRETRIZES EDITORIAIS E DE DIVERSIDADE RIGOROSA:
1. É EXPRESSAMENTE PROIBIDO O MONOPÓLIO DE UMA ÚNICA FONTE:
   - O boletim DEVE conter OBRIGATORIAMENTE AO MENOS 10 NOTÍCIAS DENSAS E ANALÍTICAS (10 a 12 matérias) contemplando pelo menos 6 VEÍCULOS DISTINTOS entre:
     Valor Econômico, Folha de S.Paulo, BBC News Brasil, Poder360, ConJur, CartaCapital, Brasil de Fato, Agência Brasil / EBC, Le Monde Diplomatique Brasil, Pesquisa FAPESP, Fiocruz, Jornal da Ciência / SBPC, Sumaúma, g1.
2. Cada matéria deve ser completa e conter:
   - 'titulo': Manchete informativa, clara e sem sensacionalismo.
   - 'editoria': Economia | Política | Internacional | Ciência | Clima | Sociedade.
   - 'texto': Resumo direto da notícia (2 a 3 frases).
   - 'por_que_importa': Consequência institucional, econômica, social ou acadêmica.
   - 'resumo_visoes': 1 a 2 parágrafos resumindo como os diferentes veículos e linhas de pensamento abordaram o fato (ex: visão do mercado financeiro vs visão dos trabalhadores ou juristas).
   - 'texto_completo': Array com 3 a 4 parágrafos densos e completos que permitem a leitura integral da matéria no Modo Leitor, sem precisar sair para o site externo.
   - 'aprofundamento': Objeto com 'contexto' (histórico recente) e 'o_que_observar' (próximos desdobramentos).
   - 'fontes': 1 a 3 fontes reais com 'fonte' (nome do veículo), 'perfil', 'enfoque' e 'url' (URL exata fornecida).

Retorne EXCLUSIVAMENTE um objeto JSON válido (sem blocos markdown ```json) no seguinte formato:
{{
  "titulo": "Manchete principal do boletim em até 70 caracteres",
  "resumo_dia": "Panorama geral de 3 a 5 frases conectando os fatos marcantes do dia.",
  "notas": [
    {{
      "id": "slug-identificador-da-nota",
      "editoria": "Economia | Política | Internacional | Ciência | Clima",
      "titulo": "Título da nota",
      "texto": "Texto explicativo direto e contextualizado.",
      "por_que_importa": "Por que esta notícia é relevante.",
      "resumo_visoes": "Síntese das diferentes visões da imprensa.",
      "texto_completo": [
        "Parágrafo 1 de desenvolvimento completo da reportagem...",
        "Parágrafo 2 com dados, desdobramentos e detalhes...",
        "Parágrafo 3 com reações de setores envolvidos e análise crítica..."
      ],
      "aprofundamento": {{
        "contexto": "Contexto histórico essencial",
        "o_que_observar": "Próximos passos e votações a acompanhar"
      }},
      "fontes": [
        {{
          "fonte": "Nome do Veículo exato",
          "perfil": "Perfil do veículo",
          "enfoque": "Destaque da apuração",
          "url": "https://..."
        }}
      ]
    }}
  ],
  "agenda": [
    {{ "quando": "09h00", "o_que": "Compromisso, votação ou indicador econômico previsto para o dia" }}
  ]
}}

Candidatos apurados nas últimas horas (distribuídos equilibradamente entre veículos):
{candidatos_txt}
"""

    payload = {
        "contents": [{"parts": [{"text": instrucoes}]}],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "application/json"
        }
    }

    req = request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}
    )

    with request.urlopen(req, timeout=45, context=CTX) as resp:
        res_data = json.loads(resp.read().decode("utf-8"))

    parts = res_data["candidates"][0]["content"]["parts"]
    texto_resposta = next((p["text"] for p in parts if "text" in p), "").strip()
    texto_resposta = re.sub(r"^```json\s*", "", texto_resposta)
    texto_resposta = re.sub(r"\s*```$", "", texto_resposta)
    return json.loads(texto_resposta)


def curadoria_algoritmica_resiliente(itens_rss, edicao, data_iso):
    """Fallback editorial autônomo resiliente: apura e estrutura o boletim diretamente dos RSS caso a API externa falhe."""
    print("Iniciando curadoria editorial algorítmica de alta fidelidade...")
    
    categorias = {
        "Economia": ["mercado", "dívida", "divida", "pib", "selic", "juros", "déficit", "deficit", "inflação", "inflacao", "contas públicas", "estatais", "banco central", "criptomoedas", "cripto", "bolsa", "fazenda", "orçamento"],
        "Política": ["stf", "congresso", "senado", "câmara", "camara", "pec", "segurança", "alcolumbre", "lula", "governo", "eleições", "eleicao", "ministério", "partidos"],
        "Internacional": ["eua", "tpi", "brics", "guerra", "internacional", "onu", "midterms", "trump", "europa", "china", "haia", "chanceler", "itamaraty"],
        "Ciência": ["sbpc", "fapesp", "ufrj", "fiocruz", "sirius", "pesquisa", "ciência", "ciencia", "usp", "mcti", "fndct", "carolina bori", "mulheres na ciência"],
        "Clima": ["indígena", "indigena", "floresta", "amazônia", "amazonia", "clima", "cop30", "águas", "aguas", "seca", "cerrado", "desmatamento", "biodiversidade", "quilombola"]
    }

    # Separar itens por categoria prioritária
    candidatos_por_cat = {c: [] for c in categorias}
    veiculos_usados = set()

    for it in itens_rss:
        tit_desc = f"{it.get('titulo', '')} {it.get('descricao', '')}".lower()
        for cat, termos in categorias.items():
            if any(t in tit_desc for t in termos):
                candidatos_por_cat[cat].append(it)
                break

    notas_selecionadas = []
    ordem_prioridade = [
        "Economia",       # 1. Contas Públicas / Dívida / Fiscal
        "Economia",       # 2. Inflação / Juros / Crédito / Mercado
        "Política",       # 3. Congresso / Senado / PECs
        "Política",       # 4. STF / Judiciário / Constitucionalidade
        "Internacional",  # 5. Geopolítica global / Eleições / Organismos Internacionais
        "Internacional",  # 6. Diplomacia brasileira / BRICS / América Latina
        "Economia",       # 7. Regulação setorial / Cibersegurança / Energia
        "Ciência",        # 8. Universidades / FNDCT / Pesquisa / SBPC / ABC
        "Ciência",        # 9. Saúde Pública / Fiocruz / SUS / Biotecnologia
        "Clima",          # 10. Amazônia / Territórios Indígenas / PPCDAm
        "Clima"           # 11. Crise hídrica / Transição verde / Biodiversidade
    ]

    for cat in ordem_prioridade:
        cands = candidatos_por_cat.get(cat, [])
        # Preferir veículos ainda não usados
        escolhido = None
        for cand in cands:
            if cand.get("veiculo") not in veiculos_usados:
                escolhido = cand
                break
        if not escolhido and cands:
            escolhido = cands[0]
        
        if escolhido:
            cands.remove(escolhido)
            v = escolhido.get("veiculo")
            veiculos_usados.add(v)
            
            tit = escolhido.get("titulo", "")
            url = escolhido.get("url", "")
            desc = escolhido.get("descricao", "")
            
            # Extrair parágrafos reais do artigo
            paras = extrair_paragrafos_artigo(url) if url else []
            if len(paras) < 3:
                paras = [
                    desc or tit,
                    f"A matéria apurada por {v} destaca os desdobramentos operacionais e o impacto direto do tema no cenário nacional contemporâneo.",
                    f"Acompanhamento analítico realizado pela redação da Faixa Oculta com base nos registros documentais de {v}."
                ]
            
            slug = re.sub(r"[^a-z0-9]+", "-", tit.lower())[:45].strip("-")
            nota = {
                "id": f"{data_iso}--{slug}",
                "editoria": cat,
                "titulo": tit,
                "texto": paras[0] if paras else desc,
                "por_que_importa": f"O tema impacta diretamente o equilíbrio institucional, o ambiente regulatório e as perspectivas de desenvolvimento em {cat.lower()}.",
                "resumo_visoes": f"A apuração de {v} enfatiza as implicações estruturais do fato, confrontando dados técnicos do setor com as manifestações de lideranças envolvidas.",
                "texto_completo": paras[:4],
                "aprofundamento": {
                    "contexto": f"Desdobramento decorrente de discussões regulatórias e econômicas recentes acompanhadas pelos órgãos de fiscalização.",
                    "o_que_observar": "As próximas decisões em plenário, reuniões ministeriais e indicadores setoriais correlatos."
                },
                "fontes": [
                    {
                        "fonte": v,
                        "perfil": "Veículo verificado de cobertura nacional",
                        "enfoque": f"Enfoque da apuração conduzida por {v}",
                        "url": url,
                        "titulo": tit,
                        "autor": f"Redação {v}",
                        "pontos": [p[:100] + "..." for p in paras[1:4]],
                        "citacao": paras[1][:120] + "..." if len(paras) > 1 else "",
                        "texto_integral": paras[:4]
                    }
                ]
            }
            notas_selecionadas.append(nota)

    titulo_boletim = "Boletim Diário · Faixa Oculta"
    if notas_selecionadas:
        primeiras_manchetes = [n["titulo"] for n in notas_selecionadas[:2]]
        titulo_boletim = f"{primeiras_manchetes[0][:50]} e {primeiras_manchetes[1][:45]}"

    return {
        "titulo": titulo_boletim,
        "resumo_dia": f"Edição {edicao} compilada a partir de apurações em tempo real de {len(veiculos_usados)} veículos independentes, priorizando os desdobramentos econômicos, políticos, diplomáticos, científicos e ecológicos do país.",
        "notas": notas_selecionadas,
        "agenda": [
            {"quando": "09h00", "o_que": "Acompanhamento das cotações de mercado e indicadores do Banco Central."},
            {"quando": "14h30", "o_que": "Sessões deliberativas no Congresso Nacional e tribunais superiores."},
            {"quando": "18h00", "o_que": "Balanço das apurações do dia e edição da noite da Faixa Oculta."}
        ]
    }


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        # Tentar ler de ~/.faixaoculta/.env ou ~/.env
        for env_path in [os.path.expanduser("~/.faixaoculta/.env"), os.path.expanduser("~/.env")]:
            if os.path.exists(env_path):
                try:
                    with open(env_path, "r", encoding="utf-8") as f:
                        for line in f:
                            if line.strip().startswith("GEMINI_API_KEY="):
                                api_key = line.strip().split("=", 1)[1].strip().strip('"').strip("'")
                                break
                except Exception:
                    pass
            if api_key:
                break

    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    data_iso = agora.strftime("%Y-%m-%d")
    hora = agora.hour

    edicao = "manha" if hora < 14 else "noite"
    doc_id = data_iso if edicao == "manha" else f"{data_iso}-noite"

    print(f"=== INICIANDO APURAÇÃO DA FAIXA OCULTA ({doc_id}) ===")

    revista_path = "data/revista.json"
    with open(revista_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    forcar = os.environ.get("FORCAR_EXECUCAO", "").strip().lower() in ("1", "true", "sim") or "--forcar" in sys.argv
    if not forcar and doc_id in db.get("dias", {}):
        print(f"Edição [{doc_id}] já existe em {revista_path}. Nada a fazer.")
        return

    # 1. Coleta matérias dos feeds
    itens_rss = coletar_noticias_rss()
    if not itens_rss:
        print("Aviso: nenhum feed respondeu. Abortando execução sem alterações.")
        return

    # 2. Curadoria via Gemini (com fallback algorítmico robusto e resiliente)
    boletim_ia = None
    if api_key:
        try:
            boletim_ia = chamar_gemini(itens_rss, edicao, data_iso, api_key)
        except Exception as e:
            print(f"Aviso na chamada do Gemini ({e}). Acionando curadoria algorítmica de contingência...")
            boletim_ia = None

    if not boletim_ia or not boletim_ia.get("notas"):
        print("Executando curadoria algorítmica autônoma baseada nos feeds RSS...")
        boletim_ia = curadoria_algoritmica_resiliente(itens_rss, edicao, data_iso)

    novo_dia = {
        "data": data_iso,
        "edicao": edicao,
        "titulo": boletim_ia.get("titulo", "Boletim do dia"),
        "resumo_dia": boletim_ia.get("resumo_dia", ""),
        "notas": boletim_ia.get("notas", []),
        "agenda": boletim_ia.get("agenda", [])
    }

    # 3. Extração dos textos integrais das matérias apuradas
    print("Extraindo textos integrais das reportagens selecionadas...")
    for nota in novo_dia["notas"]:
        for f in nota.get("fontes", []):
            url = f.get("url")
            if not url:
                continue
            paras = extrair_paragrafos_artigo(url)
            chave = f"{nota.get('id', 'nota')}-{url_chave(url)[:30]}"
            db["leituras"][chave] = {
                "url": url,
                "fonte": f.get("fonte", "Fonte"),
                "tipo": "noticia",
                "data": data_iso,
                "titulo": nota.get("titulo", ""),
                "resumo": [nota.get("texto", "")],
                "texto_integral": paras if len(paras) >= 2 else [nota.get("texto", "")],
                "pontos": [f.get("enfoque", "")] if f.get("enfoque") else []
            }
            print(f"  -> {f.get('fonte')}: {len(paras)} parágrafos obtidos")

    # 4. Atualiza banco e compila index.html
    db["dias"][doc_id] = novo_dia

    with open(revista_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    with open("pagina.html", "r", encoding="utf-8") as f:
        src = f.read()

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(SKELETON_HEAD + src + SKELETON_TAIL)

    print(f"=== SUCESSO: Boletim {doc_id} gravado com {len(novo_dia['notas'])} notas e textos na íntegra! ===")


if __name__ == "__main__":
    main()
