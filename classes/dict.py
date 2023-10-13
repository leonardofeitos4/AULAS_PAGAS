# __dict__ e vars para atributos de instância
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {'nome': 'leo', 'idade': 19}
p1 = Pessoa(**dados)
# p1.nome = 'KKK'
# print(p1.idade)
#dict troca a chave por outra que eu quero ---->    
# p1.__dict__['outra'] = 'coisa'
# p1.__dict__['nome'] = 'KKK'
# del p1.__dict__['nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)
print(vars(p1))
print(p1.nome)