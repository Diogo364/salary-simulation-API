from resources.pessoas.pessoa import Pessoa


class PJ(Pessoa):
    def __init__(self, nome, cnpj, dependentes):
        super().__init__(nome, cnpj, dependentes)
