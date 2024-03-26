valores = []

while True:
    valor = int(input("Digite um valor: "))
    
    valores.append(valor)
    
    cont = input("Deseja continuar? (S/N): ").lower().strip()
    if cont not in ['s', 'n']:
        print("Valor incorreto!")
        cont = input("Deseja continuar? (S/N): ").lower().strip()
    
    if cont == "n":
        break

valores.sort(reverse=True)

print(f"Foi digitado {len(valores)} valores!")
print(f"A lista em ordem decrescente: {valores}")
print("O valor 5 está na lista!" if 5 in valores else "O valor 5 não está na lista!")