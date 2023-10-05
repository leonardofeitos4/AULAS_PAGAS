
caminho = 'caminho.txt'
caminho_arquivo = 'D:\\py\\AULAS_PAGAS\\caminho\\'
caminho_arquivo += 'caminho.txt'

print(caminho_arquivo)

# arquivo = open(caminho_arquivo, 'w')
# #fechar manualmente
# arquivo.close()


#with ele ja abre e fecha

#otav.miranda site dele

caminho_arquivo = 'caminho.txt'
#w apaga tudo e bota o que eu peço
#A ele acrescenta com o que ja está lá
with open(caminho_arquivo, 'w+',encoding='utf8') as arquivo:
    arquivo.write('LEONARDOOOO FEITOSAAAA\n')
    arquivo.write('LEONARDOOOO FEITOSAAão\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    #strip remove os espaços do começo e do fim
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())
