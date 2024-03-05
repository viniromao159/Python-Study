termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
total = 0
cont = 0

while cont <= 10:
    
    if cont == 0: #primeita interação adiciona e apresenta o valor do termo
        print(termo)
        total += termo
        cont += 1
    
    else: 
        total += razao
        print(total)
        cont += 1
    
    while cont == 10: #Na ultima interação
        addtermo = int(input("Deseja mostrar mais termos? Digite a quantidade:"))
        
        if addtermo != 0: # Se for diferente de 0
            
            cont2 = 1 # Cria outra flag
            while cont2 <= addtermo:
                total += razao
                print(total)
                cont2 += 1
                
        else:
            print("Encerrado!")
            cont += 1