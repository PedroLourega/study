#CONJUNTOS EM PYTHON

"""
Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjunstos matemáticos ou eliminar itens duplicados de um iterável.

NÃO CONFIAR NAS ORDENS DO SET

"""

print(set([1, 2, 3, 1, 3, 4]))

print(set("abacaxi"))

print(set(("palio", "gol","celta", "palio" )))

linguagens ={"python", "java", "python"}
print(linguagens)

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])


# caso queira saber os itens que estão no conjunto
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# caso queira saber o indice daquele elemento

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")




# UNIÃO

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

print(conjunto_a.union(conjunto_b))


# DIFERENÇA

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))


# SIMETRICA

print(conjunto_a.symmetric_difference(conjunto_b))

# issubset booleano (quando se tocam postivo)

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

#isdisjoint

conjunto_a1 = {1, 2, 3, 4, 5}
conjunto_b1 = {6, 7, 8, 9}
conjunto_c1 = {1, 0}

print(conjunto_a1.isdisjoint(conjunto_b1))
print(conjunto_a1.isdisjoint(conjunto_c1))


# add (se o elemento não existir, ele é adicionado)

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)


# clear (limpa a set)
sorteio.clear()

print(sorteio)

# copy (faz uma copia da set)

sorteio = {1, 23}

sorteio2 = sorteio.copy()

print(sorteio2)

# discard (serve para descartar um valor)(se descartar um valor que existe ele é excluido, caso o valor não esteja presente não de erro, é apenas ignorado)

numeros1 = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros1)

numeros1.discard(1)
numeros1.discard(45)

print(numeros1)


# pop (tira o primeiro valor da lista por padrão, a não ser que coloque o indice)

print(numeros1.pop())

#remove autoexplicativo, exclui um valor

print(numeros1.remove(9))

# in serve para ver o tamanho

numeros2 = {1,2,3, 1, 2, 4, 5,5,6,7,8,9,0}
print(1 in numeros2)
print(10 in numeros2)

