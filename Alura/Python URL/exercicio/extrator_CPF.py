from extratores import Extratores
 
usuario = Extratores("504.395.158-31, Noah Manuel da Cruz, 03/12/1988")

cpf = usuario.get_cpf()
data_nasc = usuario.get_data()

print(cpf)
print(data_nasc)