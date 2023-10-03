# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


    #vai armazenar o x
def criar_funcao(funcao, x):
    #pedindo so o argumento y
    def interna(y):
        return funcao(x,y) 
    #me retorna só com o argumento y
    return(interna)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))

