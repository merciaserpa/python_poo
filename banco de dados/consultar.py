import sqlite3

#Passo1 -  Conexão com o banco
conexao = sqlite3.connect("departamento.db")

#Passo2 - Verificar se a tabela existe ou não,

tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)    
);
"""
#Passo3 - Acessar o objeto cursor() da biblioteca sqlite3, para manipular banco de dados
consulta = conexao.cursor()

#Passo4 - Executar o comando de criação da tabela
consulta.execute(tabela)

#Passo5 - Criando no SQL para inserir os dados na tabela
sql = "SELECT * FROM funcionario"  

#Passo6 - Executar o comando sql e substituir '?' pelos campos
consulta.execute(sql)

#Passo7 - Exibir dados da tabela
resultado = consulta.fetchall()# fetchall () irá trazer todos os registros que existem na tabela do banco de dados 

for itens in resultado:
    print(f"Código: {itens[0]}, Nome:{itens[1]}")

#Passo8 - encerrar a conexão
conexao.close()