s1 = {2,3,4}
s2 = {1,3,4}
s3 = {2,3,5}



# Operadores úteis:

# diferença - Itens presentes apenas no conjunto da esquerda
s3 = s1 - s2
#união | união (união) - Une
s3 = s1 | s2 
# intersecção & (interseção) - Itens presentes em ambos
s3 = s1 & s2 
# diferença simétrica ^ - Itens que não estão em ambos
s3 = s1 ^ s2 

print(s3)