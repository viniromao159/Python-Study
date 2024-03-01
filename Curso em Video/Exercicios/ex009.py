# Leia um numero e mostre sua tabuada

num = int(input("Digite o numero para tabuada: "))

for n in range(1, 11):
  print(f"{num} x {n} = {num * n}")