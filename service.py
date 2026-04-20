from docx import Document

def gerar_documento(nome, idade):
    doc = Document("template.docx")

    for p in doc.paragraphs:
        if "{{nome}}" in p.text:
            p.text = p.text.replace("{{nome}}", nome)
        if "{{idade}}" in p.text:
            p.text = p.text.replace("{{idade}}", idade)

    doc.save(f"{nome}.docx")