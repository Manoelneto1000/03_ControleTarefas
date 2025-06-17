import streamlit as st
import datetime

st.set_page_config(page_title="Cadastrar Tarefa", layout="wide")

# Sidebar: menu de seções
secao = st.sidebar.radio(
    "🔸 Navegação por seção",
    ["Dados Básicos", "Datas", "Cadastrar"]
)

# Cabeçalho principal
st.title("✏️ Cadastro de Tarefa")

# Sessão 1: Dados Básicos
if secao == "Dados Básicos":
    st.subheader("📝 Sessão: Dados Básicos")
    descricao = st.text_area("Descrição da tarefa:")
    responsavel = st.text_input("Responsável:")

# Sessão 2: Datas
elif secao == "Datas":
    st.subheader("📅 Sessão: Datas")
    col1, col2 = st.columns(2)
    with col1:
        data_inicio = st.date_input("Data de Início", min_value=datetime.date.today())
    with col2:
        data_fim = st.date_input("Data de Fim", min_value=datetime.date.today())

# Sessão 3: Cadastrar
elif secao == "Cadastrar":
    st.subheader("✅ Sessão: Cadastrar")
    st.write("Confira os dados antes de cadastrar.")
    
    # Atenção: você precisa armazenar os dados em estado para usar aqui
    if st.button("Cadastrar"):
        st.success("Tarefa cadastrada com sucesso!")