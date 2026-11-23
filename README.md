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

# 5. Auditoria de uso das rotinas do time (state/routines.json)
python scripts/usage_audit.py

# 6. Pre-flight antes de qualquer post/envio/candidatura (binário, fail-closed)
python scripts/preflight.py --text-file content/drafts/<id>.md --channel x --owner-bot TWITTER \
  --approved-in TWITTER --approval-ref "<msg>" --target @vinipinheiro42 --target-confirmed --facts-checked

# 7. Arquivo seen de uma rotina (processa só o novo)
python scripts/seen.py filter vagas-fde id1 id2 && python scripts/seen.py add vagas-fde id1 id2

# 8. Decision gate em modo sombra (registra, não libera sozinho)
python scripts/decision_gate.py --self-test --shadow --log state/decision_log.jsonl
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

## Protocolo do Time e Economia (23/11/2026)

Regras novas que saíram dos salvos do X (fontes em `docs/ENRIQUECIMENTO-SALVOS-X.md`):
- `pointers/07` segundo cérebro · `pointers/08` uso e pool do Grok Bot · `pointers/09` protocolo do time (dono, handoff, revisão, pre-flight).
- Modelos em `templates/` · lições curtas em `LESSONS.md` · conhecimento em `knowledge/`.
- O que exige mudança nos bots vivos do Grok Bot está em `docs/MUDANCAS-PARA-APLICAR.md` e não é aplicado por este repo.
- **Portabilidade:** integrações vivem em MCP/CLI e nos arquivos do MAIN, não presas a um harness (catálogo GB, "OpenBot ou agentes.chat?").

