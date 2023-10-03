string = 'Leonardo'
metodo = 'strip'

if hasattr(string,metodo):
    print('Existe um Upper')
    print(getattr(string, metodo)())
else:
    print('Não Existe', metodo)

