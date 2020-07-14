import sqlite3
from dao.db_constants import *
from model.usuario import Usuario

class DataUsuarios():
    def open(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.c = self.conn.cursor()

    def drop_usuarios_table(self):
        try:
            self.c.execute(DROP_USUARIOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def create_usuarios_table(self):
        try:
            self.c.execute(CREATE_USUARIOS_TABLE)
            self.conn.commit()
            return True
        except sqlite3.Error:
            return False

    def insert_usuario(self, usuario):
        nome = usuario.get_nome()
        email = usuario.get_email()
        senha = usuario.get_senha()
        setor = usuario.get_setor()
        t = (nome, email, senha, setor)
        try:
            self.c.execute(INSERT_USUARIO, t)
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def query_usuario_by_email(self, email):
        try:
            self.c.execute(QUERY_USUARIO_BY_EMAIL, (email,))
            user_data = self.c.fetchone()
            if user_data is None:
                return None
            _id = user_data[0]
            nome = user_data[1]
            email = user_data[2]
            senha = user_data[3]
            setor = user_data[4]
            return Usuario(nome, email, senha, setor, _id)
        except sqlite3.Error as e:
            return None

    def delete_usuario_by_email(self, email):
        try:
            self.c.execute(QUERY_USUARIO_BY_EMAIL, (email,))
            user_data = self.c.fetchone()
            if user_data is None:
                return False
            self.c.execute(DELETE_USUARIO, (email,))
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


