import json
from datetime import datetime

def salvar_relatorio(nome_arquivo, data):
    try:
        with open("relatorio.json", "r") as f:
            dados = json.load(f)
    except:
        dados = []

    dados.append({
        "nome_arquivo": nome_arquivo,
        "data": data
    })

    with open("relatorio.json", "w") as f:
        json.dump(dados, f, indent=4)

def carregar_relatorio():
    try:
        with open("relatorio.json", "r") as f:
            return json.load(f)
    except:
        return []


