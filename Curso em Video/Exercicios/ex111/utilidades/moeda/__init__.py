def aumentar(preco, porcent, format=False):
    result = preco + (preco * porcent / 100)
    return moeda(result) if format else result


def diminuir(preco, porcent, format=False):
    result = preco - (preco * porcent / 100)
    return moeda(result) if format else result


def dobro(preco, format=False):
    result = preco * 2
    return moeda(result) if format else result


def metade(preco, format=False):
    result = preco / 2
    return moeda(result) if format else result


def moeda(preco, moeda="R$"):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco, taxaa=5, taxar=10):
    print("-" * 30)
    print("RESUMO")
    print("-" * 30)
    print(f"Valor análisado: {moeda(preco)}")
    print(f"Dobro do valor: {dobro(preco, True)}")
    print(f"Metade do valor: {metade(preco, True)}")
    print(f"{taxaa}% de aumento: {aumentar(preco, taxaa, True)}")
    print(f"{taxar}% de redução: {diminuir(preco, taxar, True)}")
    print("-" * 30)
