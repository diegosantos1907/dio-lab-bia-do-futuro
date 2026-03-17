import streamlit as st
import pandas as pd
import json
import plotly.express as px
from src.agente import responder

st.set_page_config(layout="wide")

# =========================
# CARREGAR DADOS
# =========================

with open("data/perfil_cliente.json", encoding="utf-8") as f:
    perfil = json.load(f)

transacoes = pd.read_csv("data/transacoes.csv")

# =========================
# TÍTULO
# =========================

st.title("💰 Digo - Assistente Financeiro Inteligente")

# =========================
# CHAT
# =========================

st.subheader("💬 Converse com o Digo")

if "historico" not in st.session_state:
    st.session_state.historico = []

def enviar(pergunta):

    if pergunta.strip() == "":
        return

    resposta = responder(
        pergunta,
        st.session_state.historico,
        perfil,
        transacoes
    )

    st.session_state.historico.append((pergunta, resposta))


# Form permite enviar com ENTER ou botão
with st.form("chat_form", clear_on_submit=True):

    pergunta = st.text_input("Digite sua pergunta sobre finanças")

    enviado = st.form_submit_button("Enviar")

    if enviado:
        enviar(pergunta)

# Mostrar histórico
for pergunta, resposta in reversed(st.session_state.historico):

    st.write(f"👤 Você: {pergunta}")
    st.write(f"🤖 Digo: {resposta}")

# =========================
# DASHBOARD
# =========================

st.divider()
st.header("📊 Dashboard Financeiro")

renda = perfil["renda_mensal"]
gastos = abs(transacoes["valor"].sum())
saldo = renda - gastos

col1, col2, col3 = st.columns(3)

col1.metric("Renda", f"R$ {renda:,.0f}")
col2.metric("Gastos", f"R$ {gastos:,.0f}")
col3.metric("Saldo", f"R$ {saldo:,.0f}")

# =========================
# SAÚDE FINANCEIRA
# =========================

st.subheader("🧠 Saúde Financeira")

score = int((saldo / renda) * 100) if renda > 0 else 0
score = max(0, min(score, 100))

st.metric("Score", f"{score}/100")

if score >= 70:
    st.success("Suas finanças estão saudáveis.")
elif score >= 40:
    st.warning("Seus gastos estão relativamente altos.")
else:
    st.error("Seus gastos estão muito altos.")

# =========================
# GRÁFICOS
# =========================

gastos_categoria = (
    transacoes.groupby("categoria")["valor"]
    .sum()
    .abs()
    .reset_index()
)

col1, col2 = st.columns(2)

fig_bar = px.bar(
    gastos_categoria,
    x="categoria",
    y="valor",
    color="categoria",
    title="Gastos por categoria"
)

col1.plotly_chart(fig_bar, use_container_width=True)

fig_pie = px.pie(
    gastos_categoria,
    names="categoria",
    values="valor",
    title="Distribuição dos gastos"
)

col2.plotly_chart(fig_pie, use_container_width=True)