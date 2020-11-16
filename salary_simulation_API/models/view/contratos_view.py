from salary_simulation_API.models.modelos.contratos import Contratos


class Contratos_View:
    def __init__(self, contrato):
        """
        Viewer de Contratos
        @type contrato: Contratos
        """
        self._contrato = contrato

    def serialize_imposto(self):
        dict_impostos = self._contrato.__dict__['_total_imposto']
        return dict_impostos

    def serialize_beneficios(self):
        dict_beneficios = []
        for beneficio in self._contrato.lista_beneficios:
            dict_beneficios.append({
                beneficio.get_nome(): {
                    'valor': beneficio.get_valor(),
                    'descontar': beneficio.get_descontar(),
                    'incluir_salario': beneficio.is_incluido_salario(),
                    'frequencia': beneficio.get_frequencia()
                }
            })
        return dict_beneficios

    def serialize_pessoa(self):
        return {
            'nome': self._contrato.get_nome_pessoa(),
            'id': self._contrato.get_id(),
            'dependentes': self._contrato.get_dependentes()
        }

    def to_json(self):
        serialized = {
            'pessoa': self.serialize_pessoa(),
            'salario_bruto': self._contrato.get_salario_bruto(),
            'impostos': self.serialize_imposto(),
            'beneficios': self.serialize_beneficios(),
            'salario_liquido': self._contrato.get_salario_liquido()
        }
        return serialized
