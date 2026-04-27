from datetime import datetime

def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def formatar_data_extenso(data_str):
    data = datetime.strptime(data_str, "%d/%m/%Y")

    meses = [
        "janeiro", "fevereiro", "março", "abril",
        "maio", "junho", "julho", "agosto",
        "setembro", "outubro", "novembro", "dezembro"
    ]

    dia = data.day
    mes = meses[data.month - 1]
    ano = data.year

    return f"{dia} de {mes} de {ano}"

def substituir_com_formatacao(paragrafo, substituicoes):
    texto = paragrafo.text

    # verifica se tem algum placeholder
    if not any(ph in texto for ph in substituicoes):
        return

    paragrafo.clear()

    i = 0
    while i < len(texto):
        encontrou = False

        for placeholder, (valor, negrito) in substituicoes.items():
            if texto[i:].startswith(placeholder):
                run = paragrafo.add_run(str(valor))
                if negrito:
                    run.bold = True
                i += len(placeholder)
                encontrou = True
                break

        if not encontrou:
            run = paragrafo.add_run(texto[i])
            i += 1

def montar_resultado(var_inapto, var_apto, var_altura, var_inapto_altura, var_espaco, var_inapto_espaco):
    frases = []

    if var_inapto.get():
        frases.append("INAPTO ao Cargo")

    if var_apto.get():
        frases.append("APTO ao Cargo")

    if var_altura.get():
        frases.append("APTO ao trabalho em altura")

    if var_inapto_altura.get():
        frases.append("INAPTO ao trabalho em altura")

    if var_espaco.get():
        frases.append("APTO ao trabalho em espaço confinado")
    if var_inapto_espaco.get():
        frases.append("INAPTO ao trabalho em espaço confinado")

    # Se nada foi selecionado
    if not frases:
        return "NÃO INFORMADO"

    return "\n".join(frases)

def validar_idade(P):
    # P = valor que o campo terá após a digitação
    if P == "":
        return True  # permite apagar

    if not P.isdigit():
        return False

    if len(P) > 2:
        return False

    return True