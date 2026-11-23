---
id: PTR-05
module: loop_jev_economia_tokens
load_when: ["loop", "jev", "token", "router", "qa", "auditoria", "observabilidade", "qwen", "grokbot", "hermes", "omarchy", "hardware", "vram", "rtk", "graphify", "cache", "docx"]
depends_on: ["AGENT.md", "MEMORY.md"]
owner_agent: "systems_architect"
max_tokens: 1500
sla_review_days: 7
---

# PTR-05 — LOOP ENGINEERING, PADRÃO JEV, HARDWARE RX 7800 XT & ECONOMIA DE TOKENS

## 1. Explicação Direta de Hardware (Sem Juridiquês)

### Por que modelos densos >14B–16B travam na RX 7800 XT 16GB?
- Pense na **VRAM da placa de vídeo (16 GB GDDR6)** como uma **mesa de estudo ultrarrápida** na sua frente, e na **RAM do PC (32 GB DDR5)** como um **armário do outro lado do quarto**.
- Um modelo de **14B (quantizado Q4)** ocupa ~9–10 GB: ele cabe **inteiro em cima da mesa (VRAM)** + sobra espaço para o caderno de rascunho (*KV cache* / contexto). A placa responde em altíssima velocidade (30–50+ tokens/s).
- Um modelo denso de **32B (Q4)** precisa de ~20 GB. Como não cabe nos 16 GB da mesa, o computador é obrigado a guardar parte do cérebro no armário do outro lado do quarto (**offload em RAM**) e atravessar o quarto (barramento PCIe) a **cada palavra gerada**. A velocidade despenca de ~40 tokens/s para ~3–6 tokens/s — matando qualquer loop autônomo.
- **Conclusão prática para o Omarchy (ROCm/Vulkan):**
  - **System-2 padrão (código/texto):** `Qwen2.5-Coder-14B` ou `Qwen3-14B` (`Q4_K_M`, 100% em VRAM).
  - **System-1 padrão (JEV local):** `Qwen2.5-1.5B` ou `3B` (~1.5–2 GB VRAM, cabe **junto** com o 14B na mesma GPU!).

### Por que PROIBIR LLM (System-2) em tarefas determinísticas?
- Usar um LLM grande para checar se um SLA venceu, converter `.md` em `.docx`, ler um JSON ou checar `git status` é como **pagar um cirurgião PhD para apertar o botão da calculadora**: é lento, gasta cota/energia e ainda pode errar a conta por alucinação.
- Tudo o que tem regra fixa vira script Python em `scripts/` -> roda em **50ms, 100% determinístico e 0 tokens**.

## 2. Esteira Loop Engineering + JEV (5 Estágios)

```text
[1. SPEC (.md + expected_outputs)]
        │
        ▼ (scripts/router.py — 0 tokens: seleciona 1–2 ponteiros via YAML)
        ▼ (scripts/decision_gate.py — System-1 JEV: escolhe Script vs Qwen vs Grokbot)
[2. EXECUÇÃO em branch bot/<id>]
        │
        ▼
[3. QA & AUDITORIA (Esperado vs. Real)]
    ├── Barreira 1 (0 tokens): pytest, ruff, schema, security check
    │     └── Falhou? Traceback volta ao [2] (Circuit Breaker: máx 3x)
    └── Barreira 2 (JEV System-1): passed (Bool), score (0–10), confidence (0–1)
          ├── passed=True & confidence>=0.85 -> PR pronto / staging
          └── confidence<0.85 ou 3 falhas -> ESCALA PRO VINICIUS (3 bullets)
        │
        ▼
[4. PRODUTIZAÇÃO & DEPLOY (Docker / tag / rollback 1 cmd / build_book.py)]
        │
        ▼
[5. OBSERVABILIDADE (métricas reais -> se drift/erro -> grava em PTR-06 -> abre nova task)]
```

## 3. Protocolo Book-OS (`.md` SSOT -> `.docx` Compilado)
- **Fonte única de verdade:** arquivos `.md` versionados no Git + `state/*.json`.
- **Exportação para leitura/revisão humana:** rode `python scripts/build_book.py` -> gera o livro consolidado em `exports/` (`.md` único e `.docx` automático se `pandoc` estiver instalado). Nunca edite o `.docx` gerado como paralelo.

## 4. Checklist das 7 Alavancas de Economia de Tokens
1. **Ponteiros YAML (`router.py`)** — só injeta os 1–2 módulos necessários.
2. **Scripts locais (`scripts/`)** — 0 tokens para todo processo repetível.
3. **JEV System-1 local (`decision_gate.py`)** — roteamento e QA barato/rápido.
4. **Separação Estático vs. Dinâmico** — `.md` fixos no topo (Prompt Caching 75–90% off no DeepSeek/Claude), `state/*.json` no final.
5. **RTK / Filtro de Logs** — nunca colar output gigante de terminal; filtrar apenas linhas de erro/resumo.
6. **Graphify / Mapa de Repositório** — consultar o grafo estrutural do código antes de abrir arquivos aleatórios.
7. **Diff-Only Review** — passar `git diff` em vez de arquivos inteiros nas auditorias.

## Atualização 23/11/2026 — Uso do Grok Bot e Gate fail-closed
- As regras de uso/pool/rotinas do Grok Bot ficam em `pointers/08_grokbot_uso_economia.md` (não duplicar aqui).
- `scripts/decision_gate.py` agora é **fail-closed**: erro, timeout ou valor fora da lista viram `escalate_to_human=true` (nunca a 1ª opção em silêncio). O `bool_gate` heurístico exige `no_secrets_leaked=true` explícito. Há também o **modo sombra** (`--shadow`/`DECISION_SHADOW=1`, com trilha em `--log`) para ligar o JEV primeiro só registrando (fonte: "How To Wire Jev Into Grok Bot", catálogo GB).
- Princípio de custo (catálogo GB, "Stop Paying for Failed Tasks"): o modelo mais barato é o que **termina a tarefa e passa no check**. Suba de tier só depois que o check falhar.

