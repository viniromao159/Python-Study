'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = input("Digite seu nome completo: ").lower()

silva = "silva" in nome #boolean
 
if silva:
    print("Seu nome tem SILVA :)")
else:
    print("Seu nome não tem SILVA :(")