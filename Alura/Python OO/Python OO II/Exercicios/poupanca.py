class Conta__Poupanca():
    def __init__(self, nome, numero_conta, saldo):
        self.nome=nome
        self.numero_conta=numero_conta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self,valor):
        self.saldo -= valor
        if self.idade <= 0 :
            return "Sem saldo para saque!"

    def alterar_nome(self, nome_novo):
        if self.nome == nome_novo:
            return "Nome atual é identico ao novo!"
        else:
            self.nome = nome_novo
