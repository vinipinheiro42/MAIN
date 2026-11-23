---
skill: loop-qa-audit
version: "1.0"
triggers: ["auditar", "qa", "homologar", "verificar entrega", "esperado vs real"]
token_budget: 500
---

# SKILL: Loop QA & Auditoria (`Esperado vs. Real`)

## Quando Usar
Antes de aprovar qualquer PR, artigo, oferta, script ou deploy gerado por agente ou humano.

## Passo a Passo Obrigatório

1. **Extrair Spec (`Expected`):**
   - Liste explicitamente os critérios de aceite da tarefa (ex: testes passam, sem secrets, tamanho do texto, CTA binário presente, margem >= X%).
   - Se a tarefa não tiver `expected_outputs`, **PARE** e exija a Spec antes de auditar.

2. **Barreira 1 — Verificação Determinística (0 Tokens — SEMPRE PRIMEIRO):**
   - Para código: rodar `pytest`, `ruff`/linter, checagem de secrets e execução real do script.
   - Para conteúdo/docs: validar links, ausência de dados internos da Permaneo e conformidade com `VALUES.md`.
   - **Se falhar:** devolver erro exato ao agente executor (incrementa `retry_count`).

3. **Barreira 2 — Verificação Semântica (Padrão JEV — `scripts/decision_gate.py`):**
   - Comparar `Expected` vs. `Actual` e emitir rigorosamente:
     - `passed`: `true | false`
     - `score`: `0–10`
     - `confidence`: `0.0–1.0`
     - `gaps`: lista objetiva (máx. 3 itens) do que divergiu.

4. **Política de Decisão & Circuit Breaker:**
   - `passed == true` e `confidence >= 0.85` -> **APROVADO** para PR/staging/publicação.
   - `passed == false` e `retry_count < 3` -> volta ao loop automaticamente com o `gaps` como instrução cirúrgica.
   - `retry_count >= 3` ou `confidence < 0.85` -> **TRAVAR LOOP** e escalar ao Vinicius no formato de 3 bullets (`Origem`, `Esperado vs. Real`, `Decisão Dominante`).

5. **Retroalimentação:**
   - Se for um padrão de erro novo, registrar em `pointers/06_auditoria_erros.md` com contramedida permanente.
