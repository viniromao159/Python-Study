''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

valores = []

while True:
    valor = int(input(f"Digite seu valor: "))
    
    if valor not in valores:
        valores.append(valor)
    
    continuar = input("Deseja continuar S/N: ").lower().strip()
    while continuar not in ['s', 'n']:
        print("Valor incorreto!")
        continuar = input("Deseja continuar S/N: ").lower().strip()
    if "n" == continuar:
        break

for num in sorted(valores):
    print(f"{num}", end=" -> ")

print("FIM")
