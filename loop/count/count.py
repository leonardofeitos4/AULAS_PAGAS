from itertools import count

#loop infinito, iniciando do 10
c1 = count(10)
#range iniciando do 10 e acabando em 100
r = range(10, 100)

#for para regrar o loop
for i in c1:
    if i > 100:
        break
    
    print(i)
#for em range
for i in r:
    print(i)