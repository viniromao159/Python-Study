velocidade = 75 #Variavel comum
local_carro = 101

RADAR_1 = 60 #Variavel constante (FIXA)
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar 1!')
  
if local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE):
    pass
#Muitos IF pode deixar complexo o código. Quanto mais bloco longe da esquerda, mais complexo o código.