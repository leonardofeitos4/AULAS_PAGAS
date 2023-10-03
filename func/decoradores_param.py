#Decoradores com parametros
def fabrica_de_decoradores(a=None, b=None, c=None):
    #decorador, pegar a função
    def fabrica_de_funcoes(func):
        print('Decoradora 1')
        #função interna que é a m inha
        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            #Chamando a função mae e botando os paramentos da interna
            res = func(*args, **kwargs)
            return res
        return aninhada
    #Resultado final
    return fabrica_de_funcoes

#Decoradora -->
@fabrica_de_decoradores(1,2,3)
def soma(x,y):
    return x+y


multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

#Crio a variavel e chamo a funçao e boto nos param

dez_mais_5 = soma(10,5)
dez_vezes_5 = multiplica(10,5)
#print
print(dez_mais_5)
print(dez_vezes_5)

