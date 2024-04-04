'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''

def maior(*num): # '*' Quando não é especificado a quantidade de parametros
    print(f"Foram passados {len(num)} números!")
    print(f"O maior numero é {max(num)} e o menor é {min(num)}." if len(num) > 0 else "Lista vazia.")

maior(20,5,10,100,3)
