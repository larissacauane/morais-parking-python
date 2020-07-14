# DATA BASE
DB_NAME = "../morais_parking.db"

# NOMES TABELA
USUARIOS_TABLE = "usuarios"
VEICULOS_TABLE = "veiculos"
PROPRIETARIOS_TABLE = "proprietarios"
AREAS_TABLE = "areas"
PERMISSOES_TABLE = "permissoes"
EVENTOS_TABLE = "eventos"
RESERVAS_TABLE = "reservas"
ESTACIONAMENTO_TABLE = "estacionamento"

# USUARIO
DROP_USUARIOS_TABLE = "DROP TABLE IF EXISTS " + USUARIOS_TABLE
CREATE_USUARIOS_TABLE = "CREATE TABLE IF NOT EXISTS " + USUARIOS_TABLE + \
                        " (_id INTEGER PRIMARY KEY," + \
                        " nome TEXT NOT NULL," + \
                        " email TEXT NOT NULL UNIQUE," + \
                        " senha TEXT NOT NULL," + \
                        " setor TEXT NOT NULL)"

INSERT_USUARIO = "INSERT INTO " + USUARIOS_TABLE + \
                 " (nome, email, senha, setor)" + \
                 " VALUES (?, ?, ?, ?)"

DELETE_USUARIO = "DELETE FROM " + USUARIOS_TABLE + \
                 " WHERE email = ?"

QUERY_USUARIO_BY_EMAIL = "SELECT * FROM " + USUARIOS_TABLE + \
                         " WHERE email = ?"

# VEICULO
DROP_VEICULOS_TABLE = "DROP TABLE IF EXISTS " + VEICULOS_TABLE
CREATE_VEICULOS_TABLE = "CREATE TABLE IF NOT EXISTS " + VEICULOS_TABLE + \
                        "(placa TEXT NOT NULL UNIQUE, " + \
                        "modelo TEXT NOT NULL, " + \
                        "cor TEXT NOT NULL, " + \
                        "proprietario TEXT NOT NULL, " + \
                        "tipo TEXT NOT NULL)"

INSERT_VEICULO = "INSERT INTO " + VEICULOS_TABLE + \
                 "(placa, modelo, cor, proprietario, tipo)" + \
                 " VALUES (?, ?, ?, ?, ?)"

DELETE_VEICULO = "DELETE FROM " + VEICULOS_TABLE + \
                 " WHERE placa = ?"

QUERY_VEICULO_BY_PLACA = "SELECT * FROM " + VEICULOS_TABLE + \
                         " WHERE placa = ?"

QUERY_PLACAS_BY_PROPRIETARIO = "SELECT placa FROM " + VEICULOS_TABLE + \
                               " WHERE proprietario = ?"


# PROPRIETARIO
DROP_PROPRIETARIOS_TABLE = "DROP TABLE IF EXISTS " + PROPRIETARIOS_TABLE
CREATE_PROPRIETARIOS_TABLE = "CREATE TABLE IF NOT EXISTS " + PROPRIETARIOS_TABLE + \
                             " (nome TEXT NOT NULL UNIQUE, " + \
                             " matricula TEXT, " + \
                             " curso TEXT)"

INSERT_PROPRIETARIOS = "INSERT INTO " + PROPRIETARIOS_TABLE + \
                       "(nome, matricula, curso)" + \
                       " VALUES (?, ?, ?)"

DELETE_PROPRIETARIO = "DELETE FROM " + PROPRIETARIOS_TABLE + \
                       " WHERE nome = ?"

QUERY_PROPRIETARIO_BY_NOME = "SELECT * FROM " + PROPRIETARIOS_TABLE + \
                              " WHERE nome = ?"


# AREA
DROP_AREAS_TABLE = "DROP TABLE IF EXISTS " + AREAS_TABLE
CREATE_AREAS_TABLE = "CREATE TABLE IF NOT EXISTS " + AREAS_TABLE + \
                    " (nome TEXT NOT NULL UNIQUE," + \
                    " ocupacao INTEGER NOT NULL," + \
                    " capacidade INTEGER NOT NULL," + \
                    " tipo TEXT NOT NULL," + \
                    " especial INTEGER NOT NULL)"

INSERT_AREA = "INSERT INTO " + AREAS_TABLE + \
              " (nome, ocupacao, capacidade, tipo, especial)" + \
              " VALUES (?, ?, ?, ?, ?)"

DELETE_AREA = "DELETE FROM " + AREAS_TABLE + \
              " WHERE nome = ?"

QUERY_AREA_BY_NOME = "SELECT * FROM " + AREAS_TABLE + \
                     " WHERE nome = ?"

QUERY_SPECIAL_AREAS = "SELECT * FROM " + AREAS_TABLE + \
                      " WHERE especial = ?"

QUERY_ALL_AREAS = "SELECT * FROM " + AREAS_TABLE

QUERY_AREAS_COMPATIVEIS = "SELECT * FROM " + AREAS_TABLE + \
                          " WHERE especial = ? AND tipo = ?"


# PERMISSOES
DROP_PERMISSOES_TABLE = "DROP TABLE IF EXISTS " + PERMISSOES_TABLE
CREATE_PERMISSOES_TABLE = "CREATE TABLE IF NOT EXISTS " + PERMISSOES_TABLE + \
                    " (veiculo_placa TEXT NOT NULL UNIQUE," + \
                    " area_nome TEXT NOT NULL)"

INSERT_PERMISSAO = "INSERT INTO " + PERMISSOES_TABLE + \
                   " (veiculo_placa, area_nome) VALUES (?, ?)"

DELETE_PERMISSAO = "DELETE FROM " + PERMISSOES_TABLE + \
                   " WHERE veiculo_placa = ? AND area_nome = ?"

DELETE_PERMISSOES_BY_VEICULO = "DELETE FROM " + PERMISSOES_TABLE + \
                               " WHERE veiculo_placa = ?"

DELETE_PERMISSOES_BY_AREA = "DELETE FROM " + PERMISSOES_TABLE + \
                            " WHERE area_nome = ?"

QUERY_PERMISSAO = "SELECT * FROM " + PERMISSOES_TABLE + \
                 " WHERE veiculo_placa = ? AND area_nome = ?"

QUERY_PERMISSOES_BY_VEICULO = "SELECT * FROM " + PERMISSOES_TABLE + \
                              " WHERE veiculo_placa = ?"


# EVENTOS
DROP_EVENTOS_TABLE = "DROP TABLE IF EXISTS " + EVENTOS_TABLE
CREATE_EVENTOS_TABLE = "CREATE TABLE IF NOT EXISTS " + EVENTOS_TABLE + \
                    " (nome TEXT NOT NULL UNIQUE," + \
                    " inicio TEXT NOT NULL UNIQUE," + \
                    " fim TEXT NOT NULL UNIQUE)"

INSERT_EVENTO = "INSERT INTO " + EVENTOS_TABLE + \
                " (nome, inicio, fim) VALUES (?, ?, ?)"

DELETE_EVENTO = "DELETE FROM " + EVENTOS_TABLE + \
                " WHERE nome = ?"

QUERY_EVENTO_BY_NAME = "SELECT * FROM " + EVENTOS_TABLE + \
                       " WHERE nome = ?"

QUERY_ALL_EVENTOS = "SELECT * FROM " + EVENTOS_TABLE


# RESERVAS
DROP_RESERVAS_TABLE = "DROP TABLE IF EXISTS " + RESERVAS_TABLE
CREATE_RESERVAS_TABLE = "CREATE TABLE IF NOT EXISTS " + RESERVAS_TABLE + \
                        " (evento_nome TEXT NOT NULL," + \
                        " area_nome TEXT NOT NULL," + \
                        " vagas INTEGER NOT NULL)"

INSERT_RESERVA = "INSERT INTO " + RESERVAS_TABLE + \
                 " (evento_nome, area_nome, vagas) VALUES (?, ?, ?)"

DELETE_RESERVAS_BY_EVENTO = "DELETE FROM " + RESERVAS_TABLE + \
                            " WHERE evento_nome = ?"

DELETE_RESERVAS_BY_AREA = "DELETE FROM " + RESERVAS_TABLE + \
                          " WHERE area_nome = ?"

QUERY_RESERVAS_BY_EVENTO = "SELECT * FROM " + RESERVAS_TABLE + \
                           " WHERE evento_nome = ?"

QUERY_RESERVA = "SELECT * FROM " + RESERVAS_TABLE + \
                " WHERE evento_nome = ? AND area_nome = ?"

# ESTACIONAMENTO
DROP_ESTACIONAMENTO_TABLE = "DROP TABLE IF EXISTS " + ESTACIONAMENTO_TABLE
CREATE_ESTACIONAMENTO_TABLE = "CREATE TABLE IF NOT EXISTS " + ESTACIONAMENTO_TABLE + \
                              " (placa TEXT NOT NULL UNIQUE," + \
                              " area TEXT NOT NULL)"

INSERT_VEICULO_IN_ESTACIONAMENTO = "INSERT INTO " + ESTACIONAMENTO_TABLE + \
                                   " (placa, area) VALUES (?, ?)"

DELETE_PLACA_FROM_ESTACIONAMENTO = "DELETE FROM " + ESTACIONAMENTO_TABLE + \
                                   " WHERE placa = ?"

DELETE_PLACAS_BY_AREA = "DELETE FROM " + ESTACIONAMENTO_TABLE + \
                        " WHERE area = ?"

QUERY_PLACAS_BY_AREA = "SELECT * FROM " + ESTACIONAMENTO_TABLE + \
                       " WHERE area = ?"

QUERY_ALL_PLACAS = "SELECT * FROM " + ESTACIONAMENTO_TABLE

