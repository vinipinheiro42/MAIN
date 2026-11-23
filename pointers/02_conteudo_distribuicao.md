---
id: PTR-02
module: conteudo_distribuicao
load_when: ["artigo", "post", "thread", "tiktok", "conteudo", "viral", "hook", "copy", "linkedin", "twitter", "x", "youtube", "ugc", "seo"]
depends_on: ["SOUL.md"]
owner_agent: "content_engine"
max_tokens: 1300
sla_review_days: 7
---

# PTR-02 — MOTOR DE CONTEÚDO & DISTRIBUIÇÃO (SUBPRODUTO DO TRABALHO REAL)

## 1. Regra de Sobrevivência (Aprendida com o Legado 04/11/2026)

- **Zero invenção de pauta do nada.** 100% do conteúdo nasce de 3 fontes que já existem:
  1. **Código/Commits reais** nos repos `PUB-JOURN-PROJ-*` e `PUB-BIZ-PROJ-*` (padrões de engenharia, bugs reais, benchmarks na RX 7800 XT);
  2. **45 artigos/aulas já curados** em `PESSOAL_MAIN_ANTIGO/INICIATIVAS/FORMACAO/ARTIGOS/` (JEV, Loops, AGH, RTK+Graphify, Uncle Bob, Workslop, Cerebras RAG);
  3. **Padrões arquiteturais sanitizados** (NUNCA dados/clientes/schemas internos da Permaneo).

## 2. Fases de Canais (Serialização Anti-Burnout)

| Fase | Canais Ativos | Cadência Mínima | Formato |
|---|---|---|---|
| **Fase 1 (Dias 1–30)** | **LinkedIn + X (Twitter)** (Primários) + **TikTok** (1 roteiro curto simples/sem) | 3 peças/sem (LinkedIn + Thread X derivada) + 1 TikTok curto | Texto estruturado, diagrama limpo, print de terminal/código, tela gravada 60s (sem superprodução) |
| **Fase 2 (Dias 31–60)** | + **YouTube** (1 vídeo longo/live técnica semanal -> vira curso/infoproduto) + **Newsletter** | +1 sessão 45–60 min/sem | Tela compartilhada + código rodando ao vivo + 10 ex-alunos/amigos no seeding inicial |
| **Fase 3 (Gate 3 — MRR >= R$ 5k)** | + **Instagram / Threads / Cortes / UGC IA** (com `t3code + Claude`) | Escala diária semi-automatizada | Cortes verticais + UGC + tráfego pago amplificando SÓ o que já viralizou no orgânico |

## 3. Regra de Tráfego Pago (Caixa R$ 0 -> Reserva R$ 200/mês)

- **PROIBIDO** impulsionar post que não teve tração orgânica.
- Só aplicar os R$ 200/mês depois de ter >= 10 peças orgânicas publicadas e **somente no Top 1–2 posts** com maior taxa de salvamento/visita ao perfil/clique no link.

## 4. Pipeline 1 -> 4 (Reaproveitamento Máximo)
Cada entrega técnica da semana gera automaticamente:
1. **1 Post/Artigo LinkedIn** (profundidade técnica + lição de negócio -> atrai recrutadores FDE e decisores B2B);
2. **1 Thread X (6–9 tweets)** (gancho forte + arquitetura + CTA binário);
3. **1 Roteiro TikTok/Reels (60–75s)** (direto ao ponto, sem edição pesada);
4. **1 Bloco de Documentação/Aula** (acumula material que vira o Degrau 1/2 da esteira de produtos).

## 5. Critério Anti-Workslop (Obrigatório Antes de Publicar)
Toda peça gerada com apoio do Qwen/Grokbot precisa ter:
- Pelo menos **1 dado real, comando, código ou trade-off concreto** (nunca conselho genérico de IA);
- **1 opinião forte/crítica** alinhada ao `SOUL.md`;
- **1 CTA binário fechado** (ex: "comenta 1 ou 2", "baixa o repo aqui").
