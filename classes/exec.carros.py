# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

civic = Carro("O carro é: Civic,")     
fabricante_civic = Fabricante("O fabricante é da : Honda,")
motor_civc = Motor("O motor é: 1.5L Turbo 16V DOHC Duplo VTC")
# civic.fabricante = fabricante_civic
# civic.motor = motor_civc
print(civic.nome, fabricante_civic.nome, motor_civc.nome)

uno = Carro("O carro é: Uno,")     
fabricante_uno = Fabricante("O fabricante é da : Fiat,")
motor_uno = Motor("O motor é: Firefly 1.0 de três cilindros")
uno = fabricante_uno
uno.motor = motor_uno

print(uno.nome, fabricante_uno.nome, uno.motor.nome)