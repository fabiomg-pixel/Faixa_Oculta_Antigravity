#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quality Gate Pré-Publicação da Faixa Oculta / Radar Cultural (tools/validar_edicao.py).

Verifica rigorosamente a integridade de `data/revista.json` (e shards em `data/dias/*.json`, se presentes):
1. Zero notas internacionais com `titulo == titulo_original` ou texto em idioma estrangeiro (EN/ES/FR) na edição mais recente.
2. Máximo de 2 notas do mesmo veículo internacional na edição mais recente.
3. Zero frases de boilerplate ("A matéria apurada por", "A reportagem apurada pela redação internacional") na edição mais recente.
4. 100% das capas referenciadas existem no disco e possuem tamanho > 2 KB (2048 bytes).
5. 100% dos itens de `itens`, `cine_itens` e `livro_itens` da edição atual possuem `len(resenha) >= 3` parágrafos.
6. Zero links `.pdf` expostos na estrutura de dados.

Uso:
    python3 tools/validar_edicao.py [--json data/revista.json] [--dia ID_DIA]
Retorna exit code 0 (APROVADO) ou 1 (REPROVADO com relatório detalhado).
"""

import argparse
import json
import os
import re
import sys
from collections import Counter

FRASES_BOILERPLATE_PROIBIDAS = [
    "A matéria apurada por",
    "A reportagem apurada pela redação internacional",
    "Texto apurado originalmente por correspondentes",
    "Análise de acompanhamento compilada pela redação da Faixa Oculta",
    "Em desdobramento acompanhado pelas editorias",
]

# Marcadores léxicos exclusivos de textos não traduzidos em inglês, espanhol ou francês
REGEX_IDIOMA_ESTRANGEIRO = re.compile(
    r"\b("
    r"the|and|with|from|that|this|have|would|after|their|which|while|between|against|under|"
    r"según|también|después|durante|contra|gobierno|aunque|mientras|hacia|desde|"
    r"dans|avec|pour|cette|sont|mais|comme|plus|entre|après|contre"
    r")\b",
    re.I,
)


def _eh_texto_estrangeiro(texto):
    """Detecta se uma frase/parágrafo permaneceu em inglês, espanhol ou francês (4+ stopwords estrangeiras)."""
    if not texto:
        return False
    hits = REGEX_IDIOMA_ESTRANGEIRO.findall(texto)
    return len(hits) >= 4


def _coletar_capas_e_pdfs(obj, caminho="", capas=None, pdfs=None):
    if capas is None:
        capas = []
    if pdfs is None:
        pdfs = []

    if isinstance(obj, dict):
        for k, v in obj.items():
            sub_path = f"{caminho}.{k}" if caminho else k
            if isinstance(v, str):
                v_str = v.strip()
                if k in ("capa", "imagem", "foto") and v_str and not v_str.startswith("http"):
                    capas.append((v_str, sub_path))
                if k in ("url_pdf", "jornal_pdf_nome") or (
                    re.search(r"\.pdf(\b|$|\?)", v_str, re.I)
                    and (not v_str.startswith("http") or "jornais/" in v_str.lower() or caminho.startswith("dias."))
                ):
                    pdfs.append((v_str, sub_path))
            else:
                _coletar_capas_e_pdfs(v, sub_path, capas, pdfs)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _coletar_capas_e_pdfs(v, f"{caminho}[{i}]", capas, pdfs)

    return capas, pdfs


def _ordenar_chaves_dias(chaves):
    """Ordena chaves de dias cronologicamente garantindo que AAAA-MM-DD-noite venha após AAAA-MM-DD."""
    def _key(k):
        base = k[:10]
        turno = 1 if k.endswith("-noite") else 0
        return (base, turno, k)
    return sorted(chaves, key=_key)


def validar_banco(caminho_json="data/revista.json", dia_alvo=None, validar_shards=True):
    erros = []
    avisos = []
    estatisticas = {}

    if not os.path.exists(caminho_json):
        return False, [f"Arquivo principal não encontrado: {caminho_json}"], [], {}

    with open(caminho_json, "r", encoding="utf-8") as f:
        db = json.load(f)

    dias = db.get("dias", {})
    if not dias:
        erros.append("Coleção 'dias' está vazia em data/revista.json.")
        return False, erros, avisos, estatisticas

    chaves_ordenadas = _ordenar_chaves_dias(list(dias.keys()))
    edicao_recente_id = dia_alvo if (dia_alvo and dia_alvo in dias) else chaves_ordenadas[-1]
    data_base_recente = edicao_recente_id[:10]

    # Validar as edições do dia mais recente (manhã e noite, se ambas existirem)
    edicoes_para_validar = [
        k for k in chaves_ordenadas if k.startswith(data_base_recente)
    ] if not dia_alvo else [edicao_recente_id]

    estatisticas["edicoes_diarias_inspecionadas"] = edicoes_para_validar

    # 1, 2 e 3: Validação das notas nas edições do dia mais recente
    for d_id in edicoes_para_validar:
        d_obj = dias[d_id]
        notas = d_obj.get("notas", [])
        if len(notas) < 20:
            erros.append(f"[{d_id}] Volume insuficiente de notícias: {len(notas)} notas (mínimo exigido: 20).")

        contagem_veiculos_inter = Counter()
        notas_nao_traduzidas = []
        notas_com_boilerplate = []

        for idx, n in enumerate(notas):
            escopo = n.get("escopo", "")
            tit = (n.get("titulo") or "").strip()
            tit_orig = (n.get("titulo_original") or "").strip()
            tc = n.get("texto_completo") or []
            rv = n.get("resumo_visoes") or ""
            aprof = json.dumps(n.get("aprofundamento") or {}, ensure_ascii=False)
            bloco_texto = " ".join([tit, rv, aprof] + (tc if isinstance(tc, list) else [str(tc)]))

            # Check 3: Zero frases de boilerplate
            for frase_proibida in FRASES_BOILERPLATE_PROIBIDAS:
                if frase_proibida in bloco_texto:
                    notas_com_boilerplate.append(f"Nota #{idx+1} ({tit[:45]}...): contém '{frase_proibida}'")
                    break

            # Checks 1 e 2: Internacional
            if escopo == "internacional":
                fontes = n.get("fontes") or []
                veiculo = fontes[0].get("fonte", "Desconhecido") if fontes else "Desconhecido"
                contagem_veiculos_inter[veiculo] += 1

                if tit and tit_orig and tit.lower() == tit_orig.lower():
                    notas_nao_traduzidas.append(f"Nota #{idx+1} [{veiculo}]: titulo == titulo_original ('{tit[:55]}')")
                elif _eh_texto_estrangeiro(tit) or (tc and _eh_texto_estrangeiro(tc[0])):
                    notas_nao_traduzidas.append(f"Nota #{idx+1} [{veiculo}]: título ou 1º parágrafo em idioma estrangeiro ('{tit[:55]}')")

        if notas_nao_traduzidas:
            erros.append(
                f"[{d_id}] {len(notas_nao_traduzidas)} nota(s) internacional(is) sem tradução:\n    - "
                + "\n    - ".join(notas_nao_traduzidas[:6])
            )

        for veic, qtd in contagem_veiculos_inter.items():
            if qtd > 2:
                erros.append(
                    f"[{d_id}] Veículo internacional '{veic}' aparece {qtd} vezes (máximo permitido: 2 por veículo)."
                )

        if notas_com_boilerplate:
            erros.append(
                f"[{d_id}] {len(notas_com_boilerplate)} nota(s) com frases de boilerplate/template proibidas:\n    - "
                + "\n    - ".join(notas_com_boilerplate[:6])
            )

    # 4 e 6: 100% das capas existem e > 2 KB (2048 bytes) & Zero links .pdf expostos
    capas_ref, pdfs_ref = _coletar_capas_e_pdfs(db)
    estatisticas["total_capas_referenciadas"] = len(capas_ref)
    estatisticas["total_pdfs_expostos"] = len(pdfs_ref)

    capas_invalidas = []
    for c_path, json_loc in capas_ref:
        if not os.path.exists(c_path):
            capas_invalidas.append(f"{c_path} (AUSENTE em {json_loc})")
        else:
            sz = os.path.getsize(c_path)
            if sz <= 2048:
                capas_invalidas.append(f"{c_path} ({sz} B <= 2 KB em {json_loc})")

    if capas_invalidas:
        erros.append(
            f"{len(capas_invalidas)} capa(s) ausente(s) ou <= 2 KB:\n    - "
            + "\n    - ".join(capas_invalidas[:10])
        )

    if pdfs_ref:
        erros.append(
            f"{len(pdfs_ref)} referência(s) a .pdf exposta(s) na base:\n    - "
            + "\n    - ".join([f"{u} (em {loc})" for u, loc in pdfs_ref[:10]])
        )

    # 5: 100% dos itens culturais da edição atual têm len(resenha) >= 3 parágrafos
    edicoes_musica = sorted(list(db.get("edicoes", {}).keys()))
    edicao_cultural_atual = edicoes_musica[-1] if edicoes_musica else "2026-11"
    estatisticas["edicao_cultural_atual"] = edicao_cultural_atual

    itens_resenha_curta = []
    for col_nome in ("itens", "cine_itens", "livro_itens"):
        col = db.get(col_nome, {})
        for item_id, item_obj in col.items():
            if item_obj.get("edicao") == edicao_cultural_atual:
                res = item_obj.get("resenha")
                if not isinstance(res, list) or len(res) < 3 or any(len(str(p).strip()) < 40 for p in res[:3]):
                    qtd_p = len(res) if isinstance(res, list) else 0
                    itens_resenha_curta.append(f"{col_nome}[{item_id}] (len(resenha)={qtd_p})")

    if itens_resenha_curta:
        erros.append(
            f"{len(itens_resenha_curta)} item(ns) da edição cultural '{edicao_cultural_atual}' com resenha < 3 parágrafos:\n    - "
            + "\n    - ".join(itens_resenha_curta[:12])
        )

    # Validação complementar de shards v2 se já existirem em data/dias/
    shards_dir = os.path.join(os.path.dirname(caminho_json), "dias")
    if validar_shards and os.path.isdir(shards_dir):
        for d_id in edicoes_para_validar:
            shard_p = os.path.join(shards_dir, f"{d_id}.json")
            if not os.path.exists(shard_p):
                avisos.append(f"Shard v2 ainda não gerado para {d_id} ({shard_p}). Execute tools/particionar_dados_v2.py.")

    aprovado = len(erros) == 0
    return aprovado, erros, avisos, estatisticas


def main():
    parser = argparse.ArgumentParser(description="Quality Gate Pré-Publicação da Faixa Oculta")
    parser.add_argument("--json", default="data/revista.json", help="Caminho para data/revista.json")
    parser.add_argument("--dia", default=None, help="ID específico do dia a validar (default: dia mais recente)")
    args = parser.parse_args()

    aprovado, erros, avisos, stats = validar_banco(caminho_json=args.json, dia_alvo=args.dia)

    print("=================================================================")
    print(" QUALITY GATE PRÉ-PUBLICAÇÃO · FAIXA OCULTA V2")
    print("=================================================================")
    print(f" Arquivo auditado         : {args.json}")
    print(f" Edições diárias checadas : {', '.join(stats.get('edicoes_diarias_inspecionadas', []))}")
    print(f" Edição cultural checada  : {stats.get('edicao_cultural_atual', '-')}")
    print(f" Capas verificadas (>2KB) : {stats.get('total_capas_referenciadas', 0)}")
    print(f" Links PDF expostos       : {stats.get('total_pdfs_expostos', 0)}")
    print("-----------------------------------------------------------------")

    if avisos:
        print(f"AVISOS ({len(avisos)}):")
        for av in avisos:
            print(f"  [!] {av}")
        print("-----------------------------------------------------------------")

    if aprovado:
        print("✅ STATUS: APROVADO (Exit Code 0) — 100% dos critérios de qualidade atendidos.")
        sys.exit(0)
    else:
        print(f"❌ STATUS: REPROVADO (Exit Code 1) — {len(erros)} falha(s) crítica(s) detectada(s):")
        for i, err in enumerate(erros, 1):
            print(f"\n  {i}. {err}")
        print("\n=================================================================")
        sys.exit(1)


if __name__ == "__main__":
    main()
