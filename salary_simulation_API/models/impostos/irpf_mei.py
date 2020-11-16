from salary_simulation_API.models.impostos.irpf_clt import IRPF_CLT


class IRPF_MEI(IRPF_CLT):
    def __init__(self, adaptador_imposto):
        super().__init__(adaptador_imposto)
        self._percentual_nao_tributavel = 0.32
        self.__limite_isencao = 28559.7

    def calcular_imposto(self, **kwargs):
        rendimento_anual = 12 * kwargs['salario_mensal']
        tributavel = rendimento_anual * (1 - self._percentual_nao_tributavel)
        if tributavel <= self.__limite_isencao:
            self._imposto_total = 0.0
        else:
            salario_mensal = tributavel / 12
            super().calcular_imposto(salario_mensal=salario_mensal, dependentes=kwargs['dependentes'])

        self._calcular_percentual_de_imposto(kwargs['salario_mensal'])
