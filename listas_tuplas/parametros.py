# Problema dos parâmetros mutáveis em funções Python
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('leonardo')
adiciona_clientes('joao', cliente1)
adiciona_clientes('pedro', cliente1)
cliente1.append('lucas')

cliente2 = adiciona_clientes('livia')
adiciona_clientes('luana', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('leo', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)