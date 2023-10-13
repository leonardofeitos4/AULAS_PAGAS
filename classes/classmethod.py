# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.


class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def criar_20_anos(cls, nome):
        return cls(nome, 20)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

p1 = Pessoa.criar_20_anos('leonardo')
print(p1.nome, p1.idade)    
p2 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
p3 = Pessoa('leonardo', 19)
print(p3.nome, p3.idade)