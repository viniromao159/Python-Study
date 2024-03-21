numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezesete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Escreva um numero entre 0 - 20: "))
    
    if num >= 0:
        print(f"Você digitou o número {numeros[num]}!")
        break
    
    else:
        print("Valor inválido!")

