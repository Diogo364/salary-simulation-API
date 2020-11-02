import pandas as pd
from abc import ABC
from zope.interface import implementer
from resources.impostos.calculadora_imposto import Calculadora_Imposto


@implementer(Calculadora_Imposto)
class INSS(ABC):
    def __init__(self):
        self._tabela_imposto['inss'] = pd.read_csv('resources/data/tabela_INSS.csv')
        self.imposto_total = {}
        self.aliquota_real = {}

    def valor_aliquota(self, idx, excedente_faixa=None, tipo_imposto='inss'):
        if excedente_faixa is None or excedente_faixa > self._tabela_imposto[tipo_imposto].loc[idx, 'base_maior']:
            excedente_faixa = self._tabela_imposto[tipo_imposto].loc[idx, 'base_maior']
        delta = excedente_faixa - self._tabela_imposto[tipo_imposto].loc[idx, 'base_menor']
        return delta * self._tabela_imposto[tipo_imposto].loc[idx, 'aliquota'] / 100

    def calcular_percentual(self, salario_mensal, tipo_imposto='inss'):
        self.aliquota_real[tipo_imposto] = self.imposto_total[tipo_imposto] / float(salario_mensal)

    def calcular_imposto(self, salario_mensal, tipo_imposto='inss'):
        indices_imposto = self._tabela_imposto[tipo_imposto].loc[(self._tabela_imposto[tipo_imposto].base_menor <= salario_mensal), :].index
        inss_total = 0.0
        for idx in indices_imposto[:-1]:
            inss_total += self.valor_aliquota(idx)
        else:
            inss_total += self.valor_aliquota(indices_imposto[-1], salario_mensal)
        self.imposto_total[tipo_imposto] = inss_total
        self.calcular_percentual(salario_mensal, tipo_imposto)

        return self.imposto_total[tipo_imposto]
