from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_area import ControllerAreaEstacionamento

from model.constants import *

controller_veiculo = ControllerVeiculos()
controller_proprietario = ControllerProprietario()
controller_areas = ControllerAreaEstacionamento()


def cadastrar_area_especial():
    print("\n====== CADASTRAR AREA ESPECIAL ======")
    nome = input("Nome: ")
    try:
        capacidade = int(input("Capacidade: "))
        print("[1] Carro; [2] Motocicleta; [3] Onibus")
        tipo = TIPO_VEICULO[int(input("Tipo de veiculo (1, 2, ou 3): "))]
        controller_areas.register_area(nome, tipo, capacidade)
    except:
        print("Input invalido")


def remover_area_especial():
    print("\n====== REMOVER AREA ESPECIAL ======")
    areas = controller_areas.find_special_areas()
    areas_str = ""
    if len(areas) <= 0:
        print("Nao existem areas especiais cadastradas")
        return
    for i in range(len(areas)):
        areas_str += "[{}] {}  ".format((i + 1), areas[i].get_nome())
    print(areas_str)
    try:
        area_nome = areas[(int(input("Area (indice): ")) - 1)].get_nome()
        controller_areas.remove_area(area_nome)
    except:
        print("Input invalido. Voce precisa inserir um indice valido")



