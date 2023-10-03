# filter é um filtro funcional
def  print_iter ( iterador ):
    print( * list( iterador ), sep = ' \n ' )
    print ()


produtos  = [
    { 'nome' : 'Produto 5' , 'preco' : 10.00 },
    { 'nome' : 'Produto 1' , 'preco' : 22.32 },
    { 'nome' : 'Produto 3' , 'preco' : 10.11 },
    { 'nome' : 'Produto 2' , 'preco' : 105.87 },
    { 'nome' : 'Produto 4' , 'preco' : 69.90 },
]

def filtrar(produto):
    return produto['preco'] > 100

#filtro para ver so os maiores que 10
# novos_produtos = [

#     p for p in produtos
#     if p['preco'] > 10
# ]

novos_produtos = filter(
    #pode fazer uma lambda em vez da função
    #lambda produto: produto['preco'] > 100,
    #pode criar a função filtrar
    filtrar,
    produtos
)


print_iter(produtos)
print_iter(novos_produtos)