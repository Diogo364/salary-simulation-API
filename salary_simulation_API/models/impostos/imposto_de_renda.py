from salary_simulation_API.models.impostos.calculador_de_imposto import Calculador_de_Imposto


class Imposto_de_Renda(Calculador_de_Imposto):
    def __init__(self, adaptador_imposto):
        super().__init__(adaptador_imposto, 2)

    def _calcular_percentual_de_imposto(self, salario_mensal):
        self._aliquota_real = self.get_imposto_total() / float(salario_mensal)

    def calcular_imposto(self, **kwargs):
        super().calcular_imposto(**kwargs)
        faixa_imposto = self._adaptador_imposto.get_faixas_de_imposto(kwargs['salario_mensal'])
        aliquota, parcela_dedutivel = faixa_imposto[['aliquota', 'parcela_dedutivel']].values[0]
        self._imposto_total = \
            (kwargs['salario_mensal'] * aliquota / 100) - parcela_dedutivel - (kwargs['dependentes'] * 189.59)

        self._calcular_percentual_de_imposto(kwargs['salario_mensal'])
