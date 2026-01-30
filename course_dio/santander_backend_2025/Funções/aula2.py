
# Funcao que calcula o total de uma lista de números
def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 34]))
print(retornar_antecessor_e_sucessor(10))
print(func_3())