import sqlite3
from dao.db_constants import *
from model.proprietario import Proprietario


class DataProprietarios():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_proprietarios_table(self):
        try:
            self.c.execute(DROP_PROPRIETARIOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_proprietarios_table(self):
        try:
            self.c.execute(CREATE_PROPRIETARIOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_proprietario(self, proprietario):
        nome = proprietario.get_nome()
        matricula = proprietario.get_matricula()
        curso = proprietario.get_curso()
        t = (nome, matricula, curso)
        try:
            self.c.execute(INSERT_PROPRIETARIOS, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_proprietario_by_nome(self, nome):
        try:
            self.c.execute(QUERY_PROPRIETARIO_BY_NOME, (nome,))
            proprietario_data = self.c.fetchone()
            if proprietario_data is not None:
                nome = proprietario_data[0]
                matricula = proprietario_data[1]
                curso = proprietario_data[2]
                return Proprietario(nome, matricula, curso)
        except sqlite3.Error:
            return None

    def delete_proprietario_by_nome(self, nome):
        try:
            self.c.execute(QUERY_PROPRIETARIO_BY_NOME, (nome,))
            proprietario_data = self.c.fetchone()
            if proprietario_data is None:
                return False
            self.c.execute(QUERY_PLACAS_BY_PROPRIETARIO, (nome,))
            placas = self.c.fetchall()
            for placa in placas:
                self.c.execute(DELETE_PERMISSOES_BY_VEICULO, (placa[0],))
                self.c.execute(DELETE_VEICULO, (placa[0],))
            self.c.execute(DELETE_PROPRIETARIO, (nome,))
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



