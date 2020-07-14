from control.controller_login import ControllerLogin
from model.constants import *

controller_login = ControllerLogin()


def login():
    print("\n====== LOGIN ======")
    email = input("Email: ")
    senha = input("Senha: ")

    usuario = controller_login.sign_in(email, senha)
    return usuario


def cadastrar_funcionario():
    print("\n====== CADASTRO FUNCIONARIO ======")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    print("[1] Estacionamento; [2] RH; [3] Gestao")
    setor = SETOR[int(input("Setor (1, 2, ou 3): "))]

    controller_login.sign_up(nome, email, senha, setor)


def remover_funcionario():
    print("\n====== REMOVER FUNCIONARIO ======")
    email = input("Email: ")

    controller_login.remove_user(email)

