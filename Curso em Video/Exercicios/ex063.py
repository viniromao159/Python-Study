# leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

n = int(input("Digite o valor para sequencia de fibonacci: "))
fib = [0,1]

cont = 2
while cont < n:
    proxseq = fib[-1]+fib[-2]
    fib.append(proxseq)
    cont += 1

for i in fib:
    print(i, end=" -> ")
    if i == fib[-1]:
        print("FIM")
    