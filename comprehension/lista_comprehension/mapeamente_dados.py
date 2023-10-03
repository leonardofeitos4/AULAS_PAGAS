produtos= [ 

    {'nome':'p1', 'preço': 20, },
    {'nome':'p2', 'preço': 10, },
    {'nome':'p3', 'preço': 30, }

]

novos_produtos = [

    {'nome': produto['nome'], 'preço': produto['preço']}
    for produto in produtos 
]

#print(novos_produtos)
#print(*novos_produtos, sep='\n')

#ou pode fazer o mapeamento desse jeito --->

import pprint

def p(v):
    pprint.pprint(v,sort_dicts=False,width=40)

produtos= [ 

    {'nome':'p1', 'preco': 20, },
    {'nome':'p2', 'preco': 10, },
    {'nome':'p3', 'preco': 30, }

]

novos_produtos = [
    #Multipliando o valor de preco por 1.05
    {**produto, 'preco': produto['preco'] * 1.05}
    #If para aumentar so os valores acima de 20
    if produto['preco'] > 20 else {**produto}
    for produto in produtos 
]

#print(novos_produtos)
print(*novos_produtos, sep='\n')
p(novos_produtos)
