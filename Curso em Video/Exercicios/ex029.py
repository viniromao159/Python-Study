#Digite um programa que multa assima dos 80, com 7 por km a mais.

traffic_ticket = 7.00
limit = 80.00

car_speed = float(input("Digite a velocidade do carro: "))

if car_speed > limit:
    total = (car_speed - limit) * traffic_ticket
    print(f"Valor da multa é R${total:.2f}!")
else:
    print("Dentro do limite de 80km/h!")