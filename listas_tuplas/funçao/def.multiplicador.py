'''Crie  funções que duplicam, triplicam e quadruplicam
o numero recebido como parâmetro'''

'''
def duplicar(numero):
   return numero *2 

duplicar_2 = duplicar(4)

def triplicar (numero_3):
   return numero_3 *3

triplicar_3 = triplicar(4)

def quadruplicar (numero_4):
   return numero_4 *4

quadruplicar_4 = quadruplicar(4)

print(duplicar_2)
print(triplicar_3)
print(quadruplicar_4)'''

#criador de multplicador
def criador_multiplicar(multiplicador):
    #Como será a funçao mutiplicar
    def mulplicar(numero):
        #me retorna o numero * o multiplicador
        return numero * multiplicador
    #volta para o multplicador e me retorna ela multiplicada
    return mulplicar

#variavel para multplicar, duplicar ou triplicar..
duplicar = criador_multiplicar(2)
triplicar = criador_multiplicar(3)
quadruplicar = criador_multiplicar(4)

#print para multplicar o valor que eu quero
print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))