#repetições em python

#for - faz repetições definidas 
#while - segue repetindo enquanto der verdadeiro ou repetições definidas.

"""
notas = []

codigo_aluno = input("RM: ")
nota = float(input("Nota: "))
resultado = [codigo_aluno, nota]
notas.append(resultado)

"""

notas = []

#repetição (5) - numero de repetições
#a função range, cria uma repetição começando no 0 ou seja[0, 1, 2, 3, 4]
for x in range(5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)