from dados import produtos
import copy

novos_produtos = [
    #Multipliando o valor de preco por 1.05
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    
    for produto in produtos 
   
]
print(f'Multiplicando por 10%:  \n {novos_produtos}')

# Ordene os produtos por nome decrescente (do maior para menor)

produtos_ordem_decrecente = sorted(
    novos_produtos,
      key= lambda produtos:produtos['preco'], reverse=True)

print(f'Do maior para o maior : \n {produtos_ordem_decrecente}')

# Gere produtos_ordenados_por_nome por cópia profunda (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos),
      key= lambda produtos:produtos['nome'], reverse=True)

print(f'Ordenando por nome: \n {produtos_ordenados_por_nome}')
# Ordene os produtos por preço crescente (do menor para maior)

produtos_menor_maior = sorted(copy.deepcopy(produtos),
                #Lambda, recebe o produto e retorna o produto ['preco']
     key= lambda produto:produto ['preco'])

for produto in produtos_menor_maior:
    print(f"Menor para o maior: {produto}")

# Gere produtos_ordenados_por_preco por cópia profunda (cópia profunda)

produtos_ordenados_por_preco = produtos_menor_maior.copy()

print(f'produtos ordenado por preço: \n {produtos_ordenados_por_preco}')