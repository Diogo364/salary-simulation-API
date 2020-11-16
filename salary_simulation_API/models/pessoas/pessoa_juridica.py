from salary_simulation_API.models.pessoas.pessoa import Pessoa


class Pessoa_Juridica(Pessoa):
    def __init__(self, nome, cnpj, qtd_dependentes):
        super().__init__(nome, cnpj, qtd_dependentes)
