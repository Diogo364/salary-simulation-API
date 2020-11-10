class Beneficio:
    def __init__(self, nome, valor, frequencia, incluido_salario=False):
        self._nome = nome
        self._valor = float(valor)
        self._frequencia = frequencia
        self._incluido_salario = incluido_salario

    def get_valor(self):
        return self._valor

    def get_nome(self):
        return self._nome

    def get_frequencia(self):
        return self._frequencia

    def is_incluido_salario(self):
        return self._incluido_salario
