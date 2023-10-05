import json

pessoa = {
    'nome': 'Leonardo ',
    'sobrenome': 'Feitosa',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.75,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        #para botar os acentos certinho
        ensure_ascii=False,
        #deixar o dicionario formatado
        indent=2,
    )

with open('aula.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])