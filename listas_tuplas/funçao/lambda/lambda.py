#Cria a função
def executa(funçao, *args):
    return funçao(*args)

#Cria a variavel e chama a função
duplica = executa(
    #chama a função lambda e os atributos
       lambda m: lambda n: n * m,
    #Coloca por quanto vai ser multiplicado e da o print
    2
)
print(duplica(3))

soma = executa(
    lambda x: lambda y: x + y,
    3
)
print(soma(4))

arg = print(

    executa(
        lambda *args: sum(args),
        1,2,3,5,6,7
)

)