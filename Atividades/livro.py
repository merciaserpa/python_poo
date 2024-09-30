class Livro:
    
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        
    def exibirInformacoes(self):
        print(f"Título:{self.titulo}")
        print(f"Autor:{self.autor}")
        print(f"Ano de Publicação:{self.anoPublicacao}")
        
    def verificacaoLivro(self):
        idade= 2024 - self.anoPublicacao
    #considerando o ano atual como 2024
        if idade > 50:
            print("Este livro é um clássico. ")
        else:
            print("Ainda não é considerado um clássico")        