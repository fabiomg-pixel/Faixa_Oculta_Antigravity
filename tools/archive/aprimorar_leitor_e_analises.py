import re

css_leitor_definitivo = """/* Modo Leitor Avançado (Controles de Fonte, Tamanho e Tema) */
/* ========================================================
   MODO LEITOR DEFINITIVO (Tipografia, Tamanho, Temas e Contraste)
   ======================================================== */
dialog.texto, dialog.leitura {
  background: var(--lt-bg, #F3EEE4) !important;
  color: var(--lt-fg, #1C1A17) !important;
  border-color: var(--lt-rule, #D4CBBA) !important;
  transition: background .2s ease, color .2s ease;
}

dialog.texto .lt-box,
dialog.leitura,
dialog.leitura .l-bar,
dialog.leitura .l-corpo,
dialog.leitura .l-hero,
dialog.leitura .l-aside,
dialog.leitura .l-criticas {
  background: var(--lt-bg, #F3EEE4) !important;
  color: var(--lt-fg, #1C1A17) !important;
}

/* Forçar TODAS as cores de texto nos modais do leitor para respeitar o tema */
dialog.texto h1, dialog.texto h2, dialog.texto h3, dialog.texto h4,
dialog.texto p, dialog.texto span:not(.fl-ler):not(.edt):not(.mono):not(.lt-meta),
dialog.texto b, dialog.texto strong,
dialog.texto li, dialog.texto blockquote,
dialog.leitura h1, dialog.leitura h2, dialog.leitura h3,
dialog.leitura p, dialog.leitura span:not(.dot):not(.badge):not(.mono):not(.kicker):not(.l-ctx),
dialog.leitura b, dialog.leitura strong,
dialog.leitura li, dialog.leitura dd,
dialog.leitura .l-alb, dialog.leitura .l-olho {
  color: var(--lt-fg, #1C1A17) !important;
}

dialog.texto .mono, dialog.texto .lt-meta,
dialog.leitura .mono, dialog.leitura .kicker, dialog.leitura .l-ctx,
dialog.leitura .ficha dt, dialog.leitura .lt-aviso {
  color: var(--lt-muted, #666055) !important;
}

/* Linhas e bordas nos leitores */
dialog.leitura .l-bar,
dialog.leitura .l-corpo,
dialog.leitura .ficha dt, dialog.leitura .ficha dd,
dialog.leitura .l-criticas,
dialog.leitura .l-criticas .lc,
dialog.texto .lt-link-rodape {
  border-color: var(--lt-rule, #D4CBBA) !important;
}

/* Botões nos leitores */
dialog.leitura .l-btn,
dialog.texto .l-btn {
  border: var(--bw) solid var(--lt-fg, #1C1A17) !important;
  color: var(--lt-fg, #1C1A17) !important;
  background: transparent !important;
}
dialog.leitura .l-btn:hover:not([disabled]),
dialog.texto .l-btn:hover:not([disabled]) {
  background: var(--lt-fg, #1C1A17) !important;
  color: var(--lt-bg, #F3EEE4) !important;
}

/* Controles de leitura */
.lt-controles {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
  padding: 8px 12px;
  background: var(--lt-card, #EAE3D2) !important;
  border: var(--bw) solid var(--lt-rule, #D4CBBA) !important;
  margin: 12px 0 20px;
  font-size: var(--fs-xs);
}
.lt-grupo-ctrl {
  display: flex;
  align-items: center;
  gap: 5px;
}
.lt-lbl-ctrl {
  text-transform: uppercase;
  color: var(--lt-muted, #666055) !important;
  font-size: 11px;
  letter-spacing: .05em;
  margin-right: 2px;
}
.lt-btn-ctrl {
  border: var(--bw) solid var(--lt-rule, #1C1A17) !important;
  background: transparent !important;
  color: var(--lt-fg, #1C1A17) !important;
  padding: 4px 9px;
  cursor: pointer;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  border-radius: 2px;
  transition: all .15s ease;
}
.lt-btn-ctrl.ativo, .lt-btn-ctrl:hover:not([disabled]) {
  background: var(--lt-fg, #1C1A17) !important;
  color: var(--lt-bg, #F3EEE4) !important;
}
.lt-btn-ctrl[disabled] {
  opacity: .35;
  cursor: not-allowed;
}
.lt-tam-val {
  font-weight: 700;
  min-width: 38px;
  text-align: center;
  color: var(--lt-fg, #1C1A17) !important;
}

/* Caixas de destaque e cards de críticas */
dialog.texto .importa,
dialog.texto .lt-visoes-box,
dialog.texto .lt-aprofunda-box,
dialog.texto .cob-card,
dialog.leitura .l-criticas .lc {
  background: var(--lt-card, #EAE3D2) !important;
  color: var(--lt-fg, #1C1A17) !important;
  border-color: var(--lt-rule, #D4CBBA) !important;
}
.lt-visoes-box {
  margin: 22px 0;
  padding: 16px 20px;
  border-left: 4px solid var(--ocre, #B5862C) !important;
}
.lt-aprofunda-box {
  margin: 22px 0;
  padding: 16px 20px;
  border-left: 4px solid var(--anil, #2F4F6F) !important;
}

/* TAMANHO E FONTE DINÂMICOS DO TEXTO (com especificidade sobre 'p') */
dialog.texto .lt-corpo-completo,
dialog.texto .lt-corpo-completo p,
dialog.texto .lt-box p,
dialog.leitura .l-texto,
dialog.leitura .l-texto p,
dialog.leitura .l-criticas .lc p,
dialog.texto .lt-visoes-box p,
dialog.texto .lt-aprofunda-box p,
dialog.texto .importa p {
  font-family: var(--lt-font, var(--f-body, "Newsreader", Georgia, serif)) !important;
  font-size: var(--lt-size, 17px) !important;
  line-height: var(--lt-lh, 1.65) !important;
  color: var(--lt-fg, #1C1A17) !important;
}

/* Espaçamento e alinhamento elegante para leitura fluida */
dialog.texto .lt-corpo-completo p,
dialog.leitura .l-texto p {
  margin: 0 0 1.25em !important;
  text-align: justify !important;
}

.lt-orig-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 5px 12px;
  border: var(--bw) solid var(--sec, var(--red));
  color: var(--sec, var(--red));
  font-size: var(--fs-xs);
  text-decoration: none;
  font-weight: 600;
  border-radius: var(--pill);
  transition: all .15s ease;
}
.lt-orig-btn:hover {
  background: var(--sec, var(--red));
  color: var(--on-sec, #fff) !important;
}
"""

def atualizar_arquivo(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Substituir bloco CSS do Modo Leitor no final do stylesheet
    idx_css_old = content.find('/* Modo Leitor Avançado (Controles de Fonte, Tamanho e Tema) */')
    if idx_css_old != -1:
        end_style = content.find('</style>', idx_css_old)
        content = content[:idx_css_old] + css_leitor_definitivo + "\n" + content[end_style:]
    else:
        last_style = content.rfind('</style>')
        content = content[:last_style] + "\n" + css_leitor_definitivo + "\n" + content[last_style:]

    # 2. Corrigir aplicarLeitorPrefs
    novo_aplicar = """function aplicarLeitorPrefs() {
    const fontesMap = {
      serif: 'var(--f-body, "Newsreader", Georgia, serif)',
      sans: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
      mono: 'var(--f-mono, "IBM Plex Mono", monospace)'
    };
    const temasMap = {
      creme: { bg: "#F3EEE4", fg: "#1C1A17", card: "#EAE3D2", rule: "#D4CBBA", muted: "#666055" },
      escuro: { bg: "#161513", fg: "#EAE5DB", card: "#22201C", rule: "#3E3830", muted: "#9C9588" },
      alvo: { bg: "#FFFFFF", fg: "#111111", card: "#F5F5F5", rule: "#E0E0E0", muted: "#666666" }
    };

    const root = document.documentElement;
    root.style.setProperty("--lt-font", fontesMap[leitorPrefs.fonte] || fontesMap.serif);
    root.style.setProperty("--lt-size", `${leitorPrefs.tam}px`);
    root.style.setProperty("--lt-lh", leitorPrefs.tam >= 20 ? "1.75" : "1.65");

    const t = temasMap[leitorPrefs.tema] || temasMap.creme;
    root.style.setProperty("--lt-bg", t.bg);
    root.style.setProperty("--lt-fg", t.fg);
    root.style.setProperty("--lt-card", t.card);
    root.style.setProperty("--lt-rule", t.rule);
    root.style.setProperty("--lt-muted", t.muted);
  }"""
    content = re.sub(r'function aplicarLeitorPrefs\(\)\s*\{[\s\S]*?root\.style\.setProperty\("--lt-rule",\s*t\.rule\);\s*\}', lambda m: novo_aplicar, content)

    # 3. Corrigir barraControlesLeitor(() => renderAberto()) -> barraControlesLeitor(() => renderLeitura())
    content = content.replace('barraControlesLeitor(() => renderAberto())', 'barraControlesLeitor(() => renderLeitura())')

    # 4. Adicionar aplicarLeitorPrefs em abrirLeitura
    content = re.sub(
        r'function abrirLeitura\(key\)\s*\{\s*opener = document\.activeElement;\s*openerRef = guardarFoco\(\);\s*S\.aberto = key;\s*renderLeitura\(\);\s*\}',
        lambda m: 'function abrirLeitura(key) { opener = document.activeElement; openerRef = guardarFoco(); S.aberto = key; aplicarLeitorPrefs(); renderLeitura(); }',
        content
    )

    # 5. Adicionar aplicarLeitorPrefs em renderLeitura se não tiver
    if 'function renderLeitura() {\n    aplicarLeitorPrefs();' not in content:
        content = re.sub(
            r'function renderLeitura\(\)\s*\{',
            lambda m: 'function renderLeitura() {\n    aplicarLeitorPrefs();',
            content
        )

    # 6. Aprimorar criticasDe para buscar tanto em S.leituras quanto em item.analises_criticas
    novo_criticas_de = """function criticasDe(ref, item) {
    const chaveItem = item ? (item._id || item.id || ref) : ref;
    const slugLimpo = str(ref).replace(/^\\d{4}-\\d{2}--/, "");
    const slugItem = item ? str(item._id || item.id || "").replace(/^\\d{4}-\\d{2}--/, "") : "";
    const lista = (S.leituras || []).filter((l) => {
      if (!l.ref) return false;
      return l.ref === ref || l.ref === chaveItem || l.ref === slugLimpo || (slugItem && l.ref === slugItem);
    }).sort((a, b) => (Number(a.ordem) || 9) - (Number(b.ordem) || 9));

    if (lista.length) return lista;
    if (item && Array.isArray(item.analises_criticas) && item.analises_criticas.length) {
      return item.analises_criticas;
    }
    return [];
  }"""
    content = re.sub(r'const criticasDe = \(ref\) => S\.leituras\.filter\(\(l\) => l\.ref === ref\)\.sort\(\(a, b\) => \(Number\(a\.ordem\) \|\| 9\) - \(Number\(b\.ordem\) \|\| 9\)\);', lambda m: novo_criticas_de, content)

    # 7. Passar 'a' para criticasDe em renderLeitura: criticasDe(S.aberto, a)
    content = content.replace('const cs = criticasDe(S.aberto);', 'const cs = criticasDe(S.aberto, a);')

    # 8. Atualizar abrirTexto para usar aplicarLeitorPrefs, barraControlesLeitor e lt-corpo-completo
    novo_abrir_texto = """function abrirTexto(l) {
    aplicarLeitorPrefs();
    const t = document.getElementById("texto");
    t.replaceChildren(h("div", { class: "lt-box" },
      h("div", { class: "lt-bar" },
        h("span", { class: "mono" }, l.tipo === "review" ? "Modo Leitor · Crítica Especializada" : "Modo Leitor · Conteúdo na Íntegra"),
        h("button", { class: "l-btn", type: "button", onclick: () => t.close(), "aria-label": "Fechar" }, "Fechar ×")),
      barraControlesLeitor(() => abrirTexto(l)),
      h("div", { class: "lt-meta mono" },
        h("b", null, str(l.fonte)),
        [l.autor, l.data ? fmtData(l.data) : ""].map(str).filter(Boolean).join(" · "),
        l.nota ? h("span", { class: "lt-nota" }, str(l.nota)) : null),
      l.titulo ? h("h2", { class: "lt-tit", style: "margin:10px 0 16px;line-height:1.18;" }, str(l.titulo)) : null,
      safeUrl(l.url) ? h("div", { class: "lt-link-topo", style: "margin-bottom:18px;" },
        h("a", { class: "lt-orig-btn", href: safeUrl(l.url), target: "_blank", rel: "noopener" }, `Acessar no site original de ${str(l.fonte) || "origem"} ↗`)) : null,
      h("div", { class: "lt-corpo-completo" },
        arr(l.texto_integral && l.texto_integral.length ? l.texto_integral : l.resumo).map((p) => h("p", null, str(p)))),
      arr(l.pontos).length ? [
        h("h4", { style: "margin:24px 0 10px;font-size:var(--fs-xs);text-transform:uppercase;color:var(--muted);letter-spacing:.05em;" }, "Pontos centrais da reportagem"),
        h("ul", { class: "lt-pontos" }, arr(l.pontos).map((x) => h("li", null, str(x))))
      ] : null,
      l.citacao ? h("blockquote", { class: "lt-cit", style: "margin:20px 0;padding:12px 18px;border-left:4px solid var(--sec, var(--red));font-style:italic;" }, `“${str(l.citacao)}”`) : null,
      safeUrl(l.url) ? h("div", { class: "lt-link-rodape", style: "margin-top:28px;padding-top:16px;border-top:1px solid var(--lt-rule, var(--rule));display:flex;align-items:center;justify-content:space-between;" },
        h("a", { class: "lt-orig-btn", href: safeUrl(l.url), target: "_blank", rel: "noopener" }, `Acessar no site original de ${str(l.fonte) || "origem"} ↗`),
        h("span", { class: "mono lt-aviso" }, "Texto carregado previamente no modo leitor")) : null,
      h("p", { class: "lt-aviso mono", style: "margin-top:20px;" }, "Faixa Oculta · Conteúdo na íntegra em formato leitor padronizado, sem anúncios nem rastreadores.")));
    t.showModal();
    t.querySelector(".l-btn").focus({ preventScroll: true });
  }"""
    content = re.sub(r'function abrirTexto\(l\)\s*\{[\s\S]*?t\.querySelector\("\.l-btn"\)\.focus\(\{ preventScroll: true \}\);\s*\}', lambda m: novo_abrir_texto, content)

    # 9. Tornar os cards clicáveis diretamente para o modo leitor
    # card(it)
    content = re.sub(
        r'function card\(it\)\s*\{\s*const key = it\._id;\s*const cur = S\.marcas\[key\];\s*const clsCard = "card" \+ \(cur === "nao" \? " d-nao" : cur === "quero" \? " d-quero" : ""\);\s*const meta = \[fmtData\(it\.data \|\| it\.ano\), it\.formato, it\.selo, it\.genero\]\.map\(str\)\.filter\(Boolean\);\s*const abrir = \(\) => abrirLeitura\(key\);\s*const nome = str\(it\.exibir_artista \|\| it\.artista\);\s*return h\("article", \{ class: clsCard \}',
        lambda m: 'function card(it) {\n    const key = it._id;\n    const cur = S.marcas[key];\n    const clsCard = "card" + (cur === "nao" ? " d-nao" : cur === "quero" ? " d-quero" : "");\n    const meta = [fmtData(it.data || it.ano), it.formato, it.selo, it.genero].map(str).filter(Boolean);\n    const abrir = () => abrirLeitura(key);\n    const nome = str(it.exibir_artista || it.artista);\n    return h("article", { class: clsCard, onclick: abrir, style: "cursor:pointer" }',
        content
    )

    # cardObra(a, key, cfg)
    content = re.sub(
        r'function cardObra\(a, key, cfg\)\s*\{\s*const cur = S\.marcas\[key\];\s*const clsCard = "card mcard" \+ \(cur === "nao" \? " d-nao" : cur === "quero" \? " d-quero" : ""\);\s*const abrir = \(\) => abrirLeitura\(key\);\s*return h\("article", \{ class: clsCard \}',
        lambda m: 'function cardObra(a, key, cfg) {\n    const cur = S.marcas[key];\n    const clsCard = "card mcard" + (cur === "nao" ? " d-nao" : cur === "quero" ? " d-quero" : "");\n    const abrir = () => abrirLeitura(key);\n    return h("article", { class: clsCard, onclick: abrir, style: "cursor:pointer" }',
        content
    )

    # d-nota
    content = re.sub(
        r'h\("article", \{ class: "d-nota" \}',
        lambda m: 'h("article", { class: "d-nota", onclick: () => abrirNota(n, bol), style: "cursor:pointer" }',
        content
    )

    # Proteger botões internos do d-nota contra propagação indevida
    content = re.sub(
        r'h\("div", \{ class: "d-nota-acts" \}',
        lambda m: 'h("div", { class: "d-nota-acts", onclick: (e) => e.stopPropagation() }',
        content
    )

    # Proteger atos em card e cardObra
    content = re.sub(
        r'h\("div", \{ class: "acts" \}, it\._semLeitura \? null : botaoOuvir\(it\), marcas\(key, it\._rot\)\)',
        lambda m: 'h("div", { class: "acts", onclick: (e) => e.stopPropagation() }, it._semLeitura ? null : botaoOuvir(it), marcas(key, it._rot))',
        content
    )
    content = re.sub(
        r'h\("div", \{ class: "acts" \}, botaoTrailer\(a\), botaoStremio\(a\), marcas\(key, cfg\.rot\)\)',
        lambda m: 'h("div", { class: "acts", onclick: (e) => e.stopPropagation() }, botaoTrailer(a), botaoStremio(a), marcas(key, cfg.rot))',
        content
    )

    # Botão "Fonte" em links(a) e linksObra(a): abrir no leitor primeiro!
    content = content.replace(
        'safeUrl(a.fonte) ? h("a", { href: safeUrl(a.fonte), target: "_blank", rel: "noopener" }, "Fonte") : null',
        'safeUrl(a.fonte) ? h("button", { type: "button", class: "fl-ler", style: "font-size:11px;", onclick: (e) => { e.stopPropagation(); abrirTexto({ fonte: "Fonte Oficial", titulo: `${str(a.album || a.titulo)} — Cobertura e Análise`, resumo: Array.isArray(a.resenha) && a.resenha.length ? a.resenha : [a.texto || a.nota || ""], url: a.fonte }); }, title: "Abrir fonte no modo leitor" }, "Fonte") : null'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Atualizado {path} com sucesso.")

atualizar_arquivo('index.html')
atualizar_arquivo('pagina.html')
