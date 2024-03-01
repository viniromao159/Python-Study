while True:
    try: # Tente isso
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))

        divisão = num1 / num2
    except ValueError: # Se der esse erro, faça isso
        print("Valor incorreto, digite um numero para divisão")
    except ZeroDivisionError:
        print("Não é possivel dividir por 0")
    else:#Se não de erro mostre isso
        print(f"valor da divisão é {divisão}")
        break
    finally: #Mostre isso independete
      print("Esse é o finally")

    