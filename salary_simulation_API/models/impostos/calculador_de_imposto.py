from abc import ABC
from salary_simulation_API.models.impostos.calculadora_imposto_interface import Calculadora_Imposto_Interface


class Calculador_de_Imposto(Calculadora_Imposto_Interface, ABC):
    def __init__(self, adaptador_imposto):
        # assert issubclass(Adaptador_Imposto_Interface, type(adaptador_imposto)), 'Precisa de um adaptador que siga a ' \
        #                                                                    'interface: Adaptador_Imposto_Interface'
        self._adaptador_imposto = adaptador_imposto
        self._imposto_total = 0.0
        self._aliquota_real = 0.0

    def get_aliquota_real(self):
        return self._aliquota_real

    def get_imposto_total(self):
        return self._imposto_total
