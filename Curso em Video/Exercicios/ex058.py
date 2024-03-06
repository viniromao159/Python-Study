'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random
from time import sleep

secret_number = random.randint(1,10)
attempt_cont = 0
while True:
    print("+-+-"*15)
    attempt = int(input("Digite seu chute de 1 a 10: "))
    attempt_cont += 1
           
    if attempt < 0 or attempt > 10:
        print("Numero invalido! Tente novamente!")
        attempt_cont -= 1
        
    else:
        if attempt == secret_number:
            print(f"Você venceu! {secret_number} é o numero correto! Você tentou {attempt_cont}x !")
            break
        
        else:
            if attempt > secret_number:
                print(f"Errou, o numero é menor! Tente novamente! ")
            else:
                print(f"Errou, o numero é maior! Tente novamente! ")
            