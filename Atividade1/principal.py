from livro import Livro
#criando dois objetos de livro
livro1 = Livro("O pequeno prícipe","Antoine de Saint-Exupéry",1943)
livro2 = Livro("O gato de botas","Charles Perrault",1697)

#chamada do 1 livro
livro1.exibirInformacoes()
livro1.verificacaoLivro()

#chamada do livro 2
livro2.exibirInformacoes()
livro2.verificacaoLivro()

#SOLICITANDO DADOS DO USUÁRIO
tituloLivro= input("Informe o título do livro: ")
autorLivro = input("Informe o autor do livro: ")
anodpubliLivro = int(input("Qual o ano de Publicação do livro? "))

livro3 = Livro(tituloLivro, autorLivro, anodpubliLivro)
livro3.exibirInformacoes()
livro3.verificacaoLivro()