# DICIONÁRIOS ANINHADOS

contatos = {
    "pedro@gmail.com": {"nome": "Pedro", "telefone": "3333-1515"},
    "igor@gmail.com": {"nome": "igor", "telefone": "4444-1515"},
    "joao@gmail.com": {"nome": "joao", "telefone": "5555-1515"},
    "luis@gmail.com": {"nome": "luis", "telefone": "6666-1515"},
}

print(contatos["pedro@gmail.com"]["telefone"])

# como iterar o dicionario
"""
for chave in contatos:
    print(chave, contatos[chave])


# melhor opção
 
for chave, valor in contatos.items():
    print(chave, valor)
"""

# função para percorrer o dicionario citada acima
for chave, valor in contatos.items():
    print(chave, valor)