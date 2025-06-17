import streamlit as st
import datetime
from db import inserir_tarefa

st.title("✏️ Cadastrar Tarefa")

with st.form('add_task'):
    descricao = st.text_area("Descrição da tarefa:")
    responsavel = st.text_input("Responsável:")
    status = st.selectbox("Status", ('Aberto', 'Em andamento', 'Concluído'))
    col1, col2 = st.columns(2)
    with col1:
        data_inicio = st.date_input("Data Início", min_value=datetime.date.today())
    with col2:
        data_fim = st.date_input("Data Fim", min_value=datetime.date.today())
    btnCadastrar = st.form_submit_button("Cadastrar")

    if btnCadastrar:
        if descricao and responsavel:
            inserir_tarefa(descricao, responsavel, status, data_inicio, data_fim)
            st.success("Tarefa cadastrada com sucesso!")
        else:
            st.error("Preencha todos os campos.")
