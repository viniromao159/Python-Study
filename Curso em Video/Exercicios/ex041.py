birth = int(input("Digite o seu ano de nascimento: "))
category = 2024 - birth

if category < 9:
    print("Mirim!")
    
elif category < 14:
    print("Infantil!")
    
elif category < 19:
    print("Junior!")
    
elif category < 20:
    print("Sênior!")
    
else:
    print("Master!")