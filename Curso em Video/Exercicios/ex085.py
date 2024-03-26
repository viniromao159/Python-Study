'''Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

valores = [[],[]]

for i in range(7):
    valor = int(input(f"Digite {i+1}º valor: "))
    
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print(f"Valores pares = {valores[0]}")
print(f"Valores impares = {valores[1]}")
