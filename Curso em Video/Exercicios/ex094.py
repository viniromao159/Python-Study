'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

pessoas = []

while True:
    nome = input("Nome: ")
    sexo = input("Sexo: [M/F] ").lower()
    while sexo not in ['m', 'f']:
        print("Sexo inválido!")
        sexo = input("Sexo: [M/F] ").lower()
    idade = int(input("Idade: "))
    
    pessoas.append({'nome':nome, 'sexo':sexo, 'idade':idade})
    
    cont = input("Continuar: [S/N] ").lower()
    while cont not in ['s', 'n']:
        print("Valor inválido!")
        cont = input("Continuar: [S/N] ").lower()
    if cont == 'n':
        break
print('=-'*20)

print(f'-> O grupo tem {len(pessoas)} pessoas.')

idade = []
for p in pessoas:
    idade.append(p['idade'])
media = sum(idade)/len(idade)
print(f'-> A média de idade é de {media}.')

mulheres= []
for p in pessoas:
    if p['sexo'] == 'f':
        mulheres.append(p['nome'])
print('-> Não tem mulheres no grupo.' if len(mulheres) == 0 else f'-> As mulheres do grupo são: {', '.join(mulheres)}.')

print(f'-> Lista de pessoas acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        print(f'Nome = {p['nome']}; Sexo = {p['sexo']}; Idade = {p['idade']};')
