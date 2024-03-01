# Crie uma lista de 10 números inteiros.
# Crie uma sublista contendo apenas os elementos nas posições ímpares da lista original.
# Imprima a sublista.

numeros = [10,15,48,74,65,12,85,7,15,3]

pares = []

for ipar, valor in enumerate(numeros):
  if ipar % 2 == 0:
    pares.append(valor)
    print(valor)
  


