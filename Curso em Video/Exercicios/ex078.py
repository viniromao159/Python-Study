
valores = []
for i in range(4):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

print(f"Maior valor é {max(valores)} e sua posição é {valores.index(max(valores))+1}º valor!")
print(f"Menor valor é {min(valores)} e sua posição é {valores.index(min(valores))+1}º valor!")
