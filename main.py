import tkinter as tk
from docx import Document


def gerar_doc():
    nome = entry_nome.get()
    idade = entry_idade.get()

    doc = Document("template.docx")

    for p in doc.paragraphs:
        if "{{nome}}" in p.text:
            p.text = p.text.replace("{{nome}}", nome)
        if "{{idade}}" in p.text:
            p.text = p.text.replace("{{idade}}", idade)

    doc.save(f"{nome}.docx")
    janela.destroy()


# Interface
janela = tk.Tk()
janela.title("Gerador de Documento")

tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Idade").pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

tk.Button(janela, text="Gerar Documento", command=gerar_doc).pack()

janela.mainloop()