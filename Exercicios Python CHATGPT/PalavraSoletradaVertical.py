palavra = input("Digite uma palavra: ").upper()

for i in palavra:
    if i == " ":
      print('-')
    else:
      print(i)
