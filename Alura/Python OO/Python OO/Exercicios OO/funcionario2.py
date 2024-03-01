class Funcionario:

    def __init__(self, nome, salario) -> None:
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario

    def set_aumentarSalario(self, porcentagem):
        salarioNovo = (porcentagem / 100) * self.__salario
        self.__salario = self.__salario + salarioNovo
        #print (f"Novo salario é: {self.__salario} ")

vinicius = Funcionario("Vinicius", 1000)
print (vinicius.get_salario())
vinicius.set_aumentarSalario(porcentagem=30)
print (vinicius.get_salario())