BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "permissoes" (
	"veiculo_placa"	TEXT NOT NULL UNIQUE,
	"area_nome"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "estacionamento" (
	"placa"	TEXT NOT NULL UNIQUE,
	"area"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "eventos" (
	"nome"	TEXT NOT NULL UNIQUE,
	"inicio"	TEXT NOT NULL UNIQUE,
	"fim"	TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "reservas" (
	"evento_nome"	TEXT NOT NULL,
	"area_nome"	TEXT NOT NULL,
	"vagas"	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "areas" (
	"nome"	TEXT NOT NULL UNIQUE,
	"ocupacao"	INTEGER NOT NULL,
	"capacidade"	INTEGER NOT NULL,
	"tipo"	TEXT NOT NULL,
	"especial"	INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS "veiculos" (
	"placa"	TEXT NOT NULL UNIQUE,
	"modelo"	TEXT NOT NULL,
	"cor"	TEXT NOT NULL,
	"proprietario"	TEXT NOT NULL,
	"tipo"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "proprietarios" (
	"nome"	TEXT NOT NULL UNIQUE,
	"matricula"	TEXT,
	"curso"	TEXT
);
CREATE TABLE IF NOT EXISTS "usuarios" (
	"_id"	INTEGER,
	"nome"	TEXT NOT NULL,
	"email"	TEXT NOT NULL UNIQUE,
	"senha"	TEXT NOT NULL,
	"setor"	TEXT NOT NULL,
	PRIMARY KEY("_id")
);
INSERT INTO "permissoes" VALUES ('CBA4321','VIP');
INSERT INTO "eventos" VALUES ('Hackathon','2020-06-02','2020-06-16');
INSERT INTO "reservas" VALUES ('Hackathon','Carros',5);
INSERT INTO "reservas" VALUES ('Hackathon','Motos',5);
INSERT INTO "reservas" VALUES ('Hackathon','Ônibus',5);
INSERT INTO "reservas" VALUES ('Hackathon','Deficientes',0);
INSERT INTO "reservas" VALUES ('Hackathon','VIP',3);
INSERT INTO "reservas" VALUES ('Hackathon','Escolar',0);
INSERT INTO "reservas" VALUES ('Hackathon','Alunos',0);
INSERT INTO "areas" VALUES ('Carros',0,30,'Carro',0);
INSERT INTO "areas" VALUES ('Motos',0,20,'Motocicleta',0);
INSERT INTO "areas" VALUES ('Ônibus',0,20,'Onibus',0);
INSERT INTO "areas" VALUES ('Deficientes',0,5,'Carro',1);
INSERT INTO "areas" VALUES ('VIP',0,5,'Carro',1);
INSERT INTO "areas" VALUES ('Escolar',0,5,'Onibus',1);
INSERT INTO "areas" VALUES ('Alunos',0,5,'Carro',1);
INSERT INTO "veiculos" VALUES ('ABC1234','Honda','Vermelho','Arthur','Motocicleta');
INSERT INTO "veiculos" VALUES ('CBA4321','Kombi','Branco','Iria','Carro');
INSERT INTO "veiculos" VALUES ('XXX0000','Mercedes Benz','Branco','Roberto','Onibus');
INSERT INTO "veiculos" VALUES ('XUN1077','Ferrari','Vermelha','Junior','Carro');
INSERT INTO "veiculos" VALUES ('JUN107','Honda','Preta','Junior','Motocicleta');
INSERT INTO "veiculos" VALUES ('BUZ40','Mercedes Benz','Cinza','Junior','Onibus');
INSERT INTO "veiculos" VALUES ('HP93/4','Buzao','Vermelho','Arthur','Onibus');
INSERT INTO "proprietarios" VALUES ('Roberto','20192007002','Sistemas para Internet');
INSERT INTO "proprietarios" VALUES ('Larissa','20192007003','Sistemas para Internet');
INSERT INTO "proprietarios" VALUES ('Iria','20192007004','Sistemas para Internet');
INSERT INTO "proprietarios" VALUES ('Arthur','20192007000','Sistemas para Internet');
INSERT INTO "proprietarios" VALUES ('Junior','20192007004','Sistemas para Internet');
INSERT INTO "usuarios" VALUES (2,'Larissa','larissa@cauane.com','hunterhunter','RH');
INSERT INTO "usuarios" VALUES (3,'Iria','iria@guazzi.com','soju','Gestao');
INSERT INTO "usuarios" VALUES (4,'Roberto','robertompfm@gmail.com','beto','Estacionamento');
INSERT INTO "usuarios" VALUES (5,'Arthur','arthur@lacet.com','harry','RH');
COMMIT;
