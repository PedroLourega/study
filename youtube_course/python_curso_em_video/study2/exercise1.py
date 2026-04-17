def soma_positivos(numeros):
    soma = 0
    for numero in numeros:
        if numero > 0:
            soma += numero
    return soma

numeros = [1, -2, 3, -4, 5]
print("Soma dos números positivos:", soma_positivos(numeros))
