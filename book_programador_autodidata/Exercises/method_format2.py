# Mais um exemplo do método format, agora aplicado para substituir dados de autor e data de falecimento.
author = "William Faulkner"
year_born = "1897"

print("{} was born in {}.".format(author, year_born))

# Exercicio feito por mim para praticar alguns conceitos aprendidos neste capitulo, tentei realizar um código que 
# perguntasse ao usuário nome e curso para fazer uma frase semipronta no final.
nome = input("Digite seu nome:")
curso = input("Digite agora o curso em que você está inscrito:")

text = "Seja muito bem vindo {}!\n" \
"Você agora está inscrito no curso de: {}\n" \
"Desejamos ótimos estudos!!".format(nome, curso)

print(text)