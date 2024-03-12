while True:
    print("-"*30)
    x = int(input("Digite um numero para ver a tabuada: "))
    print("-"*30)
    
    if x < 0:
        print("Fim!")
        break
    
    else:
        for div in range(1, 11):
            print(f"{x} x {div} = {x*div}")