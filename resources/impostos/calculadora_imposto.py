from zope.interface import Interface, Attribute


class Calculadora_Imposto(Interface):

    tabela_imposto = Attribute('Tabela Contendo Faixas de imposto')
    imposto_total = Attribute('Dicionário contendo o valor total de cada imposto em reais')
    aliquota_real = Attribute('Dicionário contendo a porcentagem total de cada imposto')

    def calcular_imposto(salario_mensal, tipo_imposto):
        '''Calculo do imposto devido baseado no salario mensal'''

    def calcular_percentual(salario_mensal, tipo_imposto):
        '''Cálculo do percentual para cada tipo de imposto'''


