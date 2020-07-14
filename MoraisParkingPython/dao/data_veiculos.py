import sqlite3
from dao.db_constants import *
from model.veiculo import Veiculo
from model.proprietario import Proprietario

class DataVeiculos():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_veiculos_table(self):
        try:
            self.c.execute(DROP_VEICULOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_veiculos_table(self):
        try:
            self.c.execute(CREATE_VEICULOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_veiculo(self, veiculo):
        placa = veiculo.get_placa()
        modelo = veiculo.get_modelo()
        cor = veiculo.get_cor()
        proprietario = veiculo.get_proprietario()
        proprietario_nome = proprietario.get_nome()
        tipo = veiculo.get_tipo()
        t = (placa, modelo, cor, proprietario_nome, tipo)
        try:
            self.c.execute(INSERT_VEICULO, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_veiculo_by_placa(self, placa):
        try:
            self.c.execute(QUERY_VEICULO_BY_PLACA, (placa,))
            veiculo_data = self.c.fetchone()
            if veiculo_data is None:
                return None
            placa = veiculo_data[0]
            modelo = veiculo_data[1]
            cor = veiculo_data[2]
            proprietario_nome = veiculo_data[3]
            area = veiculo_data[4]
            self.c.execute(QUERY_PROPRIETARIO_BY_NOME, (proprietario_nome,))
            proprietario_info = self.c.fetchone()
            proprietario = Proprietario(
                proprietario_info[0],
                proprietario_info[1],
                proprietario_info[2]
            )
            return Veiculo(placa, modelo, cor, proprietario, area)
        except sqlite3.Error as e:
            return None

    def query_placas_by_proprietario(self, proprietario_nome):
        try:
            self.c.execute(QUERY_PLACAS_BY_PROPRIETARIO, (proprietario_nome,))
            placas_data = self.c.fetchall()
            placas = []
            for placa_data in placas_data:
                placas.append(placa_data[0])
            return placas
        except:
            return []

    def delete_veiculo_by_placa(self, placa):
        try:
            self.c.execute(QUERY_VEICULO_BY_PLACA, (placa,))
            veiculo_data = self.c.fetchone()
            if veiculo_data is None:
                return False
            self.c.execute(DELETE_PERMISSOES_BY_VEICULO, (placa,))
            self.c.execute(DELETE_VEICULO, (placa,))
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




