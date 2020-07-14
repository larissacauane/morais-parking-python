import sqlite3
from dao.db_constants import *
from model.evento import Evento
from datetime import datetime


class DataEventos():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_eventos_table(self):
        try:
            self.c.execute(DROP_EVENTOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_eventos_table(self):
        try:
            self.c.execute(CREATE_EVENTOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_evento(self, nome, inicio, fim):
        try:
            queried = self.query_evento_by_nome(nome)
            if queried is not None:
                return False
            self.c.execute(INSERT_EVENTO, (nome, inicio, fim))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_evento_by_nome(self, nome):
        try:
            self.c.execute(QUERY_EVENTO_BY_NAME, (nome,))
            evento_data = self.c.fetchone()
            evento = None
            if evento_data is not None:
                nome = evento_data[0]
                inicio = (datetime.strptime(evento_data[1], "%Y-%m-%d")).date()
                fim = (datetime.strptime(evento_data[2], "%Y-%m-%d")).date()
                evento = Evento(nome, inicio, fim)
            return evento
        except sqlite3.Error:
            return None

    def query_all_eventos(self):
        try:
            self.c.execute(QUERY_ALL_EVENTOS)
            eventos_data = self.c.fetchall()
            eventos = []
            for evento_data in eventos_data:
                nome = evento_data[0]
                inicio = (datetime.strptime(evento_data[1], "%Y-%m-%d")).date()
                fim = (datetime.strptime(evento_data[2], "%Y-%m-%d")).date()
                eventos.append(Evento(nome, inicio, fim))
            return eventos
        except sqlite3.Error:
            return []

    def delete_evento(self, nome):
        try:
            self.c.execute(DELETE_EVENTO, (nome,))
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




