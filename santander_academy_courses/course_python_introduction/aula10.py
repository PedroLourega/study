"""
# Conjuntos (set)

Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().

## Criação e operações básicas
Para criar um conjunto, utilize chaves ou a função set():
"""
# frutas = {"maça", "banana", "laranja"}
# numero = set([1, 2, 3, 4, 5])

# Os conjuntos suportam operações matemáticas de conjuntos, como a união (|),
#  a interseção (&),
#  a diferença (-)
#  e a diferença simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


uniao = conjunto1 | conjunto2
print(uniao)  # Imprime {1, 2, 3, 4, 5}


intersecao = conjunto1 & conjunto2
print(intersecao)  # Imprime {3}


diferenca = conjunto1 - conjunto2
print(diferenca)  # Imprime {1, 2}


diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)  # Imprime {1, 2, 4, 5}

"""
## Métodos de conjuntos

Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:


add(elemento): adiciona um elemento ao conjunto.

remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.

discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.

clear(): remove todos os elementos do conjunto.

Exemplo:
"""
frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()

#As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e manipular dados em nossos programas. As listas são úteis para coleções ordenadas e mutáveis, as tuplas para coleções ordenadas e imutáveis, os dicionários para armazenar pares de chave valor e os conjuntos para coleções não ordenadas de elementos únicos
