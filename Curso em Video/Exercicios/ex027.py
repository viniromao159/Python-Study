'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = input("Digite seu nome completo: ").strip()

nome_picotado = nome.split()

print(f"Seu primeiro nome é {nome_picotado[0]} e seu utimo nome é {nome_picotado[len(nome_picotado)-1]}")
#print(f"Seu primeiro nome é {nome_picotado[0]} e seu utimo nome é {nome_picotado[-1]}")