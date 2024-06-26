"""Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""

print("="*35)
valor = float(input("Qual valor você quer sacar? R$"))
print("="*35)

while True:
    if valor // 50 >= 1:
        print(f"Total de {int(valor // 50)} de cédulas de R$50")
        valor = valor % 50
    
    elif valor // 20 >= 1:
        print(f"Total de {int(valor // 20)} de cédulas de R$20")
        valor = valor % 20
        
    
    elif valor // 10 >= 1:
        print(f"Total de {int(valor // 10)} de cédulas de R$10")
        valor = valor % 10
        
    
    elif valor // 1 >= 1:
        print(f"Total de {int(valor // 1)} de moedas de R$1")
        valor = valor % 1   
    
    else:
        print("="*35)
        break
