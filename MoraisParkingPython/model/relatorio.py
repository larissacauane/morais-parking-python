from datetime import datetime
from model.area_estacionamento import AreaEstacionamento


class Relatorio(object):
    ocupacoes_max = dict()
    ocorrencias = list()
    evento = None

    @classmethod
    def get_ocupacoes_max(cls):
        return cls.ocupacoes_max

    @classmethod
    def set_ocupacoes_max(cls, ocupacoes_max):
        cls.ocupacoes_max = ocupacoes_max

    @classmethod
    def get_ocorrencias(cls):
        return cls.ocorrencias

    @classmethod
    def set_ocorrencias(cls, ocorrencias):
        cls.ocorrencias = ocorrencias

    @classmethod
    def add_ocorrencia(cls, ocorrencia):
        cls.ocorrencias.append(ocorrencia)

    @classmethod
    def del_ocorrencia(cls, ocorrencia):
        cls.ocorrencias.remove(ocorrencia)

    @classmethod
    def get_evento(cls):
        return cls.evento

    @classmethod
    def set_evento(cls, evento):
        cls.evento = evento

    @classmethod
    def generate_relatorio_string(cls):
        cabecalho = "MORAIS PARKING RELATORIO\n"
        cabecalho += "Estacionamento: UNIESP\n"
        cabecalho += "Data: " + str(datetime.now().date()) + "\n"

        ocupacao = "\nOCUPACAO MAXIMA:\n"
        if len(cls.ocupacoes_max) == 0:
            ocupacao += "Sem informacao disponivel\n"
        else:
            for area, ocupacao_max in cls.ocupacoes_max.items():
                currArea = AreaEstacionamento(area.get_nome(), area.get_tipo(), area.get_capacidade())
                currArea.set_ocupacao(ocupacao_max)
                ocupacao += str(currArea) + "\n"

        evento = "\nEVENTO DO DIA:\n"
        if cls.evento is None:
            evento += "Nao ha evento no dia de hoje\n"
        else:
            evento += str(cls.evento) + "\n"

        ocorrencias = "\nOCORRENCIAS:\n"
        if len(cls.ocorrencias) == 0:
            ocorrencias += "Nao existem ocorrencias\n"
        else:
            for ocorrencia in cls.ocorrencias:
                ocorrencias += str(ocorrencia) + "\n"

        return cabecalho + ocupacao + evento + ocorrencias


