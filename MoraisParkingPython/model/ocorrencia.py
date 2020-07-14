from datetime import datetime


class Ocorrencia():

    # CONSTRUTOR
    def __init__(self, tipo, veiculos, data):
        self.tipo = tipo
        self.veiculos = veiculos
        self.data = data

    # GETTERS AND SETTERS
    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_veiculos(self):
        return self.veiculos

    def set_veiculos(self, veiculos):
        self.veiculos = veiculos

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    # STR (toString)
    def __str__(self):
        ocorrencia_str = ""
        ocorrencia_str += "Categoria: " + self.tipo
        ocorrencia_str += "\nData: " + str(self.data)
        ocorrencia_str += "\nVeiculos: "
        for veiculo in self.veiculos:
            ocorrencia_str += "\n\t" + veiculo
        ocorrencia_str += "\n"

        return ocorrencia_str
