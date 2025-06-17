import streamlit as st
from db import buscar_tarefas

st.title("📋 Visualizar Tarefas")

tarefas = buscar_tarefas()

if tarefas:
    for tarefa in tarefas:
        with st.container():
            st.subheader(f"📝 {tarefa['descricao']}")
            st.write(f"👤 Responsável: {tarefa['responsavel']}")
            st.write(f"📅 De {tarefa['data_inicio']} até {tarefa['data_fim']}")
            st.write(f"📌 Status: {tarefa['status']}")
            st.divider()
else:
    st.info("Nenhuma tarefa encontrada.")
