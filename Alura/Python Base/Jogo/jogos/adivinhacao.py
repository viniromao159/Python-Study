import random

def jogar_adivinhacao():

    print("----------------------------------\n")
    print("Bem vindo ao jogo de adivinhação!\n")
    print("----------------------------------\n")

    secret_number = int(random.randrange(1,101))

    print(secret_number)

    cont = 1
    while cont == 1:
        print("Niveis: (1)Fácil - (2)Médio - (3)Difícil ")
        nivel = int(input("Escolha o nivel do jogo: "))

        if nivel == 1:
            full_attempt = 15
            cont += 1
        elif nivel == 2:
            full_attempt = 10
            cont += 1
        elif nivel == 3:
            full_attempt = 5
            cont += 1
        else:
            print("\nNivel inválido!\n")

    for rounds in range(1, full_attempt+1):
        print(f"\nTentativa {rounds} de {full_attempt} tentativa!")

        attempt = int(input("Digite seu número entre 1 e 100: "))

        print(f"\nVocê digitou: {attempt}\n")

        if attempt < 1 or attempt > 100:
            print("Você deve digitar um numero entre 1 e 100!\n ")
            continue

        if attempt == secret_number:
            print("VOCÊ ACERTOUUUUUUU!")
            break
        else:
            if attempt > secret_number:
                print("O numero secreto é MENOR !\n")
                continue
            elif attempt < secret_number:
                print("O numero secreto é MAIOR !\n")
                continue

    print("----------------------------------")
    print(f"Número secreto: {secret_number}")
    print("----------------------------------")        
    print("Fim do jogo!")
    print("----------------------------------")

if(__name__ == "__main__"):
    jogar_adivinhacao()