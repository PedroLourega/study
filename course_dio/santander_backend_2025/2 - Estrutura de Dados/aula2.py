#Métodos utilizados em listas python:

#ADICIONA ITENS NA LISTA
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

l2 = lista.copy()

print(lista)
print("ULTIMA MENSAGEM DA LISTA ANTES DO CLEAR")

#LIMPA A LISTA
lista.clear()

print(lista)

#COPIA A LISTA
"""
[nome da lista].copy
"""

print(l2)

#CONTAGEM DE ITENS

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# EXTENSAO DE LISTA

linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)


# PESQUISA DE ITENS NA LISTA, E MOSTRA A PRIMEIRA POSIÇÃO

print(linguagens.index("python"))


# REMOVE ELEMENTOS DA LISTA (POR PADRÃO TIRA O ULTIMO, MAS VOCÊ PODE DEFINIR)

linguagens.pop()
linguagens.pop(2)
print(linguagens)

# REMOVE SEM USAR O INDICE

linguagens.remove("java")
print(linguagens)

# COLOCA A LISTA AO CONTRÁRIO

linguagens.reverse()
print(linguagens)

# ORGANIZA A ORDEM DA LISTA (PADRÃO: ORDEM ALFABETICA)
linguagens2 = ["python", "js", "c"]
linguagens2.extend(["java", "csharp"])
linguagens2.sort()
print(linguagens2)

linguagens2.sort(reverse=True)
print(linguagens2)

linguagens2.sort(key=lambda x: len(x))
print(linguagens2)

linguagens2.sort(key=lambda x: len(x), reverse=True)
print(linguagens2)

# VERIFICA O TAMANHO

print(len(linguagens2))

#FUNÇÃO SORTED, PARECIDA COM SORT

print(sorted(linguagens2, key=lambda x:len(x)))
print(sorted(linguagens2, key=lambda x:len(x), reverse=True))
