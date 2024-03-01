'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = input("Digite a frase do dia: ").lower()

"""rep_a = []
for a in frase:
    if a == "a":
        rep_a.append(a)"""

print(f"Na frase do dia apareceu a letra A {frase.count("a")}x!") #Conta
print(f"A posição do primeiro A é no index {frase.find("a")+1}!") #procura o primeiro a e retorna o index
print(f"A ultima posição do A é no index {frase.rfind("a")+1}!") #procura o primeiro a começando pela direita e retorna o index