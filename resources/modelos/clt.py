import pandas as pd
from resources.pessoas.pf import PF
from resources.impostos.inss import INSS
from resources.impostos.ir import IR


class CLT(PF, INSS, IR):
    def __init__(self, nome, cpf, qtd_dependentes, salario, beneficios_incluidos=False):
        self._tabela_imposto = {}
        self.salario_liquido = salario
        self.beneficios = pd.DataFrame(columns=['nome', 'valor', 'tipo'])
        self.beneficios_incluidos = beneficios_incluidos
        PF.__init__(self, nome, cpf, qtd_dependentes, salario)
        INSS.__init__(self)
        IR.__init__(self)

    def adicionar_beneficios(self, nome, valor, frequencia):
        idx = len(self.beneficios) + 1
        self.beneficios.loc[idx, ['nome', 'valor', 'frequencia']] = nome, valor, frequencia
        if self.beneficios_incluidos:
            self.salario_liquido -= abs(valor)

    def calcular_imposto(self):
        self.salario_liquido -= INSS.calcular_imposto(self, self.salario_liquido)
        self.salario_liquido -= IR.calcular_imposto(self, self.salario_liquido, dependentes=self.qtd_dependentes)

    def __repr__(self):
        clt_str = []
        clt_str.append('===/' * 6 + '===')
        clt_str.append('\t|INFORMAÇÕES|')
        clt_str.append(f'Nome: {self.nome}')
        clt_str.append(f'CPF: {self.id}')
        clt_str.append(f'Qtd Dependentes: {self.qtd_dependentes}')
        clt_str.append(f'Salario Bruto: R$ {self.salario:.2f}')
        clt_str.append('----' * 7 + '')
        clt_str.append('\t  |IMPOSTOS|')
        total_imposto = 0.0
        for imposto in self.imposto_total:
            clt_str.append(
                f'{imposto.upper()}: {self.aliquota_real[imposto] * 100:.2f}% | R$ {self.imposto_total[imposto]:.2f}')
            total_imposto += self.imposto_total[imposto]
        else:
            clt_str.append(f'TOTAL: {total_imposto / self.salario * 100:.2f}% | R$ {total_imposto:.2f}')

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
