"""
# ESTRUTURAS DE DADOS

As estruturas de dados nos permitem organizar e armazenar dados de maneira eficiente em nossos programas. Python fornece várias estruturas de dados integradas, como listas, tuplas, dicionários e conjuntos, cada uma com suas próprias características e usos.


## Listas

Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma lista podem ser de diferentes tipos de dados e são encerrados entre colchetes [], separados por vírgulas.

 # Criação e Acesso 

 Para criar uma lista, simplesmente encerre os elementos entre colchetes:

frutas = ["maçã", "banana", "laranja"]
Para acessar os elementos de uma lista, utilize o índice do elemento entre colchetes. Os índices começam a partir de 0.

print(frutas[0])  # Imprime "maçã"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "laranja"

Você também pode acessar os elementos a partir do final da lista utilizando índices negativos. O índice -1 representa o último elemento, -2 representa o penúltimo, e assim por diante.

print(frutas[-1])  # Imprime "laranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "maçã"

"""

"""
## Métodos de listas

As listas em Python têm vários métodos incorporados que nos permitem manipular e modificar os elementos da lista. Alguns métodos comuns são:

append(elemento): adiciona um elemento ao final da lista.
insert(indice, elemento): insere um elemento em uma posição específica da lista.
remove(elemento): remove a primeira ocorrência de um elemento na lista.
pop(indice): remove e retorna o elemento em uma posição específica da lista.
sort(): ordena os elementos da lista em ordem ascendente.
reverse(): inverte a ordem dos elementos na lista.
Exemplo:

"""
frutas = ["maçã", "banana", "laranja"]

frutas.append("pera")
print(frutas)  # Imprime ["maçã", "banana", "laranja", "pera"]

frutas.insert(1, "uva")
print(frutas)  # Imprime ["maçã", "uva", "banana", "laranja", "pera"]

frutas.remove("banana")
print(frutas)  # Imprime ["maçã", "uva", "laranja", "pera"]

fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ["maçã", "uva", "pera"]
print(fruta_removida)  # Imprime "laranja"

frutas.sort()
print(frutas)  # Imprime ["maçã", "pera", "uva"]

frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "maçã"]

"""
### Listas de compreensão
As listas de compreensão são uma forma concisa de criar novas listas baseadas em uma sequência existente. Permitem filtrar e transformar os elementos de uma lista em uma única linha de código.

nova_lista = [expressão for elemento in sequência if condição]

Neste exemplo, é criada uma nova lista chamada quadrados, que contém os quadrados dos números pares da lista números. A expressão x ** 2 eleva cada elemento ao quadrado, e a condição if x % 2 == 0 filtra apenas os números pares.

Exemplo:
"""
numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 
             for x in numeros 
             if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]