def area(largura, comprimento):
    area = largura * comprimento
    return f'A área de um terreno {largura}x{comprimento} é de {area}m².'

largura = float(input("Digite a largura (M): "))
comprimento = float(input("Digite o comprimento (M): "))

print(area(largura, comprimento))