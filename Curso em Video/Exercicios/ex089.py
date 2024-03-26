'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos_nota = []

while True:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite o nota 1 do aluno: "))
    nota2 = float(input("Digite o nota 2 do aluno: "))
    
    alunos_nota.append([nome,[nota1,nota2]])
    
    continuar = input("(N) para parar: ").lower().strip()
    if "n" in continuar:
        break
    
print("=-"*30)
    
for i,aluno in enumerate(alunos_nota):
    print(f"{i} - Nome: {aluno[0]} - Média: {sum(aluno[1]) / 2}")

print("=-"*30)
    
while True:
    notas = int(input("Mostar notas de qual aluno? (999 - parar): "))
    
    if notas < len(alunos_nota):
        print(f"Notas do aluno {alunos_nota[notas][0]} são: {alunos_nota[notas][1]}")
        print("-"*30)
        
    elif notas == 999:
        print("FIM!")
        break
    
    else:
        print("Aluno não encontrado!")
        print("-"*30)