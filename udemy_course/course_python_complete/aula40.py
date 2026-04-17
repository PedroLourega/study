qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}') #Colocando o sinal de = ao lado, mostramos o nome da variavel + seu valor
        coluna += 1
    linha += 1

print("Acabou")