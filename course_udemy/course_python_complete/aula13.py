nome = 'Pedro Henrique'
altura = 1.76
peso = 63
imc = peso / altura **2

#f-strings -> strings formatadas
linha_1 = f"{nome} tem altura de {altura:.2f} pesa {peso} quilos e seu IMC é: {imc:.2f}" #f{} em volta das variaveis
#podemos escolher quantas casas decimais queremos mostrar na tela também, com o comando :.2f ou mudando o numero de acordo com quantas casas(aqui aparecem 2 e depois nenhuma)
print(linha_1)

... #Ellipsis, pode ser utilizado para colocar em um campo onde você não sabe qual informação vai por, entre outras funções.