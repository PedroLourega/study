"""
Interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""

nome = "Pedro"
preco = 1000.95897643
variavel = '%s, o preço é de R$' % nome
variavel2 = '%s, o preço é de R$%.2f' %(nome,preco)
print(variavel)
print(variavel2)
print('O Hexadecimal de %d é %08X'%(15,15))