#  Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
cont = 0

while cont <= 10:
    print(termo)
    termo += razao
    cont += 1
    
    while cont == 10:   #Na ultima interação
        print("-"*30)
        addtermo = int(input("Deseja mostrar mais termos? Digite a quantidade: "))
        
        if addtermo != 0:   # Se for diferente de 0
            cont2 = 1  # Cria outra flag
            print("-"*30)
            
            while cont2 <= addtermo:
                print(termo)
                termo += razao
                cont2 += 1
                
        else:
            print("Encerrado!")
            cont += 1
            