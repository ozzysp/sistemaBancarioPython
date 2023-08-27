class Usuario:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, agencia, numero, titular):
        self.agencia = agencia
        self.numero = numero
        self.titular = titular
        self.saldo = 0
        self.depositos = []
        self.saques = []


class SistemaBancario:
    def __init__(self):
        self.usuarios = []
        self.contas = []

    def cadastrar_usuario(self, nome, data_nascimento, cpf):
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("CPF já cadastrado. Não é possível cadastrar novamente.")
                return
        novo_usuario = Usuario(nome, data_nascimento, cpf)
        self.usuarios.append(novo_usuario)
        print("Usuário cadastrado com sucesso.")

    def cadastrar_conta(self, cpf, agencia, numero):
        usuario = None
        for u in self.usuarios:
            if u.cpf == cpf:
                usuario = u
                break

        if usuario is None:
            print("Usuário não encontrado.")
            return

        for conta in self.contas:
            if conta.numero == numero:
                print("Número da conta já cadastrado. Escolha outro número.")
                return

        nova_conta = Conta(agencia, numero, usuario)
        self.contas.append(nova_conta)
        print("Conta cadastrada com sucesso.")

    def depositar(self, numero_conta, valor):
        # Implementação do depósito

    def sacar(self, numero_conta, valor):
        # Implementação do saque

    def extrato(self, numero_conta):
        # Implementação do extrato

    # Restante das funções do sistema


def main():
    banco = SistemaBancario()

    while True:
        print("\nEscolha uma operação:")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Conta")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")

        escolha = int(input("Digite o número da operação: "))

        if escolha == 1:
            nome = input("Digite o nome do usuário: ")
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
            cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")
            banco.cadastrar_usuario(nome, data_nascimento, cpf)
        elif escolha == 2:
            cpf = input("Digite o CPF do titular da conta: ")
            agencia = "0001-1"
            numero = input("Digite o número da conta (xx.xxx-x): ")
            banco.cadastrar_conta(cpf, agencia, numero)
        # Restante das opções do menu


if __name__ == "__main__":
    main()
