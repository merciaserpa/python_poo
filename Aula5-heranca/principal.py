from funcionario import Funcionario, Engenheiro, Supervisor

f1 = Funcionario("Fiona", 3000)
engenheiro1 = Engenheiro("Shrek",3000)
supervisor1 = Supervisor("Flatus",3300)

f1.informacoes()

engenheiro1.bonusEngenheiro()
engenheiro1.informacoes()

supervisor1.relatorio()