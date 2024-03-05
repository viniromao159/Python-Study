fat = int(input("Digite um numero para fatorar: "))
total = 1

cont = 0
while cont < fat:
    total *=  cont + 1
    cont += 1

print(f"Total da fatoração é: {total}")