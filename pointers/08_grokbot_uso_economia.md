---
id: PTR-08
module: grokbot_uso_economia
load_when: ["uso", "limite", "cota", "pool", "rotina", "routine", "agenda", "gatilho", "trigger", "economia", "tokens", "custo", "grok bot", "grokbot", "medidor", "auditoria de uso"]
depends_on: ["PTR-05"]
owner_agent: "systems_architect"
max_tokens: 1400
sla_review_days: 14
---

# PTR-08 — GROK BOT: USO, POOL E ECONOMIA (REGRAS DO TIME)

> **Fontes principais:**
> - "Grok Bot Usage. Fix Everything That Burns Your Limit" (@Mahaximus_, https://x.com/Mahaximus_/status/2119435020704112933)
> - "12 Ways to Reduce Your Grok Bot Token Bill" (@maestrooth, https://x.com/maestrooth/status/2118061328405561352)
> - "GrokBot Token Usage: 10 steps" (@vartekxx, https://x.com/vartekxx/status/2119105285851656535)
> - os demais itens GB de `docs/ENRIQUECIMENTO-SALVOS-X.md`
>
> Os números abaixo são dos autores e servem de referência, não de fato medido no time do Vini.

## 1. O modelo mental

**Uso ≈ quantas vezes o bot roda × quanto ele carrega em cada execução.** Toda economia ataca um dos dois fatores. Na X Subscription, o chat do Grok, o Grok Bot e os agentes Cursor saem do **mesmo pool semanal** (@vartekxx). Por isso, o que um bot desperdiça falta para os outros.

## 2. Os 7 vazamentos e a regra do MAIN para cada um

| # | Vazamento | Regra do MAIN | Ferramenta |
|---|---|---|---|
| 1 | Rotina roda mais vezes que o dado muda | A agenda acompanha a velocidade do dado. Padrão: no máximo 3 execuções por dia. Use gatilho quando houver. | `scripts/usage_audit.py` |
| 2 | Rotina relê tudo a cada execução | Arquivo "seen": processar só o que é novo, podando a cada 30 dias | `scripts/seen.py`, `state/seen/` |
| 3 | Contexto nunca é limpo (chat longo relido a cada mensagem) | Uma conversa por tarefa. Ao trocar de assunto, nota de handoff + chat novo. Um autor relata que 84% dos tokens dele eram releitura do chat (@maestrooth). | `templates/HANDOFF_NOTE.md` |
| 4 | Ferramentas carregadas sem uso | Cada bot liga só os conectores do seu trabalho. A lista por bot está em MUDANCAS M2. | MUDANCAS M2 |
| 5 | Navegador quando existe plugin/API | Ordem: script local → API/conector → navegador como último recurso | AGENT.md §2 (Camada 0) |
| 6 | Bots duplicando trabalho | Um dono por fonte e por trabalho. "Não-faz" (anti-jobs) explícito no perfil de cada bot. | `bot.yaml: anti_jobs`, PTR-09 |
| 7 | Loop sem saída | Toda tarefa tem condição de parada + máximo de 3 tentativas + máximo de 3 handoffs | `templates/TASK_BRIEF.md`, `bot.yaml` |

## 3. Regras de rotina (valem para toda rotina nova ou alterada)

1. **Gatilho estreito > agenda.** Se existe evento ("email novo de X", "post novo em Y"), use o evento com filtro estreito.
2. **Agenda larga por padrão.** Diário ou dias úteis. "A cada hora" exige justificativa escrita no `state/routines.json`.
3. **Silêncio por padrão.** A rotina só fala quando há algo novo ou alguma ação pedida. "Nada novo" não vira mensagem.
4. **Saída que ninguém lê → pausar.** Rotina pausada custa zero.
5. **O botão "Test" faz trabalho real e consome.** Teste com escopo pequeno (1 item, 1 dia).
6. **Rotina nova entra no `state/routines.json`** com dono, fonte, cadência, arquivo seen e condição de parada.
7. **Rotinas concentradas num bot só** (proposta M4) para não espalhar contexto por todos.

## 4. Group chat e pool

- **Imposto do group chat:** cada bot que responde num grupo consome (@vartekxx). Regra: em grupo, só o bot citado responde, em 1 a 3 linhas, com ponteiro para o arquivo. Nada de colar resultado longo.
- **Aprovações não aparecem em group chat** e aprovações pedidas por outro bot ou rotina expiram em cerca de 10 min (artigo "5 Bots 1 Computer", @0xcloudvex, https://x.com/0xcloudvex/status/2114761069084160507). Ação que precisa de aprovação acontece no chat privado do bot dono.
- **Código pesado:** o conselho "não programe no Grok Bot, use um agente de código" (@maestrooth) **conflita** com o fato de que o agente Cursor sai do mesmo pool. A economia real vem do Hermes/Qwen local (R$ 0, `MEMORY.md` §3). Grok Bot e Cursor ficam para revisão e para o que o local não resolve.

## 5. Antes de um job grande

1. Confira o medidor de uso antes de começar ("12 Ways", @maestrooth). Regra do MAIN, ajustável: acima de 70% do pool com mais de 2 dias até o reset, divida o job ou passe para o local.
2. Escreva o brief com linha de chegada e condição de parada (`templates/TASK_BRIEF.md`).
3. Ações caras ou irreversíveis ficam em "ask first" nas Custom Rules (MUDANCAS M1).

## 6. Auditoria semanal (no dia do reset)

1. Atualize `state/routines.json` com o que os bots responderem ao prompt M3.
2. Rode `python scripts/usage_audit.py`. Cada item HIGH vira uma ação: pausar, alargar a agenda, trocar por gatilho ou fundir donos.
3. **Prova da economia:** pause o suspeito principal por 24h e compare o % semanal. Estimativa não é prova (@Mahaximus_).
4. Registre o resultado em 1 linha no `LESSONS.md`, se houver lição.
