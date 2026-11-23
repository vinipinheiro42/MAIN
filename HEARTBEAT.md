---
id: MAIN-HEARTBEAT-04
role: "Rituais Lineares, Gatilhos, SLA Watchdog & Escalação Humana"
token_budget: 600
---

# HEARTBEAT.md — RITMO, SLAs & PROTOCOLO DE DECISÃO HUMANA

## 1. Workflow Linear Diário (Empilhamento na Janela de 10h)

O dia funciona como **linha de montagem linear** (sem multitarefa caótica):

| Bloco | Janela Sugerida | Foco Único | Regra de Proteção |
|---|---|---|---|
| **Bloco 0 — Boot & SLA** | 15 min (início) | Rodar `python scripts/check_sla.py` + ler `state/sprint_atual.json` | 0 tokens de LLM; define a **ÚNICA entrega crítica do dia** |
| **Bloco 1 — Permaneo (Obrigação)** | Conforme demanda real (1h–3h) | Entregas CLT + AIOps/BigQuery com excelência | Garante renda base + transforma padrões aprendidos (sem dados internos) em matéria-prima |
| **Bloco 2 — Deep Work FDE/FDDS** | 3h (manhã/início tarde) | Estudo aplicado -> código -> testes -> deploy em `PUB-JOURN-PROJ-*` | Celular longe; Qwen local + Grokbot executam sob Spec; foco em 1 commit real/dia |
| **Bloco 3 — Distribuição & Negócio** | 2h (tarde) | Publicar conteúdo derivado do Bloco 2 + construir oferta/ponte da semana | Sem gravação complexa na Fase 1; texto + diagrama + print limpo de código/arquitetura |
| **Bloco 4 — Auditoria & Fechamento** | 30 min (fim) | Revisar PRs/outputs dos bots, atualizar `state/sprint_atual.json` e `slas.json` | Encerramento firme para proteger família, sono e evitar ciclo de fadiga |

## 2. Gatilhos Rápidos de Comando (Compatível com Qualquer Harness)

| Gatilho | Ação Executada pelo Agente / Script |
|---|---|
| `bom dia` / `briefing` | Roda `scripts/check_sla.py` + lê `state/sprint_atual.json` + entrega briefing de 8 linhas com 1 foco P0 |
| `foco` | Responde em 3 linhas qual é a **ÚNICA tarefa** que destrava o Gate atual agora |
| `sla` | Lista todos os SLAs em `GREEN` / `YELLOW` (<24h) / `RED` (estourado) via `scripts/check_sla.py` |
| `check gates` | Lê `state/gates.json` e mostra barra de progresso real (`[███░░░░░░░] 30%`) de cada Gate |
| `publicar` | Ativa `skills/SKILL_content_from_work.md` sobre o último commit/estudo real |
| `auditar` | Ativa `skills/SKILL_loop_qa_audit.md` comparando Spec (`Expected`) vs. Artefato (`Actual`) |
| `uso` / `auditar uso` | Ativa `skills/SKILL_usage_audit.md`: `python scripts/usage_audit.py` sobre `state/routines.json` + plano de 1 ajuste por item HIGH |
| `preflight` | Ativa `skills/SKILL_preflight_externo.md` antes de qualquer post/envio/candidatura |
| `fim do dia` | Registra entregas reais, move pendências, atualiza `state/sprint_atual.json` e trava plano de amanhã |

## 3. Regra de Severidade de SLA (Cobrança Agressiva)

- **GREEN (> 48h do prazo):** execução normal pelo loop.
- **YELLOW (<= 24h do prazo):** alerta imediato; **proibido iniciar tarefas secundárias** até fechar o item amarelo.
- **RED (prazo estourado):** congela TODAS as outras frentes; ativa modo "cirurgia de escopo" (cortar escopo em 50% e entregar versão funcional em até 4h, ou registrar pós-mortem em `pointers/06_auditoria_erros.md`).

## 4. Protocolo de Escalação Humana (Human-in-the-Loop — 3 Bullets)

Os bots só interrompem o Vinicius quando: (a) `confidence < 0.85` no Gate JEV, (b) `circuit breaker` bateu 3 falhas seguidas, (c) SLA entrou em `YELLOW/RED`, ou (d) aprovação final de publicação/deploy/gasto.

Formato obrigatório do alerta (máximo 5 linhas):
- **Origem:** `[Repo / Módulo / Estágio do Loop / Task ID]`
- **Esperado vs. Real:** `[Critério da Spec] vs. [Resultado obtido + causa do bloqueio]`
- **Decisão Dominante:** `[Opção A] vs. [Opção B] — responda A ou B`

## 5. Ritual Semanal de Higiene do Time (dia do reset do pool)

Fonte: artigos de uso do Grok Bot nos salvos do X (`docs/ENRIQUECIMENTO-SALVOS-X.md`, GB). Total: 20 min, quase tudo a 0 token.
1. **Auditoria de uso:** inventário M3 → `state/routines.json` → `python scripts/usage_audit.py`. Um ajuste por item HIGH. Prova = pausar o suspeito por 24h e comparar o % semanal.
2. **Auditoria dos rejeitados:** ler `state/preflight_log.jsonl`. O gate barrou certo? Precisa de termo novo na lista ou de ajuste no gate?
3. **Modo sombra do DECISOR (se ativo):** ler `state/decision_log.jsonl` e anotar quantas decisões bateram com a escolha real.
4. **Segundo cérebro:** fontes novas em `knowledge/raw/`; lint do `wiki/` (fato sem fonte, checagem com mais de 90 dias, conflito aberto).
5. **Lições:** `LESSONS.md` com no máximo 20 linhas. Lição que já virou script sai da lista.

