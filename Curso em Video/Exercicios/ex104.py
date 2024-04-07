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