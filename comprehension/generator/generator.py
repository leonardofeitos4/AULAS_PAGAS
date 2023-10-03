iterable = ['eu', 'lucas', 'luana']
iterator = iter(iterable)    

'''for item in range(iterator):
    #print(item)'''


def generator(n=0):
    yield 1 #pausar
    print ('Continuando..')
    yield 2
    print('Mais uma...')
    yield 3
    print('AGORA É SERIO, ACABOU!')
    return 'Acabou!!!!!!'

gen = generator(n=0) 
#for n in gen:
    #print(n)


'''Loop infinito'''

def generator(n=0, maximum = 25):
    while True:
        yield n
        n+=1

        if n > maximum:
            return


gen = generator() 
for n in gen:
    print(n)