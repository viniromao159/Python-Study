import os

buy_list = []
while True:
    option = input("Escolha uma opção \n i - Inserir | r - Remover | l - Listar | s - Sair:").lower()
    
    if option == "i":
        os.system("cls")
        item = input("Oque deseja inserir na lista: ").lower()
        buy_list.append(item)
        print("Item inserido!")

    elif option == "r":
        os.system("cls")
        try:
            index = int(input("Informe o indice do item que deseja remover da lista: "))
            del buy_list[index]
        except ValueError:
            print("Valor incorreto!")
        except IndexError:
            print("Valor inexistente!")
        else:
            print("Item Removido!")

    elif option == "l":
        os.system("cls")

        if len(buy_list)==0:
            print("Lista vazia")

        for i, itens in enumerate(buy_list):
            print(i, itens)

    else:
        print("Saindo!")
        break
