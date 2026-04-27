import os
import sys
from datetime import datetime
from docx import Document
from utils import substituir_com_formatacao

def caminho_recurso(nome_arquivo):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, nome_arquivo)
    return os.path.join(os.path.abspath("."), nome_arquivo)

def gerar_documento(nome, idade, formacao, cargo, motivo, empresa, cpf, data, data_extenso, resultado):
    doc = Document(caminho_recurso("template.docx"))

    substituicoes = {
        "{{nome}}": (nome, True),
        "{{cpf}}": (cpf, True),
        "{{idade}}": (idade, False),
        "{{formacao}}": (formacao, False),
        "{{cargo}}": (cargo, False),
        "{{motivo}}": (motivo, False),
        "{{empresa}}": (empresa, False),
        "{{data}}": (data, False),
        "{{data_extenso}}": (data_extenso, False),
        "{{resultado}}": (resultado, True),
    }

    for p in doc.paragraphs:
        substituir_com_formatacao(p, substituicoes)

    # 📅 converter data
    data_dt = datetime.strptime(data, "%d/%m/%Y")

    # 📁 pasta por mês/ano
    pasta_mes = os.path.join("laudos", data_dt.strftime("%m-%Y"))

    # 📁 subpasta por dia
    pasta_dia = os.path.join(pasta_mes, data_dt.strftime("%d"))

    # cria TODA a estrutura de uma vez
    os.makedirs(pasta_dia, exist_ok=True)

    # 📄 caminho final
    caminho = os.path.join(pasta_dia, f"{nome}.docx")

    doc.save(caminho)

    print(f"Documento salvo em: {os.path.abspath(caminho)}")

