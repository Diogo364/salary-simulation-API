import pandas as pd
from abc import ABC
from zope.interface import implementer
from resources.impostos.calculadora_imposto import Calculadora_Imposto


@implementer(Calculadora_Imposto)
class IR(ABC):
    def __init__(self):
        self._tabela_imposto['ir'] = pd.read_csv('resources/data/tabela_IR.csv')
        self.imposto_total = {}
        self.aliquota_real = {}

    def calcular_percentual(self, salario_mensal, tipo_imposto='ir'):
        self.aliquota_real[tipo_imposto] = self.imposto_total[tipo_imposto] / float(salario_mensal)

    def calcular_imposto(self, salario_mensal, tipo_imposto='ir', dependentes=0):
        ir_mask = (
                (self._tabela_imposto[tipo_imposto].base_menor <= salario_mensal) &
                (self._tabela_imposto[tipo_imposto].base_maior > salario_mensal)
        )
        aliquota, parcela_dedutivel = \
            self._tabela_imposto[tipo_imposto].loc[ir_mask, ['aliquota', 'parcela_dedutivel']].values[0]
        self.imposto_total[tipo_imposto] = (salario_mensal * aliquota / 100) - parcela_dedutivel - (dependentes * 189.59)
        self.calcular_percentual(salario_mensal, tipo_imposto)

        return self.imposto_total[tipo_imposto]
