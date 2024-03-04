#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menorpeso = 0
maiorpeso = 0

for p in range(0,5):
    peso = float(input("Digite seu peso: "))
    if p == 0:
        menorpeso = peso
        maiorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

print(f"O menor peso é: {menorpeso}KG!")
print(f"O maior peso é: {maiorpeso}KG!")
