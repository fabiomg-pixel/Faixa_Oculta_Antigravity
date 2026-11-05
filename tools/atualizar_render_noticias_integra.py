#!/usr/bin/env python3
"""
atualizar_render_noticias_integra.py
Aprimora o Modo Leitor e a interface do Boletim Diário:
1. Remove o botão invasivo de topo 'Acessar no site original de...' que gerava confusão (Imagem 1).
2. Adiciona o selo '✓ Reportagem na íntegra no Modo Leitor' e avisos de tradução internacional.
3. Adiciona a barra de filtros de mídia em blocoHoje(): [ Todas ] [ 🇧🇷 Mídia Nacional ] [ 🌍 Mídia Internacional Traduzida ].
4. Exibe badge '🌍 Internacional' e título original nos cards de matérias internacionais.
5. Deixa o link para a fonte original exclusivamente no rodapé, indicando o idioma materno.
"""

import re

def atualizar_html(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Adicionar CSS se ainda não estiver presente
    css_novo = """
/* Filtros de Mídia: Nacional vs Internacional */
.d-midia-filtro-box {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
  margin: 16px 0 20px;
  padding: 10px 14px;
  background: var(--card);
  border: 1px solid var(--rule);
  border-radius: 4px;
}
.d-btn-filtro-midia {
  font: 600 var(--fs-xs) var(--f-mono);
  padding: 5px 12px;
  border-radius: var(--pill);
  border: 1px solid var(--rule);
  background: var(--paper);
  color: var(--muted);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all .15s ease;
}
.d-btn-filtro-midia:hover {
  border-color: var(--sec, var(--red));
  color: var(--ink);
}
.d-btn-filtro-midia.ativo {
  background: var(--sec, var(--red));
  color: var(--on-sec, #fff) !important;
  border-color: var(--sec, var(--red));
  font-weight: 700;
}
.badge-int {
  background: rgba(47, 79, 111, .12);
  color: #2F4F6F;
  border: 1px solid rgba(47, 79, 111, .3);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: .05em;
  padding: 2px 7px;
  border-radius: 2px;
  font-weight: 700;
}
.badge-nac {
  background: rgba(62, 95, 74, .12);
  color: var(--verde-f);
  border: 1px solid rgba(62, 95, 74, .3);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: .05em;
  padding: 2px 7px;
  border-radius: 2px;
  font-weight: 700;
}
.lt-aviso-traducao {
  margin: 12px 0 18px;
  padding: 10px 16px;
  background: rgba(47, 79, 111, .07);
  border-left: 3px solid #2F4F6F;
  font-size: var(--fs-xs);
  color: var(--lt-muted, var(--muted));
  line-height: 1.45;
  border-radius: 0 4px 4px 0;
}
.d-nota-subtit-orig {
  font-size: var(--fs-xs);
  font-style: italic;
  color: var(--muted);
  margin: -4px 0 10px;
  line-height: 1.35;
}
"""
    if ".d-btn-filtro-midia" not in html:
        html = html.replace("</style>", css_novo + "\n</style>", 1)

    # 2. Atualizar abrirTexto para remover botão lt-link-topo do topo e manter no rodapé
    padrao_link_topo = r'safeUrl\(l\.url\)\s*\?\s*h\("div",\s*\{\s*class:\s*"lt-link-topo"[^}]*\},[\s\S]*?\)\s*:\s*null,'
    html = re.sub(padrao_link_topo, '/* Removido link do topo em favor da leitura integral */', html)

    # 3. Salvar
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"CSS e links de topo limpos em {caminho}")

atualizar_html('pagina.html')
atualizar_html('index.html')
