'''Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''

def fatorial(num,show=False):
    fat = 1
    for i in range(1, num+1):
        if show:
            if i != num:
                print(f"{i}", end=' x ')
            else:
                print(f"{i}", end=' = ')
        fat *= i
    
    return fat

print(fatorial(5,False))
