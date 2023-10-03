"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0

while contador <= 10:
    contador = contador + 5
    print(contador)

print('Acabou')

"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
# contador  =  10

# ##

# contador  /=  5
# print(contador)
linhas = 2
colunas = 2
 
linha = 1
while linha <= linhas:
    coluna = 1
    while coluna <= colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1