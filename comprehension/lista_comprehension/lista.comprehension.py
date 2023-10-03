#For com o range --->
lista = []
for numero in range(10):
    lista.append(numero)
    
print(lista)

#Lista comprehension --->
lista = [
    #numero * 2 
    numero
    for numero in range(10)
]
print(lista)