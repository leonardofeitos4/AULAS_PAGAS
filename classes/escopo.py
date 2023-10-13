class animal:
    def __init__(self, nome):
        self.nome = nome

    variavel = 'gato'
    print(variavel)

    def comendo(self, alimento):
        return f'O {self.nome} está comendo {alimento}'
    
    #def executar(self, *args, **kwargs):
     #   return self.comendo(*args, *kwargs)
    
cachorro = animal('Cachorro')
print(cachorro.nome)
print(cachorro.comendo('banana'))
