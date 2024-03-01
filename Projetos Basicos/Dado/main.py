import random

while True:
    opcao_inicial = input("Deseja jogar dado: ").lower()
    if opcao_inicial == "sim":
        dado = random.randrange(1,7)
        print(f"Girando... caiu em {dado}")
    elif opcao_inicial == "nao":
        print("Jogo encerrado!")
        break
    else:
        print('Opção invalida -> Digite "Sim" ou "Nao"!')