from abc import ABC
from salary_simulation_API.models.addapters.adaptador_imposto_interface import Adaptador_Imposto_Interface
from salary_simulation_API.models.impostos.calculadora_de_imposto_interface import Calculadora_de_Imposto_Interface


class Calculador_de_Imposto(Calculadora_de_Imposto_Interface, ABC):
    """
    Baseada no Design Pattern "Facade", tem o objetivo de ser uma classe gerencial capaz
    qualquer objeto que herde de Adaptador_Imposto_Interface.
    """
    def __init__(self, adaptador_imposto: Adaptador_Imposto_Interface):
        self._adaptador_imposto = adaptador_imposto
        self._imposto_total = 0.0
        self._aliquota_real = 0.0

    def get_aliquota_real(self):
        return self._aliquota_real

    def get_imposto_total(self):
        return self._imposto_total

    def clean_impostos(self):
        self._imposto_total = 0.0
        self._aliquota_real = 0.0

    def calcular_imposto(self, **kwargs):
        self.clean_impostos()