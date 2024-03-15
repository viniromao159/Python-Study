''' Crie um programa que leia a idade e o sexo de várias pessoas. 
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

masc = fem_mais20 = mais18 =  0

while True:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo (M | F): ").lower().strip()
    
    if idade >= 18:
        mais18 +=1
    
        if idade >= 20 and sexo == "f":
            fem_mais20 += 1
        
    if sexo == "m":
        masc += 1
    
    
    continuar = input("Deseja continuar S/N: ").lower().strip()
    
    while continuar not in ['s', 'n']:
        print("Valor incorreto!")
        
        continuar = input("Deseja continuar S/N: ").lower().strip()
        
    if "n" == continuar:
        break          

print(f"Acima de 18 anos tem {mais18} pessoa!")
print(f"Tem {masc} homens cadastrados!")
print(f"Tem {fem_mais20} mulheres acima de 20 anos!")
