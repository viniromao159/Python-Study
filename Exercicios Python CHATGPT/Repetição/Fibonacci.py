#Escreva um programa para gerar os primeiros n termos da série de Fibonacci

num = 100
fib = [0, 1]

for n in range(2 , num):
    prox = fib[-1] + fib[-2]
    fib.append(prox)

print(fib)
    
