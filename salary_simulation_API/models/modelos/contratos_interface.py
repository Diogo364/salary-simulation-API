from abc import ABC, abstractmethod
import pandas as pd


class Contratos_Interface(ABC):
    """
    Baseada no Design Pattern "Facade", tem o objetivo de fazer o gerenciamento de qualquer conjunto
    de impostos que herde de Calculadora_de_Imposto_Interface.
    """
    @abstractmethod
    def calcular_imposto_total(self, *args):
        pass
