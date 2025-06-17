import streamlit as st
import pandas as pd
from db import buscar_tarefas

#Visualizar Tarefas

#Recupera Dados do Banco
df = pd.DataFrame(buscar_tarefas())

st.title("Lista de Tarefas")
st.subheader("Estatistica")
st.write(df.describe())
st.divider()
st.subheader("Tabela")
st.dataframe(df, hide_index="hidden")
