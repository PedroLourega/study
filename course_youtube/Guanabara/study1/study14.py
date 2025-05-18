notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM:")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #alternativa: contador += 1
    contador = contador +1

    print("quantidade de notas", len(notas))