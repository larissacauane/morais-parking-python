from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario

from model.constants import *

controller_veiculo = ControllerVeiculos()
controller_proprietario = ControllerProprietario()

def cadastrar_veiculo():
    print("\n====== CADASTRO VEICULO ======")
    proprietario_nome = input("Proprietario: ")
    proprietario = controller_proprietario.find_proprietario(proprietario_nome)
    if proprietario is None:
        return
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    print("[1] Carro; [2] Motocicleta; [3] Onibus")
    try:
        tipo = TIPO_VEICULO[int(input("Tipo de veiculo (1, 2, ou 3): "))]
        controller_veiculo.register_veiculo(placa, modelo, cor, proprietario, tipo)
    except:
        print("Input invalido")


def remover_veiculo():
    print("\n====== REMOVER VEICULO ======")
    placa = input("Placa: ")
    controller_veiculo.find_veiculo(placa)
    controller_veiculo.remove_veiculo(placa)


