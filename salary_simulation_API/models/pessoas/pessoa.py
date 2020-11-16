from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, personal_id, qtd_dependentes):
        self.nome = str(nome)
        self.id = str(personal_id)
        self.qtd_dependentes = int(qtd_dependentes)

    def to_json(self):
        return self.__dict__
