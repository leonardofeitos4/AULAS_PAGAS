# valor = input('Digite o numero a ser multiplicado: ')

'''def multiplicador(*args):
    total = 1 
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicador(1,2,3,4,5) 
print(multiplicacao)  '''     



def par_impar(x):
    if x % 2 == 0:
        return f'{x} é par'
    # else:
    return f'{x} é impar'

x = int(input("Digite o numero que queres saber se é impar ou par: "))

resultado = par_impar(x)

print(resultado) 








