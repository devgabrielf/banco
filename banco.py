from typing import List

from models.cliente import Cliente
from models.conta import Conta

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
