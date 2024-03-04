valor = int(input("Digite um valor inteiro par:"))

if valor % 2 == 0:
    pares = []
    for par in range(valor+1):
        if par % 2 == 0:
          pares.append(par)
        else:
            pass
    print(pares)
else:
    print("Valor impar!")