---
id: PTR-04
module: v42_store_ecommerce
load_when: ["ecommerce", "v42", "store", "mercado livre", "shopee", "shein", "tiktok shop", "fornecedor", "alibaba", "aliexpress", "dropshipping", "galpao", "impressora 3d", "roupas", "varejo", "tendencia"]
depends_on: ["PTR-03"]
owner_agent: "retail_data_operator"
max_tokens: 1300
sla_review_days: 14
---

# PTR-04 — FRENTE 2: V42 STORE, CIÊNCIA DE DADOS NO VAREJO & ROADMAP FÍSICO

## 1. Realidade de Caixa (R$ 0 Hoje) -> Estratégia Zero-CAPEX Primeiro

Com **caixa R$ 0**, comprar estoque físico na Semana 1 é suicídio financeiro. A **V42 Store** começa como um **Laboratório Público de Ciência de Dados aplicada a Varejo** — monetizando a inteligência *antes* de imobilizar capital em caixa de papelão.

## 2. Progressão Serializada em 4 Fases (1 Canal por Vez)

### Fase A — Inteligência de Tendências & Zero-CAPEX (Dias 31–60 | Após Gate 1)
- **Projeto público (`PUB-BIZ-PROJ-01-retail-trend-radar`):** script Python local (0 tokens no scraping/cálculo) que monitora tendências internacionais (EUA/China -> atraso de 3–12 meses no Brasil), curvas de preço, avaliação de concorrentes e margem estimada.
- **Canal único inicial:** **TikTok Shop (Programa de Afiliados/Creator)** ou **Mercado Livre (Afiliados/Drop validado)** — zero estoque, testa copy, gancho, UGC e conversão real com risco R$ 0.
- **Dupla monetização:** todo achado de dados vira conteúdo ("Como usei Python + IA para achar 3 nichos de margem >40% antes de viralizarem no Brasil") -> alimenta a esteira de infoprodutos/B2B!

### Fase B — Primeira Loja Própria Enxuta (Dias 61–120 | Após Gate 2 com Caixa Positivo)
- **Canal único de operação própria:** escolher **1 marketplace** (Mercado Livre *ou* Shopee) baseado nos dados reais da Fase A.
- Testar 3–5 SKUs validados via fornecedor nacional/drop antes de importar (Alibaba/AliExpress).
- Automatizar atendimento, resposta de perguntas/feedbacks e monitoramento de buy-box/preço com scripts determinísticos + Qwen/DeepSeek (reduzindo custo operacional a quase zero).

### Fase C — Expansão Multicanal (Após Gate 3 | Margem Líquida Validada)
- Replicar os SKUs vencedores (Curva A) para os demais canais (Shopee, Shein, TikTok Shop) usando ERP/integrador único.
- Escalar criativos UGC e tráfego pago SOMENTE nos SKUs com ROAS comprovado.

### Fase D — Galpão, Produção Própria (Roupas + Impressão 3D) & Logística (BLOQUEADO ATÉ GATE 4)
- **Condição física de desbloqueio (`GATE-4`):**
  1. Caixa reservado >= **6 meses de custo fixo** (aluguel galpão + energia + máquinas + capital de giro);
  2. Pelo menos **3 linhas de produto com demanda provada** vendendo consistentemente nos marketplaces;
  3. Unit economics fechado (custo de impressão 3D/confecção + embalagem + frete + taxa marketplace + devolução <= 65% do preço final).
- *Regra de mentor:* até atingir o Gate 4, **NÃO** gastar horas cotando galpão, máquina de costura ou fazenda de impressoras 3D. Use os dados dos marketplaces para descobrir *o que* tem demanda antes de montar a fábrica.
