distance = float(input("Digite o a distancia da viagem (em KM): "))

if distance <= 200:
    value_km = 0.50
    print(f"O valor da viagem é \033[0;31mR${value_km*distance:.2f}\033[m !")
else:
    value_km = 0.45
    print(f"O valor da viagem é \033[0;31mR${value_km*distance:.2f}\033[m !")