# Dicionário para agrupar participantes por tema
eventos = {}
# Entrada do número de participantes
n = int(input().strip())


# loop para armazenas participantes e seus temas
for _ in range(n):
    linha = input().strip()

    # separa o nome e tema
    nome, tema = linha.split(", ")

    # se o tema ja existe adiciona no dict
    if tema in eventos:
        eventos[tema].append(nome)

    else:
        eventos[tema] = [nome]

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")