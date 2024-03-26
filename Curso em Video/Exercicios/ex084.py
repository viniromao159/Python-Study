'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

grupo = []

while True:
    nome = str(input("Digite seu nome: "))
    peso = int(input("Digite seu peso: "))
    
    grupo.append([nome, peso])
    
    continuar = input("(N) para parar: ").lower().strip()
    
    if "n" in continuar:
        break

pesos = []
for pessoa in grupo:
    pesos.append(pessoa[1])

print(f"Foram cadastrado {len(grupo)} pessoas!")
print(f"O maior peso foi {max(pesos)} Kg. Peso de: {[pessoa[0] for pessoa in grupo if pessoa[1] == max(pesos)]}")
print(f"O menor peso foi {min(pesos)} Kg. Peso de: {[pessoa[0] for pessoa in grupo if pessoa[1] == min(pesos)]}")
