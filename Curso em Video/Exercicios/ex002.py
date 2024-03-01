# Recebe um nome e imprime mensagem de boas vindas

nome = input("Digite seu nome: ")

print(f"Bem vindo, \033[0;31m{nome}\033[m!")
print("Bem vindo, {}!".format(nome))