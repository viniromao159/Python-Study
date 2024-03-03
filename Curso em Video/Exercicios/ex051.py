termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))

total = 0
for t in range(1, 10):
    if t == 1:
        print(termo)
        total += termo
        
    total += razao
    print(total)