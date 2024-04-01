'''jogadores = [{'nome': 'Vini', 'gols': [3, 1, 0, 2], 'total': 6},
             {'nome': 'Vitor', 'gols': [0, 1, 0], 'total': 1},
             {'nome': 'Bruno', 'gols': [1, 1, 1, 2, 3], 'total': 8}]'''

jogadores = []

while True:
    nome = input("Nome do jogador: ")
    gols = []
    partidas = int(input(f"Quantas partidas {nome} jogou: "))
    for p in range(partidas):
        gol = int(input(f"Quantos gols fez na {p+1}º partida: "))
        gols.append(gol)

    jogadores.append({'nome':nome, 'gols':gols, 'total':sum(gols)})
    
    cont = input("Continuar: [S/N] ").lower()
    while cont not in ['s', 'n']:
        print("Valor inválido!")
        cont = input("Continuar: [S/N] ").lower()
    if cont == 'n':
        break
print('=-'*20)

for ind, jogador in enumerate(jogadores):
    print(f'{ind} -> Nome: {jogador['nome']} -> Gols: {jogador['gols']} -> Total de gols: {jogador['total']}')

print('=-'*20)
while True:
    get = int(input("Mostrar dados de qual jogador: "))
    
    if get == 999:
        print("Encerrado!")
        break
    
    elif get >= len(jogadores):
        print("Jogador não encontrado!")
    
    else:
        print(f"Levantamento de {jogadores[get]['nome']}: ")
        for gol in range(len(jogadores[get]['gols'])):
            print(f"Na {gol + 1}º partida fez {jogadores[get]['gols'][gol]} gols.")