import pyodbc
import streamlit as st

# Função para conectar ao SQL Server
def conectar_sql_server():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=(localdb)\MSSQLLocalDB;'  # Servidor Banco de Dados
        'DATABASE=Tarefas;'       # Nome do Banco de Dados
        'Trusted_Connection=yes;'       
    )

# Função para inserir tarefa no Banco
def inserir_tarefa(descricao, responsavel, status, data_inicio, data_fim):
    conn = conectar_sql_server()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Tarefas_ (descricao, responsavel, status, data_inicio, data_fim)
        VALUES (?, ?, ?, ?, ?)
    """, descricao, responsavel, status, data_inicio, data_fim)
    conn.commit()
    conn.close()

# Função para recuperar Dados Cadastrados na tabela
def buscar_tarefas():
    conn = conectar_sql_server()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tarefas_")
    
    tarefas = cursor.fetchall()
    colunas = [column[0] for column in cursor.description]
    
    conn.close()

    tarefas_dict = [dict(zip(colunas, linha)) for linha in tarefas]
    return tarefas_dict
