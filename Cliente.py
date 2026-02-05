class Cliente:
    def __init__(self,nome,fone):

        self._nome = nome
        self._telefone = fone

    #metodo get
    def get_nome(self):
        return self._nome

    #metodo set
    def set_nome(self,nome):
        return self._nome


