menorpeso = 1000
maiorpeso = 0

for p in range(0,5):
    peso = float(input("Digite seu peso: "))
    if peso > maiorpeso:
        maiorpeso = peso
    if peso < menorpeso:
        menorpeso = peso

print(f"O menor peso é: {menorpeso}KG!")
print(f"O maior peso é: {maiorpeso}KG!")
