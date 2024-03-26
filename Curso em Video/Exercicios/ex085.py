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