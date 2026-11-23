---
skill: token-router
version: "1.0"
triggers: ["rotear", "economizar tokens", "carregar contexto", "qual ponteiro"]
token_budget: 400
---

# SKILL: Roteador Cirúrgico de Ponteiros (`Token Economy`)

## Regra Central
**Nunca carregue o repositório inteiro.** A janela de contexto é um recurso escasso (especialmente em Qwen 14B local na RX 7800 XT 16GB).

## Fluxo Operacional

1. **Execute primeiro o roteador determinístico (0 tokens):**
   ```bash
   python scripts/router.py "<descrição curta da tarefa>"
   ```
2. **Leia apenas os arquivos retornados pelo roteador:**
   - Sempre manter no prefixo fixo (cacheável): `AGENT.md` + `SOUL.md` (ou só `00_SUMARIO.md` em tarefas micro).
   - Carregar **no máximo 2 arquivos de `pointers/`** (+ dependências explícitas do YAML).
   - Anexar `state/sprint_atual.json` no **final** do prompt (para preservar Prompt Caching do prefixo estático).
3. **Filtro de Evidências (Anti-Bloat):**
   - Código: passe `git diff` ou apenas as funções alteradas, nunca arquivos inteiros de 1.000 linhas.
   - Logs: filtre para as últimas 30 linhas relevantes ou apenas o traceback.
   - Legado: jamais varrer `PESSOAL_MAIN_ANTIGO/` inteiro; leia somente o arquivo específico citado em `MEMORY.md`.
4. **Regra de Orçamento:** se o pacote montado passar de **4.000 tokens** para uma tarefa local em Qwen 14B, quebre a tarefa em 2 micro-tarefas antes de executar.
