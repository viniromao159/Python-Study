# Leia um numero real e mostre na tela sua porção inteira

from math import floor, trunc

num = float(input("Digite um valor real: "))
num1 = floor(num) # Arredonda pro inteiro menor
num2 = trunc(num) # Apresenta o inteiro do numero


print(f"A porção inteira é {num1} ou {int(num)} ou {num2}")