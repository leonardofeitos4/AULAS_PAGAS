class carro():
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = carro('Fusca')
print(fusca.nome)
#Quando bota o print dentro da função, não precisa botar print..
fusca.acelerar() 

civic = carro('Civic')
print(civic.nome)
#Quando bota o print dentro da função, não precisa botar print..
civic.acelerar()


'''ATRIBUTOS --------->'''

# Atributos de classe
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('LEO', 19)
p2 = Pessoa('LIVIA', 18)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())