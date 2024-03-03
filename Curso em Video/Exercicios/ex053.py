frase = input("Digite uma frase: ").replace(" ","").lower()
frase_inv = ''

for letra in frase:
    frase_inv = letra + frase_inv       #Concatena a esquerda (De acordo com a sequencia) a letra da frase 

if frase == frase_inv:
    print("Palíndromo!")
else:
    print("Não é palíndromo!")

#frase[::-1] faz o programa executar a leitura de tras pra frente. (inverte a frase)
