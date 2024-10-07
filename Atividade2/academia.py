class Aluno:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def exibirDados(self):
        print(f"Nome:{self.nome}")
        print(f"Idade:{self.idade}")
        print(f"Peso:{self.peso}")
        print(f"Altura:{self.altura}")
        
    def calcularImc(self):
        imc = self.peso/(self.altura**2)
        #Correçaõ na fórmula do Imc
        return imc