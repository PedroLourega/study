# FUNÇÕES
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a,b):
    return a * b

def dividir(a,b):
    return a // b

# EXIBIR RESULTADOS
def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


print("SOMA:")
exibir_resultado(10, 10, somar)
print("\n")
print("SUBTRAÇÃO:")
exibir_resultado(10, 10, subtrair)
print("\n")
print("MULTIPLICAÇÃO:")
exibir_resultado(10, 10, multiplicar)
print("\n")
print("DIVISÃO:")
exibir_resultado(10, 10, dividir)
print("\n")
