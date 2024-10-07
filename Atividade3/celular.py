class Celular:
    def __init__(self, numero, plano='pré-pago', saldo=0):
        self.__numero = numero
        self.__plano = plano
        self.__saldo = saldo
        self.__valorMinuto = 1.50

    @property # cria um get mais amigavel 
    def plano(self):
        return self.__plano

    @plano.setter  #criar um set para o atributo de forma "mais amigavel"
    def plano(self, novo_plano):
        self.__plano = novo_plano

    def recarregar(self, valor):
        if self.__plano == 'pré-pago':
            self.__saldo += valor
            print(f'Recarga de R$ {valor} realizada. Saldo atual: R$ {self.__saldo:.2f}')
        else:
            print('Recargas não têm efeito para planos pós-pagos.')

    def fazerChamada(self, duracao_minutos):
        if self.__plano == 'pré-pago':
            custo = duracao_minutos * self.__valorMinuto
            if custo > self.__saldo:
                print('Saldo insuficiente para realizar a chamada.')
            else:
                self.__saldo -= custo
                print(f'Chamada de {duracao_minutos} minutos realizada. Custo: R$ {custo:.2f}. Saldo restante: R$ {self.__saldo:.2f}')
        else:
            custo = duracao_minutos * self.__valorMinuto
            print(f'Chamada de {duracao_minutos} minutos realizada. O valor total de R$ {custo:.2f} será cobrado no final do mês.')

    def exibir_dados(self):
        print(f'Número: {self.__numero}, Plano: {self.__plano}, Saldo: R$ {self.__saldo:.2f}')
