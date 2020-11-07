import pandas as pd
from salary_simulation_API.models.addapters.adaptador_imposto_csv_interface import Adaptador_Imposto_CSV_Interface


class Adaptador_CSV_INSS(Adaptador_Imposto_CSV_Interface):

    def __init__(self):
        self.__inss_table = None

    def set_informacoes(self, csv_file):
        self.__inss_table = pd.read_csv(csv_file)

    def get_faixas_de_imposto(self, valor):
        assert self.__inss_table is not None, 'Você precisa executar primeiro o método set_informacoes'

        faixa_especifica_mask = (
                (self.__inss_table.base_menor <= valor)
        )
        faixa_especifica = self.__inss_table.loc[faixa_especifica_mask, :]

        return faixa_especifica
