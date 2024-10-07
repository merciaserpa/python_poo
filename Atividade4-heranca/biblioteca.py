from datetime import datetime

class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina

    def detalhes(self):
        return f"Título: {self._titulo}, Autor: {self._autor}, Ano de Publicação: {self._anoPublicacao}"

    def calcularIdadeItem(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self._anoPublicacao
        if idade > 70:
            idade_categoria = "muito antigo"
        elif 30 <= idade <= 70:
            idade_categoria = "recente"
        else:
            idade_categoria = "contemporâneo"
        
        return f"{self._titulo}, Ano: {self._anoPublicacao}, Idade: {idade} anos - {idade_categoria}"

class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina > 300:
            tamanho = "longo"
        else:
            tamanho = "curto"
        
        return f"{self._titulo} tem {self._numeroPagina} páginas e é um livro {tamanho}."

class Revista(Biblioteca):
    def verificarEdicao(self):
        if self._anoPublicacao < 1998:
            edicao = "edição especial"
        else:
            edicao = "não é uma edição especial"
        
        return f"{self._titulo}, Ano: {self._anoPublicacao} - {edicao}."
