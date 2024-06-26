url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

url = url.strip()

if url == "":
    raise ValueError("A URL está vazia")

indice_interrogacao = url.find('?') #identifia o inicio dos parametros
url_base = url[:indice_interrogacao] #Separa a base da URL
url_parametros = url[indice_interrogacao+1:] #Sepera os parametros da URL

parametro_busca = 'quantidade' 
indice_parametro = url_parametros.find(parametro_busca) #Indice do parametro
indice_valor = indice_parametro + len(parametro_busca) + 1 #Indice do valor do parametro
indice_e_comercial = url_parametros.find('&', indice_valor) 

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)