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