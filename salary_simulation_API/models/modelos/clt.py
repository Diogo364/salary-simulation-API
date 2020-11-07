import pandas as pd
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica
from salary_simulation_API.models.impostos.inss import INSS


class CLT:
    def __init__(self, pessoa_fisica, adaptador_imposto_inss, beneficios_incluidos=False):
        self._pessoa_fisica = pessoa_fisica
        self._inss = INSS(adaptador_imposto_inss)
        self.salario_liquido = pessoa_fisica.salario
        self.beneficios = pd.DataFrame(columns=['nome', 'valor', 'tipo'])
        self.beneficios_incluidos = beneficios_incluidos
        self.imposto_clt = 0.0

    def adicionar_beneficios(self, nome, valor, frequencia):
        idx = len(self.beneficios) + 1
        self.beneficios.loc[idx, ['nome', 'valor', 'frequencia']] = nome, valor, frequencia
        if self.beneficios_incluidos:
            self.salario_liquido -= abs(valor)

    def _calcular_inss(self):
        self._inss.calcular_imposto(self.salario_liquido)
        self.salario_liquido -= self._inss.get_imposto_total()

    def _calcular_ir(self):
        self._pessoa_fisica.calcular_imposto(self.salario_liquido, self._pessoa_fisica.qtd_dependentes)
        self.salario_liquido -= self._pessoa_fisica.get_imposto_total()

    def calcular_imposto(self):
        self._calcular_inss()
        self._calcular_ir()

    def get_salario_bruto(self):
        return self._pessoa_fisica.salario

    def get_inss(self):
        return self._inss.get_imposto_total()

    def get_ir(self):
        return self._pessoa_fisica.get_imposto_total()

    def get_imposto_total(self):
        imposto_total = self.get_ir() + self.get_ir()
        return imposto_total

    def __repr__(self):
        clt_str = []
        clt_str.append('===/' * 6 + '===')
        clt_str.append('\t|INFORMAÇÕES|')
        clt_str.append(f'Nome: {self._pessoa_fisica.nome}')
        clt_str.append(f'CPF: {self._pessoa_fisica.id}')
        clt_str.append(f'Qtd Dependentes: {self._pessoa_fisica.qtd_dependentes}')
        clt_str.append(f'Salario Bruto: R$ {self._pessoa_fisica.salario:.2f}')
        clt_str.append('----' * 7 + '')
        clt_str.append('\t  |IMPOSTOS|')
        clt_str.append(
            f'IR: {self._pessoa_fisica.get_aliquota_real() * 100:.2f}% | R$ {self._pessoa_fisica.get_imposto_total():.2f}'
        )
        clt_str.append(
            f'INSS: {self._inss.get_aliquota_real() * 100:.2f}% | R$ {self._inss.get_imposto_total():.2f}'
        )
        clt_str.append(
            f'TOTAL: {self.get_imposto_total() / self._pessoa_fisica.salario * 100:.2f}% | R$ {self.get_imposto_total():.2f}'
        )

        total_beneficios = 0.0
        if self.beneficios.shape[0]:
            clt_str.append('----' * 7 + '')
            clt_str.append('\t  |BENEFICIOS|')
            for _, beneficio in self.beneficios.iterrows():
                clt_str.append(
                    f'{beneficio.nome.upper()}: R$ {beneficio.valor:.2f} | {beneficio.frequencia}')
                total_beneficios += beneficio.valor
        clt_str.append('----' * 7 + '')
        clt_str.append('\t\t|TOTAL|')
        clt_str.append(f'Salário Líquido: R$ {self.salario_liquido:.2f}')
        clt_str.append(f'Benefícios: R$ {total_beneficios:.2f}')
        clt_str.append(f'Total: R$ {self.salario_liquido + total_beneficios:.2f}')

        clt_str.append('===/' * 6 + '===')

        return '\n'.join(clt_str)
