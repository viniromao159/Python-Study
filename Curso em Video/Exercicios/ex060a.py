#Faça um programa que leia um número qualquer e mostre o seu fatorial mas agora com FOR.
fat = int(input("Digite um numero para fatorar: "))
total = 1

for f in range(fat, 1, -1):
    total *= f

print(f"Total da fatoração é: {total}")
