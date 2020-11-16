import pandas as pd
from salary_simulation_API.models.addapters.adaptador_imposto_csv_interface import Adaptador_Imposto_CSV_Interface


class Adaptador_CSV_Aliquotas_Unicas(Adaptador_Imposto_CSV_Interface):

    def __init__(self):
        self.__ir_table = None

    def set_informacoes(self, csv_file):
        self.__ir_table = pd.read_csv(csv_file)

    def get_faixas_de_imposto(self, valor):
        assert self.__ir_table is not None, 'Você precisa executar primeiro o método set_informacoes'

        faixa_ir_mask = (
                (self.__ir_table.base_menor <= valor) &
                (self.__ir_table.base_maior > valor)
        )
        faixa_especifica = self.__ir_table.loc[faixa_ir_mask, :]

        assert faixa_especifica.shape[0] == 1, f'''Resultado Inesperado de faixa do IR:
Valor de Salário: {valor}
Tabela: {self.__ir_table}
'''
        return faixa_especifica
