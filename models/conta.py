from models.cliente import Cliente
from utils.helper import formata_float_str_moeda


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
               f'Saldo total: {formata_float_str_moeda(self.saldo_total)}\n'
