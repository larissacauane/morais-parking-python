from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_permissoes import ControllerPermissoes
from control.controller_area import ControllerAreaEstacionamento
from control.controller_eventos import ControllerEventos
from control.controller_estacionamento import ControllerEstacionamento

from model.constants import *
from model.veiculo import Veiculo
from model.relatorio import Relatorio


controller_veiculo = ControllerVeiculos()
controller_proprietario = ControllerProprietario()
controller_permissoes = ControllerPermissoes()
controller_areas = ControllerAreaEstacionamento()
controller_eventos = ControllerEventos()
controller_estacionamento = ControllerEstacionamento()


def autorizar_entrada():
    print("\n====== AUTORIZAR ENTRADA ======")
    placa = input("Placa: ")
    if len(placa) <= 0:
        print("Placa invalida")
        return

    veiculo = controller_veiculo.find_veiculo(placa)
    if veiculo is None:
        print("Insira dados do veiculo")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        print("[1] Carro; [2] Motocicleta; [3] Onibus")
        try:
            tipo = TIPO_VEICULO[int(input("Tipo de veiculo (1, 2, ou 3): "))]
            veiculo = Veiculo(placa, modelo, cor, None, tipo)
        except:
            print("Input invalido")
            return

    print(veiculo)
    evento = controller_eventos.find_todays_evento()
    permissao = controller_permissoes.find_permissao_by_placa(veiculo.get_placa())
    area_especial = None
    area_comum = controller_areas.find_compatible_common_area(veiculo.get_tipo())
    if permissao is not None:
        area_especial = controller_areas.find_area(permissao[1])

    success = False

    reservas_comum = 0
    reservas_especial = 0
    if evento is not None:
        if area_especial is not None:
            reservas_especial = evento.get_reservas()[area_especial]
        reservas_comum = evento.get_reservas()[area_comum]

    if area_especial is not None:
        ocupacao = len(controller_estacionamento.find_placas_by_area(area_especial.get_nome()))
        ocupacao += reservas_especial
        if ocupacao < area_especial.get_capacidade():
            success = controller_estacionamento.autorizar_entrada(placa, area_especial.get_nome())
    if not success:
        ocupacao = len(controller_estacionamento.find_placas_by_area(area_comum.get_nome()))
        ocupacao += reservas_comum
        if ocupacao < area_comum.get_capacidade():
            success = controller_estacionamento.autorizar_entrada(placa, area_comum.get_nome())

    if success:
        print("Entrada autorizada!")
    else:
        print("Entrada nao autorizada")

    update_relatorio()



def autorizar_saida():
    print("\n====== AUTORIZAR SAIDA ======")
    placa = input("Placa: ")
    if len(placa) <= 0:
        print("Placa invalida")
        return

    placas = controller_estacionamento.find_all_placas()
    if placa not in placas:
        print("Veiculo nao encontrado.")
        print("Nao foi possivel autorizar a saida")
    elif controller_estacionamento.autorizar_saida(placa):
        print("Saida autorizada")
    else:
        print("Nao foi possivel autorizar a saida")


def consultar_status():
    print("\n====== STATUS ======")
    areas = controller_areas.find_all_areas()
    evento = controller_eventos.find_todays_evento()

    total_capacidade = 0
    total_ocupacao = 0
    for area in areas:
        ocupacao = len(controller_estacionamento.find_placas_by_area(area.get_nome()))
        if evento is not None:
            ocupacao += evento.get_reservas()[area]
        area.set_ocupacao(ocupacao)
        print(area)
        total_capacidade += area.get_capacidade()
        total_ocupacao += area.get_ocupacao()

    print("\nTOTAL: {0} / {1} ({2:.2f}%)".format(total_ocupacao, total_capacidade, (total_ocupacao/total_capacidade)))


def update_relatorio():
    ocupacoes_max = Relatorio.get_ocupacoes_max()
    evento = Relatorio.get_evento()

    for area, ocupacao_max in ocupacoes_max.items():
        ocupacao = len(controller_estacionamento.find_placas_by_area(area.get_nome()))
        if evento is not None:
            ocupacao += evento.get_reservas()[area]
        area.set_ocupacao(ocupacao)
        if ocupacao_max <= ocupacao:
            ocupacoes_max[area] = ocupacao

    Relatorio.set_ocupacoes_max(ocupacoes_max)


def inicializar_relatorio():
    evento = controller_eventos.find_todays_evento()
    Relatorio.set_evento(evento)

    areas = controller_areas.find_all_areas()
    ocupacoes_max = dict()
    for area in areas:
        ocupacao = len(controller_estacionamento.find_placas_by_area(area.get_nome()))
        if evento is not None:
            ocupacao += evento.get_reservas()[area]
        area.set_ocupacao(ocupacao)
        ocupacoes_max[area] = ocupacao

    Relatorio.set_ocupacoes_max(ocupacoes_max)

