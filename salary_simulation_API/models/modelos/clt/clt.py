from salary_simulation_API.models.modelos.contratos import Contratos
from salary_simulation_API.models.pessoas.pessoa_fisica import Pessoa_Fisica


class CLT(Contratos):
    def __init__(self, pessoa_fisica, salario_bruto, dict_impostos, lista_beneficios=None):
        """
        @type pessoa_fisica: Pessoa_Fisica
        @type salario_bruto: float
        @type dict_impostos: dict of Calculador_de_Imposto
        @param lista_beneficios: list of Beneficio
        """

        if lista_beneficios is None:
            lista_beneficios = []
        self._pessoa_fisica = pessoa_fisica
        super().__init__(pessoa_fisica, salario_bruto, dict_impostos, self._pessoa_fisica.qtd_dependentes, lista_beneficios)

    def __repr__(self):
        clt_str = []
        clt_str.append('===/' * 6 + '===')
        clt_str.append('\t|INFORMAÇÕES|')
        clt_str.append(f'Nome: {self.get_nome_pessoa()}')
        clt_str.append(f'CPF: {self.get_id()}')
        clt_str.append(f'Qtd Dependentes: {self.get_dependentes()}')
        clt_str.append(f'Salario Bruto: R$ {self.salario_bruto:.2f}')
        clt_str.append('----' * 7 + '')
        clt_str.append('\t  |IMPOSTOS|')
        for nome in sorted(self.get_nome_impostos()):
            aliquota = self.get_aliquota_imposto(nome) * 100
            valor = self.get_valor_imposto(nome)
            clt_str.append(
                f'{nome.upper()}: {aliquota:.2f}% | R$ {valor:.2f}'
            )
        total_beneficios = 0.0
        if len(self.lista_beneficios):
            clt_str.append('----' * 7 + '')
            clt_str.append('\t  |BENEFICIOS|')
            for beneficio in self.lista_beneficios:
                clt_str.append(
                    f'{beneficio.get_nome().upper()}: R$ {beneficio.get_valor():.2f}')
                total_beneficios += beneficio.get_valor()
        clt_str.append('----' * 7 + '')
        clt_str.append('\t\t|TOTAL|')
        clt_str.append(f'Salário Líquido: R$ {self.salario_liquido:.2f}')
        clt_str.append(f'Benefícios: R$ {total_beneficios:.2f}')
        clt_str.append(f'Total: R$ {self.salario_liquido + total_beneficios:.2f}')

        clt_str.append('===/' * 6 + '===')

        return '\n'.join(clt_str)
