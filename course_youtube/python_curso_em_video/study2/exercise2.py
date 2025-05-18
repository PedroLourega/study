produto = {
    "nome": "Teclado Mecânico",
    "preco": 250.0,
    "quantidade_em_estoque": 15
}

def exibir_informacoes_produto(produto):
    print(f"Produto: {produto['nome']}")
    print(f"Preço: {produto['preco']}")
    print(f"Quantidade em Estoque: {produto['quantidade_em_estoque']} unidades")

exibir_informacoes_produto(produto)