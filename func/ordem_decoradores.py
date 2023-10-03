def paramentros_decorador(nome):
    def decorador(func):
        print('decorador: ',nome)

        def nova_funcao(*args, **kwargs):
            res = func(*args,**kwargs)
            fin = f'{res}, {nome}'
            return fin
        return nova_funcao
    return decorador

@paramentros_decorador(nome='5')
@paramentros_decorador(nome='4')
@paramentros_decorador(nome='3')
def soma(x,y):
    return x +y


tres_mais_tres = soma(3,3)
print(tres_mais_tres)
