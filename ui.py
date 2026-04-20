'''import tkinter as tk
from service import gerar_documento

def iniciar_interface():
    def on_click():
        nome = entry_nome.get()
        idade = entry_idade.get()
        gerar_documento(nome, idade)
        janela.destroy()

    janela = tk.Tk()
    janela.title("Gerador de Documento")

    tk.Label(janela, text="Nome").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Idade").pack()
    entry_idade = tk.Entry(janela)
    entry_idade.pack()

    tk.Button(janela, text="Gerar Documento", command=on_click).pack()

    janela.mainloop()'''

import tkinter as tk
from service import gerar_documento  # sua função separada


def mostrar_tela_inicial():
    limpar_tela()

    tk.Label(janela, text="Bem-vindo", font=("Arial", 16)).pack(pady=20)

    tk.Button(
        janela,
        text="Gerar Documento",
        command=mostrar_formulario
    ).pack()


def mostrar_formulario():
    limpar_tela()

    tk.Label(janela, text="Nome").pack()
    entry_nome = tk.Entry(janela)
    entry_nome.pack()

    tk.Label(janela, text="Idade").pack()
    entry_idade = tk.Entry(janela)
    entry_idade.pack()

    def on_click():
        nome = entry_nome.get()
        idade = entry_idade.get()
        gerar_documento(nome, idade)
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


# janela principal
janela = tk.Tk()
janela.title("Gerador de Documento")

# inicia pela tela inicial
mostrar_tela_inicial()

janela.mainloop()