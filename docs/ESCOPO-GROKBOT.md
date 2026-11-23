---
id: DOC-ESCOPO-GROKBOT
role: "Escopo temporário do Grok Bot (LinkedIn e X) a partir de 24/11/2026, até o reset da cota semanal"
updated_at: "2026-11-23"
status: "VIGENTE a partir de 24/11/2026 (instrução do Vini, 23/11/2026 20h53, America/Sao_Paulo)"
---

# Escopo do Grok Bot a partir de 24/11/2026

Fonte: instrução do Vini em 23/11/2026 às 20h53 (America/Sao_Paulo). Este arquivo descreve o que o Grok Bot faz nesta janela. Nenhuma configuração de bot foi alterada ao registrar isso.

O restante do planejamento fica a cargo de modelos fora do Grok Bot e chega ao time por atualização deste repositório. O VINI faz `git pull` no MAIN e executa só o que caiu nas três linhas abaixo.

## As três linhas

1. **Atuação principal.** Interações no LinkedIn (dono: BOT_COPY) e no X (dono: TWITTER): posts agendados com texto e horário pré-aprovados, e respostas no privado (DMs) e nos posts.
2. **Função secundária, mesmo que diária.** Listar os 10 usuários no X e no LinkedIn com mais engajamento e sugerir comentários pertinentes ao que eles postaram no dia.
3. **Comentário com link.** Procurar posts relacionados ao projeto ou ao artigo do dia e comentar na postagem com o link do repositório ou do artigo.

## Regras duras (seguem valendo)

- Todo texto de post, comentário ou DM precisa do sim do Vini ao texto exato, no chat do próprio bot dono do canal. Aprovação pedida por outro bot não vale.
- Depois que o texto exato e o horário forem aprovados nesse chat, uma rotina de disparo único pode publicar sozinha, sem perguntar de novo. Essa regra já está salva no BOT_COPY. No TWITTER, o Vini ainda precisa dizê-la no chat dele.
- A conexão com o X não publica artigo (só rascunho). Os artigos no X continuam sendo publicados pelo Vini. O bot pode deixar o rascunho pronto.
- Crescimento só ético: não infectar, não roubar, não prejudicar ninguém.
- Antes de publicar, o bot dono roda `scripts/preflight.py` (G1–G7, fail-closed) no momento da ação. Se o texto mudar depois do sim, precisa de sim novo. Se algo falhar (login do LinkedIn cair, artigo do X não estiver no ar, GIF recusado, novo "espere"), o bot não publica e pergunta ao Vini.

## Cota de uso até o reset

Medido em 23/11/2026: restavam 54,7% do limite semanal. Não há créditos extras. O limite zera na sexta, 27/11/2026, às 14h38 (America/Sao_Paulo). Se acabar antes, todos os bots param até a renovação.

Divisão combinada:

| Dia | Cota |
|---|---|
| Terça 24/11 | 15% |
| Quarta 25/11 | 15% |
| Quinta 26/11 | 15% |
| Sexta 27/11 até 14h38 | 9,7% |

Cuidados até o reset: conferir o uso na primeira mensagem do dia; não acordar outros bots para recado que não é urgente; deixar trabalho grande (pesquisa longa, documentos, varredura de vagas) para depois do reset, a menos que o Vini peça.

## Bots fora do escopo

Nesta semana, no Grok Bot, não acordar para trabalho novo (fora das três linhas) os bots abaixo. Este registro não cria, não pausa e não apaga rotina nem perfil:

- ESTRATEGISTA
- BOT_DEV
- BOT_QA
- BOT_CARREIRA e os demais bots de carreira
- BOT_GROWTH_FUNIL, BOT_SEC, BOT_V42_STORE

A rotina já agendada `escolha-do-produto-b2b-24-11-9h` (ESTRATEGISTA, 24/11 às 9h) permanece como estava: não foi alterada aqui. A rotina `relatorio-do-modo-sombra-do-decisor` (BOT_MAIN, 30/11 às 9h) também permanece. Qualquer outra frente (perfil do LinkedIn, Dual Boot/Qwen, candidaturas, oferta B2B, página, CLLT, etc.) entra pelo MAIN, não por recado entre bots no Grok Bot.

## O que o MAIN já delega ao Grok Bot em 24/11

Só o que já estava registrado em `state/routines.json` e no fechamento de 23/11, agora lido à luz das três linhas:

- **Linha 1 (agendado, texto já aprovado no chat do bot dono):** BOT_COPY publica o post curto do LinkedIn às 8h15 (`publicar-artigo-primeiro-dia-no-linkedin`, capa `cover-pt.gif`, com pre-flight). TWITTER divulga o artigo EN às 10h e o PT às 11h45, só se o artigo correspondente estiver no ar. O Vini publica à mão o artigo EN às 9h45 e o PT às 11h30. Respostas no privado e nos posts seguem a regra do texto exato aprovado no chat do dono.
- **Linha 2:** função diária a cumprir; ainda não há rotina ativa (a `listas-diarias` do TWITTER continua pausada, e este registro não a religa). Em 23/11 o TWITTER deixou uma lista e recomendou 4 respostas, à espera da escolha do Vini; no LinkedIn a lista do BOT_COPY estava incompleta (3 de 10). Comentários só depois do sim ao texto exato no chat do dono.
- **Linha 3:** ainda não há rotina nem texto aprovado no MAIN. O bot sugere; só comenta depois do sim ao texto exato, no chat do dono, com o link do repositório ou do artigo do dia.
