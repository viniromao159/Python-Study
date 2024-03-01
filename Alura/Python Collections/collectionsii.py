usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy() #.copy() - Cria uma cópia da lista
assistiram.extend(usuarios_machine_learning) #.extend() - gera uma extensão da lista com outro interavel

set(assistiram) #Transformam a lista em conjunto

print(assistiram)


usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science | usuarios_machine_learning) # | é usado como "ou", podendo assim unir os dois sets
print(usuarios_data_science & usuarios_machine_learning) # & (e)
print(usuarios_data_science - usuarios_machine_learning) # - onde tá um e não esta em outro


frozenset({1, 5, 13, 17, 34, 52, 76, 765}) # Metodo para criar um conjunto imutavel.

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
set(meu_texto.split()) # .split é usado para quebrar a string nos espaços

#Dicionario

aparicoes = {
    'guilherme' : 1, #Chave/valor
    'cachorro' : 2,
    'nome' : 2,
    'vindo' : 1
}

type(aparicoes) #dict

aparicoes['xpto', 0] #Metodo GET -> Se não tiver xpto retorna 0

aparicoes['Carlos'] = 1 #Adiciona a chave Carlos com o valor 1

del aparicoes['Carlos'] #Deleta a chave carlos

'Carlos' in aparicoes #Verifica se contém a chave no dict

for elemento in aparicoes.keys(): # O FOR passa pelas chaves
    pass

for elemento in aparicoes.values(): # O FOR passa pelos valores
    pass

for elemento in aparicoes.items(): # O FOR passa pelas linhas(Chave - Valores)
    pass