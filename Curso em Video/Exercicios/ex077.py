palavras = ("CUrso", "em", "video", "exercicios", "vinicius")
vogais = "aeiou"

for palavra in palavras:
    vogais_palavra = []
    for letra in palavra:
        letra = letra.lower()
        if letra in vogais:
            vogais_palavra.append(letra)
    
    print(f"As vogais da palavra {palavra} são: {", ".join(vogais_palavra)}")