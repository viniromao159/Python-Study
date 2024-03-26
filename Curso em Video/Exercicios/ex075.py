'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

valores = []

for i in range(1,5):
    valor = int(input(f"Digite o {i}º valor: "))
    valores.append(valor)

valores = tuple(valores)
pares = [i for i in valores if i % 2 == 0]

print("O valor 9 não está presente!" if 9 not in valores else f"O valor 9 apareceu {valores.count(9)}x!" )
print("O valor 3 não está presente!" if 3 not in valores  else f"O valor 3 apareceu na {valores.index(3)+1}º posição!")
print(f"Os valores pares são: {pares}" if pares else "Não tem números pares!" )
