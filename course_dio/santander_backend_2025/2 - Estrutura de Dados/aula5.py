# DICIONÁRIOS EM PYTHON


# dicionários necessitam de declarções imutáveis

pessoa = {"nome": "Pedro", "idade": 22}

pessoa = dict(nome="Pedro", idade=22)

pessoa["telefone"] = "3333-4444"

print(pessoa)


dados = {"nome": "Pedro", "idade": 22, "telefone": "5555-6666"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

# para adicionar alguma declaração no dicionario(o valor é substituido pelo antigo)

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9999-1515"

print(dados)