from pathlib import Path
import csv

caminho_csv = Path(__file__).parent / 'aula180.csv'

lista_clientes = [
    {'Nome': 'Leonardo', 'Endereco': 'Rua Jaime, 291'},
    {'Nome': 'Livia', 'Endereco': 'Rua Jaime, 272'},
    {'Nome': 'Lucas', 'Endereco': 'Rua jaime, 202'}
]
with open (caminho_csv, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)

    for cliente in lista_clientes:
        escritor.writerow(cliente.values())

# lista_clientes = [
#     {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
#     {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
#     {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.DictWriter(
#         arquivo,
#         mandar as colunas
#           fieldnames=nome_colunas
#     )
#   fazer o cabeçalho  
    # escritor.writeheader()

    #Mandar o dicionario para o arquivo CSV
#     for cliente in lista_clientes:
#         print(cliente)
#         escritor.writerow(cliente)


# lista_clientes = [
#     ['Luiz Otávio', 'Av 1, 22'],
#     ['João Silva', 'R. 2, "1"'],
#     ['Maria Sol', 'Av B, 3A'],
# ]
# with open(CAMINHO_CSV, 'w') as arquivo:
#     # nome_colunas = lista_clientes[0].keys()
#     nome_colunas = ['Nome', 'Endereço']
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente)        