def conversor(x):
    try:
        x = float(x)
        print(x)
        return x
    except ValueError:
        print("Erro: valor inválido. Digite um número válido.")
        return None


num = input("Digite um número: ")
conversor(num)