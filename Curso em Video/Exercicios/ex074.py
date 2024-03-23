'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

import random

valor = (random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100))

print(f"Valores sorteados: {valor}")
print(f"Maior valor: {max(valor)}")
print(f"Menor valor: {min(valor)}")
