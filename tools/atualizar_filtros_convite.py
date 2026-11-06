#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Implementa o modal de convite compartilhável, botão de convite nos eventos da agenda e deep link em pagina.html."""

import re

def atualizar_pagina_html():
    with open("pagina.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Adicionar o diálogo <dialog class="texto convite-dlg" id="dlg-convite">
    if 'id="dlg-convite"' not in html:
        alvo_dlg = '<dialog class="texto ida-dlg" id="dlg-ida" aria-labelledby="dlg-ida-tit"></dialog>'
        novo_dlg = alvo_dlg + '\n<dialog class="texto convite-dlg" id="dlg-convite" aria-labelledby="dlg-convite-tit"></dialog>'
        if alvo_dlg in html:
            html = html.replace(alvo_dlg, novo_dlg, 1)
            print("Diálogo #dlg-convite inserido com sucesso!")
        else:
            print("Aviso: alvo_dlg não encontrado!")

    # 2. Adicionar o CSS de convite
    css_convite = """
/* Convite Compartilhável Faixa Oculta */
.ag-btn-convite {
  border: 1px solid var(--ink) !important;
  background: transparent !important;
  padding: 3px 9px !important;
  border-radius: var(--pill) !important;
  font: 600 var(--fs-xs) var(--f-mono) !important;
  cursor: pointer;
  transition: all .15s ease;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  color: var(--ink) !important;
  text-decoration: none;
}
.ag-btn-convite:hover {
  background: var(--ink) !important;
  color: var(--bg) !important;
}
.ag-btn-convite.mini {
  padding: 2px 7px !important;
  font-size: 11px !important;
}
dialog.texto.convite-dlg {
  width: min(660px, calc(100% - 24px));
  max-height: min(90vh, 820px);
  padding: 0;
  border: 1px solid var(--rule);
  background: var(--bg);
  color: var(--ink);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.22);
  border-radius: 6px;
  overflow-y: auto;
}
.convite-container {
  padding: clamp(20px, 4vw, 32px);
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.convite-topo-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--rule);
  padding-bottom: 8px;
}
.convite-selo {
  font: 700 var(--fs-xs) var(--f-mono);
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .06em;
}
.convite-fechar {
  background: none;
  border: none;
  font-size: 22px;
  cursor: pointer;
  color: var(--muted);
  padding: 0 4px;
  line-height: 1;
}
.convite-fechar:hover {
  color: var(--ink);
}
.convite-tit {
  font: 800 clamp(20px, 3.2vw, 28px)/1.2 var(--f-display);
  margin: 0;
  letter-spacing: -.02em;
}
.convite-chamada {
  font-size: var(--fs-s);
  color: var(--sec);
  font-style: italic;
  margin: -6px 0 0;
}
.convite-grid-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
  background: var(--card-bg, rgba(0, 0, 0, 0.03));
  border: 1px solid var(--rule);
  padding: 12px 16px;
  border-radius: 4px;
}
.convite-info-item {
  display: flex;
  flex-direction: column;
  gap: 2px;
  font-size: var(--fs-s);
}
.convite-info-item .lbl {
  font: 700 var(--fs-xs) var(--f-mono);
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .04em;
}
.convite-secao-tit {
  font: 700 var(--fs-xs) var(--f-mono);
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .05em;
  margin: 6px 0 2px;
  border-bottom: 1px solid var(--rule);
  padding-bottom: 4px;
}
.convite-desc {
  font-size: var(--fs-m);
  line-height: 1.5;
  margin: 0;
}
.convite-artistas-lista {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}
.convite-review-box {
  background: var(--card-bg, rgba(0,0,0,0.02));
  border-left: 3px solid var(--ink);
  padding: 10px 14px;
  font-size: var(--fs-s);
  font-style: italic;
  margin: 0;
}
.convite-review-fontes {
  display: block;
  font-style: normal;
  font: 600 var(--fs-xs) var(--f-mono);
  color: var(--muted);
  margin-top: 4px;
}
.convite-acoes-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  padding-top: 14px;
  border-top: 1px solid var(--rule);
  margin-top: 4px;
}
.convite-btn-acao {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 14px;
  border-radius: 4px;
  font: 600 var(--fs-s) var(--f-mono);
  cursor: pointer;
  border: 1px solid var(--rule);
  background: var(--bg);
  color: var(--ink);
  transition: all .15s ease;
  text-decoration: none;
}
.convite-btn-acao.destaque {
  background: var(--ink);
  color: var(--bg);
  border-color: var(--ink);
}
.convite-btn-acao:hover {
  filter: brightness(0.92);
}
"""
    if ".convite-dlg" not in html:
        idx_style = html.find("</style>")
        if idx_style != -1:
            html = html[:idx_style] + css_convite + html[idx_style:]
            print("CSS de convite inserido com sucesso!")

    # 3. Adicionar botão de convite em cardEvento(ev)
    alvo_marcas_card = 'if (temDet) marcas.append(h("button", { type: "button", class: "ag-det", "aria-expanded": String(info), onclick: () => { S.agInfo[evId] = !info; render(); } }, info ? "Menos detalhes" : "Detalhes"));'
    novo_marcas_card = alvo_marcas_card + '\n    marcas.append(h("button", { type: "button", class: "ag-btn-convite mono", title: "Criar convite e compartilhar este evento", onclick: () => abrirConvite(ev, null) }, "✉️ Convidar"));'
    if alvo_marcas_card in html and 'title: "Criar convite e compartilhar este evento"' not in html:
        html = html.replace(alvo_marcas_card, novo_marcas_card, 1)
        print("Botão convite adicionado em cardEvento!")

    # 4. Adicionar botão de convite em agDestaques(ev)
    alvo_dest_marcas = 'marcasAgenda(key, true),'
    novo_dest_marcas = '(() => { const m = marcasAgenda(key, true); m.append(h("button", { type: "button", class: "ag-btn-convite mini mono", title: "Criar convite para esta atração", onclick: () => abrirConvite(ev, d) }, "✉️ Convidar")); return m; })(),'
    if alvo_dest_marcas in html and 'title: "Criar convite para esta atração"' not in html:
        html = html.replace(alvo_dest_marcas, novo_dest_marcas, 1)
        print("Botão convite adicionado em agDestaques!")

    # 5. Adicionar a função abrirConvite e checarDeepLinkConvite
    funcoes_convite = """
  function abrirConvite(ev, d) {
    if (!ev && !d) return;
    const evId = d ? `${ev.id}__${d.id}` : ev.id;
    const titulo = str(d ? d.titulo : ev.titulo);
    const local = str((d && d.local) || ev.local || "Rio de Janeiro");
    const bairro = str((d && d.sessoes && d.sessoes[0] && d.sessoes[0].bairro) || ev.bairro || "Rio de Janeiro");
    const tipo = TIPOS_AG[ev.tipo] || "evento cultural";
    
    let sessoes = [];
    if (d && arr(d.sessoes).length) {
      sessoes = arr(d.sessoes);
    } else if (arr(ev.destaques).length) {
      for (const pick of ev.destaques) {
        if (arr(pick.sessoes).length) sessoes.push(...pick.sessoes);
      }
    }
    
    let artistas = [];
    if (d && arr(d.artistas).length) {
      artistas = arr(d.artistas);
    } else if (arr(ev.artistas).length) {
      artistas = arr(ev.artistas);
    } else if (arr(ev.destaques).length) {
      for (const pick of ev.destaques) {
        if (arr(pick.artistas).length) artistas.push(...pick.artistas);
      }
    }
    artistas = [...new Set(artistas.map(str).filter(Boolean))];

    const preco = str((d && d.sessoes && d.sessoes[0] && d.sessoes[0].obs) || d?.preco || ev.preco || "");
    const linkIngresso = safeUrl((d && d.sessoes && d.sessoes[0] && d.sessoes[0].link) || d?.link || ev.link || "");
    const linkMapa = AGU.mapa(`${local}, ${bairro}, Rio de Janeiro`);
    const linkTrailer = safeUrl(d?.trailer || ev.trailer || "");
    const reviews = d?.reviews || ev.reviews || null;
    const porque = str(d?.porque || ev.porque || ev.sobre || "");

    const urlConvite = `${window.location.origin}${window.location.pathname}#convite=${encodeURIComponent(evId)}`;
    const dlg = document.getElementById("dlg-convite");
    if (!dlg) return;

    let statusCopia = null;

    const renderConteudo = () => {
      dlg.replaceChildren(h("div", { class: "convite-container" },
        h("div", { class: "convite-topo-bar" },
          h("span", { class: "convite-selo mono" }, `FAIXA OCULTA · CONVITE CULTURAL · ${tipo.toUpperCase()}`),
          h("button", { class: "convite-fechar", type: "button", onclick: () => dlg.close(), "aria-label": "Fechar" }, "×")),
        
        h("h2", { class: "convite-tit" }, titulo),
        h("p", { class: "convite-chamada" }, "Você foi convidado(a) para este evento pelo Radar Cultural Faixa Oculta"),

        h("div", { class: "convite-grid-info" },
          h("div", { class: "convite-info-item" },
            h("span", { class: "lbl" }, "📍 Onde"),
            h("b", null, local),
            bairro ? h("span", { style: "color:var(--muted);font-size:var(--fs-xs);" }, bairro) : null,
            h("a", { href: linkMapa, target: "_blank", rel: "noopener", style: "font-size:var(--fs-xs);margin-top:2px;" }, "Abrir no Google Maps ↗")),
          h("div", { class: "convite-info-item" },
            h("span", { class: "lbl" }, "📅 Quando"),
            sessoes.length ? h("ul", { style: "list-style:none;margin:0;padding:0;display:grid;gap:2px;" },
              sessoes.slice(0, 3).map((s) => h("li", null, h("b", null, agRotulo(s.data, s.hora)), s.obs ? h("span", { style: "color:var(--muted);font-size:var(--fs-xs);display:block;" }, s.obs) : null))
            ) : h("b", null, str(ev.quando || "Consulte a programação"))),
          preco || linkIngresso ? h("div", { class: "convite-info-item" },
            h("span", { class: "lbl" }, "🎟️ Ingressos"),
            preco ? h("span", null, preco) : null,
            linkIngresso ? h("a", { href: linkIngresso, target: "_blank", rel: "noopener", style: "font-weight:700;font-size:var(--fs-xs);margin-top:2px;" }, "Comprar ingresso / Info ↗") : null
          ) : null),

        porque ? [
          h("h4", { class: "convite-secao-tit" }, "Por que ir / O que esperar"),
          h("p", { class: "convite-desc" }, porque)
        ] : null,

        artistas.length ? [
          h("h4", { class: "convite-secao-tit" }, `Line-up & Ouça as bandas (${artistas.length})`),
          h("div", { class: "convite-artistas-lista" }, artistas.map((nome) => chipArtista(nome)))
        ] : null,

        reviews && reviews.texto ? [
          h("h4", { class: "convite-secao-tit" }, "Recepção Crítica"),
          h("div", { class: "convite-review-box" },
            h("p", null, `“${reviews.texto}”`),
            arr(reviews.fontes).length ? h("span", { class: "convite-review-fontes" }, `Fontes: ${reviews.fontes.join(", ")}`) : null)
        ] : null,

        linkTrailer ? [
          h("h4", { class: "convite-secao-tit" }, "Vídeo / Apresentação"),
          h("div", { style: "margin:4px 0;" },
            h("a", { href: linkTrailer, target: "_blank", rel: "noopener", class: "convite-btn-acao" }, "▶ Assistir no YouTube ↗"))
        ] : null,

        statusCopia ? h("div", { style: "padding:8px 12px;background:#eef6ee;border:1px solid #c2e2c2;color:#1e5e1e;border-radius:4px;font-size:var(--fs-s);font-weight:600;" }, statusCopia) : null,

        h("div", { class: "convite-acoes-bar" },
          h("button", {
            type: "button",
            class: "convite-btn-acao destaque",
            onclick: () => {
              if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(urlConvite).then(() => {
                  statusCopia = "✓ Link de convite copiado para a área de transferência!";
                  renderConteudo();
                  setTimeout(() => { statusCopia = null; renderConteudo(); }, 3500);
                }).catch(() => {
                  prompt("Copie o link abaixo:", urlConvite);
                });
              } else {
                prompt("Copie o link abaixo:", urlConvite);
              }
            }
          }, "🔗 Copiar link de convite"),

          h("a", {
            class: "convite-btn-acao",
            target: "_blank",
            rel: "noopener",
            href: `https://api.whatsapp.com/send?text=${encodeURIComponent(`Bora nesse show? 🎵\\n\\n*${titulo}*\\n📍 ${local}\\n📅 ${sessoes.length ? agRotulo(sessoes[0].data, sessoes[0].hora) : str(ev.quando || "")}\\n\\nOuça as bandas e veja a programação completa no convite:\\n${urlConvite}`)}`
          }, "💬 Enviar pelo WhatsApp"),

          navigator.share ? h("button", {
            type: "button",
            class: "convite-btn-acao",
            onclick: () => {
              navigator.share({
                title: `Convite: ${titulo}`,
                text: `Bora nesse show? ${titulo} no ${local}.`,
                url: urlConvite
              }).catch(() => {});
            }
          }, "📤 Compartilhar") : null,

          h("button", {
            type: "button",
            class: "convite-btn-acao",
            onclick: () => dlg.close()
          }, "Fechar")
        )
      ));
    };

    renderConteudo();
    if (!dlg.open) dlg.showModal();
    dlg.scrollTop = 0;

    history.replaceState(null, "", `#convite=${encodeURIComponent(evId)}`);
    dlg.onclose = () => {
      if (window.location.hash.startsWith("#convite=")) {
        history.replaceState(null, "", window.location.pathname + window.location.search);
      }
    };
  }

  function checarDeepLinkConvite() {
    const hash = window.location.hash || "";
    const search = new URLSearchParams(window.location.search);
    let convId = search.get("convite");
    if (!convId && hash.startsWith("#convite=")) {
      convId = decodeURIComponent(hash.slice(9));
    }
    if (!convId || !S.agenda?.eventos) return;

    for (const ev of arr(S.agenda.eventos)) {
      if (ev.id === convId) {
        setTimeout(() => abrirConvite(ev, null), 150);
        return;
      }
      for (const d of arr(ev.destaques)) {
        if (d.id === convId || `${ev.id}__${d.id}` === convId) {
          setTimeout(() => abrirConvite(ev, d), 150);
          return;
        }
      }
    }
  }
"""
    if "function abrirConvite" not in html:
        idx_bloco = html.find("function blocoPlaylists")
        if idx_bloco != -1:
            html = html[:idx_bloco] + funcoes_convite + "\n\n  " + html[idx_bloco:]
            print("Funções abrirConvite e checarDeepLinkConvite inseridas!")

    # 6. Conectar checarDeepLinkConvite no carregamento e no hashchange
    alvo_listen = 'window.addEventListener("popstate", () => {'
    novo_listen = 'window.addEventListener("hashchange", checarDeepLinkConvite);\n  ' + alvo_listen
    if alvo_listen in html and 'hashchange", checarDeepLinkConvite' not in html:
        html = html.replace(alvo_listen, novo_listen, 1)
        print("Listener de hashchange conectado!")

    alvo_carga = 'S.loaded.agenda = true;'
    novo_carga = alvo_carga + '\n      setTimeout(checarDeepLinkConvite, 200);'
    if alvo_carga in html and 'setTimeout(checarDeepLinkConvite' not in html:
        html = html.replace(alvo_carga, novo_carga, 1)
        print("Chamada de checarDeepLinkConvite conectada após carga da agenda!")

    with open("pagina.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("pagina.html gravada com sucesso!")

    # Sincronizar index.html
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
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(skeleton_head + html + skeleton_tail)
    print("index.html sincronizado com sucesso!")

if __name__ == "__main__":
    atualizar_pagina_html()
