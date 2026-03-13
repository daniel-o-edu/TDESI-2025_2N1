class Conta:
    def __init__(self, numero_conta, titular, saldo):
        self.numero = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado. Seu novo saldo é R${self.saldo}')
        else:
            print(f'{self.titular} seu saldo é insuficiente para sacar o valor de R${valor}. Seu saldo é R${self.saldo}')

    def exibir_extrato(self):
        print(f"Titular: {self.titular} | Saldo atual: R${self.saldo}")

class ContaEspecial(Conta):
    def __init__(self, numero_conta, titular, saldo, limite):
        super().__init__(numero_conta, titular, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f'Senhor {self.titular} seu saque VIP de R${valor} realizado. Novo saldo é R${self.saldo}')
        else:
            print(f'Limite excedido')

print('---- Testando conta comun -----')
conta_comun = Conta("123-4", "Ulf", 100)
conta_comun.sacar(1200)
conta_comun.exibir_extrato()

print('\n\n\n---- Testando conta VIP -----\n')
conta_vip = ContaEspecial('999-X', 'Ruan', 1000, 1000)
conta_vip.sacar(10000)
conta_vip.exibir_extrato()