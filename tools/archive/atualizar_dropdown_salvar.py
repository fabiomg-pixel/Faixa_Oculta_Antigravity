#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def main():
    with open('pagina.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. State S
    if 'noticiasSalvas: {}' not in c:
        c = c.replace(
            'podeMarcar: false, falhou: false };',
            'podeMarcar: false, falhou: false, noticiasSalvas: {}, filtroSalvas: false };'
        )

    # 2. Add helpers right above toggleVozNavegador
    antigo_audio = '  let audioNarracaoAtiva = false;\n  function toggleVozNavegador(d, btn) {'
    novo_helpers = '''  function chaveNota(n, d) {
    const dt = str(d && (d.data || d._id));
    const tit = str(n && n.titulo);
    return `${dt}:::${tit}`;
  }
  function isNotaSalva(n, d) {
    const k = chaveNota(n, d);
    return Boolean(S.noticiasSalvas && S.noticiasSalvas[k]);
  }
  function toggleSalvarNoticia(n, d) {
    const k = chaveNota(n, d);
    if (!S.noticiasSalvas) S.noticiasSalvas = {};
    if (S.noticiasSalvas[k]) {
      delete S.noticiasSalvas[k];
    } else {
      S.noticiasSalvas[k] = {
        chave: k,
        data_boletim: d ? (d.data || d._id) : "",
        rotulo_boletim: d ? rotuloBoletim(d) : "",
        salvo_em: new Date().toISOString(),
        nota: n,
        boletim: d ? { _id: d._id, data: d.data, edicao: d.edicao, titulo: d.titulo } : null
      };
    }
    try {
      localStorage.setItem("faixa_noticias_salvas", JSON.stringify(S.noticiasSalvas));
    } catch (e) {}
    render();
  }
  function toggleVozNota(n, btn) {
    if (!('speechSynthesis' in window)) {
      alert("Seu navegador não possui suporte para síntese de voz (Web Speech API).");
      return;
    }
    if (speechSynthesis.speaking) {
      speechSynthesis.cancel();
      if (btn && btn.classList.contains("falando")) {
        btn.classList.remove("falando");
        btn.textContent = "🔊 Ouvir matéria";
        return;
      }
    }
    const partes = [];
    if (n.editoria) partes.push(n.editoria + ".");
    if (n.titulo) partes.push(n.titulo + ".");
    if (n.texto) partes.push(n.texto);
    if (n.por_que_importa) partes.push(`Por que importa: ${n.por_que_importa}`);
    const txt = partes.join(" \\n ");
    const utter = new SpeechSynthesisUtterance(txt);
    utter.lang = "pt-BR";
    utter.rate = 1.03;
    const voices = speechSynthesis.getVoices().filter((v) => v.lang && v.lang.startsWith("pt"));
    if (voices.length) utter.voice = voices[0];
    const resetBtns = () => {
      document.querySelectorAll(".d-btn-ouvir-nota.falando").forEach((b) => {
        b.classList.remove("falando");
        b.textContent = "🔊 Ouvir matéria";
      });
    };
    resetBtns();
    utter.onend = () => resetBtns();
    utter.onerror = () => resetBtns();
    if (btn) {
      btn.classList.add("falando");
      btn.textContent = "⏹ Parar áudio";
    }
    speechSynthesis.speak(utter);
  }

  let audioNarracaoAtiva = false;
  function toggleVozNavegador(d, btn) {'''

    if 'function chaveNota' not in c:
        assert antigo_audio in c, 'antigo_audio not found'
        c = c.replace(antigo_audio, novo_helpers, 1)

    # 3. abrirNota top bar with Salvar and Ouvir
    antigo_ltbar = '''    t.replaceChildren(h("div", { class: "lt-box" },
      h("div", { class: "lt-bar" },
        h("span", { class: "mono" }, `Modo Leitor · Conteúdo na íntegra`),
        h("button", { class: "l-btn", type: "button", onclick: () => t.close(), "aria-label": "Fechar" }, "Fechar ×")),
      h("div", { class: "lt-meta mono" }, str(rotulo)),'''

    novo_ltbar = '''    t.replaceChildren(h("div", { class: "lt-box" },
      h("div", { class: "lt-bar" },
        h("span", { class: "mono" }, `Modo Leitor · Conteúdo na íntegra`),
        h("div", { style: "display:inline-flex;gap:8px;align-items:center;" },
          h("button", {
            class: `d-btn-salvar mono ${isNotaSalva(n, d) ? "salva" : ""}`,
            type: "button",
            onclick: (e) => {
              toggleSalvarNoticia(n, d);
              e.currentTarget.className = `d-btn-salvar mono ${isNotaSalva(n, d) ? "salva" : ""}`;
              e.currentTarget.textContent = isNotaSalva(n, d) ? "✓ Salva" : "🔖 Salvar";
            }
          }, isNotaSalva(n, d) ? "✓ Salva" : "🔖 Salvar"),
          h("button", {
            class: "d-btn-ouvir-nota mono",
            type: "button",
            onclick: (e) => toggleVozNota(n, e.currentTarget)
          }, "🔊 Ouvir"),
          h("button", { class: "l-btn", type: "button", onclick: () => t.close(), "aria-label": "Fechar" }, "Fechar ×"))),
      h("div", { class: "lt-meta mono" }, str(rotulo)),'''

    if 'isNotaSalva(n, d)' not in c:
        assert antigo_ltbar in c, 'antigo_ltbar not found'
        c = c.replace(antigo_ltbar, novo_ltbar, 1)

    # 4. blocoAudioBoletim title
    antigo_audiobloco = '''  function blocoAudioBoletim(d) {
    if (!d) return null;
    const audioUrl = safeUrl(d.audio);
    const dur = str(d.audio_duracao) || (audioUrl ? "5:30" : "");
    return h("section", { class: "wrap", style: "padding-bottom:14px" },
      h("div", { class: "d-audio-card" },
        h("div", { class: "d-audio-head" },
          h("div", { class: "d-audio-kicker" }, h("span", { class: "dot" }), "Boletim em Áudio · Síntese do Dia"),
          dur ? h("span", { class: "d-audio-dur mono" }, dur) : null),
        h("h4", { class: "d-audio-tit" }, "Ouça a transcrição narrada das notícias do dia"),'''

    novo_audiobloco = '''  function blocoAudioBoletim(d) {
    if (!d) return null;
    const audioUrl = safeUrl(d.audio);
    const dur = str(d.audio_duracao) || (audioUrl ? "13:09" : "");
    const titAudio = dur ? `Ouça a edição completa na íntegra das notícias do dia (${dur})` : "Ouça a edição completa na íntegra das notícias do dia";
    return h("section", { class: "wrap", style: "padding-bottom:14px" },
      h("div", { class: "d-audio-card" },
        h("div", { class: "d-audio-head" },
          h("div", { class: "d-audio-kicker" }, h("span", { class: "dot" }), "Boletim em Áudio · Edição Completa na Íntegra"),
          dur ? h("span", { class: "d-audio-dur mono" }, dur) : null),
        h("h4", { class: "d-audio-tit" }, titAudio),'''

    if 'Edição Completa na Íntegra' not in c:
        assert antigo_audiobloco in c, 'antigo_audiobloco not found'
        c = c.replace(antigo_audiobloco, novo_audiobloco, 1)

    # 5. blocoHoje head + dropdown + saved items filtering
    antigo_blocohoje = '''  function blocoHoje() {
    if (!S.loaded.dias) return [estado("abrindo o boletim", "As notícias do dia aparecem aqui assim que o arquivo da revista responder.")];
    const d = diaAtual();
    if (!d) return [estado("nenhum boletim ainda", "O boletim aparece aqui de manhã e no fim da tarde.")];
    const notas = arr(d.notas);
    const head = h("section", { class: "wrap d-head" },
      h("div", { style: "min-width:0" },
        h("div", { class: "kicker mono" }, `${d.edicao === "noite" ? "Boletim da noite" : "Boletim diário"} · ${rotuloDia(d.data || d._id)}`),
        h("h2", null, str(d.titulo)),
        d.resumo_dia ? h("p", { class: "lede" }, str(d.resumo_dia)) : null,
        S.dias.length > 1 ? h("div", { class: "d-dias", role: "group", "aria-label": "Boletins anteriores" }, S.dias.slice(0, 10).map((x) =>
          h("button", { class: "chip", type: "button", "aria-pressed": String(x._id === d._id), onclick: () => { S.selDia = x._id; render(); window.scrollTo(0, 0); } }, rotuloBoletim(x)))) : null),
      arr(d.agenda).length ? h("aside", { class: "d-agenda" }, h("h4", null, "Para acompanhar"),
        h("ul", null, arr(d.agenda).map((a) => h("li", null, h("span", { class: "mono" }, str(a.quando)), h("span", null, str(a.o_que)))))) : null);
    const grade = h("section", { class: "wrap", style: "padding-bottom:24px" }, h("div", { class: "d-notas" }, notas.map((n) => h("article", { class: "d-nota" },
      h("span", { class: "edt" }, str(n.editoria)),
      h("h3", { class: "d-nota-tit", role: "button", tabindex: "0", onclick: () => abrirNota(n, d), title: "Abrir matéria no modo leitor" }, str(n.titulo)),
      h("p", null, str(n.texto)),
      n.por_que_importa ? h("p", { class: "ponte" }, h("b", null, "Por que importa: "), str(n.por_que_importa)) : null,
      arr(n.fontes).length ? h("ul", { class: "d-fontes" }, arr(n.fontes).map((f) => h("li", null,
        fonteLink(f.url, str(f.fonte), n), f.perfil ? h("span", { class: "mono" }, ` · ${str(f.perfil)}`) : null,
        f.enfoque ? h("small", null, str(f.enfoque)) : null))) : null,
      h("div", { class: "d-nota-acts" },
        h("button", { class: "ler", type: "button", onclick: () => abrirNota(n, d) }, "Abrir no leitor"))
    ))));'''

    novo_blocohoje = '''  function blocoHoje() {
    if (!S.loaded.dias) return [estado("abrindo o boletim", "As notícias do dia aparecem aqui assim que o arquivo da revista responder.")];
    const d = diaAtual();
    if (!d) return [estado("nenhum boletim ainda", "O boletim aparece aqui de manhã e no fim da tarde.")];

    // Dropdown elegante com todas as edições do mês (e meses anteriores)
    const totalSalvas = Object.keys(S.noticiasSalvas || {}).length;
    const gruposMes = {};
    for (const x of S.dias) {
      const m = str(x.data || x._id).slice(0, 7);
      if (!gruposMes[m]) gruposMes[m] = [];
      gruposMes[m].push(x);
    }
    const chavesMes = Object.keys(gruposMes).sort().reverse();
    const optKids = [];
    if (chavesMes.length <= 1) {
      for (const x of S.dias) {
        optKids.push(h("option", { value: x._id, selected: x._id === d._id }, rotuloBoletim(x)));
      }
    } else {
      for (const m of chavesMes) {
        const rotMes = fmtData(m).toUpperCase();
        optKids.push(h("optgroup", { label: `Edições de ${rotMes}` },
          gruposMes[m].map((x) => h("option", { value: x._id, selected: x._id === d._id }, rotuloBoletim(x)))
        ));
      }
    }

    const seletorEdicoes = S.dias.length > 1 ? h("div", { class: "d-edsel-box" },
      h("label", { class: "d-edsel-label mono" },
        h("span", { class: "d-edsel-txt" }, "Edições do mês:"),
        h("select", {
          class: "d-edsel-select mono",
          "aria-label": "Selecionar edição do boletim",
          onchange: (e) => {
            S.selDia = e.target.value;
            S.filtroSalvas = false;
            render();
            window.scrollTo(0, 0);
          }
        }, optKids)),
      h("button", {
        class: `d-btn-filtro-salvas mono ${S.filtroSalvas ? "ativo" : ""}`,
        type: "button",
        title: "Ver matérias que você salvou",
        onclick: () => {
          S.filtroSalvas = !S.filtroSalvas;
          render();
        }
      }, `🔖 Notícias salvas (${totalSalvas})`)
    ) : null;

    const head = h("section", { class: "wrap d-head" },
      h("div", { style: "min-width:0" },
        h("div", { class: "kicker mono" }, `${d.edicao === "noite" ? "Boletim da noite" : "Boletim diário"} · ${rotuloDia(d.data || d._id)}`),
        h("h2", null, str(d.titulo)),
        d.resumo_dia ? h("p", { class: "lede" }, str(d.resumo_dia)) : null,
        seletorEdicoes),
      arr(d.agenda).length ? h("aside", { class: "d-agenda" }, h("h4", null, "Para acompanhar"),
        h("ul", null, arr(d.agenda).map((a) => h("li", null, h("span", { class: "mono" }, str(a.quando)), h("span", null, str(a.o_que)))))) : null);

    let notasParaExibir = [];
    if (S.filtroSalvas) {
      const salvasObj = S.noticiasSalvas || {};
      const listaSalvas = Object.values(salvasObj);
      if (!listaSalvas.length) {
        return [
          head,
          h("section", { class: "wrap", style: "padding: 40px 0 64px;" },
            estado("nenhuma matéria salva", "Clique em '🔖 Salvar' em qualquer notícia do boletim para guardá-la para leitura posterior."))
        ];
      }
      notasParaExibir = listaSalvas.map((s) => ({
        nota: s.nota,
        boletim: s.boletim || d,
        rotulo: s.rotulo_boletim || (s.boletim ? rotuloBoletim(s.boletim) : "")
      }));
    } else {
      notasParaExibir = arr(d.notas).map((n) => ({ nota: n, boletim: d, rotulo: "" }));
    }

    const grade = h("section", { class: "wrap", style: "padding-bottom:24px" },
      S.filtroSalvas ? h("div", { style: "display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;border-bottom:1px solid var(--rule);padding-bottom:8px;" },
        h("h3", { style: "margin:0;font-size:var(--fs-m);font-weight:700;" }, `Suas matérias salvas (${notasParaExibir.length})`),
        h("button", { class: "d-btn-filtro-salvas mono", type: "button", onclick: () => { S.filtroSalvas = false; render(); } }, "Voltar ao boletim do dia ✕")
      ) : null,
      h("div", { class: "d-notas" }, notasParaExibir.map(({ nota: n, boletim: bol, rotulo }) => h("article", { class: "d-nota" },
        h("div", { style: "display:flex;align-items:center;justify-content:space-between;gap:8px;" },
          h("span", { class: "edt" }, str(n.editoria)),
          rotulo ? h("span", { class: "mono", style: "font-size:var(--fs-xs);color:var(--muted);" }, rotulo) : null),
        h("h3", { class: "d-nota-tit", role: "button", tabindex: "0", onclick: () => abrirNota(n, bol), title: "Abrir matéria no modo leitor" }, str(n.titulo)),
        h("p", null, str(n.texto)),
        n.por_que_importa ? h("p", { class: "ponte" }, h("b", null, "Por que importa: "), str(n.por_que_importa)) : null,
        arr(n.fontes).length ? h("ul", { class: "d-fontes" }, arr(n.fontes).map((f) => h("li", null,
          fonteLink(f.url, str(f.fonte), n), f.perfil ? h("span", { class: "mono" }, ` · ${str(f.perfil)}`) : null,
          f.enfoque ? h("small", null, str(f.enfoque)) : null))) : null,
        h("div", { class: "d-nota-acts" },
          h("button", { class: "ler", type: "button", onclick: () => abrirNota(n, bol) }, "Abrir no leitor"),
          h("button", {
            class: `d-btn-salvar mono ${isNotaSalva(n, bol) ? "salva" : ""}`,
            type: "button",
            onclick: () => toggleSalvarNoticia(n, bol)
          }, isNotaSalva(n, bol) ? "✓ Salva" : "🔖 Salvar"),
          h("button", {
            class: "d-btn-ouvir-nota mono",
            type: "button",
            onclick: (e) => toggleVozNota(n, e.currentTarget)
          }, "🔊 Ouvir matéria")
        )
      ))));'''

    if 'seletorEdicoes' not in c:
        assert antigo_blocohoje in c, 'antigo_blocohoje not found'
        c = c.replace(antigo_blocohoje, novo_blocohoje, 1)

    # 6. LocalStorage loading in iniciarEstatico and claude branch
    antigo_ls = 'try { S.marcas = JSON.parse(localStorage.getItem("fo-marcas") || "{}") || {}; } catch (e) { S.marcas = {}; }'
    novo_ls = antigo_ls + '\n      try { S.noticiasSalvas = JSON.parse(localStorage.getItem("faixa_noticias_salvas") || "{}") || {}; } catch (e) { S.noticiasSalvas = {}; }'
    if 'faixa_noticias_salvas' not in c:
        assert antigo_ls in c, 'antigo_ls not found'
        c = c.replace(antigo_ls, novo_ls, 1)

    antigo_claudels = 'if (uid) {'
    novo_claudels = 'try { S.noticiasSalvas = JSON.parse(localStorage.getItem("faixa_noticias_salvas") || "{}") || {}; } catch (e) { S.noticiasSalvas = {}; }\n    if (uid) {'
    if c.count('faixa_noticias_salvas') < 2:
        assert antigo_claudels in c, 'antigo_claudels not found'
        c = c.replace(antigo_claudels, novo_claudels, 1)

    with open('pagina.html', 'w', encoding='utf-8') as f:
        f.write(c)

    # Generate index.html
    head = """<!doctype html>
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
    tail = "\n</body>\n</html>\n"
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(head + c + tail)

    print("OK: pagina.html e index.html atualizados com sucesso!")

if __name__ == '__main__':
    main()
