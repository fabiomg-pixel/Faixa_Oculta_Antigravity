#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/sintetizar_e_publicar_todos_jornais.py
--------------------------------------------
Executa a síntese completa dos 9 grandes jornais (nacionais e internacionais)
usando o motor espacial Layout-Aware v2 de alta fidelidade e injeta diretamente
em data/revista.json, nos shards data/dias/*.json e em data/boot.json.
"""

import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.extrator_pdf_layout_v2 import sintetizar_edicao_completa
from tools.processar_jornais_beeper import obter_edicao_lemonde_rss

IMAGENS_POR_JORNAL = {
    "Folha de S.Paulo": "capas/folha_capa.png",
    "O Estado de S. Paulo": "capas/estadao_capa.png",
    "O Globo": "capas/globo_capa.png",
    "Valor Econômico": "capas/valor_capa.png",
    "The Washington Post": "capas/wapo_capa.png",
    "The Guardian": "capas/guardian_capa.png",
    "Financial Times": "capas/ft_capa.png",
    "The Times UK": "capas/times_capa.png",
    "Le Monde": "capas/lemonde_capa.png"
}

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    digest_path = os.path.join(base_dir, "data", "beeper_digest_diario.json")
    revista_path = os.path.join(base_dir, "data", "revista.json")
    boot_path = os.path.join(base_dir, "data", "boot.json")
    dias_dir = os.path.join(base_dir, "data", "dias")

    if not os.path.exists(digest_path):
        print(f"Erro: Digest diário não encontrado em {digest_path}")
        sys.exit(1)

    with open(digest_path, "r", encoding="utf-8") as f:
        digest = json.load(f)

    print("Iniciando síntese de alta fidelidade para os 9 jornais...")
    manchetes_auto = []

    for it in digest.get("itens", []):
        v = it.get("veiculo")
        loc = it.get("local_path")
        escopo = it.get("escopo", "nacional")
        img = IMAGENS_POR_JORNAL.get(v, "")

        print(f"\n--- Processando {v} ({escopo}) ---")
        if v == "Le Monde":
            res = obter_edicao_lemonde_rss()
            if res:
                res["imagem"] = img
                manchetes_auto.append(res)
                print(f"  -> Sucesso: {res['manchete']}")
        elif loc and os.path.exists(loc):
            try:
                res = sintetizar_edicao_completa(v, escopo, loc, img_rel_path=img)
                manchetes_auto.append(res)
                print(f"  -> Sucesso: {res['manchete']}")
                print(f"     Editorial: {res.get('editorial', {}).get('titulo')}")
                print(f"     Reportagens extraídas: {len(res.get('reportagens', []))}")
                for idx, r in enumerate(res.get("reportagens", [])):
                    print(f"       [{idx+1}] {r['caderno']} | {r['titulo'][:65]}")
            except Exception as e:
                print(f"  -> Erro ao sintetizar {v}: {e}")
        else:
            print(f"  -> Arquivo local ausente para {v}: {loc}")

    if not manchetes_auto:
        print("Erro: Nenhum jornal pôde ser sintetizado.")
        sys.exit(1)

    # Montar bloco de leitura do Modo Leitor
    leitura_auto = []
    for m in manchetes_auto:
        if m.get("reportagens"):
            r0 = m["reportagens"][0]
            leitura_auto.append({
                "jornal": m["jornal"],
                "pagina": r0.get("pagina", "1"),
                "autor": r0.get("autor", f"Redação {m['jornal']}"),
                "titulo": r0["titulo"],
                "nota": m.get("nota", ""),
                "texto_integral": r0.get("texto_integral", []),
                "pontos": r0.get("pontos", [])
            })

    hoje_iso = datetime.now().strftime("%Y-%m-%d")
    bloco_jornais = {
        "data_edicao": hoje_iso,
        "resumo": f"Síntese das primeiras páginas, editoriais e principais reportagens dos {len(manchetes_auto)} grandes diários nacionais e internacionais processados em {hoje_iso}. Clique em qualquer jornal para ler seus cadernos e reportagens no Modo Leitor.",
        "contraste": "Confronto analítico entre as manchetes econômicas e políticas da imprensa brasileira e a cobertura internacional traduzida na íntegra.",
        "manchetes": manchetes_auto,
        "leitura": leitura_auto[:6]
    }

    # Atualizar data/revista.json
    with open(revista_path, "r", encoding="utf-8") as f:
        db = json.load(f)

    dias = db.setdefault("dias", {})
    alvos_atualizacao = ["2026-11-10", "2026-11-10-noite", "2026-11-11"]
    for alvo in alvos_atualizacao:
        if alvo in dias:
            dias[alvo]["jornais"] = bloco_jornais
            print(f"Bloco de jornais injetado na edição '{alvo}' em revista.json.")

    with open(revista_path, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    # Sincronizar Shards em data/dias/
    for alvo in alvos_atualizacao:
        if alvo in dias:
            shard_path = os.path.join(dias_dir, f"{alvo}.json")
            shard_data = dict(dias[alvo])
            shard_data["id"] = alvo
            with open(shard_path, "w", encoding="utf-8") as sf:
                json.dump(shard_data, sf, ensure_ascii=False, indent=2)
            print(f"Shard sincronizado com sucesso: {shard_path}")

    # Atualizar data/boot.json
    if os.path.exists(boot_path):
        with open(boot_path, "r", encoding="utf-8") as bf:
            boot = json.load(bf)
        hoje_id = boot.get("hoje_id", "2026-11-11")
        if hoje_id in dias:
            boot["hoje_inicial"] = dict(dias[hoje_id])
            boot["hoje_inicial"]["id"] = hoje_id
        boot["gerado_em"] = datetime.now().isoformat()
        with open(boot_path, "w", encoding="utf-8") as bf:
            json.dump(boot, bf, ensure_ascii=False, indent=2)
        print("data/boot.json atualizado com sucesso!")

    print("\nSíntese e particionamento concluídos com sucesso!")

if __name__ == "__main__":
    main()
