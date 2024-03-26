'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[],[],[]]

for i in range(len(matriz)):
    for v in range(3):
        valor = int(input(f"Digite um valor para [{i},{v}]: "))
        matriz[i].append(valor)

print("=-"*30)

for l in range(len(matriz)):
    for v in range(len(matriz[l])):
        print(matriz[l][v], end=" ")
    print()
