from personagem import  Personagem, Heroi, Vilao

# Criando os objetos
heroi = Heroi("Capitão Valor", 100, "Lendário", "João Estrela", 50)
vilao = Vilao("Senhor Trevas", 100, "Lendário", 70)
personagem = Personagem("Mercia", 100, "Novato")

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

personagem.detalhes()
personagem.receberDano(10)
personagem.verificarVida()