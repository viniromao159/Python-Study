# Leia o preço e ao apresente com 5% de desconto

preco = float(input("Digite o valor do produto: "))
preco_desconto = preco - (preco * (5/100))

print(f"Preço com desconto: R${preco_desconto:.2f}")