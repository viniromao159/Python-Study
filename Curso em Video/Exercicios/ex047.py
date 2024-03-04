#Mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print("--"*10,"PARES!","--"*10)

for n in range(1, 50):
    if n % 2 == 0:
        print(n)

print("--"*10,"FIM!","--"*10)
