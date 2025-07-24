# Compreensão de listas:

numeros = [1, 30, 21, 2, 9 , 65, 34]
"""
VERSÃO SIMPLIFICADA

pares = [numero for numero in numeros if numero % 2 == 0]
"""
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

"""
ADICIONANDO NUMEROS AO QUADRADO NA LISTA:

numeros = [1, 30, 21, 2, 9 , 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
"""


