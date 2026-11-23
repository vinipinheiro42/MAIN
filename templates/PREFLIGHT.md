# PRE-FLIGHT — checklist de ação externa (post, email, mensagem, candidatura, formulário)

> Fonte: "Grok Bot Pre-Flight: 7 Gates" (@Corki_0x). Usamos o método, não o contexto de trading. O gate é binário: se um falhar, a ação não sai. Se a checagem não rodar, a resposta é NÃO.
> Script: `python scripts/preflight.py --text-file <rascunho> --channel <x|linkedin|email|form> ...`. Rode **no momento da ação**, não horas antes.

| Gate | Pergunta | Passa quando |
|---|---|---|
| G1 aprovação | O Vini aprovou ESTE texto exato? | Sim, no chat do bot dono do canal (X/LinkedIn), com referência da mensagem |
| G2 destino | A conta/perfil/destinatário ativo é o certo? | Conferido na tela/conector agora |
| G3 confidencial | Tem nome de empregador, cliente ou projeto interno? | Nenhum (lista em `state/forbidden_terms.local.txt`) |
| G4 sensível | Tem CPF, senha, token ou cartão? | Nenhum |
| G5 fatos | Cada número/afirmação tem fonte checada? | Sim, ou o texto não tem números |
| G6 decisão | Fala de salário, proposta, relocation ou compromisso? | Só com sim explícito do Vini para isso |
| G7 fail-closed | Alguma checagem deu erro? | Nenhuma |

Rejeições vão para `state/preflight_log.jsonl`. Revise no ritual semanal: o gate barrou certo? Precisa de ajuste?
