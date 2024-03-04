'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

somaidade = 0
maiorhomem = 0
nomehomem = 0
mulhermenor = 0

for p in range(0,4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M | F): ").lower().strip()
    print("-"*20)
    
    somaidade += idade #Soma as idades pra média
    
    if p == 0 and sexo in "m":
        maiorhomem = idade
        nomevelho = nome
    
    if sexo in "m" and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    
    if sexo in "f" and idade < 20:
        mulhermenor += 1

mediaidade = somaidade / 4

print(f"A média de idade deste grupo é: {mediaidade}")
print(f"O homem mais velho se chama {nomevelho} e sua idade é {maiorhomem} anos!")
print(f"Existem {mulhermenor} mulher menor de 20 anos no grupo!")
