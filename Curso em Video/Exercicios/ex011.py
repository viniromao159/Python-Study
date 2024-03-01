# Leia a largura e altura, calcule a sua area e a quanrtidade de tinta necessária para pinta-la (Cada litro de tinta pinta uma área de 2m²)

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
area = largura * altura
tinta = area / 2

print(f"Sera necessário {tinta:.2f} litros para pintar a parede!")