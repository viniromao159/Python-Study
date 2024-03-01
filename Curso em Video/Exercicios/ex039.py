birth = int(input("Digite o seu ano de nascimento: "))
army_time = 2024 - birth

if army_time < 18:
    print(f"Você tem {army_time} anos, não precisa se alistar!")
    
elif army_time == 18:
    print(f"Você tem {army_time} anos, precisa se alistar!")
    
else:
    print(f"Você tem {army_time} anos, passou o tempo de alistamento!")