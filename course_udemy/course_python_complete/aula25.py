"""
Formatação básica de string

s - string
d - int
f - float
. <números de dígitos> f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = "ABC"
print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <15}")
print(f"{variavel:_>15}")
print(f"{variavel:.>15}")
print(f"{variavel:.^15}")
print(f"{1000.4857485674756:0=+10.1f}")
print(f"{variavel!r}")
print(f"{variavel!s}")
print(f"{variavel!a}")