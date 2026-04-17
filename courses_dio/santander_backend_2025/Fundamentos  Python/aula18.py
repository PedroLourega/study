# Estruturas de repetição

#For - Quando se sabe o numero de repetições que você terá que fazer

texto = ""
VOGAIS = "AEIOU"

for letra in texto: 
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:

    print()
    print("Executa isso no final do laço")

