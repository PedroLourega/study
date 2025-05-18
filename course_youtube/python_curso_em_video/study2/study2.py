#Loop for com dicionário

produtos = {
    "Maça": 2.5,
    "Banana": 1.8,
    "Laranja": 3.0
}

for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")