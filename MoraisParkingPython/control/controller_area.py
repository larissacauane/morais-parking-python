from dao.data_area import DataAreaEstacionamento
from model.area_estacionamento import AreaEstacionamento


class ControllerAreaEstacionamento():
    def __init__(self):
        self.data_area = DataAreaEstacionamento()

    def register_area(self, nome, tipo, capacidade):
        self.data_area.open()
        area = AreaEstacionamento(nome, tipo, capacidade)
        success = self.data_area.insert_area(area)
        if success:
            print("Area cadastrada com sucesso!")
        else:
            print("Não foi possível cadastrar a area")
        self.data_area.close()
        return success

    def remove_area(self, nome):
        self.data_area.open()
        success = self.data_area.delete_area_by_nome(nome)
        if success:
            print("Area foi removida com sucesso!")
        else:
            print("Não foi possivel remover a area ")
        self.data_area.close()
        return success

    def find_area(self, nome):
        self.data_area.open()
        area = self.data_area.query_area_by_nome(nome)
        if area is None:
            print("Area não está cadastrada")
        self.data_area.close()
        return area

    def find_special_areas(self):
        self.data_area.open()
        areas = self.data_area.query_areas_especiais()
        self.data_area.close()
        return areas


    def find_all_areas(self):
        self.data_area.open()
        areas = self.data_area.query_all_areas()
        self.data_area.close()
        return areas

    def find_compatible_special_areas(self, tipo):
        self.data_area.open()
        areas = self.data_area.query_areas_especiais_compativeis(tipo)
        self.data_area.close()
        return areas

    def find_compatible_common_area(self, tipo):
        self.data_area.open()
        areas = self.data_area.query_areas_comuns_compativeis(tipo)
        self.data_area.close()
        return areas[0]


