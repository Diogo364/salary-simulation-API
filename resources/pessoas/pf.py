from resources.pessoas.pessoa import Pessoa


class PF(Pessoa):
    def __init__(self, nome, cpf, qtd_dependentes, salario=0):
        super().__init__(nome, cpf, qtd_dependentes)
        self.salario = float(salario)