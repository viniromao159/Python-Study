'''Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

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

pares = [v for v in valores if v%2==0]
impares = [v for v in valores if v%2==1]

print(F"A lista completa é: {valores}")
print(F"A lista só com pares é: {pares}")
print(F"A lista só com impares é: {impares}")
