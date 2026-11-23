---
skill: preflight-externo
version: "1.0"
triggers: ["publicar", "postar", "enviar", "email", "candidatura", "formulario", "mensagem", "pre-flight", "preflight"]
token_budget: 350
---

# SKILL: Pre-flight de Ação Externa (binário, fail-closed)

> Fonte do método: "Grok Bot Pre-Flight: 7 Gates" (@Corki_0x), adaptado (o contexto original era trading e não foi aplicado). Checklist: `templates/PREFLIGHT.md`.

## Execução (no momento da ação, nunca horas antes)
1. Salve o texto final exato em arquivo (ex.: `content/drafts/<id>.md`).
2. Rode:
   ```bash
   python scripts/preflight.py --text-file content/drafts/<id>.md --channel <x|linkedin|email|form> \
     --owner-bot <BOT> --approved-in <BOT onde o Vini disse sim> --approval-ref "<mensagem/card>" \
     --target "<conta/destinatário>" --target-confirmed [--facts-checked] [--sensitive-approved]
   ```
3. `go: true` → executa a ação. `go: false` → **não executa**. Corrija o gate que falhou ou peça ao Vini o que falta.
4. Rejeições ficam em `state/preflight_log.jsonl` e são revisadas no ritual semanal.

## Regras
- O texto mudou depois da aprovação? Precisa de aprovação nova (G1).
- Sem `state/forbidden_terms.local.txt`, o G3 falha. Isso é proposital (fail-closed).
- Os flags `--facts-checked` e `--sensitive-approved` só valem quando a checagem foi feita de verdade e citada no chat.
