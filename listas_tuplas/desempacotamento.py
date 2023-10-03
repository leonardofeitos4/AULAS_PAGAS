# nome1, *resto = ["Maria",'Joao','Luiz']
# print(nome1, resto)

# _, nome, *_= ["Maria",'Joao','Luiz']
# print(nome)


string = 'ABCD'
lista= ['Maria', 'Helena', 'Eduarda']
tupla = 'python', 'leo', 'livia'

# a,b,c = lista
# print(a,c)
#posso fazer assim:
# for nome in lista:
#     print(nome, end= ' ' )
print(*lista)
print(*string)
#desempacotamento :
#print(salas, sep=' ')

