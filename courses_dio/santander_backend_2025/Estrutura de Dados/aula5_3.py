# AINDA EM MÉTODOS DO DICIONÁRIO

# SETDEFAULT ( SE O ATRIBUTO NAO ESTIVER ELE ADICIONA, SE JA ESTIVER OCUPADO MANTÉM OS ITENS)

contato = {
    "pedro@gmail.com":{"nome": "Pedro", "telefone": "9999-8888"}
    }

contato.setdefault("nome", "Julia") # não adicionada nada pois já possui valor
print(contato)

contato.setdefault("idade", 22) # adiciona a idade
print(contato)

print("           ")
print("           ")

# UPDATE (DEIXA ATUALIZAR O VALOR)
print("ANTES DO UPDATE")
print(contato)

print("            ")
print("            ")

print('DEPOIS DO UPDATE')
contato.update({"pedro@gmail.com": {"nome": "Pedro Henrique"}})
print(contato)

contato.update({"julia@gmail.com": {"nome": "julia", "telefone": "3323-9987"}})
print(contato)

print("           ")
print("           ")

# VALUES (RETORNA TODOS OS VALORES)

print(contato.values())

print("           ")
print("           ")

# IN (PARA VERIFICAR SE ALGO ESTA PRESENTE) retorna um valor bool

resultado = "pedro@gmail.com" in contato
print(resultado)

resultado = "julia" in contato["pedro@gmail.com"]
print(resultado)

resultado = "9999-8888" in contato["pedro@gmail.com"]
print(resultado)


print("           ")
print("           ")

# DEL (SERVE PARA REMOVER ALGO EM ESPECIFICO)

del contato

print("novo dict")
contato = {
    "pedro12312312@gmail.com":{"nome": "Pedro", "telefone": "9999-8888"}
    }

print(contato)