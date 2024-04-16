def aumentar(preco):
        return preco + (preco*10/100)

def diminuir(preco):
        return preco - (preco*13/100)

def dobro(preco):
        return preco * 2

def metade(preco):
        return preco / 2
        
def moeda(preco, moeda="R$"):
        return f'{moeda}{preco:.2f}'.replace('.',',')