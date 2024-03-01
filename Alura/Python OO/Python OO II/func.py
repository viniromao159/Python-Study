class Funcionario:
    def __init__(self, nome) -> None:
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster: #Classe Mixin
    def __str__(self) -> str:
        return f"hipster, {self.nome}"      

class Junior(Alura):
    pass

class Pleno(Alura, Caelum): #Herança multipla
    pass

class Senior(Alura, Caelum, Hipster):
    pass

