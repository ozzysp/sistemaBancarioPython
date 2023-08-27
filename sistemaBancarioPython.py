class SistemaBancario:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido para depósito.")
            return
        self.saldo += valor
        self.depositos.append(valor)
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0 or valor > 500:
            print("Valor inválido para saque.")
            return
        if len(self.saques) >= 3:
            print("Limite diário de saques atingido.")
            return
        if self.saldo < valor:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        self.saques.append(valor)
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self):
        print("Extrato bancário:")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            for idx, valor in enumerate(self.depositos, start=1):
                print(f"{idx}. Depósito: R$ {valor:.2f}")
            for idx, valor in enumerate(self.saques, start=len(self.depositos) + 1):
                print(f"{idx}. Saque: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


def main():
    banco = SistemaBancario()

    while True:
        print("\nEscolha uma operação:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

        escolha = int(input("Digite o número da operação: "))

        if escolha == 1:
            valor = float(input("Digite o valor do depósito: "))
            banco.depositar(valor)
        elif escolha == 2:
            valor = float(input("Digite o valor do saque: "))
            banco.sacar(valor)
        elif escolha == 3:
            banco.extrato()
        elif escolha == 4:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
