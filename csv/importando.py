from pathlib import Path
import csv
caminho_csv = Path(__file__).parent / 'aulateste.csv'


# with open(caminho_csv, 'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     #next(leitor)
#     #print(next(leitor))
#     for linha in leitor:
#         print(linha)
        # print(linha[0])
        # print(linha[1])

#Ler em formato de dicionario
with open(caminho_csv, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        print(linha['Nome'], linha['Idade'])
        # print(linha['Nome'])
        # print(linha['Idade'])

        