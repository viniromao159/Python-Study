# Faça um programa q leia algo e mostre informações dela

txt = input("Digite algo: ")

print(f"Tipo é {type(txt)}")
print(f"É só espaço?  {txt.isspace()}")
print(f"É um numero?  {txt.isnumeric()}")
print(f"É alfabético?  {txt.isalpha()}")
print(f"É alfanumerico?  {txt.isalnum()}")
print(f"É em maiúscula?  {txt.isupper()}")
print(f"É em minuscula?  {txt.islower()}")
print(f"Está capitalizado?  {txt.istitle()}")