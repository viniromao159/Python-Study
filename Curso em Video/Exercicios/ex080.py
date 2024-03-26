'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

valores = []

for i in range(4):
    valor = int(input("Digite um numero: "))
    
    if i == 0:
        valores.append(valor)
        
    else:
        for i, v in enumerate(valores):
            if valor >= v:
                valores.append(valor)
                break
            else:
                valores.insert(i, valor)
                break
       
print(f"A lista em ordem é: {valores}")
