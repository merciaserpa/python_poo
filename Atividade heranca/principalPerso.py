from personagem import Heroi, Vilao

# Criando os objetos
heroi = Heroi("Capitão Valor", "João da Luz")
vilao = Vilao("Senhor Trevas")

# Chamando os métodos do herói
heroi.detalhes()
heroi.executarHabilidade("Super Força")
heroi.recarregarEnergia()
heroi.verificarVida()
heroi.chamarAliado("Lâmina Dourada")

# Chamando os métodos do vilão
vilao.detalhes()
vilao.desferirGolpe("Maldição")
vilao.planejarArmadilha("Armadilha do Caos")
vilao.verificarVida()
vilao.fugir("Teleporte Dimensional")