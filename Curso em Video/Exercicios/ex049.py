num = int(input("Digite o numero para tabuada: "))
stop = int(input("Digite o numero que desejar parar a tabuada: "))

for n in range(0, stop+1):
  print(f"{num} x {n} = {num * n}")