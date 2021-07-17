from datetime import date, datetime
from typing import List


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')


def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')


def formata_float_str_moeda(valor: float) -> str:
    return f'R${valor:,.2f}'


class Cliente:
    contador: int = 101

    def __init__(self: object, nome: str, email: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contador
        self.__nome: str = nome
        self.__email: str = email
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return date_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:
        return date_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f'Código: {self.codigo}\nNome: {self.nome}\nData de nascimento: {self.data_nascimento}\n' \
               f'Cadastro: {self.data_cadastro}'


class Conta:
    codigo: int = 1001

    def __init__(self: object, cliente: Cliente) -> None:
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return self.saldo + self.limite

    def depositar(self: object, valor: float) -> None:
        self.saldo = self.saldo + valor
        self.saldo_total = self._calcula_saldo_total
        print('Depósito efetuado com sucesso.\n')

    def sacar(self: object, valor: float) -> None:
        if self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
            else:
                restante: float = valor - self.saldo
                self.limite = self.limite - restante
                self.saldo = 0
                self.saldo_total = self._calcula_saldo_total
            print('Saque efetuado com sucesso.\n')
        else:
            print('Saldo insuficiente.\n')

    def trasnferir(self: object, destino: object, valor: float) -> None:
        if self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.saldo + destino.limite
            else:
                restante: float = valor - self.saldo
                self.saldo = 0
                self.limite = self.limite - restante
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino.saldo + destino.limite
            print('Transferência efetuada com sucesso.\n')
        else:
            print('Saldo insuficiente.\n')

    def __str__(self: object) -> str:
        return f'Número da conta: {self.numero}\nCliente: {self.cliente.nome}\n' \
               f'Saldo total: {formata_float_str_moeda(self.saldo_total)}'


contas: List[Conta] = []


def main() -> None:

    print('====================================')
    print('============== PyBank ==============')
    print('====================================')

    menu()


def menu() -> None:

    print('\nSelecione uma opção no menu:')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar depósito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Sair do sistema\n')

    opcao = 0
    try:
        opcao: int = int(input())
    except ValueError:
        print('O valor precisa ser numérico.\n')
        menu()

    if opcao == 1:
        try:
            criar_conta()
        except ValueError:
            print('A data de nascimento deve estar no formato dd/mm/aaaa.')
            menu()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Saindo do sistema...')
        exit(0)
    else:
        print('Opção inválida.')
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente:')

    nome: str = input('Nome: ')
    email: str = input('E-mail: ')
    cpf: str = input('CPF: ')
    data_nascimento: str = input('Data de nascimento: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print('Conta criada com sucesso.\n')
    print('Dados da conta:')
    print('---------------------------')
    print(conta)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero = 0
        while True:
            try:
                numero: int = int(input('Informe o número da sua conta: '))
                x = 0
            except ValueError:
                print('O valor precisa ser numérico\n')
                x = 1
            if x == 0:
                break

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor = 0
            while True:
                try:
                    valor: float = float(input('Informe o valor do saque: '))
                    if valor <= 0:
                        print('O valor precisa ser positivo.\n')
                        x = 1
                    else:
                        x = 0
                except ValueError:
                    print('O valor precisa ser numérico\n.')
                    x = 1
                if x == 0:
                    break

            conta.sacar(valor)
        else:
            print('Conta não encontrada.')
    else:
        print('Ainda não há contas cadastradas.')
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero = 0
        while True:
            try:
                numero: int = int(input('Informe o número da sua conta: '))
                x = 0
            except ValueError:
                print('O valor precisa ser numérico.\n')
                x = 1
            if x == 0:
                break

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor = 0
            while True:
                try:
                    valor: float = float(input('Informe o valor do depósito: '))
                    if valor <= 0:
                        print('O valor precisa ser positivo.\n')
                        x = 1
                    else:
                        x = 0
                except ValueError:
                    print('O valor precisa ser numérico.\n')
                    x = 1
                if x == 0:
                    break

            conta.depositar(valor)
        else:
            print('Conta não encontrada.')
    else:
        print('Ainda não há contas cadastradas.')
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_origem = 0
        while True:
            try:
                numero_origem: int = int(input('Informe o número da sua conta: '))
                x = 0
            except ValueError:
                print('O valor precisa ser numérico.\n')
                x = 1
            if x == 0:
                break

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)

        if conta_origem:
            numero_destino = 0
            while True:
                try:
                    numero_destino: int = int(input('Informe o número da conta à qual deseja realizar '
                                                    'a transferência: '))
                    x = 0
                except ValueError:
                    print('O valor precisa ser numérico.\n')
                    x = 1
                if x == 0:
                    break

            conta_destino: Conta = buscar_conta_por_numero(numero_destino)
            if conta_destino and conta_destino != conta_origem:
                valor = 0
                while True:
                    try:
                        valor: float = float(input('Informe o valor da transferência: '))
                        if valor <= 0:
                            print('O valor precisa ser positivo.\n')
                            x = 1
                        else:
                            x = 0
                    except ValueError:
                        print('O valor precisa ser numérico.\n')
                        x = 1
                    if x == 0:
                        break

                conta_origem.trasnferir(conta_destino, valor)
            elif conta_destino and conta_destino == conta_origem:
                print('Não é possível realizar transferência para si mesmo.\n')
            else:
                print('Conta não encontrada.')
        else:
            print('Conta não encontrada.')
    else:
        print('Ainda não há contas cadastradas.')
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas:')
        print('---------------------------')

        for conta in contas:
            print(conta)
            print('---------------------------')
    else:
        print('Ainda não há contas cadastradas.')
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c = None

    for conta in contas:
        if conta.numero == numero:
            c = conta
    return c


if __name__ == '__main__':
    main()
