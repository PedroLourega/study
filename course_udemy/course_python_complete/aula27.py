"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome_invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""

nome =input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
nome_invertido = nome[-1::-1]
tem_espaco = " " in nome

if nome and idade:
    print(f"Seu nome é {nome}, é realmente muito bonito!")
    print(f"Seu nome invertido é: {nome_invertido}")
    print(f"Seu nome contém espaços: {tem_espaco}")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é: {nome[-1]}")

else:
    print("Desculpe, você deixou campos vazios.")


