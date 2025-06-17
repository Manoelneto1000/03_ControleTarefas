import streamlit as st
#Configuração da página
st.set_page_config(layout="wide")

# Configuração CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

# Navegação das páginas
main_page = st.Page("page01.py", title="Cadastrar Tarefa", icon="✏️")
page_2 = st.Page("page02.py", title="Visualizar Tarefas", icon="📝")
page_3 = st.Page("page03.py", title="Tarefas concluídas", icon="🟢")
pg = st.navigation([main_page, page_2, page_3])
pg.run()