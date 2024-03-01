nome = input("Digite seu nome: ").lower() #Recebe o nome e deixa minusculo
idade = input("Digite sua idade: ")

if nome and idade: #True True pq contém valor
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome: #Espaço na variavel nome
        print('Seu nome contém espaço!')
    else:
        print('Seu nome não contém espaço!')   
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Não deixe campos vazios!")