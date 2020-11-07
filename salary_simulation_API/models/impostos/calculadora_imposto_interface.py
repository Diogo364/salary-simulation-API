from abc import ABC, abstractmethod


class Calculadora_Imposto_Interface(ABC):

    @abstractmethod
    def calcular_imposto(self, *args):
        """Cálculo do imposto devido baseado no salario mensal"""
        pass

    @abstractmethod
    def _calcular_percentual_de_imposto(self, *args):
        """Cálculo do percentual para cada tipo de imposto"""
        pass
