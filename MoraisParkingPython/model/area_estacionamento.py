class AreaEstacionamento():

    # CONSTRUCTOR
    def __init__(self, nome, tipo, capacidade, especial=True, ocupacao=0):
        self.nome = nome
        self.capacidade = capacidade if capacidade > 0 else 1
        self.tipo = tipo
        self.especial = especial
        self.ocupacao = ocupacao

    # GETTERS AND SETTERS
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_capacidade(self):
        return self.capacidade

    def set_capacidade(self, capacidade):
        self.capacidade = capacidade

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def is_especial(self):
        return self.especial

    def set_especial(self):
        return self.especial

    def get_ocupacao(self):
        return self.ocupacao

    def set_ocupacao(self, ocupacao):
        self.ocupacao = ocupacao

    # HASH
    def __hash__(self):
        return hash(self.nome)

    # EQUALS
    def __eq__(self, other):
        return isinstance(other, AreaEstacionamento) and self.nome == other.nome

    # NOT EQUAL
    def __ne__(self, other):
        return not self.__eq__(other)

    # STR (toString)
    def __str__(self):
        return "Area: {0}; ocupacao: {1} / {2} ({3:.2f}%)".format(
            self.nome, self.ocupacao, self.capacidade, (self.ocupacao / self.capacidade * 100)
        )
