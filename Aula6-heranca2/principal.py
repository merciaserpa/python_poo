from pessoa import Pessoa, Aluno, Professsor

pessoa1 = Pessoa("Garibalde", 54)
aluno1 = Aluno("Jucicleia", 16, 874)
professor1 = Professsor("Anderson Bruno", 30, "Tecnologia")

pessoa1.info()

aluno1.info()
aluno1.estudar()

professor1.info()
professor1.ensinar()