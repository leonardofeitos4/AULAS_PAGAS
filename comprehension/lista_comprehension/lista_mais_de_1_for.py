lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(lista)

#ou pode fazer assim, mas não é legal

lista = [
    [letra for letra in 'Luiz']
    for x in range(3)
]
print(lista)