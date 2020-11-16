from salary_simulation_API.models.modelos.contratos import Contratos
from salary_simulation_API.models.pessoas.pessoa_juridica import Pessoa_Juridica


class MEI(Contratos):
    def __init__(self, pessoa_juridica, salario_bruto, dict_impostos, qtd_dependentes):
        """
        @type pessoa_juridica: Pessoa_Juridica
        @type salario_bruto: float
        @type dict_impostos: dict of Calculador_de_Imposto
        """

        super().__init__(pessoa_juridica, salario_bruto, dict_impostos, qtd_dependentes, [])