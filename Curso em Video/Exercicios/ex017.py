#Leia o comprimento do cateto oposto e cateto adjacente de um triangulo retangulo, e calcule e mostre o comprimento da hipotenusa
import math

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente) # (cateto_oposto ** 2 + cateto_adjacente ** 2 ) ** (1/2)

print(f"O Valor da hipotenusa é {hipotenusa}")