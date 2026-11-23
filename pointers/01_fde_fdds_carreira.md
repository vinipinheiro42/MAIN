---
id: PTR-01
module: fde_fdds_carreira
load_when: ["fde", "fdds", "estudo", "paper", "cv", "curriculo", "entrevista", "portfolio", "linkedin", "roadmap", "carreira"]
depends_on: ["MEMORY.md"]
owner_agent: "fde_architect"
max_tokens: 1400
sla_review_days: 7
---

# PTR-01 — FRENTE 1: FDE, FDDS, AI ENGINEER & 6 CURRÍCULOS

## 1. Ciclo Obrigatório de Todo Projeto (`PUB-JOURN-PROJ-*`)

Nenhum projeto de estudo termina em Jupyter Notebook. Todo repo público deve atravessar os **7 estágios**:

1. **Papers & Artigos:** 1 resumo técnico em `docs/01_research.md` (o que o paper resolve + por que escolhemos esta abordagem).
2. **Spec & Arquitetura:** `docs/02_architecture.md` com diagrama, trade-offs, custos e critérios de aceite (`expected_outputs`).
3. **Projeto End-to-End:** código modular em Python (tipado, limpo, configurável via `.env`, ZERO segredo hardcoded).
4. **Controle de Desenvolvimento (QA, Testes, Segurança & Auditoria):** `pytest`, `ruff`/linter, validação de schema (Pydantic), checagem de secrets (`bandit`/regex) e evals `Esperado vs. Real`.
5. **Deploy:** `Dockerfile` + `docker-compose.yml` (ou Cloud Run/GitHub Actions) com rollback documentado em 1 comando.
6. **Observabilidade:** logs estruturados JSON, latência por etapa, taxa de erro, consumo de tokens/custo e detecção de drift.
7. **Melhoria Contínua:** pós-mortem de bugs/gargalos em `docs/03_postmortem.md` -> v0.2.

## 2. Sequência de Projetos de Portfólio (Máximo Alavancamento dos 6 CVs)

| Repo Público | CVs Cobertos | O Que Constrói | Prazo (SLA) |
|---|---|---|---|
| `PUB-JOURN-PROJ-01-agentic-loop-jev` | **FDE, AI Engineer, DE, AE** | Motor de Loop Engineering + camada de decisão estilo JEV local (Qwen 1.5B/14B) + QA determinístico + telemetria de tokens/latência + Docker. | Dias 8–30 |
| `PUB-JOURN-PROJ-02-retail-demand-fdds` | **FDDS, Data Scientist, FDE** | Previsão de demanda + elasticidade de preço + detecção de drift + experimento causal (A/B) em produção — alimenta diretamente a **V42 Store**. | Dias 45–75 |
| `PUB-JOURN-PROJ-03-hybrid-rag-graph` | **AI Engineer, FDE, DE** | RAG híbrido (BM25 + embeddings + grafo leve inspirado no artigo Cerebras/Graphify do legado) com evals automatizados de fidelidade e latência. | Dias 76–105 |

## 3. Estratégia dos 6 CVs (1 Banco Mestre -> 6 Versões Cirúrgicas)

- **Identidade Pública Única (LinkedIn):** *"Forward Deployed AI & Data Engineer | Production ML, Agentic Systems & Cloud Data (GCP/Azure/Databricks) | 6+ yrs FinTech & Growth"*
- **6 CVs Modulares (`MAIN/priv_cvs/`):** cada CV reordena os mesmos projetos reais (Santander, BMG, Permaneo, Coderhouse + `PUB-JOURN-PROJ-*`) enfatizando as palavras-chave da vaga:
  1. `CV_FDE.md` — foco: ambiguidade de negócio, deploy end-to-end, arquitetura de sistemas, presença consultiva.
  2. `CV_FDDS.md` — foco: ML em produção (PD/LGD/EAD), causalidade/A-B, drift monitoring, MLOps.
  3. `CV_AI_ENG.md` — foco: LLMs, agentes autônomos, Loop Engineering, JEV, RAG, evals, APIs/MCP.
  4. `CV_DE.md` — foco: PySpark, BigQuery, Dataform, bronze/silver/gold, pipelines de milhões de linhas, CI/CD.
  5. `CV_DS.md` — foco: modelagem estatística/preditiva, risco de crédito, XGBoost/PyTorch, impacto financeiro.
  6. `CV_AE.md` — foco: modelagem dimensional, SQLX/dbt, governança, KPIs executivos, DataOps.

## 4. Ação Imediata de Carreira (Semana 1 — Baseada na Consultoria LinkedIn)
- Atualizar Headline, About (tom consultivo + produção), adicionar bullets com métricas nas 5 experiências, preencher Idiomas/Certificações/Projetos e solicitar 3 recomendações (Santander/Permaneo/Coderhouse).
