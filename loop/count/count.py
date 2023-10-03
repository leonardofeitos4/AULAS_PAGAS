from itertools import count

#loop infinito, iniciando do 8
#tambem pode botar pra multiplicar em 8 em 8 (8,8)
c1 = count(8,8)
#range iniciando do 10 e acabando em 100 e botar para 9 em 9 (9,9,9)
r = range(10, 100)

#for para regrar o loop
for i in c1:
    if i > 100:
        break
    
    print(i)
#for em range
for i in r:
    print(i)