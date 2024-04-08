'''Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.'''

def leiaInt(valor):
    while True:
        if valor.isnumeric():
            break
        else:
            print("Valor invalido!")
            valor = input("Digite um numero inteiro: ")
    
    return valor  
            
n = leiaInt(input("Digite um numero inteiro: "))
print(f"Você digitou o número {n}.")
