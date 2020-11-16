from salary_simulation_API.models.impostos.calculador_de_imposto import Calculador_de_Imposto


class Simples_Nacional(Calculador_de_Imposto):
    def __init__(self, adaptador_imposto, is_mei):
        """
        @type is_mei: Bool
        """
        super().__init__(adaptador_imposto, 1)
        self.__mei = is_mei

    def _calcular_percentual_de_imposto(self, salario_mensal):
        self._aliquota_real = self.get_imposto_total() / float(salario_mensal)

    def calcular_imposto(self, **kwargs):
        if self.__mei:
            self._imposto_total = 58.00
        else:
            super().calcular_imposto(**kwargs)
            faixa_imposto = self._adaptador_imposto.get_faixas_de_imposto(kwargs['salario_mensal'])
            aliquota, parcela_dedutivel = faixa_imposto[['aliquota', 'parcela_dedutivel']].values[0]
            self._imposto_total = \
                ((kwargs['salario_mensal'] * 12 * aliquota / 100) - parcela_dedutivel) / 12

        self._calcular_percentual_de_imposto(kwargs['salario_mensal'])
