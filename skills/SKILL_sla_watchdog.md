---
skill: sla-watchdog
version: "1.0"
triggers: ["sla", "prazo", "atrasado", "briefing", "cobranca", "check gates"]
token_budget: 400
---

# SKILL: SLA Watchdog & Cobrança Linear

## Objetivo
Impedir o ciclo `Over-scoping -> Meta-Produtividade -> Atraso -> Sumiço` mantendo o Vinicius focado na **1 tarefa crítica** de cada janela.

## Execução

1. **Rode o script determinístico (0 tokens):**
   ```bash
   python scripts/check_sla.py
   ```
2. **Classifique a resposta pela severidade retornada:**
   - Se houver qualquer item **RED (Estourado):**
     - **BLOQUEIE** qualquer pedido paralelo do Vinicius.
     - Exija decisão imediata: *(A) Cortar 50% do escopo e entregar versão Lean em até 4h*, ou *(B) Registrar pós-mortem em `pointers/06_auditoria_erros.md` e replanejar oficialmente*.
   - Se houver item **YELLOW (<= 24h):**
     - Coloque o item como **P0 ÚNICO** do dia antes de qualquer outra frente.
   - Se tudo **GREEN:**
     - Avance linearmente na fila de `state/sprint_atual.json` e mostre a barra de progresso do Gate atual (`state/gates.json`).
3. **Formato de Escalação (sempre 3 bullets + CTA binário):**
   - **Origem:** `[Task ID / Gate]`
   - **Esperado vs. Real:** `[Prazo/Critério] vs. [Status atual]`
   - **Decisão Dominante:** `[A] vs. [B]`
