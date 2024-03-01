from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!!")

class Cpf:
    def __init__(self, documento): 
        if self.valida_cpf(documento): #Chama a função no if
            self.cpf = documento #Se true coloca o documento na variavel CPF
        else:
            raise ValueError("CPF inválido!") #Retorna error CPF

    def valida_cpf(self, cpf): 
        validador = CPF() #instancia a classe do pacote
        return validador.validate(cpf) #Chama o método validador do pacote
    
    def formata_cpf(self): #formata o cpf com a pontuação
        formatado = CPF()
        return formatado.mask(self.cpf)#Chama o método de mask do pacote

    def __str__(self):
        return f"{self.formata_cpf()} - CPF Válido!"

class Cnpj:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido")

    def valida_cnpj(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def formata_cnpj(self):
        formatado = CNPJ()
        return formatado.mask(self.cnpj)
    
    def __str__(self):
        return f"{self.formata_cnpj()} - CNPJ Válido!"
        
    