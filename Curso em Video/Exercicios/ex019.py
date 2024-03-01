# Professor quer sorte um dos seus qautros alunos para apagar o quadro, faça um programa le o nome dos alunos e escreve o nome escolhido.
import random

#Cria e insere 4 nomes na lista.
alunos = []

while len(alunos) < 4:
  alunos.append(input("Digite o nome do aluno: "))

print(f"Aluno sorteado é {alunos[random.randint(0,3)]}")
