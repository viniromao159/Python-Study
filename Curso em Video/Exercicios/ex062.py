#  Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
cont = 0
limite = 10

while cont <= limite:
    print(termo)
    termo += razao
    cont += 1
    
    if cont == limite:  #Na ultima interação
        print("-"*30)
        addtermo = int(input("Deseja mostrar mais termos? Digite a quantidade: "))
        print("-"*30)
        
        if addtermo != 0:
            limite += addtermo  # Add a quantidade a mais de termo no limite do loop
            print(termo)
            termo += razao
            cont += 1
            
        else:
            print("Encerrado!")
            cont += 1
            

            