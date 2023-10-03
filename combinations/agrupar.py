from itertools import groupby

alunos  = [
    { 'nome' : 'Luiz' , 'nota' : 'A' },
    { 'nome' : 'Letícia' , 'nota' : 'B' },
    { 'nome' : 'Fabrício' , 'nota' : 'A' },
    { 'nome' : 'Alecrim' , 'nota' : 'C' },
    { 'nome' : 'Joana' , 'nota' : 'D' },
    { 'nome' : 'João' , 'nota' : 'A' },
    { 'nome' : 'Eduardo' , 'nota' : 'B' },
    { 'nome' : 'André' , 'nota' : 'A' },
    { 'nome' : 'Anderson' , 'nota' : 'C' },
]
#função para ordenar e chamar a chave
def ordena(aluno):
    return aluno['nota']
#juntar os alunos
alunos_agrupados = sorted(alunos, key= ordena)
#agrupar os alunos da mesma nota
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
