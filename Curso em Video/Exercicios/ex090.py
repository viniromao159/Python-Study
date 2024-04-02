#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

aluno = {'nome':nome, 'media':media}

if media >= 7:
    aluno['situação'] = 'Aprovado'
elif media >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f"{k} -> {v}")
