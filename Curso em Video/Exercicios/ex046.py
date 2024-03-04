# Mostre na tela uma contagem regressiva, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print("--"*10,"CONTAGEM REGRESSIVA","--"*10)

for c in range(10, 0, -1):
    print(f"{c}!")
    sleep(1)

print("FELIZ ANO NOVO!!!!!!!")
