expressao = input("Digite a expressão: ")
'''exp = []
for letra in expressao:
    exp.append(letra)'''

if expressao.count("(") != expressao.count(")"):
    print("Expressão invalida!")
else:
    print("Expressão valida!")