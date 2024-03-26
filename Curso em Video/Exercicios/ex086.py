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