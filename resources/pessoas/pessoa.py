from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, id, qtd_dependentes):
        self.nome = str(nome)
        self.id = str(id)
        self.qtd_dependentes = int(qtd_dependentes)
