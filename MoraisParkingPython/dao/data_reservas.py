import sqlite3
from dao.db_constants import *
from model.area_estacionamento import AreaEstacionamento


class DataReservas():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_reservas_table(self):
        try:
            self.c.execute(DROP_RESERVAS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_reservas_table(self):
        try:
            self.c.execute(CREATE_RESERVAS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_reservas(self, evento_nome, reservas):
        try:
            for area, vagas in reservas.items():
                self.c.execute(INSERT_RESERVA, (evento_nome, area.get_nome(), vagas))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_reservas_by_evento(self, evento_nome):
        try:
            self.c.execute(QUERY_RESERVAS_BY_EVENTO, (evento_nome,))
            reservas_data = self.c.fetchall()
            reservas = {}
            for reserva_data in reservas_data:
                self.c.execute(QUERY_AREA_BY_NOME, (reserva_data[1],))
                area_data = self.c.fetchone()
                nome = area_data[0]
                ocupacao = area_data[1]
                capacidade = area_data[2]
                tipo = area_data[3]
                especial = area_data[4] == 1
                area = AreaEstacionamento(nome, tipo, capacidade, especial, ocupacao)
                vagas = reserva_data[2]
                reservas[area] = vagas
            return reservas
        except sqlite3.Error:
            return None

    def query_reserva(self, evento_nome, area_nome):
        try:
            self.c.execute(QUERY_RESERVA, (evento_nome, area_nome))
            reserva = self.c.fetchone()
            return reserva
        except sqlite3.Error:
            return None

    def delete_reservas_by_evento(self, evento_nome):
        try:
            self.c.execute(DELETE_RESERVAS_BY_EVENTO, (evento_nome,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def delete_reservas_by_area(self, area_nome):
        try:
            self.c.execute(DELETE_RESERVAS_BY_AREA, (area_nome,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def close(self):
        try:
            self.conn.close()
            return True
        except sqlite3.Error:
            return False



