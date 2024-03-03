a_side = float(input("Valor da RETA A: "))
b_side = float(input("Valor da RETA B: "))
c_side = float(input("Valor da RETA C: "))

if a_side < b_side + c_side and b_side < a_side + c_side and c_side < b_side + a_side:
    print("É possivel formar um \033[0;33mTRIANGULO!\033[m!")
    
    if a_side == b_side == c_side:
        print("Triangulo EQUILÁTERO!")
    
    elif a_side != b_side != c_side != a_side :
        print("Triangulo ESCALENO!")
        
    else:
        print("Triangulo ISÓSCELES!")
        
else:
    print("Não é possivel formar um \033[0;33mTRIANGULO\033[m!")