from dao.data_usuarios import DataUsuarios
from model.usuario import Usuario

class ControllerLogin():
    def __init__(self):
        self.data_usuarios = DataUsuarios()

    def sign_up(self, nome, email, senha, setor):
        self.data_usuarios.open()
        usuario = Usuario(nome, email, senha, setor)
        success = self.data_usuarios.insert_usuario(usuario)
        if success:
            print("Funcionario cadastrado com sucesso!")
        else:
            print("Nao foi possivel cadastrar o Funcionario.")
        self.data_usuarios.close()
        return success

    def sign_in(self, email, senha):
        self.data_usuarios.open()
        usuario = self.data_usuarios.query_usuario_by_email(email)
        if usuario is None:
            print("Email nao encontrado")
        elif usuario.get_senha() != senha:
            print("Funcionario ou senha incorreta")
            usuario = None
        self.data_usuarios.close()
        return usuario

    def remove_user(self, email):
        self.data_usuarios.open()
        usuario = self.data_usuarios.query_usuario_by_email(email)
        if usuario is None:
            print("Email nao encontrado")
            self.data_usuarios.close()
            return False
        if self.data_usuarios.delete_usuario_by_email(email):
            print("Funcionario removido com sucesso!")
            return True
        return False




