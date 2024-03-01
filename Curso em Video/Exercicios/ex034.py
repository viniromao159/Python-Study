# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite seu salario para calculo de aumento: "))

if salario > 1250:
    aumento = (salario*(10/100))
    salario = salario + aumento
    print(f"Seu novo sálario é \033[0;32mR${salario:.2f}\033[m!")
else:
    aumento = (salario*(15/100))
    salario = salario + aumento
    print(f"Seu novo sálario é \033[0;32mR${salario:.2f}\033[m!")