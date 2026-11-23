---
id: PTR-09
module: time_de_bots_protocolo
load_when: ["time de bots", "handoff", "delegar", "contrato", "brief", "revisor", "revisao", "veredito", "pre-flight", "preflight", "aprovacao", "group chat", "bot novo", "criar bot", "template", "meta", "harness", "loop", "graph"]
depends_on: ["AGENT.md", "PTR-08"]
owner_agent: "orchestrator"
max_tokens: 1600
sla_review_days: 14
---

# PTR-09 — PROTOCOLO DO TIME DE BOTS (DONO, HANDOFF, REVISÃO, PRE-FLIGHT)

> **Fontes:** artigos salvos no X e citados em `docs/ENRIQUECIMENTO-SALVOS-X.md` (GB e AE):
> - "5 Bots, 1 Computer" (@0xcloudvex, https://x.com/0xcloudvex/status/2114761069084160507)
> - "Grok AGENTS" (@Bober_smart, https://x.com/Bober_smart/status/2091901718061531571)
> - "GrokBot Templates" (@0xRafy, https://x.com/0xRafy/status/2106098144320582134)
> - "6 Grok Bots Do the Work" (@s4yonnara, https://x.com/s4yonnara/status/2119777956423700863)
> - "CTO, CMO, CFO" (@luanzeraAI, https://x.com/luanzeraAI/status/2124657469288812640)
> - "Pre-Flight: 7 Gates" (@Corki_0x, https://x.com/Corki_0x/status/2117908942013481205)
> - "Harness, Loops, Graphs" (@m4lkxx, https://x.com/m4lkxx/status/2114338456750997922)
> - "Automate Anything" (@poteto, https://x.com/poteto/status/2123159537016533493)

## 1. Fatos do ambiente (não são opinião)

- **Todos os bots do Vini dividem um computador** (o box). Arquivo, login e ferramenta instalados por um bot ficam visíveis para todos. **Um bot é uma fronteira de trabalho, não de segurança.** Apagar um bot não limpa os arquivos nem os logins dele.
- **Aprovação pedida por outro bot ou rotina expira em cerca de 10 min**, e **group chat não mostra card de aprovação**. Ação que precisa de aprovação acontece no chat privado do bot dono, com o Vini presente.
- **Permissão é parede, não instrução** (@m4lkxx). O que um bot não pode fazer se garante tirando o conector ou a ferramenta dele (MUDANCAS M2), não escrevendo "não faça" no prompt.

## 2. Regra de ouro: uma tarefa, um dono, um caminho de saída, um revisor

| Campo | Regra |
|---|---|
| Dono | Um bot por tarefa e por fonte. O "não-faz" (`anti_jobs` em `bot.yaml`) impede o vizinho de pegar o trabalho. |
| Caminho de saída | Cada entrega vai para um arquivo combinado (ex.: `content/drafts/<id>.md`). O handoff passa o **caminho**, não o conteúdo colado. |
| Revisor | Quem escreve não revisa. O REVISOR (ou `BOT_QA`) dá **veredito**: PASS, FAIL ou BLOCKED, com evidência. |
| Rodadas | No máximo 2 rodadas de revisão. Na 3ª, a decisão vai para o Vini em 3 bullets (`HEARTBEAT.md` §4). |
| Handoffs | No máximo 3 por tarefa (`max_handoffs: 3`). Passou disso, é sinal de escopo mal definido: pare e escale. |

## 3. Contrato de tarefa (brief) — `templates/TASK_BRIEF.md`

Todo pedido entre bots (e do Vini para um bot, em tarefa maior que 1 resposta) leva:
1. **Resultado** observável ("o que existe quando acabar"), escrito ANTES de começar ("escreva o check antes do código", @m4lkxx).
2. **Fontes** permitidas e **escopo** (o que pode e o que não pode tocar).
3. **Restrições**: confidencialidade, sem nomes de empregadores em público, sem inventar números.
4. **Formato** e caminho de saída.
5. **Condição de parada**: quando parar e pedir aprovação; máximo de 3 tentativas.

Para metas de negócio (não tarefas), use `templates/GOAL_CONTRACT.md`: número + prazo, como medir, limites, quando acaba e prova de entrega (@luanzeraAI).

## 4. Loop com memória de tentativa (Esperado vs. Visto)

- Cada tentativa registra **ESPERADO** e **VISTO** (`templates/REVIEW_VERDICT.md`). **Mesmo resultado duas vezes = pare**: repetir não vai mudar nada (@m4lkxx).
- **Passos determinísticos viram código** (`scripts/`), e **o que passou fica congelado**: não refazer etapa aprovada sem motivo novo.
- **Todo erro que se repete vira check** (lint, teste, gate em `scripts/preflight.py`), não um parágrafo a mais no prompt (setup pstack, item GB do catálogo).
- **Paralelismo só quando a seta permite.** Para cada dependência, pergunte se o passo B pode começar antes de A acabar. Se puder, cada worker trabalha em sua própria pasta (sem dois bots escrevendo o mesmo arquivo).

## 5. Nível de aprovação = custo de desfazer

| Custo de desfazer | Exemplo | Aprovação |
|---|---|---|
| Zero (reversível, interno) | Rascunho, arquivo no box, branch, PR | Bot decide sozinho |
| Baixo | Rotina nova silenciosa, pausar rotina | Bot faz e avisa em 1 linha |
| Alto / público / dinheiro | Post no X/LinkedIn, email, candidatura, compra, apagar dado externo | **Sim do Vini ao texto exato, no chat do bot dono do canal** + `scripts/preflight.py` = GO |

## 6. Pre-flight de ação externa — `templates/PREFLIGHT.md` + `scripts/preflight.py`

O gate é binário, não um score. Ele falha fechado: um erro ou um timeout dá NÃO. A checagem roda no momento da ação, e as rejeições ficam registradas para a auditoria semanal (@Corki_0x, método adaptado; o contexto original era trading e não foi aplicado). Gates do MAIN:
- **G1** aprovação no chat certo.
- **G2** destino e conta ativa conferidos ("um perfil de navegador por conta", @luanzeraAI).
- **G3** sem termos confidenciais.
- **G4** sem CPF, senha, token ou cartão.
- **G5** números checados.
- **G6** salário, proposta ou relocation só com sim explícito.
- **G7** fail-closed.

## 7. Antes de criar um bot novo

1. **Uma skill nova resolve?** "Skills são prompts; bots são executores de skills orientados a eventos". Prefira skill a bot.
2. Procure um template pronto (diretório comunitário do Grok Bot, grok-bot.directory, item GB-28 do catálogo) e adapte; não importe nada sem o ok do Vini.
3. Escreva o perfil com `templates/BOT_BRIEF.md`: trabalho, não-faz, conectores mínimos, rotinas (silenciosas por padrão), healthcheck semanal que fica quieto quando está tudo certo.
4. Faça um piloto com tarefas reversíveis antes de liberar qualquer ação externa (@Bober_smart).

## 8. Canais públicos: olhos, mãos e cérebro

"O X são os olhos, a ferramenta de postagem são as mãos, e você é o cérebro" (@s4yonnara). Os bots de conteúdo pesquisam e rascunham. Nada vai ao ar sem o sim do Vini, e ninguém automatiza resposta a estranhos.
