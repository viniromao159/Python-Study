'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contador(inicio, fim, passo):
    for i in range(1,11):
        print(i, end= ' ')
    print()
    
    for c in range( 10, -1, -2):
        print(c, end= ' ')
    print()
    
    # Se passo for zero, conta de 1 em 1
    if passo == 0:
        passo = 1 
    #Ajusta o passo de acordo com inicio e fim    
    if fim < inicio and passo > 0:
        passo = passo * -1
    #Inverte o inicio e fim caso o passo seja negativo  
    if passo < 0 and inicio < fim:
        inicio, fim = fim, inicio
    
    for j in range(inicio, fim, passo):
        print(j, end= ' ')
    print()

contador(10, 0, 2)
