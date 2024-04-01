from random import randint
from time import sleep

jogadores = {'Jogador 1':randint(1,6),
             'Jogador 2':randint(1,6),
             'Jogador 3':randint(1,6),
             'Jogador 4':randint(1,6)}

print("Valores Sorteados: ")
for jogador, dado in jogadores.items():
    sleep(1)
    print(f"O {jogador} tirou {dado}")

print("\nRanking dos jogadores:")
rank=1
for j in sorted(jogadores, key=jogadores.get, reverse=True): #Ordena a o for de acordo com os valores da key (invertida(Maior pro menor))
    sleep(0.5)
    print(f"O {j} ficou em {rank}º")
    rank += 1
