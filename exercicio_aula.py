# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'exercicio_classes.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('leo', 19)
p2 = Pessoa('livia', 20)
p3= Pessoa('lucas', 18)
dc = [p1.__dict__, p2.__dict__ ,p3.__dict__]

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        print('FAZENDO DUMP')
        json.dump(dc,arquivo, ensure_ascii= False, indent=2)