frase = 'O Python é uma  ' \
    'linguagem de programação'\
    'multiparadigma.' \
    'Python foi criado por Guido van Rossum.'

i = 0 

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    print("A letra:", letra_atual,"[apareceu:", quantas_vezes_letra_apareceu, "vezes]")
    i += 1