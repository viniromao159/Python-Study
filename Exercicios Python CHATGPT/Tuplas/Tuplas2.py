# Crie uma função chamada encontrar_maior_menor que recebe uma tupla de números como argumento e retorna o maior e o menor número da tupla.

def encontrar_maior_menor(tupla):
  maior = 0
  menor = 0
  for numero in tupla:
    if numero > maior:
      maior = numero
    elif numero <= menor:
      menor = numero
  
  return menor, maior


numeros = (2, 5, 8, 9, 0, 15)
menor, maior = encontrar_maior_menor(numeros)

print(menor, maior)