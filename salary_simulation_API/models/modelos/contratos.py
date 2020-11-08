from salary_simulation_API.models.impostos.calculador_de_imposto import Calculador_de_Imposto
from salary_simulation_API.models.modelos.contratos_interface import Contratos_Interface


class Contratos(Contratos_Interface):
    """
    Baseada no Design Pattern "Facade", tem o objetivo de ser uma classe gerencial capaz
    qualquer objeto que herde de Calculadora_de_Imposto_Interface.
    """

    def __init__(self, salario_bruto, impostos, qtd_dependentes):
        """
        @type salario_bruto: float
        @type impostos: dict of Calculador_de_Imposto
        """
        self._impostos = impostos
        self._total_imposto = {}
        self.salario_bruto = float(salario_bruto)
        self.salario_liquido = self.salario_bruto
        self.qtd_dependentes = qtd_dependentes

    def _append_valor_imposto(self, nome, valor, aliquota):
        self._total_imposto[nome] = {
            'valor': valor,
            'aliquota': aliquota
        }

    def descontar_salario(self, valor):
        self.salario_liquido -= valor

    def calcular_imposto_total(self):
        imposto_total = 0.0
        for nome, imposto in self._impostos.items():
            imposto.calcular_imposto(salario_mensal=self.salario_liquido, dependentes=self.qtd_dependentes)
            valor = imposto.get_imposto_total()
            aliquota = imposto.get_aliquota_real()
            self._append_valor_imposto(nome, valor, aliquota)
            self.descontar_salario(valor)
            imposto_total += valor

        aliquota_total = imposto_total / self.salario_bruto
        self._append_valor_imposto('total', imposto_total, aliquota_total)

    def get_valor_imposto(self, nome):
        return self._total_imposto[nome]['valor']

    def get_aliquota_imposto(self, nome):
        return self._total_imposto[nome]['aliquota']

    def get_nome_impostos(self):
        return (nome for nome in self._total_imposto)

    def get_salario_bruto(self):
        return self.salario_bruto

    def get_salario_liquido(self):
        return self.salario_liquido
