# Lista para armazenar os produtos e preços
carrinho = [] # lista para armazenar os itens
total = 0.0 # variavel para somar os valores
# entrada do número de itens
n = int(input().strip()) # converte o valor digitado para inteiro e ja remove os espaços extras do inicio/fim
# loop para adicionar itens ao carrinho
for _ in range(n): # _ não usar variavel só queremos repetir n vezes
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ") #encontra os espaços com rfind() para separar do preço
    
    # Separa os nomes dos produtos e o preço
    item = linha[:posicao_espaco] # pega as posições exata e fatia o item do preço
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco)) # adiciona o item formatado na lista
    total += preco # adiciona o valor ao total

for item, preco in carrinho: # exibe os resultados
    print(f"{item}: R${preco:.2f}")

print(f"Total: R${total:.2f}")