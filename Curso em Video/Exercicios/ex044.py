price = float(input("Digite o valor do produto: "))
pay_style = int(input("Informe o metodo de pagamento: 1 - dinheiro | 2 - cartão: "))

if pay_style == 1:
    sale = price * (10/100)
    price = price - sale
    print(F"Desconto de 10% -> Valor do produto a ser pago: R${price:.2f}")
    
elif pay_style == 2:
    installment = int(input("Quantas parcelas: "))
    
    if installment == 1:
        sale = price * (5/100)
        price = price - sale
        print(F"Desconto de 5% -> Valor do produto a ser pago: R${price:.2f}")
        
    elif installment == 2:
        price = price
        print(F"Sem desconto -> Valor do produto a ser pago: R${price:.2f}")
        
    elif installment >= 3:
        fees = price * (20/100)
        price = price + fees
        print(F"Juros de 20% -> Valor do produto a ser pago: R${price:.2f}")
        
else:
    print("Valor Inválido!")