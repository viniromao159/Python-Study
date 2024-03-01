#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number = int(input("Digite primeiro: "))
number2 = int(input("Digite segundo: "))
number3 = int(input("Digite terceiro: "))

if number > number2 and number > number3:
    high_number = number
    if number2 > number3:
        low_number = number3
    else:
        low_number = number2     
elif number2 > number and number2 > number3:
    high_number = number2
    if number > number3:
        low_number = number3
    else:
        low_number = number
        
elif number3 > number and number3 > number2:
    high_number = number3
    if number > number2:
        low_number = number2
    else:
        low_number = number
    
    
print(f"O menor é {low_number}")
print(f"O maior é {high_number}")
    
        

