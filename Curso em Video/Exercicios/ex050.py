soma = 0

for n in range(1,7):
    num = int(input(f"Digite o {n}º numero: "))
    if num % 2 == 0:
        soma += num

print(f"A soma dos pares é {soma}!")