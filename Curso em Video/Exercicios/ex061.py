termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
total = 0

cont = 1
while cont <= 10:
    if cont == 1:
        print(termo)
        total += termo
        cont += 1
    
    total += razao
    print(total)
    cont += 1