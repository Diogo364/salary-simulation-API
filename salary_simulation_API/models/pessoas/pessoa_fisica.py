from salary_simulation_API.models.pessoas.pessoa import Pessoa


class Pessoa_Fisica(Pessoa):
    def __init__(self, nome, cpf, qtd_dependentes):
        Pessoa.__init__(self, nome, cpf, qtd_dependentes)

