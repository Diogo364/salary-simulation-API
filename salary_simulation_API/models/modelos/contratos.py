from salary_simulation_API.models.impostos.calculador_de_imposto import Calculador_de_Imposto
from salary_simulation_API.models.modelos.contratos_interface import Contratos_Interface


class Contratos(Contratos_Interface):
    """
    Baseada no Design Pattern "Facade", tem o objetivo de ser uma classe gerencial capaz
    qualquer objeto que herde de Calculadora_de_Imposto_Interface.
    """

    def __init__(self, salario_bruto, impostos, qtd_dependentes, lista_beneficios):
        """
        @type salario_bruto: float
        @type impostos: dict of Calculador_de_Imposto
        """
        self._impostos = impostos
        self._total_imposto = {}
        self._append_valor_imposto('total', 0.0, 0.0)
        self.salario_bruto = float(salario_bruto)
        self.salario_liquido = float(salario_bruto)
        self.qtd_dependentes = qtd_dependentes
        self.lista_beneficios = lista_beneficios

    def _append_valor_imposto(self, nome, valor, aliquota):
        self._total_imposto[nome] = {
            'valor': valor,
            'aliquota': aliquota
        }

    def descontar_salario(self, valor):
        self.salario_liquido -= abs(valor)

    def calcular_imposto_total(self):
        self._calcular_imposto_do_tipo(1)

        self._descontar_beneficios()

        self._calcular_imposto_do_tipo(2)
        self._total_imposto['total']['aliquota'] = self._total_imposto['total']['valor'] / self.salario_bruto

    def _calcular_imposto_do_tipo(self, tipo_imposto):
        salario_base = self.salario_bruto if tipo_imposto == 1 else self.salario_liquido

        for nome, imposto in self._impostos.items():
            if imposto.get_tipo_imposto() == tipo_imposto:
                self._total_imposto['total']['valor'] += self._calcular_imposto_salario(salario_base, nome,
                                                                                        imposto)

    def _calcular_imposto_salario(self, salario_base, nome, imposto):
        imposto.calcular_imposto(salario_mensal=salario_base, dependentes=self.qtd_dependentes)
        valor = imposto.get_imposto_total()
        aliquota = imposto.get_aliquota_real()
        self._append_valor_imposto(nome, valor, aliquota)
        self.descontar_salario(valor)
        return valor

    def _descontar_beneficios(self):
        for beneficio in self.lista_beneficios:
            if beneficio.is_incluido_salario():
                self.descontar_salario(beneficio.get_valor())

    def adicionar_beneficios(self, beneficio):
        self.lista_beneficios.append(beneficio)

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
