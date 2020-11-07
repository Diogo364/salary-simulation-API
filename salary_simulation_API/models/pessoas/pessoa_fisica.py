from salary_simulation_API.models.impostos.imposto_de_renda import Imposto_de_Renda
from salary_simulation_API.models.pessoas.pessoa import Pessoa


class Pessoa_Fisica(Pessoa, Imposto_de_Renda):
    def __init__(self, nome, cpf, qtd_dependentes, salario, adaptador_imposto_ir):
        Pessoa.__init__(self, nome, cpf, qtd_dependentes)
        Imposto_de_Renda.__init__(self, adaptador_imposto_ir)
        self.salario = float(salario)

