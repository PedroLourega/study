num = input("Digite um número: ")


def conversor(t):
    try:
        resultado = float(t)
        return resultado
    except:
        print("Digite um número válido!")

resultado_final = conversor(num)
print(resultado_final)


if type(resultado_final) == float:
    print("Você digitou o numero certo!")

elif type(num) == str:
    print("Você digitou uma string, digite algo válido")
else:
    print("Seu numero não está correto, tente de novo :/ ")

