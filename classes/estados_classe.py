'''Mantendo estados dentro da classe'''


class camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já esta filmando..')
            return
        
        print (f'{self.nome} está filmando')
        self.filmando = True

    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} Não Está filmando')
            return

        print(f'{self.nome} Está parando de filmar') 
        self.filmando = False  

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} Não pode fotografar filmando')
            return
        
        print(f'{self.nome} Agora pode fotografar')
        
sony = camera('sony')

sony.filmar()
sony.filmar()
sony.fotografar()
sony.parar_de_filmar()
sony.fotografar()