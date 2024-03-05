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
            print(f"Errou! Tente novamente!")