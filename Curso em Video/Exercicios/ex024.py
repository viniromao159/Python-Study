'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cidade = input("Digite o nome da cidade: ").lower()

cidade = cidade[:5] == "santo"

if cidade:
    print("Essa cidade começa com Santo!")
else:
    print("Essa cidade não começa com Santo!")

print(cidade)