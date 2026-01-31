# Lista geral para os gêneros musicais
lists = []

print("Lista geral antes do acréscimo de gêneros:")
print(lists)

# Lista de rappers
rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"]

# Lista de rockeiros e bandas
rock = [ "Bob Dylan",
        "The Beatles",
        "Led Zeppelin"]

# Lista de djs
djs = ["Zeds dead",
       "Tiesto"]

# Adiciona a lista de rap à lista geral
lists.append(rap)

# Adiciona a lista de rock à lista geral
lists.append(rock)

# Adiciona a lista de djs à lista geral
lists.append(djs)


# Mostra a lista nova com as bandas inseridas
print("Lista geral após o acréscimo de gêneros:")
print(lists)

# Acrescenta um indice a lista
rap = lists[0]
rock = lists[1]
print(rap)

rap.append("Kendrick Lamar")
print("Com o acrescécimo de um novo valor:")
print(rap)
print(lists)
