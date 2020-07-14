class Evento():

    # CONSTRUTOR
    def __init__(self, nome_evento, data_inicial, data_final, reservas=None):
        if reservas is None:
            reservas = dict()
        self.nome_evento = nome_evento
        self.data_inicial = data_inicial
        self.data_final = data_final
        self.reservas = reservas

    # GETTERS AND SETTERS
    def get_nome_evento(self):
        return self.nome_evento

    def set_nome_evento(self, nome_evento):
        self.nome_evento = nome_evento

    def get_data_inicial(self):
        return self.data_inicial

    def set_data_inicial(self, data_inicial):
        self.data_inicial = data_inicial

    def get_data_final(self):
        return self.data_final

    def set_data_final(self, data_final):
        self.data_final = data_final

    def get_reservas(self):
        return self.reservas

    def set_reservas(self, reservas):
        self.reservas = reservas

    def add_reserva(self, area, vagas):
        self.reservas[area] = vagas

    # STR (toString)
    def __str__(self):
        return "Nome do evento: " + self.nome_evento + "\nData inicial: " + str(self.data_inicial) + \
               "\nData Final: " + str(self.data_final)
