
from dao.data_eventos import DataEventos
from dao.data_reservas import DataReservas


from datetime import datetime

class ControllerEventos():
    def __init__(self):
        self.data_eventos = DataEventos()
        self.data_reservas = DataReservas()

    def register_evento(self, evento):
        success = True
        self.data_eventos.open()
        evento_nome = evento.get_nome_evento()
        inicio = evento.get_data_inicial()
        fim = evento.get_data_final()
        reservas = evento.get_reservas()
        queried = self.data_eventos.query_evento_by_nome(evento_nome)
        if queried is not None:
            print("Ja existe evento cadastrado com o mesmo nome")
            success = False
        success = success and self.data_eventos.insert_evento(evento_nome, inicio, fim)
        self.data_eventos.close()
        self.data_reservas.open()
        success = success and self.data_reservas.insert_reservas(evento_nome, reservas)
        self.data_reservas.close()
        if success:
            print("Evento cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar o evento")
        return success

    def remove_evento(self, evento_nome):
        self.data_eventos.open()
        success = self.data_eventos.delete_evento(evento_nome)
        self.data_eventos.close()
        self.data_reservas.open()
        success = success and self.data_reservas.delete_reservas_by_evento(evento_nome)
        self.data_reservas.close()
        if success:
            print("Evento removido com sucesso!")
        else:
            print("Não foi possivel remover o evento")
        return success

    def find_all_eventos(self):
        self.data_eventos.open()
        eventos = self.data_eventos.query_all_eventos()
        self.data_eventos.close()
        self.data_reservas.open()
        for evento in eventos:
            reservas = self.data_reservas.query_reservas_by_evento(evento.get_nome_evento())
            evento.set_reservas(reservas)
        self.data_reservas.close()
        return eventos

    def find_evento(self, nome):
        self.data_eventos.open()
        evento = self.data_eventos.query_evento_by_nome(nome)
        self.data_eventos.close()
        return evento

    def find_todays_evento(self):
        today = datetime.now().date()
        eventos = self.find_all_eventos()
        for evento in eventos:
            inicio = evento.get_data_inicial()
            fim = evento.get_data_final()
            if inicio <= today <= fim:
                return evento
        return None



