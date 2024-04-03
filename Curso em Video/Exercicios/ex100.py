from random import randint

def sorteia():
    lista = []
    for num in range(5):
        lista.append(randint(1,20))
    return lista

def somaPar():
    lista = sorteia()
    print(f"Valores sorteados: {lista}.")
    print(f"A soma dos valores pares é: {sum([n for n in lista if n%2==0])}.")

somaPar()