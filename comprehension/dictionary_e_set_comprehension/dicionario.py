produto = {

    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
}
print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('c', 'valor a'),
]
print(dict(lista))

'''SET ----->'''

si = {i for i in range(20)}
print(si)