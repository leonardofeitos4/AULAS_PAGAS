# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))  

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)      
   
    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    

    def __del__(self):
        print('APAGANDO,', self.nome)   
        

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('LEONARDO')
cliente1.inserir_endereco('Rua jaime gomes', 291)
cliente1.inserir_endereco('Rua jaime Gomes', 272)
endereco_externo = Endereco('Rua jaime', 272)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.lista_endereco()

