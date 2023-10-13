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
