'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = dict()

jogador['nome'] = input("Nome do jogador: ")

gols = []
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
for p in range(partidas):
    gol = int(input(f"Quantos gols fez na {p+1}º partida: "))
    gols.append(gol)

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('=-'*20)
print(jogador)

print('=-'*20)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}.")
    
print('=-'*20)
for j in range(len(jogador['gols'])):
    print(f"-> Na partida {j+1}, fez {jogador['gols'][j]} gols.")
print(f'Total de gols: {jogador['total']}')
print('=-'*20)
