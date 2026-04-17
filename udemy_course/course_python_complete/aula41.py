nome = input("Digite seu nome:")

contador = 0
resultado = ""

while contador < len(nome):
    letra = nome[contador]
    resultado += "*" + letra
    contador += 1

resultado += "*"
print(resultado)