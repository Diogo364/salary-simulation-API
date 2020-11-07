from entities.pessoas.pessoa import Pessoa


class Pessoa_Juridica(Pessoa):
    def __init__(self, nome, cnpj, dependentes):
        super().__init__(nome, cnpj, dependentes)
