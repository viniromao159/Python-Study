import re

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url)

if not match:
    raise ValueError("URL inválida!")

print("URL válida!")