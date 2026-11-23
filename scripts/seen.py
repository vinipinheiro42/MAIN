#!/usr/bin/env python3
"""
Arquivo "seen" para rotinas (0 tokens): processa so o que e novo.

Padrao dos artigos de uso do Grok Bot (docs/ENRIQUECIMENTO-SALVOS-X.md, GB):
estado de rotina vai em ARQUIVO, nao na memoria do bot. Cada execucao:
  1) le o arquivo e filtra so itens ainda nao vistos;
  2) processa;
  3) grava o que foi tratado + horario da execucao;
  4) poda o que tem mais de N dias (padrao 30) para o arquivo nao virar o novo peso.

Uso:
    python scripts/seen.py filter vagas-fde id1 id2 id3     # imprime so os novos
    echo "id1\nid2" | python scripts/seen.py filter vagas-fde -
    python scripts/seen.py add vagas-fde id1 id2            # marca como tratados
    python scripts/seen.py stats vagas-fde
Arquivos: state/seen/<nome>.json (gitignored).
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEEN_DIR = ROOT / "state" / "seen"


def _path(name: str) -> Path:
    safe = "".join(c for c in name if c.isalnum() or c in "-_")
    if not safe:
        raise SystemExit("nome invalido")
    return SEEN_DIR / f"{safe}.json"


def load(name: str) -> dict:
    p = _path(name)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return {"items": {}, "last_run": None}


def save(name: str, data: dict, keep_days: int) -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(days=keep_days)
    data["items"] = {k: v for k, v in data["items"].items() if datetime.fromisoformat(v) >= cutoff}
    data["last_run"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    SEEN_DIR.mkdir(parents=True, exist_ok=True)
    _path(name).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")


def _ids(args_ids: list[str]) -> list[str]:
    if args_ids == ["-"]:
        return [line.strip() for line in sys.stdin if line.strip()]
    return args_ids


def main() -> int:
    ap = argparse.ArgumentParser(description="Seen-file para rotinas")
    ap.add_argument("cmd", choices=["filter", "add", "stats"])
    ap.add_argument("name")
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--keep-days", type=int, default=30)
    a = ap.parse_args()
    data = load(a.name)
    if a.cmd == "filter":
        for i in _ids(a.ids):
            if i not in data["items"]:
                print(i)
        return 0
    if a.cmd == "add":
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        for i in _ids(a.ids):
            data["items"][i] = now
        save(a.name, data, a.keep_days)
        print(f"{a.name}: {len(data['items'])} itens vistos (ultimos {a.keep_days} dias)")
        return 0
    print(json.dumps({"name": a.name, "seen": len(data["items"]), "last_run": data["last_run"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
