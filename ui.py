import tkinter as tk
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

    janela.mainloop()