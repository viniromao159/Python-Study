'''Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

total = 0
cont = 1

while cont == 1:
    num = int(input("Digite valor para soma: "))
    if num != 999:
        total += num
    else:
        cont -= 1

print(f"O total da soma dos valores digitados é: {total}")
