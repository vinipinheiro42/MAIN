# `vinipinheiro42/MAIN` — Ecossistema Central & Kit Portável de Bots

> Repositório central (**privado**) de planejamento, governança, memória, SLAs, scripts determinísticos (0 tokens) e **bots auto-contidos** para **Grokbot**, **Hermes (Qwen local no Omarchy)**, **Claude Code** e **Antigravity**.

## Estrutura de Bots (Pull Direto por Grokbot & Hermes)

Cada pasta dentro de `bots/` é um **bot especialista auto-contido** (padrão AGH: `AGENT.md` + `bot.yaml`) que consome apenas seus ponteiros autorizados em `pointers/` (economia >80% de tokens, zero duplicação de verdade):

| Pasta do Bot | Papel | Runtime Padrão | Ponteiros Autorizados |
|---|---|---|---|
| `bots/BOT_MAIN/` | Orquestrador, Mentor Agressivo & SLA Watchdog | Grokbot Premium / Qualquer Harness | `PTR-01..06` (via `router.py`) |
| `bots/BOT_CARREIRA/` | FDE, FDDS, AI Eng, DE, DS, AE (Estudos, Papers, 6 CVs, Entrevistas) | Grokbot + Qwen 14B | `PTR-01`, `PTR-05` |
| `bots/BOT_COPY/` | LinkedIn, X/Twitter, Threads, TikTok, Newsletter, Hooks & Anti-Workslop | Grokbot Premium | `PTR-02`, `PTR-03` |
| `bots/BOT_DEV/` | Código End-to-End, Docker, CI/CD, Scripts Determinísticos (Omarchy) | **Hermes / Qwen 14B Local (R$ 0)** | `PTR-01`, `PTR-05` |
| `bots/BOT_QA/` | Auditoria `Esperado vs. Real`, JEV Gate, Pytest & Circuit Breaker 3x | **Qwen 1.5B/14B Local + `decision_gate.py`** | `PTR-05`, `PTR-06` |
| `bots/BOT_SEC/` | Segurança, Secrets, Compliance/NDA Permaneo, Isolamento de Cota | **Scripts Locais + Qwen 14B Local** | `PTR-05`, `PTR-06` |
| `bots/BOT_GROWTH_FUNIL/` | Funil de 2 Trilhas, Pontes Orgânicas, Starter Kit, Plataforma, Mentoria & B2B | Grokbot Premium | `PTR-03`, `PTR-02` |
| `bots/BOT_V42_STORE/` | V42 Store (Zero-CAPEX -> Dados de Varejo -> Marketplaces -> Gate 4 Galpão) | Qwen 14B Local + Scripts | `PTR-04`, `PTR-03` |

## Comandos Rápidos (0 Tokens — Python 3 Stdlib)

```bash
# 1. Briefing matinal + checagem de SLAs + barras de progresso dos Gates
python scripts/check_sla.py

# 2. Montar contexto mínimo (ponteiros) para um bot específico
python scripts/router.py --bot BOT_DEV "implementar loop qa com pytest"
python scripts/router.py --bot BOT_COPY "criar post linkedin e thread x" --bundle

# 3. Testar o motor JEV System-1 (offline / Ollama local / JEV API)
python scripts/decision_gate.py --self-test

# 4. Compilar todo o SSOT Markdown em um Livro único (+ .docx via pandoc)
python scripts/build_book.py
```

## Primeiro Uso (Git Push Inicial)

```bash
cd MAIN
git init -b main
git add .
git commit -m "feat: bootstrap MAIN portable bot harness, ecosystem master plan and article 01"
git remote add origin git@github.com:vinipinheiro42/MAIN.git
git push -u origin main
```
