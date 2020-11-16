class Beneficio:
    def __init__(self, nome, valor, desconto, frequencia, incluido_salario=False):
        self._nome = nome
        self._valor = float(valor)
        self._desconto = float(desconto)
        self._frequencia = frequencia
        self._incluido_salario = incluido_salario

    def get_valor(self):
        return self._valor

    def get_descontar(self):
        return self._desconto

    def get_nome(self):
        return self._nome

    def get_frequencia(self):
        return self._frequencia

    def is_incluido_salario(self):
        return self._incluido_salario

    def to_json(self):
        return {
            self.get_nome(): {
                'valor': self.get_valor(),
                'descontar': self.get_descontar(),
                'incluir_salario': self.is_incluido_salario(),
                'frequencia': self.get_frequencia()
            }
        }
