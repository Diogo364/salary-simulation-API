from abc import ABC, abstractmethod


class Adaptador_Imposto_Interface(ABC):
    """Interface adaptadora para criação de objetos a partir de diversas fontes"""

    @abstractmethod
    def set_informacoes(self, *args):
        pass

    @abstractmethod
    def get_faixas_de_imposto(self, salario_mensal):
        pass
