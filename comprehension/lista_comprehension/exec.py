import copy
# copiar, classificar, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por cópia profunda (cópia profunda)
produtos  = [
    { 'nome' : 'Produto 5' , 'preco' : 10.00 },
    { 'nome' : 'Produto 1' , 'preco' : 22.32 },
    { 'nome' : 'Produto 3' , 'preco' : 10.11 },
    { 'nome' : 'Produto 2' , 'preco' : 105.87 },
    { 'nome' : 'Produto 4' , 'preco' : 69.90 },
]

novos_produtos = [
    #Multipliando o valor de preco por 1.05
    {**produto, 'preco': produto['preco'] * 1.10}
    
    for produto in produtos 
   
]
print(f'Multiplicando por 10%:  \n {novos_produtos}')

# Ordene os produtos por nome decrescente (do maior para menor)

produtos_ordem_decrecente = sorted(novos_produtos, key= lambda x:x['preco'], reverse=True)

print(f'Do maior para o maior : \n {produtos_ordem_decrecente}')

# Gere produtos_ordenados_por_nome por cópia profunda (cópia profunda)

produtos_ordenados_por_nome = copy.deepcopy(produtos)

print(f'Ordenando por nome: \n {produtos_ordenados_por_nome}')
# Ordene os produtos por preço crescente (do menor para maior)

produtos_menor_maior = sorted(produtos, key= lambda x:x ['preco'], reverse=True)

for produto in produtos_menor_maior:
    print(f"Menor para o maior: {produto}")

# Gere produtos_ordenados_por_preco por cópia profunda (cópia profunda)

produtos_ordenados_por_preco = produtos_menor_maior.copy()

print(f'produtos ordenado por preço: \n {produtos_ordenados_por_preco}')
