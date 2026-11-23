---
id: PTR-03
module: funil_infoprodutos_b2b
load_when: ["funil", "ebook", "plataforma", "mentoria", "b2b", "consultoria", "vendas", "oferta", "preco", "abacatepay", "hotmart", "lancamento", "perpetuo", "afiliado"]
depends_on: ["PTR-02"]
owner_agent: "revenue_architect"
max_tokens: 1500
sla_review_days: 7
---

# PTR-03 — FUNIL DE PRODUTOS, PONTES ORGÂNICAS & MONETIZAÇÃO B2B

## 1. Arquitetura das 2 Trilhas + Pontes Orgânicas

Não misture comprador de ebook frio com decisor B2B no mesmo discurso. Use **2 portas de saída** a partir do mesmo topo de funil técnico:

| Degrau | Produto | Preço | Gateway | Quem Compra | Ponte Orgânica para o Próximo Degrau |
|---|---|---|---|---|---|
| **0 (Topo)** | Conteúdo + Repos `PUB-*` + Mini-Kit Gratuito (1 script + 1 `.md`) | **R$ 0** | GitHub / Lead Magnet | Devs, Analistas, Gestores | Entrega 1 vitória rápida em 10 min e mostra que falta o sistema completo |
| **1 (Entrada)** | **Starter Kit Executável + Playbook** (NÃO é ebook puro: PDF curto + ZIP com 3 `.md` + 2 scripts Python prontos) | **R$ 57 – R$ 75** | AbacatePay / Hotmart | Builders / Profissionais não-tech | No checkout + dentro do kit: *crédito de 100% do valor por 7 dias* para subir à Plataforma Anual |
| **2 (Core)** | **Plataforma V42 Agents & Playbooks** (biblioteca viva de `.md`s, MCPs, Skills, Loop/JEV, scripts 0-token, bots + gravações) | **R$ 997/ano** | AbacatePay / Hotmart | Implementadores & Profissionais | Quem tem os kits quer adaptar pro próprio cargo/empresa sem errar 3 meses -> aplica pra Mentoria |
| **3 (Mentoria)** | **Mentoria de Implementação** (sair com agentes/pipelines em produção em 8–12 sem) | **R$ 2.397/mês** Coletiva (máx. 8) / **R$ 2.997/mês** Individual (2x/sem) | AbacatePay / Contrato | Profissionais Sênior, Leads, Founders | Alunos gestores trazem a própria empresa para projeto fechado (Degrau 4) |
| **4 (B2B Direct)** | **Sprint Diagnóstico (R$ 2.5k–4k)** -> **Consultoria / Retainer FDE B2B** | **R$ 10.000+ / mês** | Contrato PJ / NF | Diretores / Founders (B2B) | Entrada DIRETA pelo LinkedIn/estudos de caso técnicos (sem precisar comprar Degrau 1!) |

## 2. Foco Vertical B2B (Disciplina de Nicho)

Você listou 9 áreas não-tech/tech (produtos, marketing, comercial, jurídico, financeiro/fintechs, startups, engenharia, medicina, audiovisual). **Atacar 9 ao mesmo tempo dilui toda a autoridade.**

- **Fase 1 B2B (Primeiros 2 contratos pagos):**
  1. **Financeiro / Fintechs / Seguros** (prova irrefutável: Santander Brasil + Santander Asset + BMG).
  2. **Marketing / Comercial / Infoprodutos / E-commerce** (prova irrefutável: operação atual no Grupo Permaneo + V42).
- **Fase 2 B2B (Após 2 cases documentados):** expandir horizontalmente para **Startups, Jurídico, Engenharia, Medicina e Audiovisual** vendendo o *mesmo motor de agentes/dados* com camada de domínio trocada.

## 3. Gatilhos de Validação Antes de Construir (Anti-Desperdício)

- **Regra do Pré-Pedido:** nunca grave 40 aulas antes de vender. Valide o Degrau 1 com página simples (AbacatePay) + lista de espera/pré-venda de 10 compradores (incluindo rede de ex-alunos/audiência orgânica).
- **Regra da Mentoria:** 1 turma coletiva cheia (8 × R$ 2.397 = **R$ 19.176/mês**) já paga toda a infraestrutura (DeepSeek + t3code + Claude + 2º SSD + caixa pra V42 Store).
- **Programa de Afiliados:** 35% no Degrau 1 e 2 para compradores/ex-alunos; 10% por 3 meses em indicação B2B fechada.

## 4. Gates de Reinvestimento de Caixa (Regra Rígida)
- **Caixa acumulado >= R$ 1.500 (Gate 2):** liberar até 15% do lucro líquido mensal em tokens **DeepSeek API**.
- **MRR >= R$ 5.000 por 2 meses (Gate 3):** liberar **`t3code` + assinatura Claude** + 2º SSD NVMe na MSI B650.
