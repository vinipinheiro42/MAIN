---
id: PTR-07
module: segundo_cerebro
load_when: ["segundo cerebro", "second brain", "wiki", "obsidian", "knowledge", "memoria", "nota", "fonte", "conhecimento", "pesquisa", "resumo"]
depends_on: ["MEMORY.md"]
owner_agent: "knowledge_curator"
max_tokens: 1100
sla_review_days: 30
---

# PTR-07 — SEGUNDO CÉREBRO DO MAIN (RAW → WIKI → OUTPUT)

> **Fonte:** artigos salvos no X: "Second Brain Engineering" (@tsukiema_, https://x.com/tsukiema_/status/2112947495059743047), "Second Brain Claude+Obsidian" (@imryven, https://x.com/imryven/status/2115046979659055476) e os itens SB de `docs/ENRIQUECIMENTO-SALVOS-X.md`. Este arquivo adapta o método à estrutura do MAIN, sem copiar os artigos.

## 1. O que já existia e o que faltava

| Peça do método | No MAIN antes | Ajuste aplicado |
|---|---|---|
| Regras do sistema (o "rulebook") | `AGENT.md` + `VALUES.md` | Mantido. A regra de memória foi acrescentada (§4). |
| Fatos verificados | `MEMORY.md` (fatos do operador) | Mantido como fonte de verdade sobre o Vini. |
| Índice para o modelo achar as coisas | `00_SUMARIO.md` + `router.py` | Mantido. `knowledge/wiki/INDEX.md` foi criado para os temas. |
| **raw/** (fonte bruta, nunca editada) | não existia; os resumos se misturavam com as regras | `knowledge/raw/`: só índices de fonte (link, data, autor) |
| **wiki/** (síntese escrita pelo modelo) | espalhado em pointers | `knowledge/wiki/`: uma página por tema, cada fato com fonte |
| **output/** (entrega pronta) | `content/`, `exports/` | Continua em `content/` (textos) e `exports/` (gerados) |
| Lições (o que deu errado) | `pointers/06` (pós-mortem longo) | `LESSONS.md` com até 20 linhas, lido no boot. O detalhe continua no PTR-06. |

## 2. Regras de escrita (valem para todo bot que escreve em `knowledge/`)

1. **Nunca editar `raw/`.** Fonte nova entra como linha nova; a antiga fica como está.
2. **Todo fato no `wiki/` leva fonte + data da última checagem:** `(fonte: <link>, checado: AAAA-MM-DD)`.
3. **Conflito não se resolve em silêncio.** Quando duas fontes discordam, marcar `> CONFLITO:` com as duas e deixar a decisão para o Vini ou para o bot dono do tema.
4. **Número de terceiros não é fato do MAIN.** Fica entre aspas, com o autor. Antes de ir para conteúdo público, passa pelo gate G5 de `scripts/preflight.py`.
5. **Texto bruto de terceiros não vai para o Git.** O repo guarda link + resumo próprio. O bruto fica no box.
6. **Uma página por tema, curta.** Se passar de ~150 linhas, quebrar e linkar no `INDEX.md`.

## 3. Ciclo semanal (junto do ritual de domingo do `HEARTBEAT.md`)

- **Ingerir:** fontes novas (salvos do X, artigos lidos, aulas) viram linhas em `knowledge/raw/<origem>-<data>.md`.
- **Compilar:** o bot dono do tema atualiza a página do `wiki/` só com o que mudou. Lê o diff, não o tema inteiro.
- **Lint:** procurar fato sem fonte, checagem com mais de 90 dias e conflito aberto. O resultado vai para o resumo semanal com no máximo 5 linhas.
- **Produzir:** conteúdo e entregas saem de `wiki/` para `content/` e citam a página de origem.

## 4. O que vai em cada lugar (para não inflar contexto)

| Tipo de informação | Lugar | Por quê |
|---|---|---|
| Preferência estável do Vini (tom, horários, regras) | Memória do bot / `SOUL.md` | É curta e vale em toda sessão. |
| Fato verificado sobre o Vini (CV, hardware, caixa) | `MEMORY.md` | Fonte de verdade. |
| Conhecimento de domínio (método, mercado, técnica) | `knowledge/wiki/` | Só é carregado quando o tema aparece. |
| Estado de rotina (o que já foi visto) | `state/seen/` (`scripts/seen.py`) | Arquivo e não memória: a rotina não relê tudo. |
| Lição operacional | `LESSONS.md` (≤ 20 linhas) | Evita repetir o erro sem carregar o pós-mortem inteiro. |

**Regra:** a memória do bot guarda preferências, não dumps. Conteúdo longo vai para arquivo, e a memória guarda só o caminho.
