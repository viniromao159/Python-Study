'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date

dados = dict()

dados['nome'] = input("Nome: ")
ano_nasc = int(input("Ano de nascimento: "))
dados['idade'] = date.today().year - ano_nasc
dados['cpts'] = input("Carteira de trabalho(não tem 0): ")
if dados['cpts'] != "0": 
    dados['ano_contr'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário: "))
    dados['aposenta'] = (35 - (date.today().year - dados['ano_contr'])) + dados['idade']

for d, v in dados.items():
    print(f"O {d} tem valor {v}!" if v != '0' else f"Não tem {d}")
