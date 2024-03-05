cont = 1
while cont > 0:
    num = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o primeiro numero: "))
    print("-"*30)
    cont += 1
    
    while cont == 2:
        menu = int(input("MENU:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Numeros\n[5] Sair\nOpção: "))
        print("-"*30)
        
        if menu == 1:
            print(f"\033[0;32mSoma dos valores é: {num + num2}\033[m")
            print("-"*30)
            
        if menu == 2:
            print(f"\033[0;32mMultiplicação dos valores é: {num * num2}\033[m")
            print("-"*30)
            
        if menu == 3:
            if num > num2:
                print(f"\033[0;32mO maior numero é: {num}\033[m")
                print("-"*30)
                
            elif num < num2:
                print(f"\033[0;32mO maior numero é: {num2}\033[m")
                print("-"*30)
                
            else:
                print(f"\033[0;32mO numeros são iguais!\033[m")
                print("-"*30)
                
        if menu == 4:
            cont -= 1
        
        if menu == 5:
            print(f"\033[0;34mEncerrado!\033[m")
            cont -= 2
            
        else:
            print(f"\033[0;34mValor incorreto!\033[m")
            