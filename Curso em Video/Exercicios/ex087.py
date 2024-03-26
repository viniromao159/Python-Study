'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[],[],[]]
s_linha = []
soma_t = pares = 0


for i in range(len(matriz)):
    for v in range(3):
        valor = int(input(f"Digite um valor para [{i},{v}]: "))
        matriz[i].append(valor)

for i in range(len(matriz)):
    for v in range(len(matriz[i])):
        
        if matriz[i][v] % 2 == 0:
            pares += matriz[i][v]
        
        if v == 2:
            soma_t += matriz[i][v]
        
        if i == 1:
            s_linha.append(matriz[i][v])

print(f"A soma dos valores pares é: {pares}")
print(f"A soma dos valores da terceira coluna é: {soma_t}")
print(f"O maior valor da segunda linha é: {max(s_linha)}")
