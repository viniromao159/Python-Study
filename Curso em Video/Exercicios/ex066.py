total = cont = 0

while True:
    num = int(input("Digite um número para soma: "))
    
    if num != 999:
        cont += 1
        total += num
    
    else:
        break
    
if cont > 0:
    print(f"Foi digitado {cont} numeros. A soma deles é: {total}")

print("FIM!")
