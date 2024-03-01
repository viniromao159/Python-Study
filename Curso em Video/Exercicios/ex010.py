# Leia o dinheiro da pessoa e converta em dolar (U$1 = R$4,96)

carteira = float(input("Digite seu valor em carteira: "))
dolar = 4.96
conversao = carteira*dolar

print(f"Seu valor em dolar é {conversao:.2f}") # 2 casas depois da virgula