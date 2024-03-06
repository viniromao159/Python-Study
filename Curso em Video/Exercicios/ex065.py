#Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = 0
menor = 0
media = 0
total = 0

cont = 1
while cont == 1:
    num = int(input("Digite valor para soma: "))
    media += 1
    total += num
    
    if media == 1:
        maior = num
        menor = num
    
    if media > 1:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    
        flag = input("Deseja continuar? [s]im | [n]ão: ").lower().strip()
        
        if flag == "n":
            media = total / media
            cont -= 1
    
print(f"O maior numero é {maior} e o menor é {menor}!")
print(f"O total dos valores é {total} e sua média é {media}!")
