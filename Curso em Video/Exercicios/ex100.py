'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint

def sorteia(qtd):
    lista = []
    for num in range(qtd):
        lista.append(randint(1,20))
    return lista

def somaPar():
    lista = sorteia(5)
    print(f"Valores sorteados: {' '.join(str(n) for n in lista)}.")
    print(f"A soma dos valores pares é: {sum([n for n in lista if n%2==0])}.")

somaPar()
