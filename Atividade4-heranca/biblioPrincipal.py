from biblioteca import Livro, Revista

# Criando objetos
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, 320)
livro2 = Livro("O Alquimista", "Paulo Coelho", 1988, 208)
revista1 = Revista("Revista Veja", "Diversos", 1997, 120)

# Chamando métodos para o primeiro livro
print(livro1.detalhes())
print(livro1.calcularIdadeItem())
print(livro1.verificarTamanho())

print()  # Linha em branco para separação

# Chamando métodos para o segundo livro
print(livro2.detalhes())
print(livro2.calcularIdadeItem())
print(livro2.verificarTamanho())

print()  # Linha em branco para separação

# Chamando métodos para a revista
print(revista1.detalhes())
print(revista1.calcularIdadeItem())
print(revista1.verificarEdicao())
