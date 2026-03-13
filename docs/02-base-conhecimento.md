# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|--------|--------|----------------------|
| perfil_cliente.json | JSON | Armazena informações do cliente como nome, renda mensal e objetivos financeiros |
| perfil_investidor.json | JSON | Define o perfil de investidor do usuário (conservador, moderado ou arrojado) |
| produtos_financeiros.json | JSON | Contém informações educativas sobre produtos financeiros como CDB, Tesouro Selic e LCI/LCA |
| transacoes.csv | CSV | Registra transações financeiras do cliente para análise de gastos e organização financeira |


## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados utilizados pelo agente foram criados como dados mockados para simular um cenário real de organização financeira pessoal.

Foram desenvolvidos arquivos JSON e CSV representando informações de um cliente fictício, incluindo perfil financeiro, histórico de transações e produtos financeiros disponíveis para explicação.

Esses dados foram estruturados de forma simples e organizada para facilitar o processamento pelo agente e permitir que o modelo de linguagem gere respostas contextualizadas com base nas informações do cliente.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os dados da base de conhecimento são carregados no início da execução do sistema utilizando Python.

Os arquivos no formato JSON são lidos utilizando a biblioteca padrão `json`, enquanto os arquivos CSV são carregados com a biblioteca `pandas`.

Após o carregamento, essas informações são armazenadas em estruturas de dados dentro da aplicação e utilizadas pelo agente para analisar o perfil do cliente, interpretar transações financeiras e fornecer respostas contextualizadas.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados carregados da base de conhecimento são utilizados para montar o contexto enviado ao modelo de linguagem.

Antes de gerar uma resposta, o agente organiza informações relevantes do cliente, como perfil de investidor, renda mensal e resumo de transações financeiras.

Esses dados são incluídos no contexto do prompt enviado ao modelo de linguagem para que as respostas sejam baseadas nas informações disponíveis, garantindo maior precisão e reduzindo o risco de alucinações.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: Carlos Silva
- Idade: 38 anos
- Renda Mensal: R$ 5.500
- Objetivo Financeiro: Construir uma reserva de emergência

Perfil do Investidor:
- Tipo: Conservador
- Tolerância a risco: Baixa
- Preferência: Investimentos de renda fixa

Resumo de Gastos Mensais:
- Alimentação: R$ 770
- Transporte: R$ 660
- Moradia: R$ 1.500
- Lazer: R$ 540

Saldo disponível estimado após despesas: R$ 2.030

Produtos Financeiros Disponíveis para Explicação:
- Tesouro Selic
- CDB
- LCI/LCA
