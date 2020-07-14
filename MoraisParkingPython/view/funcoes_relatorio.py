from model.relatorio import Relatorio



def gerar_relatorio():
    print("\n====== RELATORIO ======")
    print("Gerando relatorio...\n\n")
    arquivo = open('../relatorio.txt', 'w')
    arquivo.write(Relatorio.generate_relatorio_string())
    arquivo.close()

    arquivo = open('../relatorio.txt', 'r')
    print(arquivo.read())



