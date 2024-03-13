masc = fem_mais20 = mais18 =  0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M | F): ").lower().strip()
    
    if idade >= 18:
        mais18 +=1
    
        if idade >= 20 and sexo == "f":
            fem_mais20 += 1
        
    if sexo == "m":
        masc += 1
    
    cont = 0
    while cont == 0:
        continuar = input("Deseja continuar S/N: ").lower().strip()
            
        if "s" == continuar:
            break
        
        elif "n" == continuar:
            cont+=1
        
        else:
            print("Valor incorreto!")
    
    if "n" == continuar:
        break    

print(f"Acima de 18 anos tem {mais18} pessoa!")
print(f"Tem {masc} homens cadastrados!")
print(f"Tem {fem_mais20} mulheres acima de 20 anos!")
