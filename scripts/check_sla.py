#!/usr/bin/env python3
"""
Deterministic SLA Watchdog & Gate Progress Reporter (0 LLM tokens).
Reads state/slas.json, state/gates.json and state/sprint_atual.json, prints a
linear daily executive briefing with progress bars, and exits with code 2 if
any SLA is RED (overdue) so cron/Grokbot/Hermes can trigger alerts automatically.

Usage:
    python scripts/check_sla.py
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = ROOT / "state"


def progress_bar(pct: int, width: int = 12) -> str:
    pct = max(0, min(100, pct))
    filled = round((pct / 100) * width)
    return "[" + "#" * filled + "-" * (width - filled) + f"] {pct:3d}%"


def classify_sla(due_iso: str, today: date) -> tuple[str, int]:
    due = date.fromisoformat(due_iso)
    delta = (due - today).days
    if delta < 0:
        return "RED", delta
    if delta <= 1:
        return "YELLOW", delta
    return "GREEN", delta


def main() -> int:
    today = date.today()
    slas_data = json.loads((STATE_DIR / "slas.json").read_text(encoding="utf-8"))
    gates_data = json.loads((STATE_DIR / "gates.json").read_text(encoding="utf-8"))
    sprint_data = json.loads((STATE_DIR / "sprint_atual.json").read_text(encoding="utf-8"))

    print("=" * 68)
    print(f"MAIN SLA WATCHDOG & BRIEFING | DATA: {today.isoformat()} | 0 TOKENS")
    print("=" * 68)
    print(f"ESTADO ATUAL : {gates_data['current_state']}")
    print(f"SPRINT ATIVO : {sprint_data['sprint_id']} ({sprint_data['period']})")
    print(f"FOCO P0 HOJE : {sprint_data['p0_single_focus_today']}")
    print("-" * 68)

    print("GATES DE PROGRESSAO:")
    for g in gates_data["gates"]:
        total = len(g["criteria"])
        done = sum(1 for c in g["criteria"] if c["done"])
        pct = int(round((done / total) * 100)) if total else 0
        print(f"  {g['id']:<7} {progress_bar(pct)} | {g['status']:<11} | {g['name']}")

    print("-" * 68)
    print("SLAS ATIVOS:")
    has_red = False
    for item in slas_data["slas"]:
        if item["status"].upper() == "DONE":
            print(f"  [DONE  ] {item['id']} | {item['title']}")
            continue
        sev, days = classify_sla(item["due_date"], today)
        if sev == "RED":
            has_red = True
            timing = f"ESTOURADO ha {abs(days)}d"
        elif days == 0:
            timing = "VENCE HOJE"
        else:
            timing = f"faltam {days}d ({item['due_date']})"
        print(f"  [{sev:<6}] {item['id']} ({item['gate']}) | {timing:<24} | {item['title']}")

    print("=" * 68)
    if has_red:
        print("[ALERTA RED] Existe SLA estourado! Congele frentes secundarias e execute cirurgia de escopo.")
        return 2
    print("[OK] Nenhum SLA estourado. Execute o FOCO P0 antes de abrir novas tarefas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
