# Crie uma tupla chamada precos com três valores de preços. Em seguida, crie uma nova tupla chamada precos_dobrados que contenha o dobro de cada preço da tupla original.

precos = (10, 53, 25, 12)

precos_dobrados = []

for preco in precos:
  precos_dobrados.append(preco*2)

precos_dobrados = tuple(precos_dobrados)

print(type(precos_dobrados))
print(precos_dobrados)