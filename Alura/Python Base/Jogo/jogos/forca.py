import random

def jogar_forca():

    intro_game()

    secret_word = load_secret_word()

    correct_word = correct_wordfunc(secret_word)
    
    print(correct_word)

    win = False
    dead = False
    erros = 0

    while (not win and not dead):

        attemp = attemp_player()
        attemptype = attemp_type(attemp)

        if attemptype == 1:
            if(attemp in secret_word):
                attemp_correct_position(attemp, secret_word, correct_word)
            else:
                erros += 1
                desenha_forca(erros)

        elif attemptype > 1:
            if(attemp == secret_word):
                attemp_correct_position(attemp, secret_word, correct_word)
            else:
                erros += 1
                desenha_forca(erros)
        
        if erros == 7:
            break
        if  ("_" not in correct_word):
            break
        print(correct_word,"\n")
        
    if("_" not in correct_word):
        message_winner()    
    else:
        message_loser(secret_word)

    print("Fim do jogo")

#Functions

def intro_game():#Introdução

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def load_secret_word():#Carrega a palavra secreta

    arq = open("C:\WorkSpace\Alura\Cursos\Python\Python I\Jogos\jogos\word.txt","r")
    word = []

    for linha in arq:
        linha = linha.strip()
        word.append(linha)

    arq.close()

    number = random.randrange(0, len(word))
    secret_word = word[number].upper()

    return secret_word

def correct_wordfunc(secret_word):#Modela as letras a serem adivinhadas

    lista = ["_" for word in secret_word ]
    return lista

def attemp_player():#Tentativa do jogador
    attemp = int(input("Chutar letra (1) / Adivinhar tudo(2): "))
    if attemp == 1:
        attemp = input("Qual letra: ").strip()
        attemp = attemp.strip().upper()
        return attemp
    elif attemp == 2:
        attemp = input("Qual palavra: ").strip()
        attemp = attemp.strip().upper()
    else:
        print("Opção inválida!")

def attemp_correct_position(attemp, secret_word, correct_word):#Coloca a tentativa correta na posição certa
    index = 0
    for word in secret_word:
        if attemp == word:
            correct_word[index] = word
        index += 1

def attemp_type(attemp):
    attemptype = len(attemp)
    return attemptype
       
def message_winner():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def message_loser(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar_forca()