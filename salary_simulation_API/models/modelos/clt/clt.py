from salary_simulation_API.models.modelos.contratos import Contratos
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica


class CLT(Contratos):
    def __init__(self, pessoa_fisica, salario_bruto, dict_impostos, lista_beneficios=None):
        """
        @type pessoa_fisica: Pessoa_Fisica
        @type salario_bruto: float
        @type dict_impostos: dict of Calculador_de_Imposto
        @param lista_beneficios: list of Beneficio
        """

        if lista_beneficios is None:
            lista_beneficios = []
        self._pessoa_fisica = pessoa_fisica
        super().__init__(pessoa_fisica, salario_bruto, dict_impostos, self._pessoa_fisica.qtd_dependentes, lista_beneficios, total_meses=13)
