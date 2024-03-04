#Escreva um programa para calcular a soma dos dígitos de um número inteiro

num = 123
total = 0

for n in str(num):
    total += int(n)

print(total)
