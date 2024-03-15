''' Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''


import random

while True:
    cpu = random.randint(1,10)
    print("-"*30)
    jogador_op = int(input("1 - IMPAR | 2 - PAR:  "))
    jogador_num = int(input("Escolha um numero: "))
    print("-"*30)
    
    final = (jogador_num + cpu) % 2
    
    if jogador_op == 1:
        if final == 0:
            print(f"Jogador = {jogador_num} | CPU = {cpu} -> {cpu+jogador_num} = PAR! \nPERDEU!")
            break
        else:
            print(f"Jogador = {jogador_num} | CPU = {cpu} -> {cpu+jogador_num} = IMPAR! \nVENCEU!")
    
    else:
        if final == 0:
            print(f"Jogador = {jogador_num} | CPU = {cpu} -> {cpu+jogador_num} = PAR! \nVENCEU!")
        else:
            print(f"Jogador = {jogador_num} | CPU = {cpu} -> {cpu+jogador_num} = IMPAR! \nPERDEU!")
            break

print("FIM!")
