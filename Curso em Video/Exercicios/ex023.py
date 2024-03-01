'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

"""numero = input("Digite um numero: ")

for num in numero:
    print(int(num))"""
    
numero = input("Digite um numero: ")

num_list = []

for num in numero:
    num_list.append(int(num))

print(num_list)