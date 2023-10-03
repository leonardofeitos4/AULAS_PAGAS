lista = [2 , 50, 23, 64, 88, 20]
lista.sort() #ou o inverso lista.sort(reverse=True)

#sorted(lista)

# print(lista)

lista = [

    {'Nome': 'Leonardo', 'Sobrenome': 'Feitosa'},
    {'Nome': 'Tuana', 'Sobrenome': 'Maria'},
    {'Nome': 'Pucas', 'Sobrenome': 'Feitosa'},
    {'Nome': 'Auciana', 'Sobrenome': 'Oliveira'},
    {'Nome': 'Francisco', 'Sobrenome': 'Barroso'}

]


def exibir(lista):
    for item in lista:
        print(item)
    print()

'''sort(key=ordenar) key sempre chama a funçao e sorte organiza em ordem alfabetica
                              ou 
Lambda é uma função ai coloco o item que quero que puxe ---> '''
l1 = sorted(lista, key=lambda item: item['Nome'])
l2 = sorted(lista, key=lambda item: item['Sobrenome'])
#print(lista)

exibir(l1)
exibir(l2)
