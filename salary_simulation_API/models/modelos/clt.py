import pandas as pd

from salary_simulation_API.models.modelos.contratos import Contratos
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica


class CLT(Contratos):
    def __init__(self, pessoa_fisica, salario_bruto, dict_impostos, beneficios_incluidos=False):
        """
        @type pessoa_fisica: Pessoa_Fisica
        @type salario_bruto: float
        @type dict_impostos: dict of Calculador_de_Imposto
        @param beneficios_incluidos: Boolean se o valor dos benefícios deve ser removido do salário.
        """

        self._pessoa_fisica = pessoa_fisica
        super().__init__(salario_bruto, dict_impostos, self._pessoa_fisica.qtd_dependentes)
        self.beneficios = pd.DataFrame(columns=['nome', 'valor', 'tipo'])
        self.beneficios_incluidos = beneficios_incluidos

    def adicionar_beneficios(self, nome, valor, frequencia):
        idx = len(self.beneficios) + 1
        self.beneficios.loc[idx, ['nome', 'valor', 'frequencia']] = nome, valor, frequencia
        if self.beneficios_incluidos:
            self.salario_liquido -= abs(valor)

    def __repr__(self):
        clt_str = []
        clt_str.append('===/' * 6 + '===')
        clt_str.append('\t|INFORMAÇÕES|')
        clt_str.append(f'Nome: {self._pessoa_fisica.nome}')
        clt_str.append(f'CPF: {self._pessoa_fisica.id}')
        clt_str.append(f'Qtd Dependentes: {self._pessoa_fisica.qtd_dependentes}')
        clt_str.append(f'Salario Bruto: R$ {self.salario_bruto:.2f}')
        clt_str.append('----' * 7 + '')
        clt_str.append('\t  |IMPOSTOS|')
        for nome in self.get_nome_impostos():
            aliquota = self.get_aliquota_imposto(nome) * 100
            valor = self.get_valor_imposto(nome)
            clt_str.append(
                f'{nome.upper()}: {aliquota:.2f}% | R$ {valor:.2f}'
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
