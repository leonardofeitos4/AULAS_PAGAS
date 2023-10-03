#Unir as duas listas

from itertools import  zip_longest

#lista
lista_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_2 = ['BA', 'SP', 'MG', 'RJ']


#função para zipar as duas listas
def zipar(lista_1, lista_2):
   lista = list(zip_longest(lista_1,lista_2))
#  return lista

    
print(list(zip_longest(lista_1,lista_2, fillvalue='NDA')))