#!/usr/bin/env python3
"""
Book-OS Compiler (0 LLM tokens).
Single Source of Truth (SSOT) lives in Git Markdown files. This script compiles
MAIN into a unified readable book at exports/MAIN_BOOK_LIVE.md and, if `pandoc`
is installed on PATH, automatically generates exports/MAIN_BOOK_LIVE.docx with TOC.

Usage:
    python scripts/build_book.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPORTS_DIR = ROOT / "exports"

CHAPTER_ORDER = [
    "00_SUMARIO.md",
    "ECOSYSTEM_MASTER.md",
    "AGENT.md",
    "SOUL.md",
    "VALUES.md",
    "HEARTBEAT.md",
    "MEMORY.md",
    "LESSONS.md",
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return text


def main() -> int:
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    sections: list[str] = [
        f"# VINIPINHEIRO42 — MAIN OPERATING BOOK\n\n"
        f"> Compilado automaticamente a partir do SSOT Markdown em {datetime.now().strftime('%Y-%m-%d %H:%M')}.\n"
        f"> **NUNCA edite este arquivo ou o `.docx` manualmente.** Edite os `.md` fonte no Git e rode `python scripts/build_book.py`.\n"
    ]

    for rel in CHAPTER_ORDER:
        p = ROOT / rel
        if p.exists():
            sections.append(strip_frontmatter(p.read_text(encoding="utf-8")).strip())

    for ptr in sorted((ROOT / "pointers").glob("*.md")):
        sections.append(strip_frontmatter(ptr.read_text(encoding="utf-8")).strip())

    bots_dir = ROOT / "bots"
    if bots_dir.exists():
        sections.append("# CATÁLOGO DE BOTS AUTO-CONTIDOS (GROKBOT & HERMES)\n")
        for bot_agent in sorted(bots_dir.glob("*/AGENT.md")):
            sections.append(strip_frontmatter(bot_agent.read_text(encoding="utf-8")).strip())

    out_md = EXPORTS_DIR / "MAIN_BOOK_LIVE.md"
    out_md.write_text("\n\n---\n\n".join(sections) + "\n", encoding="utf-8")
    print(f"[BOOK-OS] Compiled Markdown book: {out_md}")

    pandoc = shutil.which("pandoc")
    if pandoc:
        out_docx = EXPORTS_DIR / "MAIN_BOOK_LIVE.docx"
        subprocess.run(
            [pandoc, str(out_md), "-o", str(out_docx), "--toc", "--toc-depth=2"],
            check=True,
        )
        print(f"[BOOK-OS] Compiled DOCX with TOC: {out_docx}")
    else:
        print("[BOOK-OS] pandoc not found on PATH (skipping .docx export).")
        print("          Windows: winget install JohnMacFarlane.Pandoc")
        print("          Omarchy: sudo pacman -S pandoc")
    return 0


if __name__ == "__main__":
    sys.exit(main())
