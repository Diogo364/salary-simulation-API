from abc import ABC
from salary_simulation_API.models.impostos.calculador_de_imposto import Calculador_de_Imposto


class INSS(Calculador_de_Imposto, ABC):
    def __init__(self, adaptador_imposto):
        super().__init__(adaptador_imposto)

    @staticmethod
    def __valor_aliquota(faixa_atual, excedente_faixa=None):
        if excedente_faixa is None or excedente_faixa > faixa_atual['base_maior']:
            excedente_faixa = faixa_atual['base_maior']
        delta = excedente_faixa - faixa_atual['base_menor']
        return delta * faixa_atual['aliquota'] / 100

    def _calcular_percentual_de_imposto(self, salario_mensal):
        self._aliquota_real = self.get_imposto_total() / float(salario_mensal)

    def calcular_imposto(self, salario_mensal):
        faixas_imposto = self._adaptador_imposto.get_faixas_de_imposto(salario_mensal)
        assert faixas_imposto.shape[0] > 0, 'Verifique a origem dos dados utilizados para carregar as informacões de ' \
                                            'imposto '

        inss_total = 0.0
        for _, faixa in faixas_imposto.iloc[:-1].iterrows():
            inss_total += self.__valor_aliquota(faixa)
        else:
            inss_total += self.__valor_aliquota(faixas_imposto.iloc[-1], salario_mensal)
        self._imposto_total = inss_total

        self._calcular_percentual_de_imposto(salario_mensal)
