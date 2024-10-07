from academia import Aluno

# criando dois objetos de aluno
aluno1 = Aluno("Adeniel",18,65.6,1.80)
aluno2 = Aluno("Ala",18,57.2,1.68)

#chamada do 1 aluno
aluno1.exibirDados()
print(f"{aluno1.calcularImc():.2f}")

#chamada do 2 aluno
aluno2.exibirDados()
print(f"{aluno2.calcularImc():.2f}")

#SOLICITANDO DADOS DO USUÁRIO
nomeAluno= input("Informe o seu nome: ")
idadeAluno = int(input("Informe a sua idade: "))
pesoAluno = float(input("Qual o seu peso? "))
alturaAluno = float(input("Qual a sua altura? "))

aluno3 = Aluno(nomeAluno, idadeAluno, pesoAluno, alturaAluno)
aluno3.exibirDados()
print(f"{aluno3.calcularImc():.2f}")