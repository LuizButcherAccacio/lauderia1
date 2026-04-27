import tkinter as tk
from service import gerar_documento  # sua função separada
from storage import salvar_relatorio, carregar_relatorio
from datetime import datetime
from filtro import aplicar_filtro, filtrar_por_intervalo
from utils import validar_data
from filtro import exportar_para_word
from utils import formatar_data_extenso
from utils import validar_data
from utils import montar_resultado
from storage import carregar_relatorio

def mostrar_tela_inicial():
    limpar_tela()

    tk.Label(janela, text="Bem-vindo ao Lauderia - Prevenir", font=("Arial", 18)).pack(pady=25)

    tk.Button(
        janela,
        text="Gerar Novo Laudo",
        command=mostrar_formulario,
        width=30,
        height=4
    ).pack()

    tk.Button(
        janela,
        text="Filtrar Relatório",
        command=mostrar_filtro
    ).pack(pady=10)


def mostrar_formulario():
    limpar_tela()

    # ✅ VALIDADOR (tem que vir antes do uso)
    def validar_idade(P):
        if P == "":
            return True
        if not P.isdigit():
            return False
        if len(P) > 2:
            return False
        return True

    # 📦 Frame principal
    frame = tk.Frame(janela)
    frame.pack(pady=10)

    # ----------- CAMPOS PRINCIPAIS -----------

    tk.Label(frame, text="Nome").grid(row=0, column=0, sticky="w")
    entry_nome = tk.Entry(frame)
    entry_nome.grid(row=0, column=1, padx=5, pady=2)

    # ✅ LABEL DE IDADE (faltava)
    tk.Label(frame, text="Idade").grid(row=1, column=0, sticky="w")

    # ✅ validação aplicada corretamente
    vcmd = (janela.register(validar_idade), "%P")
    entry_idade = tk.Entry(frame, validate="key", validatecommand=vcmd)
    entry_idade.grid(row=1, column=1, padx=5, pady=2)

    tk.Label(frame, text="Formação").grid(row=2, column=0, columnspan=2)

    entry_formacao = tk.StringVar()
    entry_formacao.set(None)

    tk.Radiobutton(frame, text="Ensino Fundamental Incompleto",
                   variable=entry_formacao,
                   value="Ensino Fundamental Incompleto").grid(row=3, column=1, sticky="w")

    tk.Radiobutton(frame, text="Ensino Fundamental",
                   variable=entry_formacao,
                   value="Ensino Fundamental").grid(row=4, column=1, sticky="w")

    tk.Radiobutton(frame, text="Ensino Médio",
                   variable=entry_formacao,
                   value="Ensino Médio").grid(row=5, column=1, sticky="w")

    tk.Radiobutton(frame, text="Ensino Superior",
                   variable=entry_formacao,
                   value="Ensino Superior").grid(row=6, column=1, sticky="w")

    tk.Label(frame, text="Cargo").grid(row=7, column=0, sticky="w")
    entry_cargo = tk.Entry(frame)
    entry_cargo.grid(row=7, column=1, padx=5, pady=2)

    tk.Label(frame, text="Motivo").grid(row=8, column=0, sticky="w")
    entry_motivo = tk.Entry(frame)
    entry_motivo.grid(row=8, column=1, padx=5, pady=2)

    tk.Label(frame, text="Empresa").grid(row=9, column=0, sticky="w")
    entry_empresa = tk.Entry(frame)
    entry_empresa.grid(row=9, column=1, padx=5, pady=2)

    tk.Label(frame, text="CPF").grid(row=10, column=0, sticky="w")
    entry_cpf = tk.Entry(frame)
    entry_cpf.grid(row=10, column=1, padx=5, pady=2)

    tk.Label(frame, text="Data").grid(row=11, column=0, sticky="w")
    entry_data = tk.Entry(frame)
    entry_data.grid(row=11, column=1, padx=5, pady=2)

    # ----------- CHECKBUTTONS -----------

    tk.Label(frame, text="Resultado do Exame").grid(row=12, column=0, columnspan=2, pady=10)

    var_inapto = tk.BooleanVar()
    var_apto = tk.BooleanVar()
    var_altura = tk.BooleanVar()
    var_inapto_altura = tk.BooleanVar()
    var_espaco = tk.BooleanVar()
    var_inapto_espaco = tk.BooleanVar()

    tk.Checkbutton(frame, text="INAPTO ao Cargo", variable=var_inapto)\
        .grid(row=13, column=1, sticky="w")

    tk.Checkbutton(frame, text="APTO ao Cargo", variable=var_apto)\
        .grid(row=14, column=1, sticky="w")

    tk.Checkbutton(frame, text="APTO ao trabalho em altura", variable=var_altura)\
        .grid(row=15, column=1, sticky="w")

    tk.Checkbutton(frame, text="INAPTO ao trabalho em altura", variable=var_inapto_altura)\
        .grid(row=16, column=1, sticky="w")

    tk.Checkbutton(frame, text="APTO ao trabalho em espaço confinado", variable=var_espaco)\
        .grid(row=17, column=1, sticky="w")

    tk.Checkbutton(frame, text="INAPTO ao trabalho em espaço confinado", variable=var_inapto_espaco)\
        .grid(row=18, column=1, sticky="w")

    # ----------- FUNÇÃO BOTÃO -----------

    def on_click():
        from tkinter import messagebox

        nome = entry_nome.get()
        idade = entry_idade.get()
        formacao = entry_formacao.get()
        cargo = entry_cargo.get()
        motivo = entry_motivo.get()
        empresa = entry_empresa.get()
        cpf = entry_cpf.get()
        data = entry_data.get()

        nome_arquivo = f"{nome}.docx"

        if not validar_data(data):
            messagebox.showerror("Erro", "Data inválida! Use DD/MM/AAAA")
            return

        # ✅ VALIDAÇÃO FINAL DA IDADE
        if not idade:
            messagebox.showerror("Erro", "Informe a idade")
            return

        if not idade.isdigit():
            messagebox.showerror("Erro", "Idade deve ser numérica")
            return

        idade = int(idade)

        if idade < 0 or idade > 99:
            messagebox.showerror("Erro", "Idade inválida")
            return

        data_extenso = formatar_data_extenso(data)

        resultado = montar_resultado(
            var_inapto,
            var_apto,
            var_altura,
            var_inapto_altura,
            var_espaco,
            var_inapto_espaco
        )

        gerar_documento(
            nome, idade, formacao, cargo, motivo,
            empresa, cpf, data, data_extenso,
            resultado
        )

        salvar_relatorio(nome_arquivo, data)
        mostrar_sucesso()

    # ----------- RODAPÉ -----------

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=20)

    tk.Button(frame_botoes, text="Gerar Laudo", command=on_click)\
        .pack(side="left", padx=10)

    tk.Button(frame_botoes, text="Voltar", command=mostrar_tela_inicial)\
        .pack(side="left", padx=10)

def mostrar_sucesso():
    limpar_tela()

    tk.Label(janela, text="Laudo gerado com sucesso!", font=("Arial", 14)).pack(pady=20)

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

    # ✅ função no lugar correto
    def ao_filtrar():
        resultado = aplicar_filtro(entry_inicio.get(), entry_fim.get())

        if resultado is None:
            return

        mostrar_resultado_filtrado(resultado)

    tk.Button(
        janela,
        text="Filtrar",
        command=ao_filtrar
    ).pack(pady=10)

    tk.Button(
        janela,
        text="Voltar",
        command=mostrar_tela_inicial
    ).pack()

'''def mostrar_relatorio():
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
'''
def mostrar_resultado_filtrado(filtrados):
    limpar_tela()

    tk.Label(janela, text="Resultado do Filtro", font=("Arial", 14)).pack(pady=10)

    if not filtrados:
        tk.Label(janela, text="Nenhum registro encontrado").pack()
    else:
        # 🔽 Container principal da área rolável
        container = tk.Frame(janela)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)

        frame_lista = tk.Frame(canvas)

        frame_lista.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame_lista, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # 🔽 Sua lista agora vai aqui dentro
        for item in filtrados:
            nome = item["nome_arquivo"].replace(".docx", "")
            texto = f"{nome} - {item['data']}"
            tk.Label(frame_lista, text=texto, anchor="w").pack(fill="x", padx=10, pady=5)

    # 👇 BOTÃO NOVO AQUI
    def ao_exportar():
        exportar_para_word(filtrados)

        from tkinter import messagebox
        messagebox.showinfo("Sucesso", "Arquivo Word exportado!")

    tk.Button(
        janela,
        text="Exportar Word",
        command=ao_exportar
    ).pack(pady=5)

    tk.Button(
        janela,
        text="Voltar",
        command=mostrar_tela_inicial
    ).pack(pady=10)

# janela principal
janela = tk.Tk()
janela.title("Lauderia Prevenir")
janela.geometry("1000x600+300+150")



