from salary_simulation_API.models.impostos.calculador_de_imposto import Calculador_de_Imposto
from salary_simulation_API.models.pessoas.pessoa import Pessoa
from salary_simulation_API.models.modelos.contratos_interface import Contratos_Interface
from salary_simulation_API.models.modelos.clt.beneficio import Beneficio


class Contratos(Contratos_Interface):
    """
    Baseada no Design Pattern "Facade", tem o objetivo de ser uma classe gerencial capaz
    qualquer objeto que herde de Calculadora_de_Imposto_Interface.
    """

    def __init__(self, pessoa, salario_bruto, impostos, qtd_dependentes, lista_beneficios, total_meses=12):
        """
        @type pessoa: Pessoa
        @type salario_bruto: float
        @type impostos: dict of Calculador_de_Imposto
        @type lista_beneficios: list of Beneficio
        """
        self._pessoa = pessoa
        self._impostos = impostos
        self._total_imposto = {}
        self._append_valor_imposto('total', 0.0, 0.0)
        self.salario_bruto = float(salario_bruto)
        self.salario_liquido = float(salario_bruto)
        self.qtd_dependentes = qtd_dependentes
        self.lista_beneficios = lista_beneficios
        self._anual = total_meses
        self._desconto_total_beneficios = 0

    def _append_valor_imposto(self, nome, valor, aliquota):
        self._total_imposto[nome] = {
            'valor': valor,
            'aliquota': aliquota
        }

    def descontar_salario(self, valor):
        self.salario_liquido -= abs(valor)

    def calcular_imposto_total(self):
        self._calcular_imposto_do_tipo(1)

        self._calcular_imposto_do_tipo(2)
        
        self._descontar_beneficios()

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
            if beneficio.get_frequencia() == 'Mensal':
                descontar = beneficio.get_descontar()
            else:
                descontar = beneficio.get_descontar() / 12
            self.descontar_salario(descontar)
            self._desconto_total_beneficios += descontar

    def get_valor_beneficios(self, anual=False):
        total_beneficios = 0.0
        for beneficio in self.lista_beneficios:
            if beneficio.get_frequencia() == 'Mensal':
                total_beneficios += beneficio.get_valor()
            else:
                total_beneficios += beneficio.get_valor() / 12
        if anual:
            return total_beneficios * 12
        else:
            return total_beneficios

    def adicionar_beneficios(self, beneficio):
        self.lista_beneficios.append(beneficio)

    def get_valor_imposto(self, nome, anual=False):
        meses = 1 if not anual else self._anual
        return self._total_imposto[nome]['valor'] * meses

    def get_aliquota_imposto(self, nome):
        return self._total_imposto[nome]['aliquota']

    def get_nome_impostos(self):
        return (nome for nome in self._total_imposto)

    def get_salario_bruto(self, anual=False):
        meses = 1 if not anual else self._anual
        return self.salario_bruto * meses

    def get_salario_liquido(self, anual=False):
        meses = 1 if not anual else self._anual
        return self.salario_liquido * meses

    def get_nome_pessoa(self):
        return self._pessoa.nome

    def get_id(self):
        return self._pessoa.id

    def get_dependentes(self):
        return self._pessoa.qtd_dependentes

    def get_total_desconto_beneficios(self, anual=False):
        meses = 1 if not anual else self._anual
        return self._desconto_total_beneficios * meses

    def to_json(self):
        serialized = {
            'pessoa': self._pessoa.to_json(),
            'salario_bruto': self.get_salario_bruto(),
            'impostos': [{nome: imposto for nome, imposto in self._total_imposto.items()}],
            'beneficios': [beneficio.to_json() for beneficio in self.lista_beneficios],
            'salario_liquido': self.get_salario_liquido()
        }
        return serialized

