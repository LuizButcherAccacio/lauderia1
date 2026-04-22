from datetime import datetime
from utils import validar_data
from storage import carregar_relatorio

def filtrar_por_intervalo(dados, data_inicio, data_fim):
    data_inicio_dt = datetime.strptime(data_inicio, "%d/%m/%Y")
    data_fim_dt = datetime.strptime(data_fim, "%d/%m/%Y")

    return [
        item for item in dados
        if data_inicio_dt <= datetime.strptime(item["data"], "%d/%m/%Y") <= data_fim_dt
    ]

from tkinter import messagebox

def aplicar_filtro(data_inicio, data_fim):
    if not validar_data(data_inicio) or not validar_data(data_fim):
        messagebox.showerror("Erro", "Datas inválidas!")
        return

    dados = carregar_relatorio()
    filtrados = filtrar_por_intervalo(dados, data_inicio, data_fim)

    #mostrar_resultado_filtrado(filtrados)

"""def mostrar_resultado_filtrado(filtrados):
    limpar_tela()

    tk.Label(janela, text="Resultado do Filtro", font=("Arial", 14)).pack(pady=10)

    if not filtrados:
        tk.Label(janela, text="Nenhum registro encontrado").pack()
    else:
        for item in filtrados:
            nome = item["nome_arquivo"].replace(".docx", "")
            texto = f"{nome} - {item['data']}"
            tk.Label(janela, text=texto).pack()

    tk.Button(
        janela,
        text="Voltar",
        command=mostrar_tela_inicial
    ).pack(pady=10)
"""
"""def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

"""