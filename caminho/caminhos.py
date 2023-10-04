
caminho = 'caminho.txt'
caminho_arquivo = 'D:\\py\\AULAS_PAGAS\\caminho\\'
caminho_arquivo += 'caminho.txt'

print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'w')
# #fechar manualmente
# arquivo.close()


#with ele ja abre e fecha
with open(caminho_arquivo, 'w') as arquivo:
    print('oi')

caminho_arquivo = 'aula116.txt'


