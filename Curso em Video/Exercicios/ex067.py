'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo. '''

while True:
    print("-"*30)
    x = int(input("Digite um numero para ver a tabuada: "))
    print("-"*30)
    
    if x < 0:
        print("Fim!")
        break
    
    else:
        for mult in range(1, 11):
            print(f"{x} x {mult} = {x*mult}")
            