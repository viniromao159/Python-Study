number = int(input("Digite um numero: "))
option = int(input("Deseja converter para: 1 - Binario | 2 - Octa | 3 - Hexadecimal"))

if option == 1:
    number_bin = bin(number)
    print(F"O valor {number} em binário é: {number_bin[2:]}")
    
elif option == 2:
    number_octa = oct(number)
    print(F"O valor {number} em octa é: {number_octa[2:]}")
    
elif option == 3:
    number_hex = hex(number)
    print(F"O valor {number} em hexadecimal é: {number_hex[2:]}")
    
else:
    print("Valor inválido!")