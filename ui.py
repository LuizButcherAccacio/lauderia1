import tkinter as tk
from service import gerar_documento  # sua função separada
from storage import salvar_relatorio, carregar_relatorio
from datetime import datetime
from filtro import aplicar_filtro, filtrar_por_intervalo
from utils import validar_data

from utils import validar_data
from storage import carregar_relatorio

def mostrar_tela_inicial():
    limpar_tela()

    tk.Label(janela, text="Bem-vindo", font=("Arial", 16)).pack(pady=20)

    tk.Button(
        janela,
        text="Gerar Documento",
        command=mostrar_formulario
    ).pack()

    tk.Button(
        janela,
        text="Gerar Relatório",
        command=mostrar_relatorio
    ).pack(pady=5)

    tk.Button(
        janela,
        text="Filtrar Relatório",
        command=mostrar_filtro
    ).pack(pady=5)


def mostrar_formulario():
    limpar_tela()

    tk.Label(janela, text="Nome").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Idade").pack()
    entry_idade = tk.Entry(janela)
    entry_idade.pack()

    tk.Label(janela, text="Data").pack()
    entry_data = tk.Entry(janela)
    entry_data.pack()

    def on_click():
        nome = entry_nome.get()
        idade = entry_idade.get()
        data = entry_data.get()

        nome_arquivo = f"{nome}.docx"

        if not validar_data(data):
            from tkinter import messagebox
            messagebox.showerror("Erro", "Data inválida! Use DD/MM/AAAA")
            return

        gerar_documento(nome, idade, data)

        salvar_relatorio(nome_arquivo, data)

        mostrar_sucesso()
        # mostrar_tela_inicial()  # volta pra tela inicial

    tk.Button(janela, text="Gerar Documento", command=on_click).pack()

def mostrar_sucesso():
    limpar_tela()

    tk.Label(janela, text="Documento gerado com sucesso!", font=("Arial", 14)).pack(pady=20)

    tk.Button(
        janela,
        text="OK",
        command=mostrar_tela_inicial
    ).pack()

def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def mostrar_filtro():
    limpar_tela()

    tk.Label(janela, text="Filtrar por intervalo", font=("Arial", 14)).pack(pady=10)

    tk.Label(janela, text="Data início (DD/MM/AAAA)").pack()
    entry_inicio = tk.Entry(janela)
    entry_inicio.pack()

    tk.Label(janela, text="Data fim (DD/MM/AAAA)").pack()
    entry_fim = tk.Entry(janela)
    entry_fim.pack()

    tk.Button(
        janela,
        text="Filtrar",
        command=lambda: aplicar_filtro(entry_inicio.get(), entry_fim.get())
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Voltar",
        command=mostrar_tela_inicial
    ).pack()

def mostrar_relatorio():
    limpar_tela()

    tk.Label(janela, text="Relatório", font=("Arial", 14)).pack(pady=10)

    dados = carregar_relatorio()

    if not dados:
        tk.Label(janela, text="Nenhum documento gerado.").pack()
    else:
        for item in dados:
            texto = f"{item['nome_arquivo'].replace('.docx', '')} - {item['data']}"
            tk.Label(janela, text=texto).pack()

    tk.Button(janela, text="Voltar", command=mostrar_tela_inicial).pack(pady=10)

def mostrar_resultado_filtrado(filtrados):
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

# janela principal
janela = tk.Tk()
janela.title("Lauderia Prevenir")
janela.geometry("1000x600+300+150")

# inicia pela tela inicial
mostrar_tela_inicial()

janela.mainloop()

