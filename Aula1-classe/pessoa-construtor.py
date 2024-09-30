class Pessoa:
    # Ciar o método construtor
    def __init__(self, nome, altura, idade):
        #estamos criando os atributos da classe iltilizandoi o método construtor. Nesse caso precisamos passar os parâmetros que serão usados como os valores dos atríbutos
        self.nome = nome
        self.altura = altura
        self.idade = idade
        
    #criando os métodos
    def exibirDados(self):
        print(f"Olá {self.nome}, sua altura é {self.altura} e sua iadade é {self.idade}")

#CRIANDO OS OBJETOS
p1 = Pessoa("Getúlio",1.87,99)
p2 = Pessoa("Tatiana",1.72,75)

p1.exibirDados()
p2.exibirDados()
