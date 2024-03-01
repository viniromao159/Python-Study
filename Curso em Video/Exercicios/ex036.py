house = float(input("Digite o valor da casa: "))
payment = float(input("Digite seu salário: "))
installment = float(input("Digite a quantidade de parcelas: "))

loan = (house/installment) < (payment*(30/100))

if loan:
    print(f"Empréstimo aprovado!")
else:
    print(f"Empréstimo reprovado!")