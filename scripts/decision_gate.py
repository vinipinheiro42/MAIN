#!/usr/bin/env python3
"""
JEV-Pattern System-1 Decision Gate (Typed Probabilistic Decisions).
Separates fast, typed control-plane decisions (`choice`, `bool_gate`, `score`)
from heavy System-2 generative models (Qwen 14B / Grokbot / DeepSeek / Claude).

Backends (via env var DECISION_BACKEND):
  - heuristic (default): 0-token deterministic baseline for offline tests & dry-runs
  - ollama: local System-1 model on RX 7800 XT (e.g. qwen2.5:1.5b or qwen2.5:3b)
  - jev: ready adapter for TypeSafe AI JEV API (set JEV_API_URL + JEV_API_KEY)

Usage:
    python scripts/decision_gate.py --self-test
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from typing import Any

CONFIDENCE_THRESHOLD = float(os.getenv("JEV_CONFIDENCE_THRESHOLD", "0.85"))
# Shadow mode (fonte: post "How To Wire Jev Into Grok Bot", ver docs/ENRIQUECIMENTO-SALVOS-X.md):
# o gate decide e REGISTRA, mas nunca libera sozinho (escalate_to_human=True) ate a fase shadow acabar.
SHADOW_MODE = os.getenv("DECISION_SHADOW", "0") == "1"
DECISION_LOG = os.getenv("DECISION_LOG", "")  # ex.: state/decision_log.jsonl (gitignored)


@dataclass
class DecisionResult:
    decision_type: str
    value: Any
    confidence: float
    backend: str
    escalate_to_human: bool
    reason: str = ""


class DecisionGate:
    """Unified System-1 interface: swap local Ollama -> JEV API via 1 env var."""

    def __init__(self, backend: str | None = None) -> None:
        self.backend = (backend or os.getenv("DECISION_BACKEND", "heuristic")).lower()
        self.ollama_url = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
        self.ollama_model = os.getenv("OLLAMA_SYSTEM1_MODEL", "qwen2.5:1.5b")
        self.jev_url = os.getenv("JEV_API_URL", "")
        self.jev_key = os.getenv("JEV_API_KEY", "")

    def _post_json(self, url: str, payload: dict[str, Any], headers: dict[str, str] | None = None) -> dict[str, Any]:
        req_headers = {"Content-Type": "application/json"}
        if headers:
            req_headers.update(headers)
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers=req_headers,
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read().decode("utf-8"))

    def _call_ollama_json(self, prompt: str) -> dict[str, Any]:
        data = self._post_json(
            self.ollama_url,
            {
                "model": self.ollama_model,
                "prompt": prompt,
                "format": "json",
                "stream": False,
                "options": {"temperature": 0.0, "num_predict": 120},
            },
        )
        return json.loads(data.get("response", "{}"))

    def _finalize(self, result: DecisionResult, question: str) -> DecisionResult:
        """Aplica shadow mode e grava trilha (toda decisao deixa rastro)."""
        if SHADOW_MODE:
            result.escalate_to_human = True
            result.reason = f"[shadow] {result.reason}"
        if DECISION_LOG:
            try:
                with open(DECISION_LOG, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"question": question, **asdict(result)}, ensure_ascii=False) + "\n")
            except OSError:
                result.escalate_to_human = True
        return result

    def _fail_closed(self, decision_type: str, value: Any, err: Exception) -> DecisionResult:
        """Fail-closed: se o backend falhar, a resposta e NAO/escalar (timeout nao e pass)."""
        return DecisionResult(decision_type, value, 0.0, self.backend, True, f"backend error -> fail-closed: {err}")

    def choice(self, state: dict[str, Any], question: str, options: list[str]) -> DecisionResult:
        try:
            return self._finalize(self._choice(state, question, options), question)
        except (urllib.error.URLError, OSError, ValueError, json.JSONDecodeError) as err:
            if not options:
                raise
            return self._finalize(self._fail_closed("choice", options[0], err), question)

    def bool_gate(self, state: dict[str, Any], question: str) -> DecisionResult:
        try:
            return self._finalize(self._bool_gate(state, question), question)
        except (urllib.error.URLError, OSError, ValueError, json.JSONDecodeError) as err:
            return self._finalize(self._fail_closed("bool", False, err), question)

    def score(self, state: dict[str, Any], question: str, rubric: str, scale: tuple[int, int] = (0, 10)) -> DecisionResult:
        try:
            return self._finalize(self._score(state, question, rubric, scale), question)
        except (urllib.error.URLError, OSError, ValueError, json.JSONDecodeError) as err:
            return self._finalize(self._fail_closed("score", scale[0], err), question)

    def _choice(self, state: dict[str, Any], question: str, options: list[str]) -> DecisionResult:
        if not options:
            raise ValueError("options must be a non-empty list")

        if self.backend == "ollama":
            prompt = (
                f"Return strict JSON with keys: value (exact item from {options}), "
                f"confidence (float 0..1), reason (short).\n"
                f"State: {json.dumps(state, ensure_ascii=False)}\nQuestion: {question}"
            )
            out = self._call_ollama_json(prompt)
            if out.get("value") not in options:
                # Resposta fora da lista nao vira opcao padrao em silencio: escala (fail-closed).
                return DecisionResult("choice", options[0], 0.0, "ollama", True, f"invalid value {out.get('value')!r}")
            val = out.get("value")
            conf = float(out.get("confidence", 0.5))
            return DecisionResult("choice", val, conf, "ollama", conf < CONFIDENCE_THRESHOLD, str(out.get("reason", "")))

        if self.backend == "jev" and self.jev_url:
            out = self._post_json(
                f"{self.jev_url.rstrip('/')}/choice",
                {"state": state, "question": question, "options": options},
                headers={"Authorization": f"Bearer {self.jev_key}"},
            )
            conf = float(out.get("confidence", 0.0))
            return DecisionResult("choice", out.get("value"), conf, "jev", conf < CONFIDENCE_THRESHOLD, str(out.get("reason", "")))

        # Deterministic heuristic fallback (0 tokens)
        state_str = json.dumps(state, ensure_ascii=False).lower()
        for opt in options:
            if opt.lower() in state_str:
                return DecisionResult("choice", opt, 0.90, "heuristic", False, "Direct keyword match in state")
        return DecisionResult("choice", options[0], 0.70, "heuristic", True, "No exact match; escalate to human or local LLM")

    def _bool_gate(self, state: dict[str, Any], question: str) -> DecisionResult:
        if self.backend == "ollama":
            prompt = (
                "Return strict JSON with keys: value (boolean true/false), "
                "confidence (float 0..1), reason (short).\n"
                f"State: {json.dumps(state, ensure_ascii=False)}\nQuestion: {question}"
            )
            out = self._call_ollama_json(prompt)
            val = bool(out.get("value", False))
            conf = float(out.get("confidence", 0.5))
            return DecisionResult("bool", val, conf, "ollama", conf < CONFIDENCE_THRESHOLD, str(out.get("reason", "")))

        if self.backend == "jev" and self.jev_url:
            out = self._post_json(
                f"{self.jev_url.rstrip('/')}/bool",
                {"state": state, "question": question},
                headers={"Authorization": f"Bearer {self.jev_key}"},
            )
            conf = float(out.get("confidence", 0.0))
            return DecisionResult("bool", bool(out.get("value")), conf, "jev", conf < CONFIDENCE_THRESHOLD, str(out.get("reason", "")))

        # Deterministic check: passes only if tests_passed and no_secrets_leaked are truthy
        # Fail-closed: sem evidencia explicita de "sem segredos vazados", nao passa.
        passed = bool(state.get("tests_passed", False)) and bool(state.get("no_secrets_leaked", False))
        conf = 0.95 if "tests_passed" in state else 0.60
        return DecisionResult("bool", passed, conf, "heuristic", conf < CONFIDENCE_THRESHOLD, "Deterministic QA gate check")

    def _score(self, state: dict[str, Any], question: str, rubric: str, scale: tuple[int, int] = (0, 10)) -> DecisionResult:
        lo, hi = scale
        if self.backend == "ollama":
            prompt = (
                f"Return strict JSON with keys: value (number between {lo} and {hi}), "
                f"confidence (float 0..1), reason (short).\n"
                f"Rubric: {rubric}\nState: {json.dumps(state, ensure_ascii=False)}\nQuestion: {question}"
            )
            out = self._call_ollama_json(prompt)
            val = max(lo, min(hi, float(out.get("value", lo))))
            conf = float(out.get("confidence", 0.5))
            return DecisionResult("score", val, conf, "ollama", conf < CONFIDENCE_THRESHOLD, str(out.get("reason", "")))

        if self.backend == "jev" and self.jev_url:
            out = self._post_json(
                f"{self.jev_url.rstrip('/')}/score",
                {"state": state, "question": question, "rubric": rubric, "scale": [lo, hi]},
                headers={"Authorization": f"Bearer {self.jev_key}"},
            )
            conf = float(out.get("confidence", 0.0))
            return DecisionResult("score", float(out.get("value", lo)), conf, "jev", conf < CONFIDENCE_THRESHOLD, str(out.get("reason", "")))

        checks = state.get("checks_passed", 0)
        total = max(1, state.get("checks_total", 1))
        val = round(lo + (hi - lo) * (checks / total), 2)
        return DecisionResult("score", val, 0.90, "heuristic", False, f"Ratio {checks}/{total}")


def main() -> int:
    parser = argparse.ArgumentParser(description="JEV-Pattern System-1 Decision Gate")
    parser.add_argument("--self-test", action="store_true", help="Run offline deterministic self-test")
    parser.add_argument("--backend", default=None, help="heuristic | ollama | jev")
    parser.add_argument("--shadow", action="store_true", help="Shadow mode: decide e registra, mas sempre escala (sem liberar sozinho)")
    parser.add_argument("--log", default=None, help="Arquivo JSONL de trilha (ex.: state/decision_log.jsonl)")
    args = parser.parse_args()

    global SHADOW_MODE, DECISION_LOG
    if args.shadow:
        SHADOW_MODE = True
    if args.log:
        DECISION_LOG = args.log

    gate = DecisionGate(backend=args.backend)
    if args.self_test:
        r1 = gate.choice({"task": "run local_script sla check"}, "Select execution tier", ["LOCAL_SCRIPT", "QWEN_LOCAL", "GROKBOT"])
        r2 = gate.bool_gate({"tests_passed": True, "no_secrets_leaked": True}, "Did QA pass?")
        r3 = gate.score({"checks_passed": 4, "checks_total": 5}, "Spec compliance score", "0=failed, 10=perfect")
        print(json.dumps([asdict(r1), asdict(r2), asdict(r3)], indent=2, ensure_ascii=False))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
