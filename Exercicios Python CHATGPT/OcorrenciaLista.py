ocorrencia_hoje = [1,5,2,6,8,1,3,4,1,5,4,7,2,3,1,1,1]

numero_ocorrencia = int(input("Digite o numero da sua ocorrencia: "))

repeticao_ocorrencia = 0
for ocorrencia in ocorrencia_hoje: #Passa pela lista
    if numero_ocorrencia == ocorrencia: #Verifica se é igual a ocorrecia do usuario
        repeticao_ocorrencia += 1 

if repeticao_ocorrencia > 0:
    print(f"Houve {repeticao_ocorrencia} desta ocorrencia hoje!")
else:
    print("Não houve ocorrencia hoje!")

#Escreva um programa que receba uma lista de números e exiba a contagem de quantas vezes um determinado número ocorre na lista. 

'''
def qnt_ocorrencia(ocorrencia_hoje, numero_ocorrencia):
    repeticao_ocorrencia = 0
    for ocorrencia in ocorrencia_hoje: #Passa pela lista
      if numero_ocorrencia == ocorrencia: #Verifica se é igual a ocorrecia do usuario
        repeticao_ocorrencia += 1
    return repeticao_ocorrencia
'''