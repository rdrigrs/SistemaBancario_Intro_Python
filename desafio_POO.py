from abc import ABC, abstractmethod

class PessoaFisica:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Transacao(ABC):
    @abstractmethod
    def registrar_transacao(self, conta: 'Conta') -> None:
        pass

class Historico:
    def __init__(self, transacoes: list):
        self.transacoes = transacoes

    def adicionar_transacao(self, transacao: Transacao) -> None:
        self.transacoes.append(transacao)

class ContaCorrente:
    def __init__(self, limite, limite_saques):
        self.limite = limite
        self.limite_saques = limite_saques

class Conta(ContaCorrente):
    def __init__(self, cliente, numero, agencia, saldo, limite, limite_saques, historico: Historico):
        super().__init__(limite, limite_saques)
        self.cliente = cliente
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.historico = historico

    def obter_saldo(self):
        return self.saldo
    
    def nova_conta(self, cliente, numero):
        return Conta(cliente, numero, self.agencia, 0, self.limite, self.limite_saques, Historico([]))

    def sacar(self, valor):
        saque = Saque(valor)
        return self.cliente.realizar_transacao(self, saque)
    
    def depositar(self, valor):
        deposito = Deposito(valor)
        return self.cliente.realizar_transacao(self, deposito)

class Cliente(PessoaFisica):
    def __init__(self, cpf, nome, data_nascimento, endereco, contas: list):
        super().__init__(cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(self, conta: Conta, transacao: Transacao) -> None:
        if conta in self.contas:
            transacao.registrar_transacao(conta)
        else:
            print('Conta não encontrada')

    def adicionar_conta(self, conta: Conta) -> None:
        if conta not in self.contas:
            self.contas.append(conta)
        else:
            print('Conta já cadastrada')

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar_transacao(self, conta: Conta) -> None:
        if conta.saldo < conta.limite:
            conta.saldo += self.valor
            conta.historico.adicionar_transacao(self)
            print(f'Depósito de {self.valor} realizado com sucesso.')
            return True
        else:
            print('Limite de depósito excedido')
            return False

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar_transacao(self, conta: Conta) -> None:
        if self.valor > conta.saldo:
            print('Saldo insuficiente')
            return False
        else:
            if conta.limite_saques > 0:
                conta.saldo -= self.valor
                conta.limite_saques -= 1
                conta.historico.adicionar_transacao(self)
                print(f'Saque de {self.valor} realizado com sucesso.')
                return True
            else:
                print('Limite de saques excedido')
                return False

# Testes
cliente = Cliente('123.456.789-00', 'Fulano', '01/01/2000', 'Rua 1', [])
conta = Conta(cliente, '123', '456', 1000, 1000, 3, Historico([]))

cliente.adicionar_conta(conta)
conta.depositar(100)
conta.sacar(50)
conta.sacar(1000)
conta.depositar(100)
conta.sacar(1000)
print(conta.obter_saldo())
