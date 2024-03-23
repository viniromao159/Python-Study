'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol 2017, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''

tabela = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atlético-MG", "Botafogo",
          "Athletico-PR", "Bahia", "São Paulo", "Fluminense", "Sport", "Coritiba", "Avaí", "Ponte", "Atlético-GO")

print(f"Lista de times Brasileirão 2017: {tabela}")
print(f"O G6 do campeonato foi: {tabela[:6]}")
print(f"Os reibaxados foram: {tabela[-4:]}")
print(f"Times em ordem alfabética: {sorted(tabela)}")
print(f"O Corinthians ficou em {tabela.index("Corinthians")+1}º lugar!")
