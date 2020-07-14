
from view.view_constants import *
from view.funcoes_funcionario import *
from view.funcoes_proprietario import *
from view.funcoes_veiculo import *
from view.funcoes_areas import *
from view.funcoes_permissoes import *
from view.funcoes_eventos import *
from view.funcoes_estacionamento import *
from view.funcoes_ocorrencias import *
from view.funcoes_relatorio import *


class Main():
    def __init__(self):

        self.usuario = None
        self.veiculo = None
        self.proprietario = None
        self.area = None

        inicializar_relatorio()

    def start(self):
        print("\n====== MORAIS PARKING ======")
        print("[1] Entrar", "\n[2] Sair")

        op_menu = int(input(MENU))
        if op_menu == 1:
            self.login()
        elif op_menu == 2:
            quit()
        else:
            print("Opcao invalida")
            self.start()

    def login(self):
        self.usuario = login()
        self.menu()


    def menu(self):
        if self.usuario is None:
            self.start()
            return
        tipo = self.usuario.get_setor()
        if tipo == SETOR[1]:
            self.menu_estacionamento()
        elif tipo == SETOR[2]:
            self.menu_rh()
        elif tipo == SETOR[3]:
            self.menu_gestor()


    def logout(self):
        self.usuario = None


    def menu_rh(self):
        opcoes = {
            1: cadastrar_proprietario,
            2: remover_proprietario,
            3: cadastrar_veiculo,
            4: remover_veiculo,
            5: conceder_permissao,
            6: remover_permissao,
            7: cadastrar_funcionario,
            8: remover_funcionario,
            9: self.logout
        }
        print("\n====== MENU RH ======")
        print("[1] Cadastrar proprietario",
              "\n[2] Remover proprietario",
              "\n[3] Cadastrar veiculo",
              "\n[4] Remover veiculo",
              "\n[5] Conceder permissao",
              "\n[6] Remover proprietario",
              "\n[7] Cadastrar funcionario",
              "\n[8] Remover funcionario",
              "\n[9] Logout")

        try:
            op_menu = int(input(MENU))
            opcoes[op_menu]()
        except:
            print("Opcao invalida")
            self.menu_rh()
        self.menu()


    def menu_estacionamento(self):
        opcoes = {
            1: consultar_status,
            2: autorizar_entrada,
            3: autorizar_saida,
            4: cadastrar_proprietario,
            5: remover_proprietario,
            6: cadastrar_veiculo,
            7: remover_veiculo,
            8: registrar_ocorrencia,
            9: self.logout
        }
        print("\n====== MENU ESTACIONAMENTO ======")
        print("[1] Consultar status",
              "\n[2] Autorizar entrada",
              "\n[3] Autorizar saida",
              "\n[4] Cadastrar proprietario",
              "\n[5] Remover proprietario",
              "\n[6] Cadastrar veiculo",
              "\n[7] Remover veiculo",
              "\n[8] Registrar ocorrencia",
              "\n[9] Logout")

        try:
            op_menu = int(input(MENU))
            opcoes[op_menu]()
        except:
            print("Opcao invalida")
            self.menu_rh()
        self.menu()


    def menu_gestor(self):
        opcoes = {
            1: cadastrar_funcionario,
            2: remover_funcionario,
            3: cadastrar_area_especial,
            4: remover_area_especial,
            5: cadastrar_evento,
            6: remover_evento,
            7: gerar_relatorio,
            8: self.logout
        }
        print("\n====== MENU GESTAO ======")
        print("[1] Cadastrar funcionario",
              "\n[2] Remover funcionario",
              "\n[3] Cadastrar area especial",
              "\n[4] Remover area especial",
              "\n[5] Cadastrar evento",
              "\n[6] Remover evento",
              "\n[7] Gerar relatorio",
              "\n[8] Logout")

        try:
            op_menu = int(input(MENU))
            opcoes[op_menu]()
        except:
            print("Opcao invalida")
            self.menu_rh()
        self.menu()



main = Main()
main.start()
