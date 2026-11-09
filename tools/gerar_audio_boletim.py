#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o áudio narrado (podcast / briefing) do boletim diário de notícias da Faixa Oculta.

Usa edge-tts (voz neural natural pt-BR-AntonioNeural) ou say (macOS) como fallback.
Atualiza data/revista.json com os metadados do áudio.
Uso:
    python3 tools/gerar_audio_boletim.py [--dia YYYY-MM-DD] [--voz pt-BR-AntonioNeural]
"""

import argparse, json, os, re, subprocess, sys

MESES = {
    "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
    "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
    "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"
}

def data_por_extenso(dia_str):
    # dia_str pode ser 2026-11-02 ou 2026-11-02-noite
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})(?:-(noite|manha))?$", dia_str)
    if not m:
        return dia_str
    ano, mes, dia, turno = m.groups()
    mes_nome = MESES.get(mes, mes)
    extenso = f"{int(dia)} de {mes_nome} de {ano}"
    if turno == "noite":
        extenso += ", edição da noite"
    return extenso

def montar_roteiro_transcricao(d):
    dia_id = d.get("_id") or d.get("data") or "hoje"
    extenso = data_por_extenso(dia_id)
    
    partes = []
    partes.append(f"Faixa Oculta apresenta: o boletim diário de notícias. Edição de {extenso}.")
    
    if d.get("titulo"):
        partes.append(d["titulo"].strip() + ".")
    
    if d.get("resumo_dia"):
        partes.append(d["resumo_dia"].strip())

    notas_todas = d.get("notas", [])
    notas_nac = [n for n in notas_todas if n.get("escopo") != "internacional" and n.get("pais") != "Internacional"]
    notas_int = [n for n in notas_todas if n.get("escopo") == "internacional" or n.get("pais") == "Internacional" or n.get("titulo_original")]

    if notas_nac:
        partes.append("Iniciamos com o bloco de Mídia Nacional, destacando as pautas estruturais de economia, política, relações internacionais e sociedade no Brasil.")
        for n in notas_nac:
            ed = n.get("editoria", "").strip()
            tit = n.get("titulo", "").strip()
            tc = n.get("texto_completo")
            txt = " ".join(tc[:3]).strip() if isinstance(tc, list) and tc else n.get("texto", "").strip()
            pqi = n.get("por_que_importa", "").strip()
            bloco = []
            if ed: bloco.append(f"{ed}.")
            if tit: bloco.append(f"{tit}.")
            if txt: bloco.append(txt)
            if pqi: bloco.append(f"Por que importa: {pqi}")
            partes.append(" ".join(bloco))

    if notas_int:
        partes.append("Passamos agora ao bloco de Mídia Internacional, com as principais coberturas dos grandes veículos mundiais traduzidas integralmente pela redação da Faixa Oculta.")
        for n in notas_int:
            ed = n.get("editoria", "").strip()
            tit = n.get("titulo", "").strip()
            tc = n.get("texto_completo")
            txt = " ".join(tc[:3]).strip() if isinstance(tc, list) and tc else n.get("texto", "").strip()
            pqi = n.get("por_que_importa", "").strip()
            bloco = []
            if ed: bloco.append(f"{ed}.")
            if tit: bloco.append(f"{tit}.")
            if txt: bloco.append(txt)
            if pqi: bloco.append(f"Por que importa: {pqi}")
            partes.append(" ".join(bloco))
        
    partes.append("Este foi o boletim diário de notícias da Faixa Oculta. Você pode ler todas as reportagens na íntegra no nosso Modo Leitor imersivo, alternando entre os eixos nacional e internacional.")
    return "\n\n".join(partes)

def obter_duracao(audio_path):
    # Tenta afinfo no macOS
    try:
        r = subprocess.run(["afinfo", audio_path], capture_output=True, text=True)
        m = re.search(r"estimated duration:\s*([\d\.]+)\s*sec", r.stdout)
        if m:
            seg = int(float(m.group(1)))
            return f"{seg // 60}:{seg % 60:02d}"
    except Exception:
        pass
    # Fallback ffmpeg
    try:
        r = subprocess.run(["ffmpeg", "-i", audio_path], capture_output=True, text=True)
        m = re.search(r"Duration:\s*(\d+):(\d+):(\d+)", r.stderr)
        if m:
            h, min_, s = map(int, m.groups())
            total = h * 60 + min_
            return f"{total}:{s:02d}"
    except Exception:
        pass
    return "5:00"

def gerar_audio(roteiro_txt, saida_mp3, voz="pt-BR-AntonioNeural"):
    os.makedirs(os.path.dirname(os.path.abspath(saida_mp3)), exist_ok=True)
    tmp_txt = saida_mp3 + ".txt"
    with open(tmp_txt, "w", encoding="utf-8") as f:
        f.write(roteiro_txt)
        
    # Tentativa 1: edge-tts
    edge_tts_bin = None
    for b in ["edge-tts", "/Library/Frameworks/Python.framework/Versions/3.14/bin/edge-tts", "/opt/homebrew/bin/edge-tts", "/usr/local/bin/edge-tts"]:
        if os.path.exists(b) or subprocess.run(["which", b], capture_output=True).returncode == 0:
            edge_tts_bin = b
            break
            
    if edge_tts_bin:
        print(f"Gerando áudio em blocos com {edge_tts_bin} (voz: {voz})...")
        blocos_txt = []
        atual = []
        tam_atual = 0
        for par in roteiro_txt.split("\n\n"):
            par = par.strip()
            if not par:
                continue
            if tam_atual + len(par) > 3500 and atual:
                blocos_txt.append("\n\n".join(atual))
                atual = [par]
                tam_atual = len(par)
            else:
                atual.append(par)
                tam_atual += len(par)
        if atual:
            blocos_txt.append("\n\n".join(atual))

        partes_mp3 = []
        ok_blocos = True
        for idx_b, b_str in enumerate(blocos_txt):
            b_txt = f"{saida_mp3}.part{idx_b}.txt"
            b_mp3 = f"{saida_mp3}.part{idx_b}.mp3"
            with open(b_txt, "w", encoding="utf-8") as fb:
                fb.write(b_str)
            try:
                rb = subprocess.run(
                    [edge_tts_bin, "--voice", voz, "--rate=+3%", "--file", b_txt, "--write-media", b_mp3],
                    capture_output=True, timeout=45
                )
                if rb.returncode == 0 and os.path.exists(b_mp3) and os.path.getsize(b_mp3) > 2000:
                    partes_mp3.append(b_mp3)
                else:
                    ok_blocos = False
                    break
            except Exception:
                ok_blocos = False
                break
            finally:
                if os.path.exists(b_txt):
                    os.remove(b_txt)

        if ok_blocos and partes_mp3:
            with open(saida_mp3, "wb") as fout:
                for p_mp3 in partes_mp3:
                    with open(p_mp3, "rb") as fin:
                        fout.write(fin.read())
                    os.remove(p_mp3)
            if os.path.exists(tmp_txt):
                os.remove(tmp_txt)
            return True
        for p_mp3 in partes_mp3:
            if os.path.exists(p_mp3):
                os.remove(p_mp3)

    # Tentativa 2: macOS say + ffmpeg
    if sys.platform == "darwin":
        print("Fallback: Gerando áudio via macOS say (Luciana)...")
        tmp_aiff = saida_mp3 + ".aiff"
        r1 = subprocess.run(["say", "-v", "Luciana", "-o", tmp_aiff, "-f", tmp_txt])
        if r1.returncode == 0 and os.path.exists(tmp_aiff):
            r2 = subprocess.run(["ffmpeg", "-y", "-i", tmp_aiff, "-codec:a", "libmp3lame", "-b:a", "32k", "-ac", "1", saida_mp3], capture_output=True)
            if os.path.exists(tmp_aiff): os.remove(tmp_aiff)
            if r2.returncode == 0 and os.path.exists(saida_mp3):
                if os.path.exists(tmp_txt): os.remove(tmp_txt)
                return True
                
    if os.path.exists(tmp_txt): os.remove(tmp_txt)
    return False

def main():
    parser = argparse.ArgumentParser(description="Gera áudio do boletim diário")
    parser.add_argument("--dia", default=None, help="ID da data (ex: 2026-11-02)")
    parser.add_argument("--voz", default="pt-BR-AntonioNeural", help="Voz do edge-tts")
    parser.add_argument("--forcar", action="store_true", help="Força regeneração do áudio")
    args, _ = parser.parse_known_args()

    json_path = "data/revista.json"
    with open(json_path, "r", encoding="utf-8") as f:
        dados = json.load(f)

    dias = dados.get("dias", {})
    dia_id = args.dia
    if not dia_id:
        # Pega o primeiro dia ou o mais recente
        chaves = sorted(list(dias.keys()), reverse=True)
        dia_id = chaves[0] if chaves else None

    if not dia_id or dia_id not in dias:
        print(f"Dia '{dia_id}' não encontrado em data/revista.json!")
        sys.exit(1)

    dia_dados = dias[dia_id]
    saida = f"audios/boletim_{dia_id}.mp3"
    forcar = args.forcar or os.environ.get("FORCAR_EXECUCAO", "").strip().lower() in ("1", "true", "sim")
    if not forcar and os.path.exists(saida) and os.path.getsize(saida) > 50000 and dia_dados.get("audio") == saida:
        print(f"Áudio para [{dia_id}] já existe em {saida} ({dia_dados.get('audio_duracao', '')}). Nada a fazer.")
        return

    roteiro = montar_roteiro_transcricao(dia_dados)
    
    print(f"=== GERANDO ÁUDIO DO BOLETIM: {dia_id} ===")
    print(f"Roteiro: {len(roteiro.split())} palavras")
    
    sucesso = gerar_audio(roteiro, saida, voz=args.voz)
    if not sucesso:
        print(f"Falha ao gerar áudio para {dia_id}")
        sys.exit(1)
        
    dur = obter_duracao(saida)
    tamanho = os.path.getsize(saida)
    print(f"[OK] Áudio gerado: {saida} ({dur}, {tamanho} bytes)")

    # Atualiza dados no JSON
    dia_dados["audio"] = saida
    dia_dados["audio_duracao"] = dur
    dia_dados["audio_tamanho"] = tamanho
    dia_dados["audio_titulo"] = f"Boletim em Áudio · {data_por_extenso(dia_id)}"

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

    print("data/revista.json atualizado com metadados do áudio!")

if __name__ == "__main__":
    main()
