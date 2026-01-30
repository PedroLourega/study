frutas = ["laranja", "maca", "uva"]

fruta = []

letra = list("python") #Letras da palavra p y t h o n

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

print(frutas[0])
print(frutas[2])

numeros[-9]

#Lista aninhada

matriz = [
    [1,"a", 2],
    ["b",3 ,4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

#FATIAMENTE

lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])