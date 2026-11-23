#!/usr/bin/env python3
"""
Pre-flight de acao externa (0 tokens): post, envio de mensagem/email, candidatura, formulario.

Adaptado do artigo "Grok Bot Pre-Flight: 7 Gates" salvo pelo Vini (contexto original: trading;
aqui so o metodo). Regras do metodo:
  - gate e binario, nao score: um gate falhou -> a acao morre;
  - fail-closed: se uma checagem nao consegue rodar, a resposta e NAO;
  - checar no momento da acao (rodar logo antes de enviar, nunca horas antes);
  - toda rejeicao vai para o log, revisado 1x/semana (auditoria de rejeitados).

Os gates refletem as regras do Vini (AGENT.md, VALUES.md, MEMORY.md):
  G1 aprovacao   : X/LinkedIn exigem "sim" do Vini ao texto exato, no chat do bot dono do canal
  G2 destino     : alvo/conta conferidos (perfil ativo correto)
  G3 confidencial: nenhum termo proibido (empregadores, clientes, projetos internos)
  G4 sensivel    : sem CPF, senha, token, cartao
  G5 fatos       : numeros e afirmacoes checados contra fonte
  G6 decisao     : salario/proposta/relocation/compromisso so com aprovacao explicita
  G7 fail-closed : erro em qualquer gate = NAO

Uso:
  python scripts/preflight.py --text-file draft.md --channel x --owner-bot TWITTER \\
      --approved-in TWITTER --approval-ref "msg 2026-11-23 14:02" --target @vinipinheiro42 --target-confirmed \\
      --facts-checked
Exit 0 = GO, 1 = NO-GO.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FORBIDDEN = ROOT / "state" / "forbidden_terms.local.txt"
LOG = ROOT / "state" / "preflight_log.jsonl"
PUBLIC_CHANNELS = {"x", "linkedin", "threads", "instagram", "tiktok", "blog"}

SENSITIVE_PATTERNS = {
    "cpf": r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b",
    "cartao": r"\b(?:\d[ -]?){15,16}\b",
    "token": r"\b(?:sk-[A-Za-z0-9]{16,}|gh[opsu]_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|xox[abpr]-[A-Za-z0-9-]{10,})",
    "senha": r"(?i)\b(?:senha|password)\s*[:=]",
}
DECISION_TERMS = r"(?i)\b(pretens[aã]o|sal[aá]rio|aceito a proposta|aceitar a proposta|relocation|reloca[cç][aã]o|contrato assinado|me comprometo)\b"
NUMERIC_CLAIM = r"(?:\d+[.,]?\d*\s?%|R\$\s?\d|US\$\s?\d|\$\d|\b\d{2,}[.,]?\d*\s?(?:mil|k|M|views|seguidores|clientes|vagas)\b)"


def gate(name: str, ok: bool, why: str) -> dict:
    return {"gate": name, "pass": bool(ok), "why": why}


def run(a: argparse.Namespace) -> list[dict]:
    text = Path(a.text_file).read_text(encoding="utf-8")
    res: list[dict] = []
    ch = a.channel.lower()

    # G1 aprovacao
    if ch in PUBLIC_CHANNELS:
        ok = bool(a.approval_ref) and bool(a.approved_in) and a.approved_in.upper() == (a.owner_bot or "").upper()
        res.append(gate("G1_aprovacao", ok, "canal publico: precisa --approval-ref e --approved-in == --owner-bot"))
    else:
        res.append(gate("G1_aprovacao", bool(a.approval_ref), "acao externa: precisa --approval-ref (card/mensagem do Vini)"))

    # G2 destino
    res.append(gate("G2_destino", bool(a.target) and a.target_confirmed, "precisa --target e --target-confirmed (conta/perfil ativo conferido)"))

    # G3 confidencial (fail-closed se a lista nao existir)
    if not FORBIDDEN.exists():
        res.append(gate("G3_confidencial", False, f"lista {FORBIDDEN.name} ausente -> fail-closed (copie state/forbidden_terms.example.txt)"))
    else:
        terms = [t.strip() for t in FORBIDDEN.read_text(encoding="utf-8").splitlines() if t.strip() and not t.startswith("#")]
        hits = [t for t in terms if re.search(rf"(?i)\b{re.escape(t)}\b", text)]
        ok = not hits or (ch not in PUBLIC_CHANNELS and a.allow_private_terms)
        res.append(gate("G3_confidencial", ok, f"termos proibidos encontrados: {len(hits)}" if hits else "ok"))

    # G4 sensivel
    found = [k for k, rx in SENSITIVE_PATTERNS.items() if re.search(rx, text)]
    res.append(gate("G4_sensivel", not found, f"padroes sensiveis: {found}" if found else "ok"))

    # G5 fatos
    nums = re.findall(NUMERIC_CLAIM, text)
    res.append(gate("G5_fatos", (not nums) or a.facts_checked, f"{len(nums)} afirmacoes numericas -> exigem --facts-checked" if nums else "ok"))

    # G6 decisao pessoal
    dec = re.findall(DECISION_TERMS, text)
    res.append(gate("G6_decisao", (not dec) or a.sensitive_approved, f"termos de decisao {sorted(set(d.lower() for d in dec))} -> exigem --sensitive-approved" if dec else "ok"))
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description="Pre-flight de acao externa (fail-closed)")
    ap.add_argument("--text-file", required=True)
    ap.add_argument("--channel", required=True, help="x | linkedin | email | form | chat | outro")
    ap.add_argument("--owner-bot", default="")
    ap.add_argument("--approved-in", default="", help="bot em cujo chat o Vini aprovou o texto exato")
    ap.add_argument("--approval-ref", default="")
    ap.add_argument("--target", default="")
    ap.add_argument("--target-confirmed", action="store_true")
    ap.add_argument("--facts-checked", action="store_true")
    ap.add_argument("--sensitive-approved", action="store_true")
    ap.add_argument("--allow-private-terms", action="store_true", help="so para canais privados (ex.: email ao proprio empregador)")
    a = ap.parse_args()
    try:
        results = run(a)
    except Exception as err:  # G7 fail-closed
        results = [gate("G7_fail_closed", False, f"erro: {err}")]
    go = all(r["pass"] for r in results)
    out = {"go": go, "channel": a.channel, "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"), "gates": results}
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if not go:
        try:
            LOG.parent.mkdir(parents=True, exist_ok=True)
            with LOG.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({**out, "file": a.text_file}, ensure_ascii=False) + "\n")
        except OSError:
            pass
    return 0 if go else 1


if __name__ == "__main__":
    sys.exit(main())
