def maior(lista):
    lista = lista
    lista.sort()
    print(f"Foram passados {len(lista)} números!")
    print(f"O maior numero é {max(lista)} e o menor é {min(lista)}." if len(lista) > 0 else "Lista vazia.")

maior([20,50,60,230,815])