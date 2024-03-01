#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

alunos = []

while len(alunos) < 4:
  alunos.append(input("Digite o nome do aluno: "))

# Ordena aleatóriamente a lista
random.shuffle(alunos)

# Apresenta o aluno segudo da ordem numerica
for index, aluno in enumerate(alunos, 1): 
  print(f"{index}º - {aluno}")