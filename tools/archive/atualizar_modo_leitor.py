#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Implementa o Modo Leitor Avançado (fontes, tamanhos, temas, texto completo) em pagina.html e index.html.
Elimina a mensagem 'O texto completo entra na próxima atualização.'.
"""

import sys

def atualizar_codigo(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. CSS do Modo Leitor
    css_leitor = """
/* Modo Leitor Avançado (Controles de Fonte, Tamanho e Tema) */
dialog.texto, dialog.leitura {
  background: var(--lt-bg, var(--paper));
  color: var(--lt-fg, var(--ink));
  border: var(--bw) solid var(--lt-rule, var(--ink));
  transition: background .2s ease, color .2s ease;
}
.lt-box {
  background: var(--lt-bg, var(--paper));
  color: var(--lt-fg, var(--ink));
}
.lt-corpo-completo, .l-texto {
  font-family: var(--lt-font, var(--f-body));
  font-size: var(--lt-size, 17px) !important;
  line-height: var(--lt-lh, 1.65) !important;
  color: var(--lt-fg, var(--ink));
}
.lt-corpo-completo p, .l-texto p {
  margin: 0 0 1.25em;
  text-align: justify;
}
.lt-controles {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  flex-wrap: wrap;
  padding: 8px 12px;
  background: var(--lt-card, var(--card));
  border: var(--bw) solid var(--lt-rule, var(--rule));
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
  color: var(--muted);
  font-size: 11px;
  letter-spacing: .05em;
  margin-right: 2px;
}
.lt-btn-ctrl {
  border: var(--bw) solid var(--lt-rule, var(--ink));
  background: transparent;
  color: var(--lt-fg, var(--ink));
  padding: 4px 9px;
  cursor: pointer;
  font-family: inherit;
  font-size: 12px;
  font-weight: 600;
  border-radius: 2px;
  transition: all .15s ease;
}
.lt-btn-ctrl.ativo, .lt-btn-ctrl:hover:not([disabled]) {
  background: var(--lt-fg, var(--ink));
  color: var(--lt-bg, var(--paper));
}
.lt-btn-ctrl[disabled] {
  opacity: .35;
  cursor: not-allowed;
}
.lt-tam-val {
  font-weight: 700;
  min-width: 38px;
  text-align: center;
}
.lt-visoes-box {
  margin: 22px 0;
  padding: 16px 20px;
  background: var(--lt-card, var(--card));
  border-left: 4px solid var(--ocre, #B5862C);
}
.lt-aprofunda-box {
  margin: 22px 0;
  padding: 16px 20px;
  background: var(--lt-card, var(--card));
  border-left: 4px solid var(--anil, #2F4F6F);
}
.lt-orig-btn {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  padding: 4px 10px;
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
  color: var(--on-sec, #fff);
}
"""
    if "/* Modo Leitor Avançado" not in c:
        c = c.replace("</style>", css_leitor + "\n</style>")

    # 2. JavaScript: Estado e Funções do Leitor
    js_leitor = """
  // Modo Leitor: Preferências do usuário (persistidas em localStorage)
  let leitorPrefs = {
    fonte: "serif",
    tam: 17,
    tema: "creme"
  };
  try {
    const s = localStorage.getItem("fo_leitor_prefs");
    if (s) leitorPrefs = { ...leitorPrefs, ...JSON.parse(s) };
  } catch (e) {}

  function salvarLeitorPrefs() {
    try {
      localStorage.setItem("fo_leitor_prefs", JSON.stringify(leitorPrefs));
    } catch (e) {}
    aplicarLeitorPrefs();
  }

  function aplicarLeitorPrefs() {
    const fontesMap = {
      serif: 'var(--f-body, "Newsreader", Georgia, serif)',
      sans: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif',
      mono: 'var(--f-mono, "IBM Plex Mono", monospace)'
    };
    const temasMap = {
      creme: { bg: "var(--paper)", fg: "var(--ink)", card: "var(--card)", rule: "var(--rule)" },
      escuro: { bg: "#1C1A17", fg: "#ECE5D8", card: "#26231F", rule: "#3E3933" },
      alvo: { bg: "#FFFFFF", fg: "#111111", card: "#F7F7F7", rule: "#E0E0E0" }
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
  }

  function barraControlesLeitor(aoMudar) {
    return h("div", { class: "lt-controles mono" },
      h("div", { class: "lt-grupo-ctrl" },
        h("span", { class: "lt-lbl-ctrl" }, "Fonte:"),
        h("button", {
          type: "button",
          class: `lt-btn-ctrl ${leitorPrefs.fonte === "serif" ? "ativo" : ""}`,
          onclick: () => { leitorPrefs.fonte = "serif"; salvarLeitorPrefs(); if (aoMudar) aoMudar(); }
        }, "Serif"),
        h("button", {
          type: "button",
          class: `lt-btn-ctrl ${leitorPrefs.fonte === "sans" ? "ativo" : ""}`,
          onclick: () => { leitorPrefs.fonte = "sans"; salvarLeitorPrefs(); if (aoMudar) aoMudar(); }
        }, "Sans"),
        h("button", {
          type: "button",
          class: `lt-btn-ctrl ${leitorPrefs.fonte === "mono" ? "ativo" : ""}`,
          onclick: () => { leitorPrefs.fonte = "mono"; salvarLeitorPrefs(); if (aoMudar) aoMudar(); }
        }, "Mono")
      ),
      h("div", { class: "lt-grupo-ctrl" },
        h("span", { class: "lt-lbl-ctrl" }, "Tamanho:"),
        h("button", {
          type: "button",
          class: "lt-btn-ctrl",
          disabled: leitorPrefs.tam <= 14,
          title: "Diminuir fonte",
          onclick: () => {
            if (leitorPrefs.tam > 14) {
              leitorPrefs.tam -= 2;
              salvarLeitorPrefs();
              if (aoMudar) aoMudar();
            }
          }
        }, "A−"),
        h("span", { class: "lt-tam-val" }, `${leitorPrefs.tam}px`),
        h("button", {
          type: "button",
          class: "lt-btn-ctrl",
          disabled: leitorPrefs.tam >= 24,
          title: "Aumentar fonte",
          onclick: () => {
            if (leitorPrefs.tam < 24) {
              leitorPrefs.tam += 2;
              salvarLeitorPrefs();
              if (aoMudar) aoMudar();
            }
          }
        }, "A+")
      ),
      h("div", { class: "lt-grupo-ctrl" },
        h("span", { class: "lt-lbl-ctrl" }, "Tema:"),
        h("button", {
          type: "button",
          class: `lt-btn-ctrl ${leitorPrefs.tema === "creme" ? "ativo" : ""}`,
          title: "Tema Creme (Papel)",
          onclick: () => { leitorPrefs.tema = "creme"; salvarLeitorPrefs(); if (aoMudar) aoMudar(); }
        }, "Papel"),
        h("button", {
          type: "button",
          class: `lt-btn-ctrl ${leitorPrefs.tema === "escuro" ? "ativo" : ""}`,
          title: "Tema Escuro (Leitura Noturna)",
          onclick: () => { leitorPrefs.tema = "escuro"; salvarLeitorPrefs(); if (aoMudar) aoMudar(); }
        }, "Escuro"),
        h("button", {
          type: "button",
          class: `lt-btn-ctrl ${leitorPrefs.tema === "alvo" ? "ativo" : ""}`,
          title: "Tema Branco Puro",
          onclick: () => { leitorPrefs.tema = "alvo"; salvarLeitorPrefs(); if (aoMudar) aoMudar(); }
        }, "Branco")
      )
    );
  }
"""

    if "let leitorPrefs =" not in c:
        c = c.replace("function chaveNota(n, d) {", js_leitor + "\n  function chaveNota(n, d) {")

    # 3. Substituir abrirNota por versão completa com texto_completo, visões e aprofundamento
    codigo_antigo_abrirNota = """  function abrirNota(n, d) {
    const t = document.getElementById("texto");
    const rotulo = d ? rotuloBoletim(d) : "Boletim diário";
    const fontesLeituras = arr(n.fontes).map((f) => ({ f, leitura: leituraDe(f.url) }));
    const secaoFontes = fontesLeituras.map(({ f, leitura }) => {
      if (leitura) {
        const paras = arr(leitura.texto_integral && leitura.texto_integral.length ? leitura.texto_integral : leitura.resumo);
        return h("div", { class: "lt-fonte-bloco" },
          h("div", { class: "lt-meta mono" },
            h("b", null, str(f.fonte)),
            [f.perfil, leitura.autor, leitura.data ? fmtData(leitura.data) : ""].filter(Boolean).join(" · ")),
          leitura.titulo ? h("h4", { class: "lt-art-tit" }, str(leitura.titulo)) : null,
          f.enfoque ? h("p", { class: "lt-enfoque" }, `Enfoque da apuração: ${str(f.enfoque)}`) : null,
          safeUrl(f.url) ? h("div", { class: "lt-link-topo" },
            h("a", { class: "lt-orig", href: safeUrl(f.url), target: "_blank", rel: "noopener" }, `Acessar no site original de ${str(f.fonte)} ↗`)) : null,
          ...paras.map((p) => h("p", null, str(p))),
          arr(leitura.pontos).length ? [
            h("h5", { style: "margin:18px 0 6px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.05em;color:var(--muted);" }, "Pontos centrais destacados"),
            h("ul", { class: "lt-pontos" }, arr(leitura.pontos).map((x) => h("li", null, str(x))))
          ] : null,
          leitura.citacao ? h("blockquote", { class: "lt-cit" }, `“${str(leitura.citacao)}”`) : null,
          safeUrl(f.url) ? h("div", { class: "lt-link-rodape" },
            h("a", { class: "lt-orig", href: safeUrl(f.url), target: "_blank", rel: "noopener" }, `Matéria original completa em ${str(f.fonte)} ↗`)) : null);
      }
      return h("div", { class: "lt-fonte-bloco" },
        h("div", { class: "lt-meta mono" }, h("b", null, str(f.fonte)), f.perfil ? ` · ${str(f.perfil)}` : ""),
        f.enfoque ? h("p", { class: "lt-enfoque" }, str(f.enfoque)) : null,
        safeUrl(f.url) ? h("div", { class: "lt-link-rodape" },
          h("a", { class: "lt-orig", href: safeUrl(f.url), target: "_blank", rel: "noopener" }, `Consultar no site original de ${str(f.fonte)} ↗`)) : null);
    });

    t.replaceChildren(h("div", { class: "lt-box" },
      h("div", { class: "lt-bar" },
        h("span", { class: "mono" }, `Modo Leitor · Conteúdo na íntegra`),
        h("button", { class: "l-btn", type: "button", onclick: () => t.close(), "aria-label": "Fechar" }, "Fechar ×")),
      h("div", { class: "lt-meta mono" }, str(rotulo)),
      h("h3", { class: "lt-tit" }, str(n.titulo)),
      h("div", { class: "lt-lead" }, str(n.texto)),
      n.por_que_importa ? h("div", { class: "importa", style: "margin:20px 0;padding:16px 20px;background:var(--card);border-left:var(--bw-rule) solid var(--sec);" },
        h("h4", { style: "margin:0 0 6px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.06em;color:var(--sec);" }, "Por que importa"),
        h("p", { style: "margin:0;" }, str(n.por_que_importa))) : null,
      secaoFontes.length ? [
        h("h4", { class: "lt-divisor-tit" }, "Cobertura das fontes apuradas (conteúdo na íntegra)"),
        ...secaoFontes
      ] : null,
      h("p", { class: "lt-aviso mono", style: "margin-top:32px;" }, "Faixa Oculta · Conteúdo na íntegra em formato leitor padronizado, sem anúncios nem rastreadores.")));
    t.showModal();
    t.querySelector(".l-btn").focus({ preventScroll: true });
  }"""

    codigo_novo_abrirNota = """  function abrirNota(n, d) {
    aplicarLeitorPrefs();
    const t = document.getElementById("texto");
    const rotulo = d ? rotuloBoletim(d) : "Boletim diário";
    const redesenharNota = () => abrirNota(n, d);

    // Texto completo na íntegra (usa array texto_completo se existir, ou divide o texto)
    let paras = [];
    if (Array.isArray(n.texto_completo) && n.texto_completo.length) {
      paras = n.texto_completo;
    } else if (n.texto) {
      paras = String(n.texto).split("\\n\\n").filter(Boolean);
    }

    // Fontes apuradas com botão destacado para abrir site original
    const secaoFontes = arr(n.fontes).map((f) => {
      const leitura = leituraDe(f.url);
      const parasFonte = leitura ? arr(leitura.texto_integral && leitura.texto_integral.length ? leitura.texto_integral : leitura.resumo) : [];
      return h("div", { class: "lt-fonte-bloco", style: "border-top:1px solid var(--lt-rule, var(--rule));padding-top:14px;margin-top:16px;" },
        h("div", { style: "display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;" },
          h("div", { class: "lt-meta mono" }, h("b", null, str(f.fonte)), f.perfil ? ` · ${str(f.perfil)}` : ""),
          safeUrl(f.url) ? h("a", { class: "lt-orig-btn mono", href: safeUrl(f.url), target: "_blank", rel: "noopener" }, `Acessar no site original de ${str(f.fonte)} ↗`) : null
        ),
        f.enfoque ? h("p", { class: "lt-enfoque", style: "margin:8px 0 6px;font-style:italic;" }, `Enfoque da apuração: ${str(f.enfoque)}`) : null,
        parasFonte.length ? h("div", { style: "margin-top:8px;" }, parasFonte.map((p) => h("p", null, str(p)))) : null,
        leitura && arr(leitura.pontos).length ? [
          h("h5", { style: "margin:14px 0 6px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.05em;color:var(--muted);" }, "Pontos centrais destacados"),
          h("ul", { class: "lt-pontos" }, arr(leitura.pontos).map((x) => h("li", null, str(x))))
        ] : null,
        leitura && leitura.citacao ? h("blockquote", { class: "lt-cit" }, `“${str(leitura.citacao)}”`) : null
      );
    });

    t.replaceChildren(h("div", { class: "lt-box" },
      h("div", { class: "lt-bar" },
        h("span", { class: "mono" }, `Modo Leitor · ${str(n.editoria || "Notícia")}`),
        h("button", { class: "l-btn", type: "button", onclick: () => t.close(), "aria-label": "Fechar" }, "Fechar ×")),
      barraControlesLeitor(redesenharNota),
      h("div", { class: "lt-meta mono" }, str(rotulo)),
      h("h2", { class: "lt-tit", style: "margin:10px 0 16px;line-height:1.18;" }, str(n.titulo)),
      
      // Conteúdo completo na íntegra
      h("div", { class: "lt-corpo-completo" }, paras.map((p) => h("p", null, str(p)))),

      // Por que importa
      n.por_que_importa ? h("div", { class: "importa", style: "margin:20px 0;padding:16px 20px;background:var(--lt-card, var(--card));border-left:4px solid var(--sec, var(--red));" },
        h("h4", { style: "margin:0 0 6px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.06em;color:var(--sec, var(--red));" }, "Por que importa"),
        h("p", { style: "margin:0;line-height:1.55;" }, str(n.por_que_importa))) : null,

      // Resumo das Diferentes Visões e Linhas Editoriais
      n.resumo_visoes ? h("div", { class: "lt-visoes-box" },
        h("h4", { style: "margin:0 0 8px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.06em;color:var(--ocre, #B5862C);" }, "Diferentes Visões & Linhas Editoriais"),
        h("p", { style: "margin:0;font-size:15px;line-height:1.6;" }, str(n.resumo_visoes))) : null,

      // Para aprofundar: Contexto e desdobramentos
      n.aprofundamento ? h("div", { class: "lt-aprofunda-box" },
        h("h4", { style: "margin:0 0 8px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.06em;color:var(--anil, #2F4F6F);" }, "Para Aprofundar: Contexto & Desdobramentos"),
        n.aprofundamento.contexto ? h("p", { style: "margin:0 0 8px;font-size:15px;line-height:1.6;" }, [h("b", null, "Contexto histórico: "), str(n.aprofundamento.contexto)]) : null,
        n.aprofundamento.o_que_observar ? h("p", { style: "margin:0;font-size:15px;line-height:1.6;" }, [h("b", null, "O que observar a seguir: "), str(n.aprofundamento.o_que_observar)]) : null
      ) : null,

      // Fontes verificadas com links diretos
      secaoFontes.length ? [
        h("h4", { class: "lt-divisor-tit", style: "margin:28px 0 10px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.05em;color:var(--muted);" }, "Fontes verificadas & Cobertura original"),
        ...secaoFontes
      ] : null,

      h("div", { style: "margin-top:32px;padding-top:16px;border-top:1px solid var(--lt-rule, var(--rule));display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;" },
        h("button", {
          class: `d-btn-salvar mono ${isNotaSalva(n, d) ? "salva" : ""}`,
          type: "button",
          onclick: () => { toggleSalvarNoticia(n, d); redesenharNota(); }
        }, isNotaSalva(n, d) ? "✓ Matéria salva" : "🔖 Salvar para ler depois"),
        h("p", { class: "lt-aviso mono", style: "margin:0;" }, "Faixa Oculta · Modo Leitor imersivo, sem anúncios nem rastreadores."))
    ));
    t.showModal();
    t.querySelector(".l-btn").focus({ preventScroll: true });
  }"""

    if codigo_antigo_abrirNota in c:
        c = c.replace(codigo_antigo_abrirNota, codigo_novo_abrirNota)
        print(f"abrirNota atualizado com sucesso em {caminho}!")
    else:
        print(f"Aviso: trecho exato de abrirNota não encontrado em {caminho}. Verificando variações...")

    # 4. Eliminar completamente "O texto completo entra na próxima atualização." em renderAberto
    texto_sem_resenha_antigo = """resenha.length ? resenha.map((p) => h("p", null, p))
          : [h("p", null, str(a.texto || a.nota || "")), h("p", { class: "l-sem" }, "O texto completo entra na próxima atualização.")]"""

    texto_sem_resenha_novo = """resenha.length ? resenha.map((p) => h("p", null, p))
          : [
              h("p", null, str(a.texto || a.nota || "")),
              a.olho ? h("p", { class: "l-olho-int", style: "font-style:italic;margin-top:12px;" }, str(a.olho)) : null,
              a.recepcao ? h("p", { class: "rec", style: "margin-top:12px;" }, [h("b", null, "Recepção crítica: "), str(a.recepcao)]) : null
            ].filter(Boolean)"""

    if texto_sem_resenha_antigo in c:
        c = c.replace(texto_sem_resenha_antigo, texto_sem_resenha_novo)
        print(f"Frase placeholder erradicada em {caminho}!")

    # 5. Adicionar toolbar do leitor também dentro do diálogo da obra (renderAberto)
    trecho_hero_antigo = """h("div", { class: "wrap l-hero" },"""
    trecho_hero_novo = """h("div", { class: "wrap" }, barraControlesLeitor(() => renderAberto())),
      h("div", { class: "wrap l-hero" },"""

    if trecho_hero_antigo in c and "barraControlesLeitor(() => renderAberto())" not in c:
        c = c.replace(trecho_hero_antigo, trecho_hero_novo)
        print(f"Toolbar adicionada ao modal de obras em {caminho}!")

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(c)

    print(f"Concluído com sucesso para {caminho}!")

if __name__ == "__main__":
    atualizar_codigo("pagina.html")
    atualizar_codigo("index.html")
