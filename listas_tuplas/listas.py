salas = [
    #0             1
    ['Maria', 'Helena',],

    #0
    ['Elaine',], #1
    #0           #1       #2
    ['Luiz', 'João', 'Eduarda',(0,10,20,30,40)],#2
]
# print(salas[0][1])
# print(salas[1][0])
# print(salas[2][2])
# print(salas[2][3][4])

for sala in salas:
    print(f"A sala é: {sala}")
    for aluno in sala:
        print(aluno)

print(salas, sep=' ')