# Leia um angulo e mostre o valor de cosseno, seno e tangente desse angulo
import math

angulo = int(input("Digite um angulo: "))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print(f"Cosseno deste angulo é: {cos:.2f}\nSeno deste angulo é: {sen:.2f}\nTangente desse angulo é: {tang:.2f}")