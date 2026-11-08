#!/usr/bin/env python3
"""
atualizar_filtros_midia_html.py
Aplica a barra de filtros de mídia, os badges e a tradução no leitor em pagina.html e index.html.
"""

import re

def aplicar(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Atualizar blocoHoje
    alvo_bloco_hoje = """    let notasParaExibir = [];
    if (S.filtroSalvas) {"""

    subst_bloco_hoje = """    // Filtros de Mídia: Nacional vs Internacional
    S.filtroEscopo = S.filtroEscopo || "todas";
    const totalTodas = arr(d.notas).length;
    const totalNac = arr(d.notas).filter((n) => n.escopo !== "internacional" && n.pais !== "Internacional").length;
    const totalInt = arr(d.notas).filter((n) => n.escopo === "internacional" || n.pais === "Internacional" || n.titulo_original).length;

    const barraFiltroMidia = totalInt > 0 && !S.filtroSalvas ? h("div", { class: "d-midia-filtro-box" },
      h("span", { class: "mono", style: "font-size:var(--fs-xs);color:var(--muted);margin-right:6px;" }, "Eixo de apuração:"),
      h("button", {
        class: `d-btn-filtro-midia mono ${S.filtroEscopo === "todas" ? "ativo" : ""}`,
        type: "button",
        onclick: () => { S.filtroEscopo = "todas"; render(); }
      }, `Todas (${totalTodas})`),
      h("button", {
        class: `d-btn-filtro-midia mono ${S.filtroEscopo === "nacional" ? "ativo" : ""}`,
        type: "button",
        onclick: () => { S.filtroEscopo = "nacional"; render(); }
      }, `🇧🇷 Mídia Nacional (${totalNac})`),
      h("button", {
        class: `d-btn-filtro-midia mono ${S.filtroEscopo === "internacional" ? "ativo" : ""}`,
        type: "button",
        onclick: () => { S.filtroEscopo = "internacional"; render(); }
      }, `🌍 Mídia Internacional Traduzida (${totalInt})`)
    ) : null;

    let notasParaExibir = [];
    if (S.filtroSalvas) {"""

    if "S.filtroEscopo = S.filtroEscopo ||" not in code:
        code = code.replace(alvo_bloco_hoje, subst_bloco_hoje, 1)

    # 2. Filtragem de notas
    alvo_else_notas = """    } else {
      notasParaExibir = arr(d.notas).map((n) => ({ nota: n, boletim: d, rotulo: "" }));
    }"""

    subst_else_notas = """    } else {
      let listaNotas = arr(d.notas);
      if (S.filtroEscopo === "nacional") {
        listaNotas = listaNotas.filter((n) => n.escopo !== "internacional" && n.pais !== "Internacional");
      } else if (S.filtroEscopo === "internacional") {
        listaNotas = listaNotas.filter((n) => n.escopo === "internacional" || n.pais === "Internacional" || n.titulo_original);
      }
      notasParaExibir = listaNotas.map((n) => ({ nota: n, boletim: d, rotulo: "" }));
    }"""

    if "let listaNotas = arr(d.notas);" not in code:
        code = code.replace(alvo_else_notas, subst_else_notas, 1)

    # 3. Inserir barraFiltroMidia antes da grade de notas
    alvo_grade = """    const grade = h("section", { class: "wrap", style: "padding-bottom:24px" },"""
    subst_grade = """    const grade = h("section", { class: "wrap", style: "padding-bottom:24px" },
      barraFiltroMidia,"""

    if "barraFiltroMidia," not in code:
        code = code.replace(alvo_grade, subst_grade, 1)

    # 4. Inserir badge internacional e título original no card d-nota
    alvo_card_head = """        h("div", { style: "display:flex;align-items:center;justify-content:space-between;gap:8px;" },
          h("span", { class: "edt" }, str(n.editoria)),
          rotulo ? h("span", { class: "mono", style: "font-size:var(--fs-xs);color:var(--muted);" }, rotulo) : null),
        h("h3", { class: "d-nota-tit", role: "button", tabindex: "0", onclick: () => abrirNota(n, bol), title: "Abrir matéria no modo leitor" }, str(n.titulo)),"""

    subst_card_head = """        const ehInt = n.escopo === "internacional" || n.pais === "Internacional" || n.titulo_original;
        return h("article", { class: `d-nota ${ehInt ? "d-nota-int" : ""}`, onclick: () => abrirNota(n, bol), style: "cursor:pointer" },
          h("div", { style: "display:flex;align-items:center;justify-content:space-between;gap:8px;" },
            h("div", { style: "display:flex;align-items:center;gap:6px;flex-wrap:wrap;" },
              h("span", { class: "edt" }, str(n.editoria)),
              ehInt ? h("span", { class: "badge-int mono" }, "🌍 Internacional") : null
            ),
            rotulo ? h("span", { class: "mono", style: "font-size:var(--fs-xs);color:var(--muted);" }, rotulo) : null),
          h("h3", { class: "d-nota-tit", role: "button", tabindex: "0", onclick: () => abrirNota(n, bol), title: "Abrir matéria no modo leitor" }, str(n.titulo)),
          n.titulo_original && n.titulo_original !== n.titulo ? h("p", { class: "d-nota-subtit-orig mono" }, `Original: “${str(n.titulo_original)}”`) : null,"""

    # Substituir no map das notas
    alvo_map_artigo = """      h("div", { class: "d-notas" }, notasParaExibir.map(({ nota: n, boletim: bol, rotulo }) => h("article", { class: "d-nota", onclick: () => abrirNota(n, bol), style: "cursor:pointer" },
        h("div", { style: "display:flex;align-items:center;justify-content:space-between;gap:8px;" },
          h("span", { class: "edt" }, str(n.editoria)),
          rotulo ? h("span", { class: "mono", style: "font-size:var(--fs-xs);color:var(--muted);" }, rotulo) : null),
        h("h3", { class: "d-nota-tit", role: "button", tabindex: "0", onclick: () => abrirNota(n, bol), title: "Abrir matéria no modo leitor" }, str(n.titulo)),"""

    subst_map_artigo = """      h("div", { class: "d-notas" }, notasParaExibir.map(({ nota: n, boletim: bol, rotulo }) => {
        const ehInt = n.escopo === "internacional" || n.pais === "Internacional" || n.titulo_original;
        return h("article", { class: `d-nota ${ehInt ? "d-nota-int" : ""}`, onclick: () => abrirNota(n, bol), style: "cursor:pointer" },
          h("div", { style: "display:flex;align-items:center;justify-content:space-between;gap:8px;" },
            h("div", { style: "display:flex;align-items:center;gap:6px;flex-wrap:wrap;" },
              h("span", { class: "edt" }, str(n.editoria)),
              ehInt ? h("span", { class: "badge-int mono" }, "🌍 Internacional") : null
            ),
            rotulo ? h("span", { class: "mono", style: "font-size:var(--fs-xs);color:var(--muted);" }, rotulo) : null),
          h("h3", { class: "d-nota-tit", role: "button", tabindex: "0", onclick: () => abrirNota(n, bol), title: "Abrir matéria no modo leitor" }, str(n.titulo)),
          n.titulo_original && n.titulo_original !== n.titulo ? h("p", { class: "d-nota-subtit-orig mono" }, `Original: “${str(n.titulo_original)}”`) : null;"""

    # Vamos fazer a substituição precisa
    if alvo_map_artigo in code:
        # Precisamos fechar a chave retornada
        code = code.replace(alvo_map_artigo, """      h("div", { class: "d-notas" }, notasParaExibir.map(({ nota: n, boletim: bol, rotulo }) => {
        const ehInt = n.escopo === "internacional" || n.pais === "Internacional" || n.titulo_original;
        return h("article", { class: `d-nota ${ehInt ? "d-nota-int" : ""}`, onclick: () => abrirNota(n, bol), style: "cursor:pointer" },
          h("div", { style: "display:flex;align-items:center;justify-content:space-between;gap:8px;" },
            h("div", { style: "display:flex;align-items:center;gap:6px;flex-wrap:wrap;" },
              h("span", { class: "edt" }, str(n.editoria)),
              ehInt ? h("span", { class: "badge-int mono" }, "🌍 Internacional") : null
            ),
            rotulo ? h("span", { class: "mono", style: "font-size:var(--fs-xs);color:var(--muted);" }, rotulo) : null),
          h("h3", { class: "d-nota-tit", role: "button", tabindex: "0", onclick: () => abrirNota(n, bol), title: "Abrir matéria no modo leitor" }, str(n.titulo)),
          n.titulo_original && n.titulo_original !== n.titulo ? h("p", { class: "d-nota-subtit-orig mono" }, `Original: “${str(n.titulo_original)}”`) : null,""")

        # Ajustar o fechamento do map
        code = code.replace("        )\n      ))));", "        );\n      }))));")

    # 5. Adicionar aviso de tradução no leitor abrirNota
    alvo_leitor_tit = """      h("h2", { class: "lt-tit", style: "margin:10px 0 16px;line-height:1.18;" }, str(n.titulo)),
      
      // Conteúdo completo na íntegra"""

    subst_leitor_tit = """      h("h2", { class: "lt-tit", style: "margin:10px 0 16px;line-height:1.18;" }, str(n.titulo)),
      n.titulo_original && n.titulo_original !== n.titulo ? h("p", { class: "d-nota-subtit-orig mono", style: "margin:-8px 0 16px;font-size:14px;" }, `Original em língua estrangeira: “${str(n.titulo_original)}”`) : null,
      (n.escopo === "internacional" || n.pais === "Internacional" || n.titulo_original) ? h("div", { class: "lt-aviso-traducao mono" },
        h("b", null, "🌍 Mídia Internacional Traduzida: "),
        "Reportagem apurada pelos correspondentes internacionais e traduzida integralmente para o português culto pela Faixa Oculta. Os links de conferência no rodapé levam diretamente ao site original no idioma de origem."
      ) : null,
      
      // Conteúdo completo na íntegra"""

    if "lt-aviso-traducao mono" not in code:
        code = code.replace(alvo_leitor_tit, subst_leitor_tit, 1)

    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f"Filtros de mídia e leitor internacional aplicados em {caminho}")

aplicar('pagina.html')
aplicar('index.html')
