total_compra = maisdemil = barato = 0

while True:
    produto = input("Digite o produto: ")
    valor_produto = float(input("Digite o valor do produto: "))
    
    if total_compra == 0:
        nomebarato = produto
        barato = valor_produto
    
    total_compra += valor_produto
    
    if valor_produto >= 1000.0:
        maisdemil += 1
    
    if valor_produto < barato:
        nomebarato = produto
        barato = valor_produto
        
    continuar = input("Encerrar programa? (1) encerrar (2) continuar:  ").lower().strip()
    
    if continuar == "1":
        break

print(f"O total da compra é R${total_compra}")
print(f"Exite {maisdemil} produtos acima de R$1000!")
print(f"O produto mais barato é {nomebarato} e seu valor é {barato}!")
