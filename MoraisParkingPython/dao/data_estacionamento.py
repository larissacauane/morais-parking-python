import sqlite3
from dao.db_constants import *


class DataEstacionamento():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_estacionamento_table(self):
        try:
            self.c.execute(DROP_ESTACIONAMENTO_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_estacionamento_table(self):
        try:
            self.c.execute(CREATE_ESTACIONAMENTO_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_veiculo_in_estacionamento(self, placa, area_nome):
        try:
            self.c.execute(INSERT_VEICULO_IN_ESTACIONAMENTO, (placa, area_nome))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_placas_by_area(self, area_nome):
        try:
            self.c.execute(QUERY_PLACAS_BY_AREA, (area_nome,))
            placas_data = self.c.fetchall()
            placas = []
            for placa_data in placas_data:
                placas.append(placa_data[0])
            return placas
        except sqlite3.Error:
            return []

    def query_all_placas(self):
        try:
            self.c.execute(QUERY_ALL_PLACAS)
            placas_data = self.c.fetchall()
            placas = []
            for placa_data in placas_data:
                placas.append(placa_data[0])
            return placas
        except sqlite3.Error:
            return []

    def delete_placa(self, placa):
        try:
            self.c.execute(DELETE_PLACA_FROM_ESTACIONAMENTO, (placa,))
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def delete_placa_by_area(self, area_nome):
        try:
            self.c.execute(DELETE_PLACAS_BY_AREA, (area_nome,))
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


