# Crie uma lista de strings com nomes de frutas.
# Inverta a ordem dos elementos na lista.
# Imprima a lista invertida.

fruts = ["Banana", "Morango", "Laranja", "Cogumelo"]
fruts.reverse()

for idx, fruta in enumerate(fruts, 1):
  print(idx, fruta)
