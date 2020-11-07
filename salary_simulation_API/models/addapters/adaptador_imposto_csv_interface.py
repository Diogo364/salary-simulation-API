from abc import ABC, abstractmethod
from salary_simulation_API.models.addapters.adaptador_imposto_interface import Adaptador_Imposto_Interface


class Adaptador_Imposto_CSV_Interface(Adaptador_Imposto_Interface, ABC):
    """Interface adaptadora específica para arquivos CSV"""

    @abstractmethod
    def set_informacoes(self, csv_file):
        pass

    @abstractmethod
    def get_faixas_de_imposto(self, valor):
        pass
