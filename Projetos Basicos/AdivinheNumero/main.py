import random

def chutes(chances, sorte):
  while True:
    try:
      if chances > 0:
        print(f"Você tem {chances} chances!")
        chute = int(input("Digite seu chute: "))
        if chute < sorte:
          print("Menor que o numero secreto!")
          chances -= 1
        elif chute > sorte:
          print("Maior que o numero secreto!")
          chances -= 1
        elif chute == sorte:
          print(f"Voce acertouuu! Numero secreto é: {sorte} !")
          break
      else:
          print(f"Voce Perdeu! Numero secreto era: {sorte} !")
          break
    except ValueError:
      print('Opção invalida!')

while True:
    opcao_inicial = input('Selecione a dificuldade (Facil = 1 a 10 | Medio = 1 a 50 | Dificil = 1 a 10): ').lower()
    if opcao_inicial == "facil":
      sorte = random.randrange(11)
      chances = 3
      chutes(chances, sorte)

    elif opcao_inicial == "medio":
      chances = 8
      sorte = random.randrange(51)
      chutes(chances, sorte)

    elif opcao_inicial == "dificil":
      chances = 10
      sorte = random.randrange(101)
      chutes(chances, sorte)
    else:
      print('Opção invalida!')

    opcao = int(input("Deseja jogar novamente: 1 - Sim | 2 - Não: "))
    if opcao == 1:
      continue
    elif opcao == 2:
      print("FIM DE JOGO!")
      break
    else:
      print('Opção invalida!')
    

  



