lista = [n for n in range(10) if n < 4]
#print(lista)

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
    #If depois do for é filtro
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
]
   

#print(novos_produtos)
#print(*novos_produtos, sep='\n')
p(novos_produtos)


