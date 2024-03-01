#Faça um programa que leia um ano e diz se ele é bissexto

ano = int(input("Digite um ano: "))

if ano % 4 == 0:
    print("Ano \033[0;33mBISSEXTO\033[m!")
else:
    print("Ano normal!")