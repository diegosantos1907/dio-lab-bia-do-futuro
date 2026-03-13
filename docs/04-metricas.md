# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** foram criadas perguntas específicas para verificar se o agente responde corretamente utilizando os dados da base de conhecimento.

2. **Feedback real:** o agente também foi testado por outras pessoas (familiares e amigos) que interagiram com o sistema fazendo perguntas sobre finanças .

Durante esses testes, os participantes avaliaram a clareza das respostas, utilidade das informações e segurança do comportamento do agente.

No geral, o agente recebeu avaliações muito positivas, com notas médias próximas de **10**, indicando que as respostas foram consideradas claras, úteis e coerentes com o objetivo de educação financeira.

Isso mostra que você teve:

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

- testes estruturados

- testes com usuários

- avaliação de qualidade

- resultado positivo

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente respondeu corretamente perguntas sobre renda, gastos e perfil financeiro utilizando os dados da base de conhecimento.
- O sistema conseguiu explicar conceitos financeiros como CDB e Tesouro Selic de forma clara e educativa.
- O agente evitou recomendações de investimentos específicos, mantendo um comportamento seguro e responsável.
- Perguntas fora do escopo financeiro foram tratadas corretamente, informando as limitações do agente.

**O que pode melhorar:**
- Expandir a base de conhecimento com mais produtos financeiros e cenários de uso.
- Melhorar a interpretação de perguntas mais abertas feitas pelos usuários.
- Adicionar mais dados financeiros para permitir análises mais detalhadas.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
