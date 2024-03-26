'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

import random

jogos = []

qtd_jogos = int(input("Quantos jogos será feito: "))

for j in range(qtd_jogos):
    jogo = []
    for n in range(6):
        aleatorio = random.randint(1,60)
        while aleatorio in jogo:
            aleatorio = random.randint(1,60)
        jogo.append(aleatorio)     
    
    jogo.sort()
    jogos.append(jogo)
    
for i, jogo in enumerate(jogos):
    print(f"Jogo {i+1}: {jogo}")