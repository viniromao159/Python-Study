valores = []

for i in range(1,5):
    valor = int(input(f"Digite o {i}º valor: "))
    valores.append(valor)

valores = tuple(valores)

print("O valor 9 não está presente!" if valores.count(9) == 0 else f"O valor 9 apareceu: {valores.count(9)}" )
print("O valor 3 não está presente!" if valores.count(3) == 0  else f"O valor 3 apareceu na posição: {valores.index(3)+1}º")
print(f"Os valores pares são: {[i for i in valores if i % 2 == 0]}" )