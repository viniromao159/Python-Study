#Escreva um programa para calcular o fatorial de um número

num = int(input("Fatorial de: "))
fat = 1

for n in range(1, num+1):
    fat *= n

print(f"{num}! = {fat}")