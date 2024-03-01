'''
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome = input("Digite seu nome completo: ")

nome_maiuscula = nome.upper()
nome_minuscula = nome.lower()

qtdletras = len(nome.replace(" ",""))
primeironome = nome.split()
qtdprimeironome = len(primeironome[0])

print(f"Em maiusculo: {nome_maiuscula}")
print(f"Em minuscula: {nome_minuscula}")
print(f"Quantidade de letras no nome: {qtdletras}")
print(f"Quantidade de letras no primeiro nome: {qtdprimeironome}")