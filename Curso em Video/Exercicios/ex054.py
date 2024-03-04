#leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

maior18 = 0
menor18 = 0
atual = date.today().year #Importa o ano atual

for y in range(0,7):
    year = int(input("Digite seu ano de nascimento: "))
    if atual - year >= 21:
        maior18 += 1
    else:
        menor18 += 1

print(f"Dessas pessoas, {maior18} são maiores de idade e {menor18} são menores de idade!")
