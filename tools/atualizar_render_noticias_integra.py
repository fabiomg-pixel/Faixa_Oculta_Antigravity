import re

novo_secao_fontes = """    // Seção de Reportagens Completas por Veículo (Notícias na íntegra no modo leitor)
    const secaoFontes = arr(n.fontes).map((f) => {
      const leitura = leituraDe(f.url);
      const parasFonte = Array.isArray(f.texto_integral) && f.texto_integral.length
        ? f.texto_integral
        : (leitura ? arr(leitura.texto_integral && leitura.texto_integral.length ? leitura.texto_integral : leitura.resumo) : (f.enfoque ? [f.enfoque] : []));
      const pontosFonte = arr(f.pontos && f.pontos.length ? f.pontos : (leitura ? leitura.pontos : []));
      const citacaoFonte = f.citacao || (leitura ? leitura.citacao : "");
      const titFonte = f.titulo || (leitura ? leitura.titulo : `${n.titulo} — Apuração por ${f.fonte}`);

      return h("div", { class: "lt-fonte-bloco", style: "border-top:2px solid var(--lt-rule, var(--rule));padding:22px 0 16px;margin-top:24px;" },
        h("div", { class: "lt-meta mono", style: "margin-bottom:6px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;" },
          h("span", null, h("b", null, str(f.fonte)), f.perfil ? ` · ${str(f.perfil)}` : "", f.autor ? ` · ${str(f.autor)}` : ""),
          h("span", { class: "badge mono", style: "font-size:10px;text-transform:uppercase;padding:2px 6px;border:1px solid var(--lt-rule, var(--rule));border-radius:2px;" }, "Reportagem na íntegra")),
        h("h3", { class: "lt-tit", style: "font-size:clamp(17px,2.2vw,22px);margin:8px 0 12px;line-height:1.22;" }, str(titFonte)),
        f.enfoque && f.enfoque !== titFonte ? h("p", { class: "lt-enfoque", style: "margin:0 0 14px;font-style:italic;color:var(--lt-muted);" }, `Enfoque da apuração: ${str(f.enfoque)}`) : null,
        h("div", { class: "lt-corpo-completo", style: "margin:14px 0;" }, parasFonte.map((p) => h("p", null, str(p)))),
        pontosFonte.length ? h("div", { style: "margin:18px 0 12px;padding:12px 16px;background:var(--lt-card, var(--card));border-left:3px solid var(--sec, var(--red));" },
          h("h5", { style: "margin:0 0 8px;text-transform:uppercase;font-size:var(--fs-xs);letter-spacing:.05em;color:var(--lt-muted);" }, "Pontos centrais destacados por este veículo:"),
          h("ul", { class: "lt-pontos", style: "margin:0;padding-left:18px;" }, pontosFonte.map((x) => h("li", null, str(x))))
        ) : null,
        citacaoFonte ? h("blockquote", { class: "lt-cit", style: "margin:16px 0;padding:12px 18px;border-left:4px solid var(--ocre, #B5862C);font-style:italic;" }, `“${str(citacaoFonte)}”`) : null,
        safeUrl(f.url) ? h("div", { style: "display:flex;align-items:center;justify-content:space-between;margin-top:14px;padding-top:10px;border-top:1px dashed var(--lt-rule, var(--rule));" },
          h("span", { class: "mono", style: "font-size:11px;color:var(--lt-muted);" }, `Publicado originalmente em ${str(f.fonte)}`),
          h("a", { class: "lt-orig-btn mono", href: safeUrl(f.url), target: "_blank", rel: "noopener", title: `Conferir matéria original em ${str(f.fonte)}` }, `Conferir no site original ↗`)
        ) : null
      );
    });"""

novo_fonte_link = """  function fonteLink(url, txt, notaContexto, fObj) {
    const l = leituraDe(url);
    const abrir = () => {
      if (l) {
        abrirTexto(l);
      } else if (fObj && Array.isArray(fObj.texto_integral) && fObj.texto_integral.length) {
        abrirTexto({
          fonte: fObj.fonte || txt || "Fonte",
          autor: [fObj.perfil, fObj.autor].filter(Boolean).join(" · "),
          titulo: fObj.titulo || `${notaContexto?.titulo || txt} — Apuração por ${fObj.fonte || txt}`,
          resumo: fObj.texto_integral,
          pontos: fObj.pontos || [],
          citacao: fObj.citacao || "",
          url: fObj.url || url
        });
      } else if (notaContexto) {
        abrirNota(notaContexto);
      } else {
        abrirTexto({
          fonte: txt || "Fonte",
          titulo: txt || "Matéria",
          resumo: ["Síntese compilada pela redação da Faixa Oculta."],
          url: url
        });
      }
    };
    return h("button", { type: "button", class: "fl-ler", onclick: (e) => { e.stopPropagation(); abrir(); }, title: `Ler reportagem completa de ${txt} no modo leitor` }, txt);
  }"""

def atualizar(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Substituir bloco secaoFontes em abrirNota
    padrao_secao = r'// Fontes apuradas com botão destacado para abrir site original\s*const secaoFontes = arr\(n\.fontes\)\.map\(\(f\) => \{[\s\S]*?\n    \}\);'
    content = re.sub(padrao_secao, lambda m: novo_secao_fontes, content)

    # 2. Atualizar título da seção de fontes em abrirNota
    content = re.sub(
        r'h\("h4", \{ class: "lt-divisor-tit", style: "margin:28px 0 10px;text-transform:uppercase;font-size:var\(--fs-xs\);letter-spacing:\.05em;color:var\(--muted\);" \}, "Fontes verificadas & Cobertura original"\)',
        lambda m: 'h("h4", { class: "lt-divisor-tit", style: "margin:36px 0 12px;text-transform:uppercase;font-size:12px;letter-spacing:.06em;color:var(--sec, var(--red));" }, "Cobertura Completa por Veículo · Notícias na Íntegra")',
        content
    )

    # 3. Substituir fonteLink
    padrao_fonte_link = r'function fonteLink\(url, txt, notaContexto\)\s*\{[\s\S]*?return h\("button", \{ type: "button", class: "fl-ler", onclick: abrir, title: `Ler matéria de \$\{txt\} no modo leitor` \}, txt\);\s*\}'
    content = re.sub(padrao_fonte_link, lambda m: novo_fonte_link, content)

    # 4. Passar 'f' para fonteLink em d-fontes
    content = content.replace(
        'fonteLink(f.url, str(f.fonte), n)',
        'fonteLink(f.url, str(f.fonte), n, f)'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Atualizado {path} com sucesso.")

atualizar('index.html')
atualizar('pagina.html')
