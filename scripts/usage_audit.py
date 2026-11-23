#!/usr/bin/env python3
"""
Auditoria deterministica de uso do time de bots (0 tokens).

Le state/routines.json (inventario de rotinas, preenchido a partir do que cada
bot responde ao prompt de inventario em docs/MUDANCAS-PARA-APLICAR.md) e aponta
os vazamentos descritos nos artigos de uso do Grok Bot salvos pelo Vini
(ver docs/ENRIQUECIMENTO-SALVOS-X.md, categoria GB):

  - rotina rodando mais vezes que o dado muda (runs/semana alto)
  - agenda onde caberia gatilho
  - rotina cuja saida ninguem le (deve ser pausada)
  - dois donos para a mesma fonte (bots duplicando trabalho)
  - rotina sem arquivo "seen" (re-le tudo a cada execucao)
  - rotina sem condicao de parada / limite de tentativas

Uso:
    python scripts/usage_audit.py            # relatorio
    python scripts/usage_audit.py --json     # saida estruturada
    python scripts/usage_audit.py --strict   # exit 1 se houver achado HIGH
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTINES = ROOT / "state" / "routines.json"

# Regras do MAIN (pointers/08): teto padrao de execucoes por dia por tipo de dado.
MAX_RUNS_PER_DAY_DEFAULT = 3
RUNS_PER_DAY = {
    "every_15_min": 96,
    "every_30_min": 48,
    "hourly": 24,
    "every_2_hours": 12,
    "every_4_hours": 6,
    "3x_day": 3,
    "2x_day": 2,
    "daily": 1,
    "weekdays": 5 / 7,
    "weekly": 1 / 7,
    "trigger": 0,  # so roda quando algo acontece
    "paused": 0,
}


def load() -> dict:
    if not ROUTINES.exists():
        return {"routines": []}
    return json.loads(ROUTINES.read_text(encoding="utf-8"))


def audit(data: dict) -> list[dict]:
    findings: list[dict] = []
    owners: dict[str, list[str]] = defaultdict(list)
    for r in data.get("routines", []):
        name = r.get("name", "?")
        bot = r.get("bot", "?")
        cadence = r.get("cadence", "?")
        per_day = RUNS_PER_DAY.get(cadence)
        data_changes = r.get("data_changes_per_day")
        src = r.get("source")
        if src:
            owners[src].append(f"{bot}/{name}")
        if cadence != "paused" and r.get("output_read") is False:
            findings.append({"sev": "HIGH", "routine": name, "bot": bot,
                             "issue": "saida nao e lida -> pausar (rotina pausada custa zero)"})
        if per_day is None:
            findings.append({"sev": "LOW", "routine": name, "bot": bot,
                             "issue": f"cadencia desconhecida '{cadence}' (use uma de {sorted(RUNS_PER_DAY)})"})
        elif per_day > MAX_RUNS_PER_DAY_DEFAULT:
            limit = data_changes if isinstance(data_changes, (int, float)) else MAX_RUNS_PER_DAY_DEFAULT
            if per_day > max(limit, MAX_RUNS_PER_DAY_DEFAULT):
                findings.append({"sev": "HIGH", "routine": name, "bot": bot,
                                 "issue": f"{per_day:.0f} execucoes/dia ({per_day*7:.0f}/semana) para dado que muda ~{limit}/dia -> alargar agenda ou trocar por gatilho"})
        if cadence not in ("trigger", "paused") and r.get("trigger_possible"):
            findings.append({"sev": "MED", "routine": name, "bot": bot,
                             "issue": "existe gatilho de evento para esta fonte -> trocar agenda por gatilho estreito"})
        if cadence != "paused" and not r.get("seen_file"):
            findings.append({"sev": "MED", "routine": name, "bot": bot,
                             "issue": "sem arquivo seen -> re-le tudo a cada execucao (use scripts/seen.py)"})
        if cadence != "paused" and not r.get("stop_condition"):
            findings.append({"sev": "MED", "routine": name, "bot": bot,
                             "issue": "sem condicao de parada / limite de tentativas"})
        if r.get("posts_in_group_chat"):
            findings.append({"sev": "MED", "routine": name, "bot": bot,
                             "issue": "responde em group chat -> cada bot que responde conta; mandar 1 linha com ponteiro de arquivo"})
    for src, who in owners.items():
        if len(who) > 1:
            findings.append({"sev": "HIGH", "routine": ", ".join(who), "bot": "-",
                             "issue": f"fonte '{src}' com {len(who)} donos -> um dono por fonte"})
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description="Auditoria de uso (0 tokens)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()
    data = load()
    findings = audit(data)
    total_week = sum(RUNS_PER_DAY.get(r.get("cadence"), 0) * 7 for r in data.get("routines", []))
    if args.json:
        print(json.dumps({"routines": len(data.get("routines", [])), "runs_per_week": round(total_week, 1),
                          "findings": findings}, ensure_ascii=False, indent=2))
    else:
        print(f"Rotinas inventariadas: {len(data.get('routines', []))} | execucoes agendadas/semana: {total_week:.0f}")
        if not data.get("routines"):
            print("Inventario vazio: rode o prompt de inventario (docs/MUDANCAS-PARA-APLICAR.md, M3) e preencha state/routines.json.")
        for f in sorted(findings, key=lambda x: {"HIGH": 0, "MED": 1, "LOW": 2}[x["sev"]]):
            print(f"[{f['sev']}] {f['bot']} :: {f['routine']} -> {f['issue']}")
        print("Prova da economia: pause o item HIGH por 24h e compare o % semanal (estimativa nao e prova).")
    if args.strict and any(f["sev"] == "HIGH" for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
