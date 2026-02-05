class Main:
    pass

from Cliente import Cliente

from Conta import Conta

c1= Cliente('João', '114444-2222')
conta=Conta(c1.get_nome(),1222,0)

conta.depositar(400)
conta.saque(500)
conta.extrato()




