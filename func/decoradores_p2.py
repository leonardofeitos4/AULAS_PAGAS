def decoradora(func):
    print('decoradora 1')
    
    #função interna 
    def aninhada(*args, **kwargs):
        print('aninhada')
        #Chamando a função mae e botando os paramentos da interna
        res = func(*args, **kwargs)
        return res
    #Resultado final
    return aninhada

#Decoradora -->
@decoradora
def soma(x,y):
    return x+y


#Crio a variavel e chamo a funçao e boto nos param
dez_mais_5 = soma(10,5)
#print
print(dez_mais_5)