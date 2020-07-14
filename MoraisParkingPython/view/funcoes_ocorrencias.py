from model.relatorio import Relatorio
from model.ocorrencia import Ocorrencia
from model.constants import *

from datetime import datetime

def registrar_ocorrencia():
    print("\n====== REGISTRAR OCORRENCIA ======")
    print("Tipos de ocorrencia:")
    tipos_ocorrencia_str = ""
    for key, val in TIPO_OCORRENCIA.items():
        tipos_ocorrencia_str += "[{}] {}  ".format(key, val)
    print(tipos_ocorrencia_str)
    try:
        tipo = TIPO_OCORRENCIA[int(input("Escolha o indice do tipo de ocorrencia: "))]
    except:
        print("Input invalido. Voce precisa inserir um indice valido")
        return

    veiculos_envolvidos = get_veiculos_envolvidos()
    data = datetime.now()

    ocorrencia = Ocorrencia(tipo, veiculos_envolvidos, data)

    Relatorio.add_ocorrencia(ocorrencia)
    print("Ocorrencia registrada com sucesso")


def get_veiculos_envolvidos():
    placas = set()
    while True:
        placa = input("Placa (ou 's' para sair): ")
        if placa.upper() == "S":
            return placas
        else:
            placas.add(placa)


