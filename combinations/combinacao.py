from itertools import combinations, permutations, product

def interar(iterator):
    print(list(iterator), sep='\n')
    print()

pessoas = [
    'leonardo', 'livia', 'lucas','luana'
]    

camisetas = [
    ['preta', 'azul'],
    ['p','m'],
    ['unissex', 'masculina', 'feminino']
]
#chama a importaçao e quantos grupos quero '2'
interar(combinations(pessoas,2))
#chama a importaçao e 2 combinações iguais
interar(permutations(pessoas,2))

interar(product(*camisetas))
