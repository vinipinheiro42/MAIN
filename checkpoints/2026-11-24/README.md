# Checkpoint dos bots — 24/11/2026

Fuso: America/Sao_Paulo. Snapshot dos 25 bots (e do grupo) vivos no Grok Bot neste dia.

Escopo deste pacote, a pedido do Vini: só o checkpoint e o commit. Cada bot tem exatamente três arquivos:

- `bots/<nome>/profile.json` — perfil ao vivo (nome, description, title, avatar, serverId, harness, namedBy quando houver)
- `bots/<nome>/settings.json` — settings ao vivo
- `bots/<nome>/estado.md` — metadados do snapshot e o estado operacional só quando havia fato confirmado

Não entram neste checkpoint: skills, custom rules, conectores, memória/store, anexos, corpos de automações, artefatos de `/workspace`, nem o `HANDOFF.md`.

Repositório de destino: `vinipinheiro42/MAIN` (privado). Sem segredos, tokens, senhas ou CPF. O perfil do RAG CORPORATIVO menciona o empregador atual: isso ficou no snapshot para restaurar o perfil com fidelidade, e não deve ir para conteúdo público.

Quatro bots já apagados constam só como id em `deleted-agents.json` (sem perfil/settings) e ficaram de fora: `28d9b4b8-479e-40e2-b6df-c1a15fb2d744`, `1b2173ab-2e20-4039-bc81-bd15c4e99427`, `e809fbd2-32b0-48f1-a160-5eb93adf0572`, `2b3ce667-6688-4bcf-a8c7-93638a0c9efe`.

## Índice

| Pasta | Nome | id | description | Arquivos |
|---|---|---|---|---|
| AI_ENGINEER | AI ENGINEER | `4b53d961-d7ed-495d-94aa-06abe8028514` | vazia | [`bots/AI_ENGINEER/`](bots/AI_ENGINEER/) |
| ANALYTICS_ENGINEER | ANALYTICS ENGINEER | `680b789b-2366-4f18-a245-94d0e9e00a8a` | vazia | [`bots/ANALYTICS_ENGINEER/`](bots/ANALYTICS_ENGINEER/) |
| AUTOMACAO_B2B | AUTOMAÇÃO B2B | `ba2d9681-7033-4a12-9069-9d02e3711446` | sim | [`bots/AUTOMACAO_B2B/`](bots/AUTOMACAO_B2B/) |
| BOT_CARREIRA | BOT_CARREIRA | `58ab111a-a9ea-4457-b2c4-4e757c739f94` | sim | [`bots/BOT_CARREIRA/`](bots/BOT_CARREIRA/) |
| BOT_COPY | BOT_COPY | `b63133c0-5fcf-4c05-8439-1dcf30cc0473` | sim | [`bots/BOT_COPY/`](bots/BOT_COPY/) |
| BOT_DEV | BOT_DEV | `341cb259-14e4-47f9-9a4b-674277aaeb11` | sim | [`bots/BOT_DEV/`](bots/BOT_DEV/) |
| BOT_GROWTH_FUNIL | BOT_GROWTH_FUNIL | `f75820ff-d563-44f3-bd56-aa77d1e04d88` | sim | [`bots/BOT_GROWTH_FUNIL/`](bots/BOT_GROWTH_FUNIL/) |
| BOT_QA | BOT_QA | `36719e43-e233-4441-8588-2c786cc115b5` | sim | [`bots/BOT_QA/`](bots/BOT_QA/) |
| BOT_SEC | BOT_SEC | `e6ebcc46-28f8-471e-aa86-f4161f35361a` | sim | [`bots/BOT_SEC/`](bots/BOT_SEC/) |
| BOT_V42_STORE | BOT_V42_STORE | `2c899a5d-1394-4f86-984a-f71c4a8d9e1e` | sim | [`bots/BOT_V42_STORE/`](bots/BOT_V42_STORE/) |
| CACADOR_DE_MONETIZACAO | CAÇADOR DE MONETIZAÇÃO | `726887ae-f55e-45f5-bd47-735110e38a29` | sim | [`bots/CACADOR_DE_MONETIZACAO/`](bots/CACADOR_DE_MONETIZACAO/) |
| CONTEUDO_EM_VIDEO | CONTEÚDO EM VÍDEO | `8c38c3ab-5bf9-47a9-94b0-8d6be8af0ceb` | sim | [`bots/CONTEUDO_EM_VIDEO/`](bots/CONTEUDO_EM_VIDEO/) |
| DATA_ENGINEER | DATA ENGINEER | `0b1cb83e-ad3a-4733-ab0f-c4fb02759d92` | vazia | [`bots/DATA_ENGINEER/`](bots/DATA_ENGINEER/) |
| DATA_SCIENTIST | DATA SCIENTIST | `aa7ec19d-7821-4462-a642-d1b93aef40cf` | vazia | [`bots/DATA_SCIENTIST/`](bots/DATA_SCIENTIST/) |
| DECISOR | DECISOR | `b23dd2b5-22eb-46e9-94da-369afbbdbb52` | sim | [`bots/DECISOR/`](bots/DECISOR/) |
| ESTRATEGISTA | ESTRATEGISTA | `c00d9b9e-5e0d-4f59-b218-52c0519fcde8` | sim | [`bots/ESTRATEGISTA/`](bots/ESTRATEGISTA/) |
| FORWARD_DEPLOYED_DATA_SCIENTIST | FORWARD DEPLOYED DATA SCIENTIST | `aa701f8c-2d23-4dee-95c3-f938a940fb26` | vazia | [`bots/FORWARD_DEPLOYED_DATA_SCIENTIST/`](bots/FORWARD_DEPLOYED_DATA_SCIENTIST/) |
| NEGOCIO_AUTOMATIZADO | NEGÓCIO AUTOMATIZADO | `53098e42-f359-4b17-b297-576cdeb0eb30` | sim | [`bots/NEGOCIO_AUTOMATIZADO/`](bots/NEGOCIO_AUTOMATIZADO/) |
| QUICK_WIN | QUICK WIN | `e33d5ec2-956c-45ce-b316-18ae8be94758` | sim | [`bots/QUICK_WIN/`](bots/QUICK_WIN/) |
| RAG_CORPORATIVO | RAG CORPORATIVO | `a794decf-f25a-421b-882d-5129e9941460` | sim | [`bots/RAG_CORPORATIVO/`](bots/RAG_CORPORATIVO/) |
| SEO_LOCAL | SEO LOCAL | `7a4d3ce1-5299-49d8-99ef-12fce28b21cc` | sim | [`bots/SEO_LOCAL/`](bots/SEO_LOCAL/) |
| TRAFEGO_PAGO | TRÁFEGO PAGO | `eac52a65-faec-43e1-b85e-f04df1ad3e44` | sim | [`bots/TRAFEGO_PAGO/`](bots/TRAFEGO_PAGO/) |
| TROPA_DO_PROCESSO_SELETIVO | TROPA DO PROCESSO SELETIVO | `45852260-f021-483b-9550-57e22cde697a` | vazia | [`bots/TROPA_DO_PROCESSO_SELETIVO/`](bots/TROPA_DO_PROCESSO_SELETIVO/) |
| TWITTER | TWITTER | `21446fa6-a6c7-4df3-8e5e-f1c85eb4e8dc` | vazia | [`bots/TWITTER/`](bots/TWITTER/) |
| VINI | VINI | `c0867b16-da2c-48c9-86b5-ed137fd3b930` | vazia | [`bots/VINI/`](bots/VINI/) |

## Como restaurar

1. Este pacote é um snapshot, não um restore automático. Não há ferramenta de `UpdateAgent` neste fluxo; a restauração é manual no Grok Bot.
2. **Bot que ainda existe** (mesmo `id` / `serverId`): abra o bot, cole de volta os campos de `profile.json` (`name`, `description`, `title`, `avatarShape`, `avatarColor`) e aplique `settings.json` (`notifyOnAgentUpdates`). Não invente um id novo. Use `estado.md` só como contexto do que estava em andamento.
3. **Bot apagado**: crie um bot com o mesmo `name`, cole `description` e os campos de aparência, e aplique as settings. Um `id` e um `serverId` novos serão emitidos — isso é esperado. Depois leia `estado.md`.
4. **Grupo TROPA DO PROCESSO SELETIVO**: além do perfil/settings, a composição dos membros está descrita em `bots/TROPA_DO_PROCESSO_SELETIVO/estado.md`. Recrie o grupo com esses membros se ele tiver sido desfeito.
5. O que este checkpoint não cobre precisa ser restaurado por outro caminho, se ainda for necessário: skills, Custom Rules, conectores, memória, rotinas/automações e arquivos de `/workspace`.
6. Antes de qualquer post, envio ou candidatura depois da restauração, o bot dono roda `scripts/preflight.py` (G1–G7, fail-closed) no momento da ação. Texto de perfil que cita empregador não vai para canal público.

## Pausa geral
Às 17h08 BRT de 24/11/2026 o Vini pediu PAUSA GERAL de todos os bots (sem ações, mensagens ou trabalho novo) até este checkpoint ser commitado. Rotinas pausadas confirmadas até o commit: BOT_V42_STORE (Checagem semanal do Gate 1), BOT_COPY (Respostas B2B LinkedIn (lote InMail); Métricas semanais Sales Navigator B2B); BOT_DEV e BOT_QA sem rotinas.
