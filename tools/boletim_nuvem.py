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
    ("g1_politica", "https://g1.globo.com/rss/g1/politica/"),
    ("g1_economia", "https://g1.globo.com/rss/g1/economia/"),
    ("g1_mundo", "https://g1.globo.com/rss/g1/mundo/"),
    ("g1_rio", "https://g1.globo.com/rss/g1/rio-de-janeiro/"),
    ("g1_tecnologia", "https://g1.globo.com/rss/g1/tecnologia/"),
    ("agencia_brasil", "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml"),
    ("folha_poder", "https://feeds.folha.uol.com.br/poder/rss091.xml"),
    ("folha_mercado", "https://feeds.folha.uol.com.br/mercado/rss091.xml")
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


def coletar_noticias_rss():
    itens_coletados = []
    print("Coletando manchetes dos feeds RSS...")
    for canal, feed_url in FEEDS:
        try:
            req = request.Request(feed_url, headers=HEADERS)
            with request.urlopen(req, timeout=8, context=CTX) as resp:
                conteudo = resp.read()
            root = ET.fromstring(conteudo)
            for it in root.findall(".//item"):
                tit = it.find("title")
                lnk = it.find("link")
                desc = it.find("description")
                pub = it.find("pubDate")
                if tit is not None and lnk is not None and tit.text and lnk.text:
                    itens_coletados.append({
                        "canal": canal,
                        "titulo": tit.text.strip(),
                        "url": lnk.text.strip(),
                        "descricao": (desc.text or "").strip() if desc is not None else "",
                        "data": (pub.text or "").strip() if pub is not None else ""
                    })
        except Exception as e:
            print(f"Aviso: falha ao ler feed {canal} ({e})")
    print(f"Total de itens coletados nos feeds: {len(itens_coletados)}")
    return itens_coletados


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
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    candidatos_txt = "\n".join([
        f"- [{item['canal']}] {item['titulo']} | URL: {item['url']}\n  Resumo: {item['descricao'][:180]}"
        for item in itens_rss[:80]
    ])

    instrucoes = f"""Você é o editor do Faixa Oculta / Radar Cultural, um jornal e boletim pessoal para o Fabio, professor de biofísica na UFRJ, no Rio de Janeiro.
Hoje é {data_iso}. Você está gerando o Boletim Diário ({edicao}).

Critérios editoriais rigorosos:
1. Pautas prioritárias: Política brasileira, Economia, Ciência e Universidades, Meio Ambiente/Clima, Tecnologia/IA e Rio de Janeiro.
2. Selecione entre 6 a 8 notas essenciais a partir dos links reais fornecidos abaixo. NUNCA invente notícias nem fatos.
3. Use estritamente as URLs reais fornecidas na lista de candidatos para cada fonte citada.
4. Para cada nota:
   - 'titulo': Manchete informativa, sem clickbait, direta e clara.
   - 'texto': 2 a 3 frases explicando o acontecimento com fatos e números precisos.
   - 'por_que_importa': 1 a 2 frases explicando a consequência prática institucional, econômica ou social.
   - 'fontes': 1 a 3 fontes com 'fonte' (nome do veículo), 'perfil' (ex: 'Portal de notícias', 'Jornal de centro'), 'enfoque' (o que destacou) e 'url' (a URL exata do candidato).

Retorne EXCLUSIVAMENTE um objeto JSON válido (sem blocos markdown ```json) no seguinte formato:
{{
  "titulo": "Manchete principal do boletim em até 70 caracteres",
  "resumo_dia": "Panorama geral de 3 a 5 frases conectando os fatos marcantes do dia.",
  "notas": [
    {{
      "id": "slug-identificador-da-nota",
      "editoria": "Política | Economia | Ciência | Clima | Tecnologia | Rio",
      "titulo": "Título da nota",
      "texto": "Texto explicativo direto e contextualizado.",
      "por_que_importa": "Por que esta notícia é relevante.",
      "fontes": [
        {{
          "fonte": "g1",
          "perfil": "Portal de notícias",
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

Candidatos apurados nas últimas horas:
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

    with request.urlopen(req, timeout=40, context=CTX) as resp:
        res_data = json.loads(resp.read().decode("utf-8"))

    texto_resposta = res_data["candidates"][0]["content"]["parts"][0]["text"].strip()
    texto_resposta = re.sub(r"^```json\s*", "", texto_resposta)
    texto_resposta = re.sub(r"\s*```$", "", texto_resposta)
    return json.loads(texto_resposta)


def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Erro: variável GEMINI_API_KEY não encontrada no ambiente.")
        sys.exit(1)

    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    data_iso = agora.strftime("%Y-%m-%d")
    hora = agora.hour

    edicao = "manha" if hora < 14 else "noite"
    doc_id = data_iso if edicao == "manha" else f"{data_iso}-noite"

    print(f"=== INICIANDO APURAÇÃO DA FAIXA OCULTA ({doc_id}) ===")

    revista_path = "data/revista.json"
    with open(revista_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    # 1. Coleta matérias dos feeds
    itens_rss = coletar_noticias_rss()
    if not itens_rss:
        print("Aviso: nenhum feed respondeu. Abortando execução sem alterações.")
        return

    # 2. Curadoria via Gemini
    boletim_ia = chamar_gemini(itens_rss, edicao, data_iso, api_key)

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
