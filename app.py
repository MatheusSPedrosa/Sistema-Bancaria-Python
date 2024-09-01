#                  DESAFIO DIO - CRIANDO UM SISTEMA BANCÁRIO COM PYTHON
#       Você foi contratado por um grande banco para desenvolver o seu novo sistema.
#       Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
#       Para a primeira versão do sistema você deve implementar apenas 3 operações: depósito, saque e extrato.


class ContaBancaria:
    def __init__(self, numero_conta, titular):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(
                f"Depósito de R${valor:.2f} realizado com sucesso.\nSaldo atualizado: R${self.saldo:.2f}\n"
            )
        else:
            print("Valor inválido para depósito.\n")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(
                f"Saque de R${valor:.2f} realizado com sucesso.\nSaldo atualizado: R${self.saldo:.2f}\n"
            )
        else:
            print("Saldo insuficiente ou valor inválido para saque.\n")

    def extrato(self):
        print(
            f"##  Extrato da conta {self.numero_conta} ## \nNome do titular: {self.titular}\nSaldo: R${self.saldo:.2f}"
        )


# Criação de conta bancária
conta = ContaBancaria(12345, "Matheus Pedrosa Sperandio")

# Teste de funcionalidade
conta.depositar(1000)
conta.sacar(500)
conta.extrato()
