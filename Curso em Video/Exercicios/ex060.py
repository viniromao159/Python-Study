#Faça um programa que leia um número qualquer e mostre o seu fatorial.

fat = int(input("Digite um numero para fatorar: "))
total = 1

cont = 0
while cont < fat:
    cont += 1
    total *= cont

print(f"Total da fatoração é: {total}")
