#Leia um salario e mostre o novo salario com 15% de aumento

salario = float(input("Digite o valor do salário: "))
aumento = salario + (salario*(15/100))

print(f"Seu novo salário: {aumento:.2f}")