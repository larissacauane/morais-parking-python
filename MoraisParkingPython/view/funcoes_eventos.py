from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_permissoes import ControllerPermissoes
from control.controller_area import ControllerAreaEstacionamento
from control.controller_eventos import ControllerEventos

from model.evento import Evento

from datetime import datetime

controller_veiculo = ControllerVeiculos()
controller_proprietario = ControllerProprietario()
controller_permissoes = ControllerPermissoes()
controller_areas = ControllerAreaEstacionamento()
controller_eventos = ControllerEventos()


def cadastrar_evento():
    print("\n====== CADASTRAR EVENTO ======")
    evento_nome = input("Nome: ")
    evento = controller_eventos.find_evento(evento_nome)

    if evento is not None:
        print("Ja existe evento cadastrado com esse nome")
        return
    try:
        inicio = datetime.strptime(input("Data inicio (\"DD/MM/AAAA\"): "), "%d/%m/%Y").date()
        fim = datetime.strptime(input("Data fim (\"DD/MM/AAAA\"): "), "%d/%m/%Y").date()
    except:
        print("Input invalido.")
        return

    if inicio > fim:
        print("A data final nao pode ser antes da data de inicio")
        return

    if inicio <= datetime.now().date():
        print("Um novo evento so pode ser cadastrado para datas futuras")
        return

    evento = Evento(evento_nome, inicio, fim)

    eventos_cadastrados = controller_eventos.find_all_eventos()
    for evento_cadastrado in eventos_cadastrados:
        if evento_cadastrado.get_data_inicial() <= inicio <= evento_cadastrado.get_data_final():
            print("Ja existe evento cadastrado nesse periodo")
            return
        if evento_cadastrado.get_data_inicial() <= fim <= evento_cadastrado.get_data_final():
            print("Ja existe evento cadastrado nesse periodo")
            return
        if inicio < evento_cadastrado.get_data_inicial() < fim:
            print("Ja existe evento cadastrado nesse periodo")
            return

    areas = controller_areas.find_all_areas()
    reservas = dict()
    print("Defina quantas vagas serao reservadas para o evento em cada area:")
    for area in areas:
        try:
            input_str = "Area: " + area.get_nome() + \
                        "; Maximo: " + str(area.get_capacidade()) + \
                        "; Vagas: "
            vagas = int(input(input_str))
            if vagas > area.get_capacidade():
                print("Voce nao pode reservar mais vagas do que a capacidade maxima da area")
                return
            # reservas[area.get_nome()] = vagas
            reservas[area] = vagas
        except:
            print("Input invalido")
            return

    evento.set_reservas(reservas)
    controller_eventos.register_evento(evento)


def remover_evento():
    print("\n====== REMOVER EVENTO ======")
    eventos = controller_eventos.find_all_eventos()
    if len(eventos) <= 0:
        print("Nao existem eventos cadastrados")
        return
    print("Eventos:")
    eventos_str = ""
    for i in range(len(eventos)):
        eventos_str += "[{}] {}  ".format((i + 1), eventos[i].get_nome_evento())
    print(eventos_str)
    try:
        evento = eventos[(int(input("Escolha o indice da evento a ser removido: ")) - 1)]
        controller_eventos.remove_evento(evento.get_nome_evento())
    except:
        print("Input invalido. Voce precisa inserir um indice valido")


