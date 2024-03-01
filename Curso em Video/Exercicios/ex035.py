# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

a_side = float(input("Valor da RETA A: "))
b_side = float(input("Valor da RETA B: "))
c_side = float(input("Valor da RETA C: "))

if a_side < b_side + c_side and b_side < a_side + c_side and c_side < b_side + a_side:
    print("É possivel formar um \033[0;33mTRIANGULO!\033[m!")
else:
    print("Não é possivel formar um \033[0;33mTRIANGULO\033[m!")