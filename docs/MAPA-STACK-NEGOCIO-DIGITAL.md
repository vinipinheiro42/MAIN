---
id: DOC-MAPA-STACK-NEGOCIO
role: "Mapa dos termos do post 'Claro que eu tô cansada…' → o que é, onde cabe nos negócios do Vini, bot dono, próximo passo"
updated_at: "2026-11-23"
load_when: ["mrr", "churn", "ltv", "cac", "cpa", "roas", "roi", "funil", "copywriting", "meta ads", "pixel", "cbo", "criativos", "teste ab", "micro-saas", "vibe coding", "trafego"]
---

# Mapa da stack de negócio digital

**Fonte:** post de @gothkuran, 21/11/2026, https://x.com/gothkuran/status/2124251884391178508. Lido via API em 23/11/2026. Ele não está nos salvos do Vini: foi achado por busca a pedido dele.

> Texto do post: "Claro que eu tô cansada, tenho que entender de claude code, engenharia de prompts, vibe coding, APIs, automações, micro-SaaS, MRR, churn, LTV, CAC, CPA, ROAS, ROI, funil de vendas, copywriting, tráfego direto, Meta Ads, pixel, CBO, criativos, testes A/B... e ainda manter a calma"

**Como ler.**
- **Onde cabe** usa as frentes do `ECOSYSTEM_MASTER.md`: Frente 1 é Carreira (FDE/FDDS/AI Eng). Frente 2 é Negócios, que inclui conteúdo, esteira digital (Starter Kit, Plataforma, Mentoria, B2B) e V42 Store.
- **Bot dono** usa os nomes do time vivo em 23/11/2026 (`bot-diff`) e, entre parênteses, o bot equivalente do repo. Se o time mudar, vale o dono atual da frente.
- **Próximo passo** respeita os gates de `state/gates.json`. Com caixa livre de R$ 0, tráfego pago só entra depois de o orgânico estar provado (`MEMORY.md` §3).
- Nenhum número abaixo é meta inventada. Onde há valor, ele vem do próprio MAIN.

## 1. Construção (produto e automação)

| Termo | O que é | Onde cabe nos negócios do Vini | Bot dono | Próximo passo |
|---|---|---|---|---|
| Claude Code | Agente de código em terminal que lê o repo, edita, roda testes e abre PR | Frente 1 (portfólio FDE) e o BOT_DEV. O MAIN trava assinatura nova até o Gate 3: o equivalente hoje é Hermes/Qwen local | DEV DE BOTS (BOT_DEV) | Manter Hermes/Qwen como padrão; reavaliar no Gate 3 (`AGENT.md` §2) |
| Engenharia de prompts | Escrever instruções, contexto e formato de saída para o modelo acertar de primeira | Toda a operação: briefs (`templates/TASK_BRIEF.md`), skills e perfis de bot | DEV DE BOTS | Toda instrução de bot nova sai do `templates/BOT_BRIEF.md` |
| Vibe coding | Construir software descrevendo em linguagem natural e aceitando o código gerado com pouca revisão | Útil para protótipo e para isca de conteúdo. Proibido em entrega B2B sem teste (`VALUES.md`, Loop QA) | DEV DE BOTS + REVISOR (BOT_QA) | Usar só em protótipo; tudo que vai para cliente passa por `decision_gate.py` e testes |
| APIs | Interfaces para um sistema conversar com outro (dados, pagamentos, IA) | Base do FDE e da oferta B2B: integrar o sistema do cliente com IA | FORWARD DEPLOYED ENGINEER (carreira) / DATA ENGINEER | Projetos P0 do portfólio (`ops-agent-mcp`, `agent-poc-to-prod` em `state/repo_queue.json`) com integração real documentada |
| Automações | Fluxos que rodam sozinhos (n8n, scripts, rotinas de bot) | Oferta B2B (automação para negócio local) + operação interna (`scripts/`) | AUTOMAÇÃO B2B (oferta) / DEV DE BOTS (interno) | Toda automação nova tem dono, condição de parada e arquivo seen (PTR-08) |
| Micro-SaaS | Software pequeno, nichado, vendido por assinatura | Candidato futuro da Frente 2. O MAIN hoje prioriza Starter Kit → Plataforma (`ECOSYSTEM_MASTER.md` §5) | ESTRATEGISTA (BOT_GROWTH_FUNIL) | Pergunta aberta ao ESTRATEGISTA (relatório): micro-SaaS entra antes ou depois da Plataforma? |

## 2. Métricas de negócio

| Termo | O que é | Onde cabe | Bot dono | Próximo passo |
|---|---|---|---|---|
| MRR | Receita recorrente mensal (assinaturas ativas × preço) | Gate 3 do MAIN: MRR ≥ R$ 5.000 por 2 meses (`state/gates.json`) | ESTRATEGISTA (leitura: MONETIZAÇÃO) | Definir a fonte do número (plataforma de pagamento) antes da 1ª venda recorrente |
| Churn | % de clientes ou receita que cancela num período | Plataforma anual, mentoria, retainer B2B | ESTRATEGISTA | Só medir quando existir base recorrente; até lá, registrar o motivo de cada cancelamento |
| LTV | Receita total esperada de um cliente durante a relação | Justifica a escada (Starter Kit → Plataforma → Mentoria → B2B) | ESTRATEGISTA | Calcular com dados reais depois das primeiras vendas; não estimar sem base |
| CAC | Custo para adquirir um cliente (marketing + vendas ÷ clientes novos) | Hoje o CAC é tempo (orgânico). Vira dinheiro quando entrar tráfego pago | ESTRATEGISTA | Registrar horas e canal de origem de cada cliente desde o 1º |
| CPA | Custo por ação (lead, compra) num canal de anúncio | Só existe com tráfego pago | TRÁFEGO PAGO (BOT_GROWTH_FUNIL) | Bloqueado até o gate de tráfego (orgânico provado + reserva de até R$ 200/mês) |
| ROAS | Receita gerada ÷ gasto em anúncio | Idem: mede o anúncio, não o negócio | TRÁFEGO PAGO | Idem |
| ROI | (Retorno − investimento) ÷ investimento, para qualquer gasto | Escada de reinvestimento por gates (DeepSeek no Gate 2, teto de 15% do lucro) | ESTRATEGISTA / DECISOR | Toda compra nova de ferramenta passa por ROI explícito no GOAL_CONTRACT |

## 3. Venda e conteúdo

| Termo | O que é | Onde cabe | Bot dono | Próximo passo |
|---|---|---|---|---|
| Funil de vendas | Caminho do desconhecido até o cliente (atenção → interesse → compra → recompra) | `ECOSYSTEM_MASTER.md` §5: duas trilhas (Builder/Carreira e Decisor/B2B) com pontes | ESTRATEGISTA (BOT_GROWTH_FUNIL) | Gate 0: publicar o Artigo #1, que é o topo do funil |
| Copywriting | Texto que leva o leitor a uma ação | Posts, página do Starter Kit, propostas B2B | TWITTER / LINKEDIN (BOT_COPY), com a skill `guia-de-voz` | Todo texto público passa pelo `scripts/preflight.py` + sim do Vini no chat do bot do canal |
| Tráfego direto | Termo ambíguo. Em analytics, são visitas sem origem identificada (digitou o link). No mercado de infoprodutos, é anúncio levando direto à página de venda, sem lançamento | Não se aplica agora: oferta e orgânico vêm antes | ESTRATEGISTA | Perguntar ao autor qual sentido usa só se o tema virar conteúdo; não é prioridade |
| Criativos | As peças do anúncio ou post (imagem, vídeo, texto) | Conteúdo orgânico agora; anúncio depois | CONTEÚDO EM VÍDEO / TWITTER / LINKEDIN | Reaproveitar os 45 artigos legados (`MEMORY.md` §4) como matéria-prima |
| Testes A/B | Comparar duas versões mudando uma variável, para ver qual converte mais | Hooks de post (orgânico), página de venda e assunto de email | TWITTER / LINKEDIN + REVISOR | Testar hooks no orgânico (custo zero) registrando versão e resultado; sem número de amostra inventado |

## 4. Tráfego pago (todos bloqueados pelo gate de caixa)

| Termo | O que é | Onde cabe | Bot dono | Próximo passo |
|---|---|---|---|---|
| Meta Ads | Plataforma de anúncios do Facebook/Instagram | Frente 2, depois do orgânico provado | TRÁFEGO PAGO (BOT_GROWTH_FUNIL) | Bloqueado: nenhum gasto sem gate e sem sim do Vini |
| Pixel | Código na página que avisa ao Meta quem visitou ou comprou, para medir e otimizar | Página do Starter Kit quando existir | TRÁFEGO PAGO (instalação: DEV DE BOTS) | Na hora de montar a página, já instalar e medir (custo zero), mesmo sem anúncio |
| CBO | Campaign Budget Optimization: o Meta distribui o orçamento entre conjuntos de anúncios | Só com tráfego pago ativo | TRÁFEGO PAGO | Bloqueado |

## 5. Leitura de mentor

O post lista 21 assuntos ao mesmo tempo. Pelo `SOUL.md`, isso é a armadilha da meta-produtividade. No MAIN, a ordem é:
1. **Agora (Gate 0/1):** engenharia de prompts, APIs, automações, Claude Code/Hermes (portfólio FDE), copywriting e funil no orgânico.
2. **Na 1ª venda:** CAC em horas, origem de cada cliente, pixel instalado.
3. **Com receita recorrente:** MRR, churn, LTV.
4. **Com orgânico provado e gate de caixa:** Meta Ads, CPA, ROAS, CBO, criativos pagos e A/B de anúncio.
