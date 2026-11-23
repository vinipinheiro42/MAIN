---
id: MAIN-SUMARIO-00
version: "2.0"
owner: "Luiz Vinicius Alves Pinheiro (@vinipinheiro42)"
updated_at: "2026-11-23"
ssot: true
token_budget: 550
---

# 00 — SUMÁRIO MESTRE (`vinipinheiro42/MAIN`)

> **Regra de Ouro (Progressive Disclosure):** NUNCA carregue todos os arquivos deste repositório de uma vez. Leia este sumário (~500 tokens), identifique o ponteiro exato da tarefa ou rode `python scripts/router.py "<tarefa>"`, e carregue **apenas os 1–2 módulos necessários**.

## 1. Núcleo Portável do Harness (Carregamento Base — AGH Standard)

| Arquivo | Papel no Harness | Quando Carregar |
|---|---|---|
| `AGENT.md` | Contrato universal de operação (Loop Engineering + JEV + Git + Compliance) | Sempre no boot da sessão |
| `SOUL.md` | Perfil cognitivo do Vinicius, tom de mentor agressivo e defesa contra as 5 armadilhas ("James") | Sempre no boot da sessão |
| `VALUES.md` | Valores inegociáveis, princípios FDE e Catálogo de Negative Space (proibições) | Em decisões de escopo, arquitetura ou revisão |
| `HEARTBEAT.md` | Rituais diários/semanais, gatilhos rápidos e protocolo de SLA/Escalação | No início/fim do dia e em alertas de SLA |
| `MEMORY.md` | Fatos verificados: CV, Hardware RX 7800 XT, Caixa R$ 0, Legado auditado | Quando precisar de contexto factual do operador |
| `LESSONS.md` | Lições operacionais de 1 linha (máx. 20) | Sempre no boot da sessão |
| `ECOSYSTEM_MASTER.md` | Artigo-Documentação completa do Ecossistema, Funil com Pontes e Roadmap 90 dias | Apenas em planejamento macro ou revisão trimestral |

## 2. Ponteiros de Módulos (`pointers/`) — Carregamento Cirúrgico

| ID | Arquivo | Domínio | Gatilhos (`load_when`) | Dependências |
|---|---|---|---|---|
| `PTR-01` | `pointers/01_fde_fdds_carreira.md` | Frente 1: FDE, FDDS, AI Eng, 6 CVs, Estudo -> Deploy | `fde`, `fdds`, `estudo`, `paper`, `cv`, `entrevista`, `portfolio`, `linkedin` | `MEMORY.md` |
| `PTR-02` | `pointers/02_conteudo_distribuicao.md` | Conteúdo, Artigo #1, LinkedIn, X, TikTok, 45 Artigos | `artigo`, `post`, `thread`, `tiktok`, `conteudo`, `viral`, `hook`, `copy` | `SOUL.md` |
| `PTR-03` | `pointers/03_funil_infoprodutos_b2b.md` | Escada de Produtos, Pontes Orgânicas, Mentoria, B2B | `funil`, `ebook`, `plataforma`, `mentoria`, `b2b`, `vendas`, `oferta`, `preco` | `PTR-02` |
| `PTR-04` | `pointers/04_v42_store_ecommerce.md` | Frente 2: V42 Store, Marketplaces, Dados de Varejo, Galpão | `ecommerce`, `v42`, `shopee`, `mercadolivre`, `tiktok shop`, `fornecedor`, `galpao` | `PTR-03` |
| `PTR-05` | `pointers/05_loop_jev_economia_tokens.md` | Loop Engineering, JEV System-1, Book-OS, Economia de Tokens | `loop`, `jev`, `token`, `router`, `qa`, `observabilidade`, `qwen`, `grokbot` | `AGENT.md` |
| `PTR-06` | `pointers/06_auditoria_erros.md` | Pós-mortem e Auto-aprendizado (Memória Anti-Repetição) | `erro`, `bug`, `falha`, `postmortem`, `auditoria`, `drift`, `revisao` | `PTR-05` |
| `PTR-07` | `pointers/07_segundo_cerebro.md` | Segundo cérebro: raw → wiki → output, fato com fonte e data | `segundo cerebro`, `wiki`, `obsidian`, `knowledge`, `fonte`, `memoria` | `MEMORY.md` |
| `PTR-08` | `pointers/08_grokbot_uso_economia.md` | Uso/pool do Grok Bot, 7 vazamentos, regras de rotina, auditoria semanal | `uso`, `limite`, `pool`, `rotina`, `gatilho`, `economia`, `grok bot` | `PTR-05` |
| `PTR-09` | `pointers/09_time_de_bots_protocolo.md` | Protocolo do time: dono, handoff, revisão, pre-flight, criar bot | `handoff`, `delegar`, `contrato`, `revisor`, `preflight`, `aprovacao`, `bot novo` | `AGENT.md`, `PTR-08` |

## 3. Diretórios de Bots Auto-Contidos (`bots/` — Pull Direto para Grokbot & Hermes)

Cada pasta contém `AGENT.md` + `bot.yaml` e carrega **apenas** seus ponteiros autorizados via `python scripts/router.py --bot <BOT_ID> "<tarefa>"`:

| Bot | Domínio | Runtime Padrão |
|---|---|---|
| `bots/BOT_MAIN/` | Orquestrador, Mentor Agressivo & SLA Dispatcher | Grokbot Premium / Qualquer Harness |
| `bots/BOT_CARREIRA/` | FDE, FDDS, AI Eng, DE, DS, AE (Estudos, Papers, 6 CVs) | Grokbot + Qwen 14B |
| `bots/BOT_COPY/` | LinkedIn, X/Twitter, Threads, TikTok, Newsletter | Grokbot Premium |
| `bots/BOT_DEV/` | Código E2E, Docker, CI/CD, Scripts 0-Token (Omarchy) | **Hermes / Qwen 14B Local (R$ 0)** |
| `bots/BOT_QA/` | Auditoria `Esperado vs. Real`, JEV Gate, Circuit Breaker 3x | **Qwen 1.5B/14B + `decision_gate.py`** |
| `bots/BOT_SEC/` | Secrets, NDA Permaneo, Vulnerabilidades, Isolamento | **Scripts Locais + Qwen 14B Local** |
| `bots/BOT_GROWTH_FUNIL/` | Funil 2 Trilhas, Pontes, Starter Kit, Plataforma, Mentoria, B2B | Grokbot Premium |
| `bots/BOT_V42_STORE/` | V42 Store (Zero-CAPEX -> Dados de Varejo -> Gate 4 Galpão) | Qwen 14B Local + Scripts |

## 4. Habilidades Portáveis (`skills/`)

- `skills/SKILL_loop_qa_audit.md` — Auditoria `Esperado vs. Real` com barreira determinística + Circuit Breaker (3x)
- `skills/SKILL_token_router.md` — Seleção mínima de contexto via Frontmatter YAML + diff-only
- `skills/SKILL_content_from_work.md` — Transformação de código/estudo real em LinkedIn + X + TikTok (zero Workslop)
- `skills/SKILL_sla_watchdog.md` — Cobrança linear, SLAs e escalação humana em 3 bullets
- `skills/SKILL_usage_audit.md` — Auditoria semanal de uso/rotinas do time (0 tokens + prova de 24h)
- `skills/SKILL_preflight_externo.md` — Pre-flight binário e fail-closed antes de post/envio/candidatura

### Modelos (`templates/`)
`TASK_BRIEF.md` (contrato de tarefa) · `HANDOFF_NOTE.md` (troca de bot/chat) · `BOT_BRIEF.md` (perfil curto de bot) · `GOAL_CONTRACT.md` (meta de negócio) · `PREFLIGHT.md` (checklist de ação externa) · `REVIEW_VERDICT.md` (veredito do revisor)

### Conhecimento e documentos (`knowledge/`, `docs/`)
- `knowledge/` — segundo cérebro (`raw/` nunca editado, `wiki/INDEX.md`), ver PTR-07
- `docs/ENRIQUECIMENTO-SALVOS-X.md` — fontes (salvos do X) de cada regra nova, com resumo e onde aplicar
- `docs/MUDANCAS-PARA-APLICAR.md` — texto exato das mudanças em bots/rotinas/skills vivos (aplicar fora do repo)
- `docs/MAPA-STACK-NEGOCIO-DIGITAL.md` — termos de negócio digital → onde cabem, bot dono, próximo passo
- `docs/ESCOPO-GROKBOT.md` — escopo do Grok Bot a partir de 24/11: três linhas (LinkedIn/X); o restante chega via MAIN

## 5. Automação Determinística Local (`scripts/` — 0 Tokens)

- `scripts/router.py` — Monta o pacote mínimo de contexto para Qwen/Grokbot/Claude
- `scripts/decision_gate.py` — Camada JEV (System-1: `choice`, `bool_gate`, `score`) com backend local ou API
- `scripts/check_sla.py` — Verifica `state/slas.json` e dispara alertas de prazo sem usar LLM
- `scripts/build_book.py` — Compila o repositório `.md` (SSOT) em Livro unificado `.md`/`.docx` em `exports/`
- `scripts/usage_audit.py` — Detetive de uso: aponta rotinas frequentes demais, sem seen, sem parada, donos duplicados (`state/routines.json`)
- `scripts/seen.py` — Arquivo "seen" por rotina (só o novo; poda de 30 dias) em `state/seen/`
- `scripts/preflight.py` — Gates G1–G7 de ação externa, binário e fail-closed, com log de rejeitados

## 6. Estado Vivo (`state/` — Dinâmico, fora do Cache Estático)

- `state/gates.json` — Gates de progressão (Estado 0 ao Estado 4) e travas de receita
- `state/slas.json` — SLAs ativos com data limite e severidade
- `state/sprint_atual.json` — Micro-atividades lineares do Sprint atual
- `state/repo_queue.json` — Inventário oficial dos repositórios GitHub e fila priorizada de evolução
- `state/routines.json` — Inventário das rotinas do time no Grok Bot (preenchido pelo prompt M3; nunca inventado)
- `state/seen/` — Arquivos seen das rotinas (gitignored) · `state/forbidden_terms.example.txt` — modelo da lista local do gate G3

## 7. Topologia Oficial de Repositórios GitHub (`github.com/vinipinheiro42`) — Padrão Opção B

1. `MAIN` (Privado) — Repositório central (cérebro, objetivos Permaneo, CVs, planejamento, bots auto-contidos, scripts, SLAs).
2. Públicos de Jornada (slug limpo + topic `pub-journ-proj`) — Portfólio técnico FDE / FDDS / AI Eng / DE / DS / AE (ex: `ops-agent-mcp`, `agent-poc-to-prod`, `credit-policy-copilot`).
3. Públicos de Negócio (slug limpo + topic `pub-biz-proj`) — Projetos de empreendedorismo, marketing, varejo e iscas (ex: `kit-ceo-de-carreira`).
4. `PRIV-PROJ-[NOME]` (Privado) — Projetos confidenciais e estudos privados.
5. `WORKSPACE-BACKUP` (Privado) — Backup estruturado de notas e arquivos pessoais.
