def calculo(graus, temperatura):
  if temperatura == "c": #Converte pra celsius
    conversao = (graus - 32) * 5 / 9
    print (f"O valor em Cº: {conversao}")
  elif temperatura == "f":#Converte pra Fahrenheit
    conversao = (9*graus+160)/5
    print (f"O valor em Fº: {conversao}")

graus = float(input("Digite a temperatura ou (enter) para parar: "))
temperatura = input("Deseja converter para Celsius = C | Fahrenheit = F: ").lower()

calculo(graus, temperatura)
