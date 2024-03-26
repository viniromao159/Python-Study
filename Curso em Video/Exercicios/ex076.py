'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = (("Lapis", 1.00), ("Borracha", 2.00), ("Caneta", 2.50), ("Caderno", 10.00))

print("PRODUTOS E PREÇOS")
for item in listagem:
    for i in range(1):
        print(f"{item[i]} -> R${item[i+1]:.2f}")
