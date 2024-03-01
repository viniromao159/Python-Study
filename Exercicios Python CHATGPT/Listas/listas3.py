lista = [10,15,87,32,32,50,50]
lista_verificada = set(lista)

if len(lista) == len(lista_verificada):
  print("Não tem duplicado")
else:
  print("Tem duplicado")
  print(f"Lista -> {lista}")
  print(f"Lista verificada -> {lista_verificada}")

