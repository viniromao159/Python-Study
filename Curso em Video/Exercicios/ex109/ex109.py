import moeda

p = float(input("Digite o preço: R$"))
print(f"A metade de {p} é {moeda.metade(p)}")
print(f"O dobro de {p} é {moeda.dobro(p,True)}")
print(f"Aumentando, temos {moeda.aumentar(p,10,True)}")
print(f"Reduzindo, temos {moeda.diminuir(p,13,True)}")