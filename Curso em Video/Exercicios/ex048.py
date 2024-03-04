 #Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print("--"*10,"MULTIPLOS DE 3!","--"*10)

acumulador = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        print(n, end=" ")
        acumulador += n

print(f"\n\033[0;32mA soma dos multiplos de 3 até 500 é: {acumulador}\033[m")

print("--"*10,"FIM!","--"*10)
