from control.controller_veiculos import ControllerVeiculos
from control.controller_proprietario import ControllerProprietario
from control.controller_permissoes import ControllerPermissoes
from control.controller_area import ControllerAreaEstacionamento


controller_veiculo = ControllerVeiculos()
controller_proprietario = ControllerProprietario()
controller_permissoes = ControllerPermissoes()
controller_areas = ControllerAreaEstacionamento()


def conceder_permissao():
    print("\n====== CONCEDER PERMISSAO ======")
    proprietario_nome = input("Proprietario: ")
    proprietario = controller_proprietario.find_proprietario(proprietario_nome)
    if proprietario is None:
        return
    placas = controller_veiculo.find_placas_by_proprietario(proprietario_nome)
    if len(placas) <= 0:
        print("O proprietario nao possui veiculos cadastrados")
        return
    print("Placas dos veiculos do proprietario:")
    placas_str = ""
    for i in range(len(placas)):
        placas_str += "[{}] {}  ".format((i + 1), placas[i])
    print(placas_str)
    try:
        placa = placas[(int(input("Escolha o indice da placa do veiculo: ")) - 1)]
        veiculo = controller_veiculo.find_veiculo(placa)
        permissao = controller_permissoes.find_permissao_by_placa(placa)
        if permissao is not None:
            print("O veiculo ja possui uma permissao especial")
            return
        areas = controller_areas.find_compatible_special_areas(veiculo.get_tipo())
        if len(areas) <= 0:
            print("Nao existem areas especiais compativeis com o veiculo")
            return
        areas_str = ""
        for i in range(len(areas)):
            areas_str += "[{}] {}  ".format((i + 1), areas[i].get_nome())
        print("Areas especiais compativeis com o veiculo:")
        print(areas_str)
        area_nome = areas[(int(input("Escolha o indice da area: ")) - 1)].get_nome()
        controller_permissoes.register_permissao(placa, area_nome)
    except:
        print("Input invalido. Voce precisa inserir um indice valido")


def remover_permissao():
    print("\n====== REMOVER PERMISSAO ======")
    proprietario_nome = input("Proprietario: ")
    proprietario = controller_proprietario.find_proprietario(proprietario_nome)
    if proprietario is None:
        return
    placas = controller_veiculo.find_placas_by_proprietario(proprietario_nome)
    if len(placas) <= 0:
        print("O proprietario nao possui veiculos cadastrados")
        return
    print("Placas dos veiculos do proprietario:")
    placas_str = ""
    for i in range(len(placas)):
        placas_str += "[{}] {}  ".format((i + 1), placas[i])
    print(placas_str)
    try:
        placa = placas[(int(input("Escolha o indice da placa do veiculo: ")) - 1)]
        permissoes = controller_permissoes.find_permissao_by_placa(placa)
        if len(permissoes) <= 0:
            print("O veiculo nao possui permissoes para estacionar em areas especiais")
            return
        areas_str = ""
        for i in range(len(permissoes)):
            areas_str += "[{}] {}  ".format((i + 1), permissoes[i][1])
        print("Areas especiais em que o veiculo possui permissao para ser estacionado:")
        print(areas_str)
        permissao = permissoes[(int(input("Escolha o indice da area: ")) - 1)]
        controller_permissoes.remove_permissao(permissao[0], permissao[1])
    except:
        print("Input invalido. Voce precisa inserir um indice valido")



