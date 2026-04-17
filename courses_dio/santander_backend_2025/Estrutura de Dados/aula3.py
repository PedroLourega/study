# COMPREENSÃO DE TUPLAS
#diferente das listas, as tuplas são imutáveis

"""
A TUPLA PODE SER FEITA TANTO ATRAVÉS DA CLASSE tuple

COMO TAMBÉM PODE SER FEITA COLOCANDO OS VALORES SEPARADOS POR VIRGULA
"""


"""
A VIRGULA NO FINAL É UMA FORMA DE IDENTIFICAR AS TUPLAS, É UM PADRÃO ENTRE DEVS DE IDENTIFICAÇÃO
"""

frutas = ("maça","laranja", "pera", "uva",)

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

print(frutas)
print(letras)
print(numeros)
print(pais)

print(frutas[0])
print(frutas[3])

# TUPLAS ANINHADAS

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[-1])
print(matriz[-1][-1])


# FATIAMENTO

tupla = ("p", "y", "t", "h", "o", "n")

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

# CONTAGEM PARA DESCOBRIR QUANTOS ELEMENTOS TEM 

print(frutas.count("pera"))

# PARA SABER QUAL A POSIÇÃO

print(frutas.index("uva"))

# PARA SABER QUANTOS ELEMENTOS POSSUI

print("Quantos elementos possui frutas? R:", len(frutas))