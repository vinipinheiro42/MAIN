---
id: PTR-06
module: auditoria_erros_postmortem
load_when: ["erro", "bug", "falha", "postmortem", "auditoria", "drift", "licao", "aprendizado", "correcao", "rota"]
depends_on: ["PTR-05"]
owner_agent: "qa_auditor"
max_tokens: 1200
sla_review_days: 7
---

# PTR-06 — MEMÓRIA OPERACIONAL DE ERROS & AUTO-APRENDIZADO (PÓS-MORTEM)

> **Propósito:** Errar rápido uma vez é aprendizado barato. Errar a mesma coisa duas vezes é falha de sistema. Todo erro relevante gera **1 entrada curta aqui + 1 regra ou script que impede a repetição**.
>
> **Regra (23/11/2026):** a contramedida preferida é um **check determinístico** (lint, teste, gate em `scripts/preflight.py` ou `decision_gate.py`), não um parágrafo a mais no prompt (setup pstack, catálogo GB). A versão de 1 linha da lição vai para `LESSONS.md` (≤ 20 linhas, lido no boot). O detalhe fica aqui.

## Formato Padrão de Registro

```markdown
### [AAAA-MM-DD] — [ID-ERRO] Título curto
- **Frente / Estágio:** [FDE | Conteúdo | Funil | V42 Store | Infra]
- **Esperado:** [O que deveria acontecer]
- **Real:** [O que aconteceu de fato]
- **Causa-Raiz:** [Por que falhou]
- **Contramedida Permanente:** [Regra no VALUES.md / teste / script criado]
```

---

## Erros Históricos Já Mapeados (Importados da Auditoria do Legado — 23/11/2026)

### [2026-11-04] — [ERR-001] 4 Documentos Mestres em 30 Dias e 0 Publicações
- **Frente / Estágio:** Conteúdo / Estado 0
- **Esperado:** Estreia do canal em 13/10/2026 e rotina de publicação semanal.
- **Real:** 4 posicionamentos criados (`08_CANAL_VP42`, `Strategy_OS`, `VINIPINHEIRO42-LAB`, `OPERACAO_CONTEUDO`), 0 publicações registradas, logs parados em 08/10.
- **Causa-Raiz:** Meta-produtividade (Armadilha #1) + subestimar custo de edição de vídeo/câmera + over-scoping de 6 plataformas.
- **Contramedida Permanente:** Trava `GATE-0` no `state/gates.json` (proibido novo plano estratégico até publicar Artigo #1 em 48h) + conteúdo Fase 1 focado em texto/código/tela sem superprodução.

### [2026-11-23] — [ERR-002] Risco de Quebra de SSOT com `.docx` Paralelo ao `.md`
- **Frente / Estágio:** Infra / Arquitetura Book-OS
- **Esperado:** Organizar projetos em formato livro com sumário e capítulos para humanos e bots.
- **Real:** Ideia inicial de manter `.docx` editado manualmente e replicar para `.md` geraria drift, conflito de versão e quebra de `git diff`.
- **Causa-Raiz:** Duplicação de fonte de verdade em formato binário.
- **Contramedida Permanente:** Markdown no Git definido como SSOT único + script determinístico `scripts/build_book.py` compilando `.docx`/`.pdf` sob demanda em `exports/`.

### [2026-11-23] — [ERR-003] Risco de Acúmulo Passivo (800 Canais do Telegram)
- **Frente / Estágio:** Estudos & Pesquisa
- **Esperado:** Usar canais de Telegram para acelerar aprendizado e negócios.
- **Real:** 800 canais geram ruído exponencial e ansiedade de informação sem execução.
- **Contramedida Permanente:** Bloqueio no `VALUES.md` (whitelist máxima de 10 fontes curadas) + priorização dos **45 artigos já resumidos** em `PESSOAL_MAIN_ANTIGO/INICIATIVAS/FORMACAO/ARTIGOS/`.
