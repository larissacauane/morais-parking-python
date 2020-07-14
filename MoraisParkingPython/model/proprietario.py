class Proprietario():

    # CONSTRUCTOR
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    # GETTERS AND SETTERS
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_curso(self):
        return self.curso

    def set_curso(self, curso):
        self.curso = curso

    # STR (toString)
    def __str__(self):
        return self.nome + " (" + str(self.matricula) + ")"

