while True:
    sexo = input("Digite o seu sexo (M | F): ").lower()
    if sexo == "m" or sexo == "f":
        print("Valor valido!")
        break
    else:
        print("Valor invalido! Digite novamente.")