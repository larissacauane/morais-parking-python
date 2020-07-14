from model.proprietario import Proprietario
from model.constants import *


class Veiculo:

    # CONSTRUTOR
    def __init__(self, placa, modelo, cor, proprietario=None, tipo=None):
        if proprietario is None:
            proprietario = Proprietario("Desconhecido", 0, "N/A")
        if tipo is None:
            tipo = TIPO_VEICULO[1]
        self.placa = placa
        self.proprietario = proprietario
        self.modelo = modelo
        self.cor = cor
        self.tipo = tipo

    # GETTERS AND SETTERS
    def get_placa(self):
        return self.placa

    def set_placa(self, placa):
        self.placa = placa

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_cor(self):
        return self.cor

    def set_cor(self, cor):
        self.cor = cor

    def get_proprietario(self):
        return self.proprietario

    def set_proprietario(self, proprietario):
        self.proprietario = proprietario

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    # STR (toString)
    def __str__(self):
        return "Veiculo: " + self.modelo + " " + self.cor + " (" + self.placa + \
               "); Proprietario: " + str(self.proprietario)

    # EQ (equals)
    def __eq__(self, other):
        return isinstance(other, Veiculo) and other.placa.upper() == self.placa.upper()

    # NE (not equals)
    def __ne__(self, other):
        return not self == other
