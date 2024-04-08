'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(jogador="<Desconhecido>", gol=0):
    print(f"O nome do jogado é {jogador}. Seus gols são {gol}.")

nome = input("Digite o nome do jogador: ")
gols = input("Quantos gols foram feitos: ")

ficha()
