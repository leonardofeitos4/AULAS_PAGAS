#criar lista
lista = [20, 50, 10, 60, 41, 25]
#mudar numero da lista
lista[2] = 25
#apagar algo da lista
del lista [3]
#aumentar lista
lista.append(500)
#excluir o ultimo item da lista ou seleção lista.pop(3)
lista.pop()
#limpar lista
# list.clear
#acrescentar algo na lista seletivo
list.insert(1, 41)
print(lista[4])
print(lista)

lista_a = [1,5,2,1]
lista_b = [1,2,6,4]
#juntar as listas
listas = lista_a + lista_b
#método extend, extende a lista mas nao retorna valor

#for em listas
lista = ["Maria", "Joao", "pedro"]
for nome in lista:
    print(nome)