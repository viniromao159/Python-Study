import re

endereço = "Rua 18 de Abril, 08226021, Cidade Antônio Estevão de Carvalho, São Paulo, SP" #Endereço a buscar

#padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]") #Cria o padrão de busca
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}") #Utiliza codificadores no padrão de busca
busca = padrao.search(endereço) #Utiliza o padrao de busca dentro da str
if busca:
    cep = busca.group() #Retorna a string que corresponde com a RE
    print(cep)