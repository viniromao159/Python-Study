#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

primo = int(input("Digite um numero: "))

if primo <= 1:
    print("Não é primo!")

elif primo == 2:
    print("É primo!")

else:
    
    for i in range(2, primo): 
        
        if (primo % i) == 0:        #Se primo divido por i sobrar 0, significa que ele contém um divisor alem de 1 e ele mesmo.
            print("Não é primo!")
            break
        
    else:
        print("É primo!")
