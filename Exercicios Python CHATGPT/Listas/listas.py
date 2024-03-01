# Crie uma lista vazia chamada numeros.
# Adicione os números de 1 a 5 à lista.
# Imprima a lista.
# Remova o número 3 da lista.
# Imprima a lista novamente.

numeros = []

for i in range(1,6):
  numeros.append(i)

print(numeros)

numeros.remove(3)

print(numeros)