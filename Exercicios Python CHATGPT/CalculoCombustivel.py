def tempo_velocidade():
    tempo = float(input("Digite o tempo de viagem: "))
    velocidade = float(input("Digite a velocidade média: "))
    return tempo, velocidade

def calcula_distancia(tempo, velocidade):
    return tempo * velocidade

def calcula_litros(distancia):
    return distancia/12

def imprime(velocidade, tempo, distancia, litros):
  print('Velocidade:', velocidade)
  print('Tempo:', tempo)
  print('Distância:', distancia)
  print('Litros:', litros)

tempo, velocidade = tempo_velocidade()
distancia = calcula_distancia(tempo, velocidade)
litros = calcula_litros(distancia)

imprime(velocidade, tempo, distancia, litros)