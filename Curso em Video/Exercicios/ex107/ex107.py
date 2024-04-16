import moeda

p = float(input("Digite o preço: R$"))
print(f"A metade de R${p} é R${moeda.metade(p):.2f}")
print(f"O dobro de R${p} é R${moeda.dobro(p):.2f}")
print(f"Aumentando 10% de R${p}, temos R${moeda.aumentar(p):.2f}")
print(f"Reduzindo 13% de R${p}, temos R${moeda.diminuir(p):.2f}")