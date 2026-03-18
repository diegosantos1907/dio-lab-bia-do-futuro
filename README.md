# 💰 Digo — Assistente Financeiro Inteligente

Projeto desenvolvido para o desafio de Agentes Inteligentes da DIO.

---

## 📌 Sobre o Projeto

O **Digo** é um agente financeiro inteligente que utiliza IA generativa para ajudar usuários a entender sua situação financeira, analisar gastos e aprender conceitos de educação financeira.

O sistema combina análise de dados com linguagem natural, permitindo que o usuário interaja por meio de um chat e receba respostas personalizadas com base em seus dados financeiros.

---

## 🚀 Funcionalidades

- 📊 Consulta de renda mensal  
- 📈 Análise de gastos por categoria  
- 💸 Identificação do maior gasto  
- 🧮 Cálculo de saldo mensal  
- 📚 Explicação de conceitos financeiros (CDB, CDI, Tesouro Selic)  
- 💬 Chat interativo com IA  
- 📊 Dashboard financeiro dinâmico  

---

## 🚀 Demonstração do Sistema (Interface)

O sistema desenvolvido permite que o usuário visualize sua situação financeira de forma clara e interativa.

A aplicação conta com um dashboard com indicadores financeiros, análise de gastos por categoria e um chat inteligente que responde com base nos dados do usuário.

Abaixo estão algumas telas reais da aplicação em funcionamento:

---

## 📸 Evidências do Sistema

### 📊 Painel Financeiro

![Painel](assets/dashboard.png)

---

### 📈 Análise de Gastos

![Gráficos](assets/gastos.png)

---

### 💬 Bate-papo com IA

![Chat](assets/chat.png)

---

## 🧠 Tecnologias Utilizadas

- Python  
- Streamlit  
- OpenAI API (GPT-4o-mini)  
- Pandas  
- JSON / CSV  

---

## 🛡️ Segurança e Confiabilidade

- O agente não recomenda investimentos específicos  
- Não acessa dados sensíveis (CPF, senhas, dados bancários)  
- Utiliza apenas dados da base de conhecimento  
- Possui regras para evitar alucinações  

---

## 📂 Estrutura do Projeto

```
data/       # Base de conhecimento (JSON e CSV)
docs/       # Documentação do agente
assets/     # Evidências do sistema
src/        # Estrutura preparada para modularização futura
app.py      # Aplicação principal (Streamlit)
README.md   # Documentação principal
```
---

### 🧠 Decisão de Arquitetura

A lógica do agente foi centralizada no arquivo `app.py` com o objetivo de simplificar a implementação do protótipo.

Essa abordagem permite uma aplicação funcional, clara e de fácil entendimento, mantendo o foco na integração com a base de dados e na geração de respostas contextualizadas.

A estrutura da pasta `src` foi mantida para possibilitar evolução futura do projeto, permitindo separação de responsabilidades como lógica do agente, análises e configurações.

---

## ▶️ Como Executar o Projeto

### 1. Clonar o repositório
git clone https://github.com/diegosantos1907/dio-lab-bia-do-futuro

### 2. Entrar na pasta do projeto
cd dio-lab-bia-do-futuro

### 3. Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv

### 4. Ativar ambiente virtual

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 5. Instalar dependências
pip install -r requirements.txt

### 6. Executar o sistema
streamlit run app.py

---

## 🎬 Demonstração

▶️ Assista ao pitch do projeto:  
https://youtu.be/8V3F7hzBNq8

---

## 👨‍💻 Autor

Diego Santos
