from abc import ABC, abstractmethod


class Adaptador_Imposto_Interface(ABC):
    """
    Baseada no Design Pattern "Adapter", essa interface padroniza comunicão entre os "Coletores de Dados" e
    os "Calculadores de Imposto" com o objetivo de minimizar mudanças decorrentes de diferentes fontes de obtenções.
    """

    @abstractmethod
    def set_informacoes(self, *args):
        pass

    @abstractmethod
    def get_faixas_de_imposto(self, salario_mensal):
        pass
