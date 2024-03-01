meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower() #Todas letras minusculas

aparicoes = {} #Cria o dict

for palavra in meu_texto.split(): #passa pelas palavras e as quebras com o split
  ate_agora = aparicoes.get(palavra, 0) #Procura a palavra e devolve ela, caso não retorna 0
  aparicoes[palavra] = ate_agora + 1 #A cada aparição de uma palavra adiciona 1 no valor da chave (palavra)

print(aparicoes)