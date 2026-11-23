---
id: MAIN-MEMORY-05
role: "Memória Factual Verificada do Operador, Hardware, Finanças e Legado"
updated_at: "2026-11-23"
token_budget: 800
---

# MEMORY.md — FATOS VERIFICADOS (FONTE DE VERDADE)

## 1. Trajetória Profissional Real (Fonte: `CV - LUIZ VINICIUS ALVES PINHEIRO.pdf`)

> **Fato Crítico:** Vinicius NÃO é iniciante. Tem **8+ anos em dados desde 2017** (inclui 2 anos de estágio na Marketdata 09/2017–08/2019), em produção em finanças + infoprodutos, e experiência docente. O gargalo é posicionamento público + engenharia de produção FDE/Agentic AI, não falta de base.

- **Grupo Permaneo** — *Senior Data Scientist & AI Engineer — AIOps & Agents* (Jan/2026–atual): pipelines autônomos de agentes (Claude/Anthropic APIs, n8n), 11+ projetos analíticos em BigQuery/Dataform (SQLX), arquitetura bronze/silver/gold no GCP, Cloud Run, observabilidade/CI-CD e infoprodutos orientados a dados. *(Momento atual Nov/2026: reestruturação com demanda leve -> janela ~10h/dia.)*
- **Santander Brasil** — *Senior Data Scientist — Credit & Cards* (Ago/2024–Dez/2025): modelos de risco de crédito (PD, LGD, EAD), precificação e default em Azure/Databricks + PySpark + CI/CD.
- **Santander Asset Management** — *Senior Data Analyst / Data Engineer* (Mai/2022–Ago/2024): ETL escalável (Python, PySpark, Polars, SQL), governança regulatória, dashboards P&L para gestores de fundo.
- **Coderhouse** — *Data Science & ML Instructor* (Nov/2023–Jan/2026): turmas de 20–40 alunos em Python, SQL, Data Science e ML aplicado.
- **BMG Seguros** — *BI & Back-End Specialist* (Jul/2019–Mai/2022): bancos transacionais SQL Server, Pentaho/SSIS, sinistros e seguro crédito.
- **Marketdata** — *Estágio* (Set/2017–Ago/2019): início da trajetória em dados (2 anos).
- **Formação:** MBA em Data Science & Analytics (USP/ESALQ) | Bacharel em Ciência da Computação (Mackenzie, 2016–2021; TCC: *Detecção de Exoplanetas com ML e Visão Computacional*).

## 2. Hardware Real da Estação de Trabalho (Build Nov/2026)

| Componente | Modelo Exato | Implicação Arquitetural no Ecossistema |
|---|---|---|
| **CPU** | AMD Ryzen 5 7600 (3.8/5.1 GHz, AM5) | Plataforma moderna AM5, excelente single-core p/ compilação, Docker e orquestração local |
| **GPU** | XFX SPEEDSTER SWFT210 AMD Radeon **RX 7800 XT 16GB GDDR6** | RDNA 3 com 16GB VRAM; no Omarchy (ROCm/Vulkan), roda **Qwen 14B Q4_K_M 100% em VRAM** + System-1 1.5B/3B |
| **RAM** | Team Group T-Force Delta RGB **32GB DDR5 6000MHz CL30** (2x16GB) | Folga para Docker, múltiplos serviços, RAG local e eventual offload leve de MoE |
| **Placa-Mãe** | **MSI B650 GAMING PLUS WIFI** | **2 slots M.2 NVMe**: permite adicionar 2º SSD dedicado (vídeos ou modelos IA) sem refazer dual boot |
| **Armazenamento** | Kingston NV2 **1TB SSD PCIe 4.0 NVMe Gen 4x4** | Compartilhado entre Dual Boot Windows (artes/vídeo) + Omarchy (dev/IA) -> monitorar espaço |
| **Fonte** | Gigabyte GP-UD750GM **750W 80 Plus Gold Modular** | Folga estável para GPU sob carga contínua de inferência local |
| **Cooler / Gabinete** | Tempest PRO 4Pipes 120mm / MSI MAG Forge 100M | Fluxo de ar adequado para inferência prolongada |
| **Monitor** | Gigabyte GS27QC **27" LED QHD 165Hz** | Alta densidade de tela para terminal tiling (Omarchy) + código + observabilidade |

## 3. Situação Financeira & Stack de IA (Nov/2026)

- **Caixa livre para estoque/tráfego:** **R$ 0** (reserva eventual de até R$ 200/mês de tráfego SÓ após orgânico provado).
- **IA Local (R$ 0):** Omarchy + Hermes (`Qwen2.5-Coder-14B` / `Qwen3-14B` + `Qwen 1.5B/3B` System-1).
- **IA Paga Pessoal:** **Grokbot Premium** (única assinatura paga pessoal atual).
- **IA Corporativa (Isolada):** Gemini do trabalho (uso estritamente profissional/Permaneo).
- **Escada de Reinvestimento Travada por Gates:**
  1. `Gate 2 (R$ 1.500 acumulados)` -> **DeepSeek API** (tokens proporcionais ao lucro, teto 15%).
  2. `Gate 3 (MRR >= R$ 5.000 x 2 meses)` -> **`t3code` + assinatura Claude** + 2º SSD NVMe.

## 4. Auditoria do Legado (`PESSOAL_MAIN_ANTIGO/`) — O Que Reaproveitar

| Ativo Legado | Status | Como Usar no `MAIN` |
|---|---|---|
| `INICIATIVAS/FORMACAO/ARTIGOS/` (45 pastas `artigo.md` + `aula.md`) | **OURO — REAPROVEITAR** | Matéria-prima pronta para 30+ posts/threads (JEV, Loops, AGH, RTK+Graphify, Uncle Bob, Workslop) |
| `PERSONALIDADE/PERSONALIDADE-PROFUNDA.md` | **INCORPORADO** | Base do `SOUL.md` |
| `OPERACAO_CONTEUDO/00_DIAGNOSTICO_E_DECISAO.md` & `05_SEMANA_1_PRONTA.md` | **REAPROVEITAR** | Alerta anti-meta-produtividade (kill switch 04/12/2026) + 3 peças já rascunhadas |
| `Consultoria LinkedIn — FDE & DS.md` + `CV PDF` | **REAPROVEITAR** | Gap analysis pronto para reformar LinkedIn na Semana 1 |
| `REPOS/graphify`, `REPOS/ai-memory`, `CEREBRO/RITUAIS/*.io.yaml` | **REAPROVEITAR** | Referência técnica p/ economia de tokens e rituais automatizados |
| `ViniPinheiro42_Strategy_OS.md` (2.363 linhas) | **ARQUIVAR** | Manter apenas banco de hooks (§30) e regras de métrica (§24) |
| `01_BIT42`, `03_FABRICA_DE_LOJAS`, `04_ACADEMIA_ECOMMERCE`, `08_CANAL_VP42`, `TARGETS/LAB`, 800 canais Telegram | **CONGELAR / ARQUIVAR** | Não tocar na Fase 1 (ruído e over-scoping) |
