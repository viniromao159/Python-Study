'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = []
for i in range(4):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

print(f"Maior valor é {max(valores)} e sua posição é {valores.index(max(valores))+1}º!")
print(f"Menor valor é {min(valores)} e sua posição é {valores.index(min(valores))+1}º!")
