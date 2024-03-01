#gere um numero e faça o usuario descobrir qual é
import random

#Gera o valor aleatório (Inteiro)
secret_number = random.randint(0,5)

#Caso o valor nao seja int apresenta o erro
try:
    print("+-+-"*15)
    attempt = int(input("Digite seu chute de 0 a 5: ").center(30, '-'))
    print("+-+"*20)
except ValueError:
    print("Valor invalido!")
    
if attempt < 0 or attempt > 5:
    print("Numero invalido!")
else:
    if attempt == secret_number:
        print(f"Você venceu! {secret_number} é o numero correto!")
    else:
        print(f"Você perdeu! O numero correto era {secret_number}!")
            
