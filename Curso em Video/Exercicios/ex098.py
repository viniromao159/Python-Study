def contador(inicio, fim, passo):
    for i in range(1,11):
        print(i, end= ' ')
    print()
    
    for c in range( 10, -1, -2):
        print(c, end= ' ')
    print()
    
    # Se passo for zero, conta de 1 em 1
    if passo == 0:
        passo = 1 
    #Ajusta o passo de acordo com inicio e fim    
    if fim < inicio and passo > 0:
        passo = passo * -1
    #Inverte o inicio e fim caso o passo seja negativo  
    if passo < 0 and inicio < fim:
        inicio, fim = fim, inicio
    
    for j in range(inicio, fim, passo):
        print(j, end= ' ')
    print()

contador(40, 80, -5)