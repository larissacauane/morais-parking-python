from dao.data_eventos import DataEventos
from dao.data_reservas import DataReservas
from dao.data_estacionamento import DataEstacionamento

class ControllerEstacionamento():
    def __init__(self):
        self.data_eventos = DataEventos()
        self.data_reservas = DataReservas()
        self.data_estacionamento = DataEstacionamento()

    def autorizar_entrada(self, placa, area_nome):
        self.data_estacionamento.open()
        success = self.data_estacionamento.insert_veiculo_in_estacionamento(placa, area_nome)
        self.data_estacionamento.close()

        return success

    def autorizar_saida(self, placa):
        self.data_estacionamento.open()
        success = self.data_estacionamento.delete_placa(placa)
        self.data_estacionamento.close()

        return success

    def find_all_placas(self):
        self.data_estacionamento.open()
        placas = self.data_estacionamento.query_all_placas()
        self.data_estacionamento.close()
        return placas

    def find_placas_by_area(self, area_nome):
        self.data_estacionamento.open()
        placas = self.data_estacionamento.query_placas_by_area(area_nome)
        self.data_estacionamento.close()
        return placas


