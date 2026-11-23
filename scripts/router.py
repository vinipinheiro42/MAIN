#!/usr/bin/env python3
"""
Deterministic Context Pointer Router (0 LLM tokens).
Supports both free-text routing and bot-scoped routing (`--bot BOT_DEV`) for
Grokbot and Hermes pulling vinipinheiro42/MAIN.

Usage:
    python scripts/router.py "criar copy e funil do starter kit na hotmart"
    python scripts/router.py --bot BOT_DEV "implementar loop qa com pytest"
    python scripts/router.py --bot BOT_COPY "adaptar post para x e tiktok" --bundle
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
POINTERS_DIR = ROOT / "pointers"
BOTS_DIR = ROOT / "bots"


def normalize(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text.lower())
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def parse_simple_yaml(raw_yaml: str) -> dict[str, Any]:
    meta: dict[str, Any] = {}
    for line in raw_yaml.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            items = re.findall(r'"([^"]+)"|\'([^\']+)\'|([^,\[\]\s]+)', val[1:-1])
            meta[key] = [next(x for x in tup if x) for tup in items]
        else:
            meta[key] = val.strip('"').strip("'")
    return meta


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---"):
        return {}, raw
    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}, raw
    return parse_simple_yaml(parts[1]), parts[2].lstrip()


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def load_pointers() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for md in sorted(POINTERS_DIR.glob("*.md")):
        meta, body = parse_frontmatter(md)
        records.append(
            {
                "path": md,
                "rel": str(md.relative_to(ROOT)).replace("\\", "/"),
                "id": meta.get("id", md.stem),
                "module": meta.get("module", md.stem),
                "load_when": [normalize(k) for k in meta.get("load_when", [])],
                "depends_on": meta.get("depends_on", []),
                "tokens": estimate_tokens(body),
            }
        )
    return records


def load_bot_manifest(bot_name: str) -> tuple[Path, dict[str, Any]]:
    bot_dir = BOTS_DIR / bot_name
    manifest_path = bot_dir / "bot.yaml"
    if not manifest_path.exists():
        available = [d.name for d in sorted(BOTS_DIR.iterdir()) if d.is_dir()] if BOTS_DIR.exists() else []
        raise FileNotFoundError(f"Bot '{bot_name}' not found. Available: {available}")
    return bot_dir, parse_simple_yaml(manifest_path.read_text(encoding="utf-8"))


def route(query: str, max_pointers: int = 2, allowed_ids: list[str] | None = None) -> list[dict[str, Any]]:
    q_norm = normalize(query)
    q_words = set(re.findall(r"[a-z0-9_]+", q_norm))
    pointers = load_pointers()
    if allowed_ids:
        pointers = [p for p in pointers if p["id"] in allowed_ids]

    scored: list[tuple[int, dict[str, Any]]] = []
    for p in pointers:
        score = 0
        for kw in p["load_when"]:
            if kw in q_norm:
                score += 3 if " " in kw else 2
            elif kw in q_words:
                score += 2
        if score > 0:
            scored.append((score, p))

    scored.sort(key=lambda item: item[0], reverse=True)
    if not scored and allowed_ids:
        return pointers[:max_pointers]
    return [item[1] for item in scored[:max_pointers]]


def resolve_files(
    selected: list[dict[str, Any]],
    bot_dir: Path | None = None,
    bot_meta: dict[str, Any] | None = None,
    full_context: bool = False,
) -> list[Path]:
    all_by_id = {p["id"]: p["path"] for p in load_pointers()}
    ordered: list[Path] = []

    if bot_dir is not None:
        bot_agent = bot_dir / "AGENT.md"
        if bot_agent.exists():
            ordered.append(bot_agent)
        if full_context:
            for core_name in ("SOUL.md", "VALUES.md"):
                core_path = ROOT / core_name
                if core_path.exists() and core_path not in ordered:
                    ordered.append(core_path)
            for skill_rel in (bot_meta or {}).get("skills", []):
                skill_path = ROOT / skill_rel
                if skill_path.exists() and skill_path not in ordered:
                    ordered.append(skill_path)
    else:
        for base in ("00_SUMARIO.md", "AGENT.md"):
            p_base = ROOT / base
            if p_base.exists():
                ordered.append(p_base)
        if full_context:
            soul_path = ROOT / "SOUL.md"
            if soul_path.exists():
                ordered.append(soul_path)

    for p in selected:
        if full_context:
            for dep in p["depends_on"]:
                dep_path = all_by_id.get(dep, ROOT / dep)
                if dep_path.exists() and dep_path not in ordered:
                    ordered.append(dep_path)
        if p["path"] not in ordered:
            ordered.append(p["path"])

    sprint_state = ROOT / "state" / "sprint_atual.json"
    if sprint_state.exists():
        ordered.append(sprint_state)
    return ordered


def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic MAIN Context Router (0 tokens)")
    parser.add_argument("query", help="Short description of the current task")
    parser.add_argument("--bot", default=None, help="Scope context to a specific bot folder (e.g. BOT_DEV)")
    parser.add_argument("--max-pointers", type=int, default=2, help="Max pointer chapters to load")
    parser.add_argument("--full", action="store_true", help="Include SOUL/VALUES/skills and transitive deps")
    parser.add_argument("--bundle", action="store_true", help="Print concatenated context bundle")
    args = parser.parse_args()

    bot_dir: Path | None = None
    bot_meta: dict[str, Any] | None = None
    allowed_ids: list[str] | None = None

    if args.bot:
        bot_dir, bot_meta = load_bot_manifest(args.bot)
        allowed_ids = bot_meta.get("allowed_pointers") or None

    selected = route(args.query, max_pointers=args.max_pointers, allowed_ids=allowed_ids)
    files = resolve_files(selected, bot_dir=bot_dir, bot_meta=bot_meta, full_context=args.full)

    total_tokens = sum(estimate_tokens(f.read_text(encoding="utf-8")) for f in files)
    print(f"[ROUTER] Bot: {args.bot or 'ROOT_MAIN'} | Runtime: {(bot_meta or {}).get('runtime', 'any')}")
    print(f"[ROUTER] Query: {args.query}")
    print(f"[ROUTER] Matched pointers: {[p['id'] for p in selected] or ['NONE (base harness only)']}")
    print("[ROUTER] Load order (static cacheable prefix -> dynamic state last):")
    for idx, f in enumerate(files, 1):
        rel = str(f.relative_to(ROOT)).replace("\\", "/")
        tok = estimate_tokens(f.read_text(encoding="utf-8"))
        print(f"  {idx}. {rel} (~{tok} tokens)")
    print(f"[ROUTER] Estimated total context: ~{total_tokens} tokens (0 LLM tokens used for routing)")

    if total_tokens > 4500:
        print("[WARN] Context > 4500 tokens for local Qwen 14B. Consider splitting into 2 micro-tasks.")

    if args.bundle:
        print("\n" + "=" * 72 + "\n")
        for f in files:
            rel = str(f.relative_to(ROOT)).replace("\\", "/")
            print(f"<!-- FILE: {rel} -->")
            print(f.read_text(encoding="utf-8").strip())
            print("\n" + "-" * 72 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
