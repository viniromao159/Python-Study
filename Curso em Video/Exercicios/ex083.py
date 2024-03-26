'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressao = input("Digite a expressão: ")

pilha = []
for letra in expressao:
    pilha.append(letra)

if pilha.count("(") != pilha.count(")"):
    print("Expressão invalida!")
else:
    print("Expressão valida!")
