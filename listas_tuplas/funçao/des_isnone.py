def soma (a, b, c=None):
    if c is not None:
        print(f'{a=}, {b=},{c=}', a + b + c)
    else:
        print (f'{a=}, {b=}', a + b)
    
soma(1, 2)
soma(b = 3, c = 3, a = 54)
soma(1, 5, 4)