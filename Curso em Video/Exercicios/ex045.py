import random
from time import sleep

jokenpo = ["Pedra", "Papel", "Tesoura"]

player = int(input("Escolha uma opção: 1 - Pedra | 2 - Papel | 3 - Tesoura: "))
cpu = random.randint(1,3)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

if player == cpu:
    print(f"Player -> {jokenpo[player-1]} | Cpu -> {jokenpo[cpu-1]}")
    print(f"EMPATE!")
    
elif player == 1 and cpu == 2 or player == 2 and cpu == 3 or player == 3 and cpu == 1:
    print(f"Player -> {jokenpo[player-1]} | Cpu -> {jokenpo[cpu-1]}")
    print(f"VOCE PERDEU!")
    
elif player == 1 and cpu == 3 or player == 2 and cpu == 1 or player == 3 and cpu == 2:
    print(f"Player -> {jokenpo[player-1]} | Cpu -> {jokenpo[cpu-1]}")
    print(f"VOCE GANHOUUU!")