#leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = input("Digite o seu sexo (M | F): ").lower()
    if sexo == "m" or sexo == "f":
        print("Valor valido!")
        break
    else:
        print("Valor invalido! Digite novamente.")
        