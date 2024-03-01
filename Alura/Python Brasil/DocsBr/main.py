from docsbr import Documento

#Exemplo CPF correto: 12354367996
#Exemplo CNPJ correto: 51011777000192

print(''' 
    --------------------------
      Validador de documentos
    --------------------------
''')

cont = 0
while cont == 0: 
    doc_number = int(input("Digite o Documento: "))
    try:
        doc = Documento.cria_documento(doc_number)
        print(doc)
    except:
        print("Documento inválido!")
    
    exit = int(input("Deseja continuar ? (1 = Continuar| 2 = Sair): "))

    if exit == 2:
        print("Saindo...")
        cont += 1      