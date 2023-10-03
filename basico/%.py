"""
Interpolação básica de strings
s - string
dei - int
f - flutuar
xe X - Hexadecimal (ABCDEF0123456789)
"""
nome  =  'Luiz'
preço  =  1000.95897643
variavel  =  '%s, o preço é R$%.2f'  % ( nome , preço )
print( variavel )
print ( 'O hexadecimal de %d é %08X'  % ( 1500,1500 ) )

"""
Formatação básica de strings
s - string
d - int
f - flutuar
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Sinalizadores de conversão - !r !s !a
"""
variavell  =  'ABC'
print ( f' { variavel } ' )
print ( f' { variavel : >10 } ' )
print ( f' { variavel : <10 } .' )
print ( f' { variavel : ^10 } .' )
print ( f' { 1000.4873648123746 :0=+10,.1f } ' )
print ( f'O hexadecimal de 1500 é {1500 :08X} ' )
print ( f' {variavel !r} ' )