import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url() #Assim que a classe for instanciada é chamado este método.
 
    def sanitiza_url(self, url): #limpa a string
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def valida_url(self):
        if not bool(self.url): #Valida se está vazia
            raise ValueError("A URL está vazia!")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")#Valida o padrão apontado pelas ?
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("URL inválida!")

    def get_url_base(self): #Separa a base da URL
        indice_interrogacao = self.url.find('?') #Localiza o ? dentro da Url
        url_base = self.url[:indice_interrogacao] 
        return url_base

    def get_url_parametros(self): #Separa os parametros
        indice_interrogacao = self.url.find('?') 
        url_parametros = self.url[indice_interrogacao + 1:] 
        return url_parametros

    def get_valor_parametros(self,parametro_busca): #Busca de parametro
        indice_parametro = self.get_url_parametros().find(parametro_busca) #Indice do parametro
        indice_valor = indice_parametro + len(parametro_busca) + 1 #Indice do valor do parametro
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor) 
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else: 
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor