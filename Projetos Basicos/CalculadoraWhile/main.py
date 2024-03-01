while True:
    n1 = input("Digite o valor: ")
    n2 = input("Digite outro valor: ")
    operador = input("Digite o operador (+-): ")
    
    numero_validos = None
    n1float = 0
    n2float = 0
    operador_validos = "+-*/"
    
    try:
        n1float = float(n1)
        n2float = float(n2)
        numero_validos = True
    except:
        numeros_validos = None
        
    if numero_validos is None:
        print("Um ou ambos os numeros digitados são inválidos!")
        continue
    
    if operador not in operador_validos:
        print("Operador invalidado!")
        continue
    
    print("Calculando, resulado a baixo")
    if operador == "+" :
        print(f'{n1float} + {n2float} = {(n1float + n2float)}')
    if operador == "-":
        print(f'{n1float} - {n2float} = {(n1float - n2float)}')
    if operador == "*":
        print(f'{n1float} * {n2float} = {n1float  * n2float}')
    if operador == "/":
        print(f'{n1float} / {n2float} = {n1float / n2float}')
    
    sair = input("Deseja [s]air: ").lower().startswith("s")
    if sair is True:
        print("Encerrando!")
        break