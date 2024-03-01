number = int(input("Digite o primeiro valor: "))
number2 = int(input("Digite o segundo valor: "))

if number > number2:
    print(f"O valor {number} é maior que o valor {number2}!")
    
elif number < number2:
    print(f"O valor {number2} é maior que o valor {number}!")
    
else:
    print(f"O valor {number} é igual ao valor {number2}!")