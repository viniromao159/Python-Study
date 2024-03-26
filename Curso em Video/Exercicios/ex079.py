
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

