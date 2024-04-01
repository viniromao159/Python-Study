nome = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

aluno = {'nome':nome, 'media':media}

if media > 7:
    aluno['estado'] = 'Aprovado'
else:
    aluno['estado'] = 'Reprovado'

for k, v in aluno.items():
    print(f"{k} -> {v}")
