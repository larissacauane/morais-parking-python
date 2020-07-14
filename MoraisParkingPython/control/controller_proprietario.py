from dao.data_proprietarios import DataProprietarios
from model.proprietario import Proprietario


class ControllerProprietario():

    def __init__(self):
        self.data_proprietario = DataProprietarios()

    def register_proprietario(self, nome, matricula, curso):
        self.data_proprietario.open()
        proprietario = Proprietario(nome, matricula, curso)
        success = self.data_proprietario.insert_proprietario(proprietario)
        if success:
            print("Prprietario cadastrado com sucesso!")
        else:
            print("Não foi possível cadastrar o proprietario")
        self.data_proprietario.close()
        return success

    def remove_proprietario(self, nome):
        self.data_proprietario.open()
        success = self.data_proprietario.delete_proprietario_by_nome(nome)
        if success:
            print("Proprietario foi removido com sucesso!")
        else:
            print("Não foi possivel remover o proprietario")
        self.data_proprietario.close()
        return success

    def find_proprietario(self, nome):
        self.data_proprietario.open()
        proprietario = self.data_proprietario.query_proprietario_by_nome(nome)
        if proprietario is None:
            print("Proprietario não encontrado")
        self.data_proprietario.close()
        return proprietario



