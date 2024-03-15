'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''

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
