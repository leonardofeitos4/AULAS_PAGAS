from modulo import soma
def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y


#quando importar com '*' so vai chamar o modulo DIVISAO
#__all__ = [
#    'divisao'
# ]

def fala_oi():
    print('oi')

from modulos_packege.modulo2 import *

print(soma(1,8))


