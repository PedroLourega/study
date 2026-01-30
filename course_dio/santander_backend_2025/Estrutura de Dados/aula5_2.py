# MÉTODOS DOS DICIONÁRIOS

contatos = {
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-1515"},
    "igor@gmail.com": {"nome": "igor", "telefone": "4444-1515"},
    "joao@gmail.com": {"nome": "joao", "telefone": "5555-1515"},
    "luis@gmail.com": {"nome": "luis", "telefone": "6666-1515"},
}


# MÉTODO CLEAR(LIMPA O DICT)
print("                   ")
print("                   ")
print(contatos)
contatos.clear()
print("                   ")
print("                   ")
print("Nova lista abaixo:")
print(contatos)

contatos = {
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-1515"},
    "igor@gmail.com": {"nome": "igor", "telefone": "4444-1515"},
    "joao@gmail.com": {"nome": "joao", "telefone": "5555-1515"},
    "luis@gmail.com": {"nome": "luis", "telefone": "6666-1515"},
}


# MÉTODO COPY FAZ UMA COPIA DO DICT
print("                   ")
print("                   ")
copia = contatos.copy()
print("A copia abaixo:")
print(copia)


# FROMKEYS( CRIA CHAVES PARA VOCÊ)

dict.fromkeys(["nome","telefone"])

dict.fromkeys(["nome","telefone"],"vazio")

# GET (UMA FORMA DISTINTA DE ACESSAR VALORES DO DICT)
print("                   ")
print("                   ")
contatos2 = {
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "5555-6666"}
}

print(contatos2.get("chave")) #não encontra pois não possui, mas isso nao gera erro
print(contatos2.get("chave", {})) #se ele não encontrar ele mostra a chave
print(contatos2.get("pedro@gmail.com",{})) # aqui ele encontra

# ITEMS (RETORNA UMA LISTA DE TUPLAS)
print("                   ")
print("                   ")
print("FUNÇÃO ITEMS:")
print(contatos.items())

# KEYS (RETORNA SÓ AS CHAVES DO DICT, UTIL QUANDO VOCE SO QUER SABER AS CHAVES DISPONIVEIS)
print("                   ")
print("                   ")
print("MOSTRA ABAIXO A FUNÇÃO KEYS")
print(contatos.keys())

# POP (REMOVE UMA CHAVE DO SEU DICT)

contatos3 = {
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "5555-6666"},
    "pedro2@gmail.com": {"nome": "Pedro2", "telefone": "5255-6666"},
}

popop = contatos3.pop("pedro2", "não encontrei") # a segunda chave, serve para reduzir o erro, você pode até digitar uma mensagem caso não haja a chave digitada

print("                        ")
print("                        ")
print("MOSTRA O A FUNÇÃO POP")
print(popop)

# POPITEM (a diferença é que não informamos a chave e ele tira os itens em sequencia, assim que nao tiver mais valor gera erro)
print("                        ")
print("                        ")
print("antes da função pop item")
print(contatos3)

print("                        ")
print("                        ")
print("MOSTRA O A FUNÇÃO POPITEM")

contatos3.popitem()
print(contatos3)
