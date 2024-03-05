total = 0

cont = 1
while cont == 1:
    num = int(input("Digite valor para soma: "))
    if num != 999:
        total += num
    else:
        cont -= 1

print(f"O total da soma dos valores digitados é: {total}")