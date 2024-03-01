import os 
os.system('cls') #Limpar terminal

def fluxodecaixa(op):
    nome = str(input("Nome: "))
    if op == 1:
      valor = float(input("Valor: "))
    else:
      valor = -float(input("Valor: "))
    fluxocaixa.append({
        "nome":nome,
        "valor":valor
    })

#Menu
print("@Fluxo de caixa")
print("---------------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("# Digite outro numero pra encerrar # ")
print("---------------")


fluxocaixa = []

while True:
    
    try:
      opcao = int(input("\nDigite a opção: "))

      if opcao == 1:
          fluxodecaixa(1)
      elif opcao == 2:
          fluxodecaixa(2)
      else :
          break
    except ValueError:
       print("Erro - tente novamente!")
       continue

#Extrato
print("---------------\n# Extrato #\n") 
total = 0

for fc in fluxocaixa:
    print(f'Nome: {fc['nome']} \nValor: RS${fc["valor"]}')
    total = total + fc["valor"]
print("---------------")

print(f"\nSaldo atual: R${total}\n")