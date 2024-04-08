''' Faça um mini-sistema que utilize o Interactive Help do Python. 
 O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.'''

def mini_help(comando):
    print(f"Comando {comando}\n")
    help(comando)
    
while True:
    comando = input("digite um comando: ")
    if comando == "FIM":
        print("Encerrado")
        break
    else:
        mini_help(comando)
