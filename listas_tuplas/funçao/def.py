def imprimir(nome = 'sem nome'):
    print(f'Olá {nome}!')

imprimir("Leonardo")
imprimir("Livia")
imprimir()

'''return de uma função --->'''

def soma(x,y):
    if x > 10:
        return (10,5)
    return(x+y)

soma1 = soma(2, 2)
soma2 = soma(3, 3)
print(soma1)
print(soma2)
print(soma(55,50))

     