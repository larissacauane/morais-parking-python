from control.controller_proprietario import ControllerProprietario

controller_proprietario = ControllerProprietario()

def cadastrar_proprietario():
    print("\n====== CADASTRO PROPRIETARIO ======")
    nome = input("Nome: ")
    matricula = input("Matricula: ")
    curso = input("Curso: ")

    controller_proprietario.register_proprietario(nome, matricula, curso)

def remover_proprietario():
    print("\n====== REMOVER PROPRIETARIO ======")
    nome = input("Nome: ")

    controller_proprietario.remove_proprietario(nome)


