# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIU  o arquivo')
    #8/0

except ZeroDivisionError:
    print('Dividiu por zero mano')

else:
    print('Não Deu erro')    

finally:
    print('Fechou papai')        