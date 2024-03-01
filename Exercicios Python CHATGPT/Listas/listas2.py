# Crie uma lista de números inteiros.
# Calcule e imprima a soma de todos os elementos da lista.
# Calcule e imprima a média dos elementos da lista.

numeros = []

for i in range(10):
  numeros.append(i+1)

print(numeros)

somaList = sum(numeros) #soma a lista
mediaList = somaList / len(numeros)

print(somaList)
print(mediaList)