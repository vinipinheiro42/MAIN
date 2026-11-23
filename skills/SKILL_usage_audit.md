---
skill: usage-audit
version: "1.0"
triggers: ["uso", "limite", "cota", "auditoria de uso", "rotinas", "pool", "reset", "economia"]
token_budget: 400
---

# SKILL: Auditoria de Uso do Time (semanal, no dia do reset)

> Fontes: "Grok Bot Usage" (@Mahaximus_), "12 Ways" (@maestrooth), "10 steps" (@vartekxx). Regras completas: `pointers/08_grokbot_uso_economia.md`.

## Execução
1. **Inventário:** cada bot responde ao prompt M3 (`docs/MUDANCAS-PARA-APLICAR.md`). Copie só o que eles confirmarem para `state/routines.json`. Não invente rotina.
2. **Detetive (0 tokens):**
   ```bash
   python scripts/usage_audit.py          # relatório
   python scripts/usage_audit.py --json   # para o resumo
   ```
3. **Ação por achado HIGH** (uma por vez):
   - saída não lida → pausar
   - frequência > velocidade do dado → alargar a agenda ou trocar por gatilho
   - fonte com 2 donos → fundir num dono e pôr anti-job no outro
4. **Prova:** pause o suspeito principal por 24h e compare o % semanal antes e depois. Sem prova, não declare economia.
5. **Saída para o Vini (máx. 5 linhas):** execuções/semana antes → depois, o que foi pausado ou mudado, o que depende de aprovação dele.
6. Se houver lição, grave 1 linha no `LESSONS.md`.

## Proibido
- Apagar rotina ou bot sem o ok do Vini (pausar é reversível; apagar não é).
- Reportar porcentagem de economia sem a medição de 24h.
