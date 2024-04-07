def mini_help(comando):
    print(f"Comando {comando}\n")
    help(comando)
    
while True:
    comando = input("digite um comando: ")
    if comando == "FIM":
        print("Encerrado")
    else:
        mini_help(comando)
