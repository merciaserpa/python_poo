class Personagem:
    def __init__(self, nome, vida=100):
        self._nome = nome
        self._vida = vida
        self._rank = "Novato"

    def receberDano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0

    def verificarVida(self):
        if self._vida > 0:
            print(f"{self._nome} ainda está vivo com {self._vida} pontos de vida.")
        else:
            print(f"{self._nome} morreu.")

    def detalhes(self):
        print(f"Nome: {self._nome}, Vida: {self._vida}, Rank: {self._rank}")


class Heroi(Personagem):
    def __init__(self, nome, identidade_secreta, energia=50):
        super().__init__(nome)
        self._identidadeSecreta = identidade_secreta
        self._energia = energia

    def executarHabilidade(self, tipoHabilidade):
        if self._energia >= 10:  # Consome 10 de energia
            self._energia -= 10
            print(f"{self._nome} usou a habilidade {tipoHabilidade} e consumiu 10 de energia. Energia restante: {self._energia}.")
        else:
            print(f"{self._nome} não tem energia suficiente para usar {tipoHabilidade}.")

    def recarregarEnergia(self):
        self._energia += 10  # Recarrega 10 de energia
        print(f"{self._nome} recarregou 10 de energia. Energia total: {self._energia}.")

    def chamarAliado(self, nomeAliado):
        print(f"{self._nome} chamou {nomeAliado} para ajudar na luta!")


class Vilao(Personagem):
    def __init__(self, nome, malicia=70):
        super().__init__(nome)
        self._malicia = malicia

    def desferirGolpe(self, tipoGolpe):
        if self._malicia >= 15:  # Consome 15 de malícia
            self._malicia -= 15
            print(f"{self._nome} desferiu o golpe {tipoGolpe} potencializado pela malícia. Malícia restante: {self._malicia}.")
        else:
            print(f"{self._nome} não tem malícia suficiente para desferir {tipoGolpe}.")

    def planejarArmadilha(self, tipoArmadilha):
        print(f"{self._nome} está planejando a armadilha {tipoArmadilha}.")

    def fugir(self, tipoFulga):
        print(f"{self._nome} conseguiu escapar usando {tipoFulga}.")
        