"""
Fatiamento de String
012345678
Olá mundo!
-987654321
Fatiamento [i:f:p] [::]
Obs: a função len retorna a qtd de caracteres da str
"""
variavel = "Olá mundo!"
print(variavel[4:])
print(variavel[7:])
print(variavel[4:7])
print(variavel[:4])
print(variavel[2:4])
print(variavel[0:9:1])
print(variavel[-1:-10:-1])
print(len(variavel[0:1]))
print(len(variavel[1:4:8]))
print(len(variavel))
print((variavel[-1::-1]))
