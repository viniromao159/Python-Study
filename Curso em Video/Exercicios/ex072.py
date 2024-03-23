'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez",
           "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Escreva um numero entre 0 - 20: "))
    
    if num >= 0:
        print(f"Você digitou o número {numeros[num]}!")
    
    else:
        print("Valor inválido!")
        
    continuar = input("Deseja continuar S/N: ").lower().strip()
    while continuar not in ['s', 'n']:
        print("Valor incorreto!")
        continuar = input("Deseja continuar S/N: ").lower().strip()
        
    if "n" == continuar:
        break
