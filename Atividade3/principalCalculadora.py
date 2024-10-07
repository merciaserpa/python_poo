from calculadora import Calculadora

# Criando um objeto da classe Calculadora
calc = Calculadora(num1=5, num2=3)

# Acessando todos os métodos
calc.somar()         
calc.subtrair()      
calc.multiplicar()   
calc.dividir()      
calc.potencia()    

# Verificando se um número é par ou ímpar
valor_para_verificar = 4
resultado = calc.verificaParImpar(valor_para_verificar)
print(resultado)

# Testando a divisão por zero
calc_zero = Calculadora(num1=5, num2=0)
calc_zero.dividir()

# Testando a potência com restrições
calc_invalid_power = Calculadora(num1=-1, num2=2)
calc_invalid_power.potencia()
