'''inteiros = [1,2,3,4,5,7,8,9]
pares = [numero for numero in inteiros if numero %2 == 0]

print(pares)'''

inteiros = [1,2,3,4,5,7,8,9,10]
pares = []
impares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Pares:{pares}")
print(f"Impares:{impares}")