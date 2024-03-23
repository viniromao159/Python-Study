'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ("CUrso", "em", "video", "exercicios", "vinicius")
vogais = "aeiou"

for palavra in palavras:
    vogais_palavra = []
    for letra in palavra:
        if letra.lower() in vogais:
            vogais_palavra.append(letra)
    
    print(f"As vogais da palavra {palavra} são: {", ".join(vogais_palavra)}")
    