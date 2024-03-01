import re

while True:
    senha = str(input("Digite sua senha : "))
    if senha.islower():
        print("A senha deve ter pelo menos um caractere Maiusculo! ")
    elif not re.search(r'[A-Z]', senha): #verifica se tem letra com Expressões Regulares
        print("A senha deve ter pelo menos uma letra! ")
    elif len(senha) < 7 :
        print("A senha deve ter pelo menos 8 caracteres! ")
    elif senha.isalpha() :
        print("Necessita de um numero! ")
    elif senha.isalnum() :
        print("Necessita de um Caractere especial! ")
    else:
        break
    
print(senha)