#def como será tudo para depois ser gerado meu print
def saudacao(saudacao):
    #def de como será meu print
    def saudar(nome):
        #2 argumentos para meu print
        return f'{saudacao}, {nome}!'
    return saudar

#bom dia ou boa noite
falar_bom_dia = saudacao('Bom dia')
falar_boa_noite = saudacao('Boa noite' )

#faz o for para quantas pessoas eu quiser
for nome in ['leonardo', 'Lucas', 'Luana']:
    print(falar_boa_noite(nome))