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