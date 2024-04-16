def aumentar(preco, porcent, format=False):
    result = preco + (preco*porcent/100)
    return moeda(result) if format else result

def diminuir(preco, porcent, format=False):
    result = preco - (preco*porcent/100)
    return moeda(result) if format else result

def dobro(preco, format=False):
    result = preco * 2
    return moeda(result) if format else result

def metade(preco, format=False):
    result = preco / 2
    return moeda(result) if format else result

def moeda(preco, moeda="R$"):
        return f'{moeda}{preco:.2f}'.replace('.',',')
        