import pandas as pd
import os

ARQUIVO_CSV = "tarefas.csv"

# Função para salvar uma nova tarefa no CSV
def inserir_tarefa(descricao, responsavel, status, data_inicio, data_fim):
    nova_tarefa = {
        "descricao": descricao,
        "responsavel": responsavel,
        "status": status,
        "data_inicio": data_inicio,
        "data_fim": data_fim
    }

    if os.path.exists(ARQUIVO_CSV):
        df = pd.read_csv(ARQUIVO_CSV)
        df = pd.concat([df, pd.DataFrame([nova_tarefa])], ignore_index=True)
    else:
        df = pd.DataFrame([nova_tarefa])
    
    df.to_csv(ARQUIVO_CSV, index=False)

# Função para buscar as tarefas do CSV
def buscar_tarefas():
    if os.path.exists(ARQUIVO_CSV):
        df = pd.read_csv(ARQUIVO_CSV)
        return df.to_dict(orient="records")
    else:
        return []
