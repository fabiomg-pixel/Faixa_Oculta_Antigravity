#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Preparador de Insumos Locais para Curadoria Nativa no Antigravity (Zero API Key Externa).

Modos:
  --checar-status : Verifica se o turno atual já está publicado e curado pelo Antigravity.
                    Retorna JSON no stdout com {"precisa_rodar": bool, "doc_id": ..., "turno": ..., "motivo": ...}.
  --coletar       : Coleta feeds RSS contemporâneos (sem API externa) e extrai os PDFs do Beeper
                    (PyMuPDF / Apple Vision OCR) gravando:
                      - data/insumos_agente_rss.json
                      - data/beeper_digest_diario.json
                      - data/beeper_digest_semana.json (quando na janela da Semana)
"""

import datetime
import json
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "tools"))


def obter_turno_brt():
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    data_iso = agora.strftime("%Y-%m-%d")
    hora = agora.hour
    if 5 <= hora < 17:
        return data_iso, "manha", agora
    if hora >= 17:
        return f"{data_iso}-noite", "noite", agora
    ontem = (agora - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    return f"{ontem}-noite", "noite", agora


def checar_status():
    doc_id, turno, agora = obter_turno_brt()
    dia_path = os.path.join(BASE_DIR, "data", "dias", f"{doc_id}.json")
    precisa = False
    motivo = "Edição já publicada e curada pelo Antigravity."

    if not os.path.exists(dia_path):
        precisa = True
        motivo = f"Edição {doc_id} ainda não existe localmente."
    else:
        try:
            with open(dia_path, "r", encoding="utf-8") as f:
                d = json.load(f)
            notas = d.get("notas") or []
            jornais = (d.get("jornais") or {}).get("manchetes") or []
            data_j = (d.get("jornais") or {}).get("data_edicao")
            modelo = d.get("curadoria_modelo") or ""
            if len(notas) < 20:
                precisa = True
                motivo = f"Edição {doc_id} tem apenas {len(notas)} notas (< 20)."
            elif len(jornais) < 8 or data_j != doc_id[:10]:
                precisa = True
                motivo = f"Jornais de {doc_id} incompletos ({len(jornais)}) ou data {data_j} != {doc_id[:10]}."
            elif "antigravity" not in modelo.lower():
                precisa = True
                motivo = f"Edição {doc_id} ainda não passou por curadoria nativa do Antigravity (modelo={modelo or 'fallback'})."
        except Exception as e:
            precisa = True
            motivo = f"Erro ao ler {dia_path}: {e}"

    res = {
        "doc_id": doc_id,
        "turno": turno,
        "agora_brt": agora.strftime("%Y-%m-%d %H:%M:%S"),
        "precisa_rodar": precisa,
        "motivo": motivo,
        "janela_semana": agora.weekday() in (3, 4, 5, 6) and (agora.weekday() != 3 or agora.hour >= 17),
    }
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


def coletar(somente_rss=False):
    os.environ["FAIXA_SEM_API_EXTERNA"] = "1"
    doc_id, turno, agora = obter_turno_brt()
    print(f"[InsumosAgente] Coletando insumos locais para {doc_id} ({turno}) sem API externa...", flush=True)

    import boletim_nuvem as bn

    itens = bn.coletar_noticias_rss()
    elegiveis = [it for it in itens if not bn._eh_item_proibido_hoje(it)]
    veiculos_int = {
        "The New York Times", "The Guardian", "Financial Times", "BBC World News",
        "Le Monde", "El País", "Al Jazeera", "DW English"
    }
    def _eh_int(it):
        v = it.get("veiculo", "")
        c = it.get("canal", "")
        return v in veiculos_int or any(vi in c for vi in veiculos_int)

    nacionais = bn.preparar_candidatos_balanceados(
        [it for it in elegiveis if not _eh_int(it)],
        max_por_veiculo=8,
        total_max=60,
    )
    internacionais = bn.preparar_candidatos_balanceados(
        [it for it in elegiveis if _eh_int(it)],
        max_por_veiculo=8,
        total_max=60,
    )

    out_rss = {
        "doc_id": doc_id,
        "turno": turno,
        "coletado_em": agora.strftime("%Y-%m-%d %H:%M:%S"),
        "total_bruto": len(itens),
        "nacionais": [
            {
                "idx": i,
                "veiculo": it.get("veiculo"),
                "canal": it.get("canal", ""),
                "titulo": it.get("titulo"),
                "descricao": (it.get("descricao") or "")[:360],
                "url": it.get("url"),
            }
            for i, it in enumerate(nacionais[:60])
        ],
        "internacionais": [
            {
                "idx": i,
                "veiculo": it.get("veiculo"),
                "canal": it.get("canal", ""),
                "titulo": it.get("titulo"),
                "descricao": (it.get("descricao") or "")[:360],
                "url": it.get("url"),
            }
            for i, it in enumerate(internacionais[:60])
        ],
    }
    rss_path = os.path.join(BASE_DIR, "data", "insumos_agente_rss.json")
    with open(rss_path, "w", encoding="utf-8") as f:
        json.dump(out_rss, f, ensure_ascii=False, indent=2)
    print(f"[InsumosAgente] RSS salvo em {rss_path} ({len(out_rss['nacionais'])} nac, {len(out_rss['internacionais'])} int).", flush=True)

    if not somente_rss:
        env = os.environ.copy()
        env["FAIXA_SEM_API_EXTERNA"] = "1"
        subprocess.run(
            [sys.executable, os.path.join(BASE_DIR, "tools", "processar_jornais_beeper.py"), "--perfil", "diario", "--pages", "15"],
            cwd=BASE_DIR,
            env=env,
            check=False,
        )

        if agora.weekday() in (3, 4, 5, 6) and (agora.weekday() != 3 or agora.hour >= 17):
            subprocess.run(
                [sys.executable, os.path.join(BASE_DIR, "tools", "processar_jornais_beeper.py"), "--perfil", "semana", "--pages", "12"],
                cwd=BASE_DIR,
                env=env,
                check=False,
            )

    print("[InsumosAgente] Coleta mecânica concluída (zero API key externa usada).", flush=True)
    return 0


if __name__ == "__main__":
    if "--coletar-rss" in sys.argv:
        raise SystemExit(coletar(somente_rss=True))
    if "--coletar" in sys.argv:
        raise SystemExit(coletar(somente_rss=False))
    raise SystemExit(checar_status())
