from celular import Celular

# Criando dois objetos da classe Celular
cliente1 = Celular(numero='142536367')
cliente2 = Celular(numero='987574566', plano='pós-pago')

# Recarregando os saldos
cliente1.recarregar(50)  
cliente2.recarregar(30)  # Recarrega R$ 30 no saldo do cliente 2 (não terá efeito)

# Exibindo dados após recarga
cliente1.exibir_dados()
cliente2.exibir_dados()

# Fazendo chamadas
cliente1.fazerChamada(10) 
cliente2.fazerChamada(5)   

# Exibindo dados após chamadas
cliente1.exibir_dados()
cliente2.exibir_dados()
