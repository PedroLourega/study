# ESCOPO GLOBAL
salario = 2000

def salario_bonus(bonus, lista):
    # É POSSIVEL ACESSAR UMA VARIAVEL DE FORA UTILIZANDO GLOBAL NA FRENTE
    global salario

    # as listas são imutaveis então é possivel acessa-las mesmo sem global
    #é utilizado uma pratica de copy de lista para nao comprometer a original
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)
print(lista)