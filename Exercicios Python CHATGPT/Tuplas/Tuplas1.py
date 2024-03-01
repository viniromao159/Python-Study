# #Tuplas são feitas para não serem alteradas

# #Crie uma tupla chamada frutas com três frutas de sua escolha. Em seguida, imprima cada fruta em uma linha.
# frutas = ("Banana", "Laranja", "morango")

# for fruta in frutas:
#   print(fruta)

# #Crie uma tupla chamada numeros com cinco números inteiros. Calcule a soma dos números e imprima o resultado
# numeros = (10, 20 ,30 ,40 ,50)

# print(sum(numeros))

# #Dada a tupla cores = ('vermelho', 'verde', 'azul'), altere a cor 'verde' para 'amarelo'. Imprima a tupla modificada.
# cores = ('vermelho', 'verde', 'azul')
# cores = list(cores)

# cores[1] = "amarelo"

# cores = tuple(cores)

# print(cores)

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

