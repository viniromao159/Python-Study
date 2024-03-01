import re

class Extratores:
    def __init__(self, str):
        self.str = str

    def get_cpf(self):
        cpf_padrao = re.compile("[0-9]{3}[.,-]?[0-9]{3}[.,-]?[0-9]{3}[-,.]?[0-9]{2}")
        cpf_usuario = cpf_padrao.search(self.str)
        if cpf_usuario:
            cpf = cpf_usuario.group()
            return cpf
    
    def get_data(self):
        data_padrao = re.compile("[0-9]{2}[.,-,/]?[0-9]{2}[.,-,/]?[0-9]{4}")
        data_str = data_padrao.search(self.str)
        if data_str:
            data_nasc = data_str.group()
            return data_nasc
