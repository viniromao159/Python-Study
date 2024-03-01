# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = 60.00
km = 0.15

aluguel_dias = int(input("Quantos dias alugado? "))
km_rodados = float(input("Quantos KM rodados? "))

valor_total = (aluguel_dias*dia) + (km_rodados*km)

print(f"O total a pagar é de R${valor_total}")