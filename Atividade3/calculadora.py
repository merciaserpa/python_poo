class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def somar(self):
        resultado = self.__num1 + self.__num2
        print(f'Soma: {resultado}')

    def subtrair(self):
        resultado = self.__num1 - self.__num2
        print(f'Subtração: {resultado}')

    def multiplicar(self):
        resultado = self.__num1 * self.__num2
        print(f'Multiplicação: {resultado}')

    def dividir(self):
        if self.__num2 == 0:
            print('Erro: Divisão por zero não é permitida.')
        else:
            resultado = self.__num1 / self.__num2
            print(f'Divisão: {resultado:.2f}')

    def potencia(self):
        if self.__num1 <= 0 or self.__num2 < 0:
            print('Erro: num1 deve ser maior que zero e num2 não pode ser negativo.')
        else:
            resultado = self.__num1 ** self.__num2
            print(f'Potência: {resultado}')

    def verificaParImpar(self, valor):
        if valor % 2 == 0:
            return f'{valor} é par.'
        else:
            return f'{valor} é ímpar.'
