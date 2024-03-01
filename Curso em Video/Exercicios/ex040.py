note1 = float(input("Digite a primeira nota: "))
note2 = float(input("Digite a segunda nota: "))
media = (note1 + note2) / 2

if media < 5.0:
    print("REPROVADO!")
    
elif media >= 5.0 and media < 7.0:
    print("Recuperação!")
    
else:
    print(f"APROVADOOO!!!! -> Sua nota fina: {media}!")