weight = float(input("Digite seu peso (KG): "))
height = float(input("Digite sua altura (M): "))
imc = weight / (height**2)

if imc < 18.5:
    print("Abaixo do peso!")
    
elif imc < 25:
    print("Peso Ideal!")
    
elif imc < 30:
    print("Sobrepeso!")
    
elif imc < 40:
    print("Obesidade!")
    
else:
    print("Obesidade mórbido!")