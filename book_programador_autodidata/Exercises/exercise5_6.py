"""
As listas, as tuplas e os dicionários são apenas alguns dos contêiners internos do Python. Faça uma pesquisa sobre os conjuntos
(Um tipo de contêiner) do Python. Quando você usaria um conjunto?
"""

#Resposta:
"""
Conjuntos são uma coleção de itens não ordenados que nao se repetem e sao imutaveis
"""

planeta_anao = {"Plutão",
                "Ceres",
                "Eris",
                "Haumea",
                "Makemake"}

qtde_planetas = len(planeta_anao)

print("Lista de planetas",planeta_anao)
print("Qantidade de planetas:",qtde_planetas)

print("Eris está no planeta?")
print("Eris" not in planeta_anao)

print("=================")

for astro in planeta_anao:
    print(astro.upper())


# As litas se repetem os itens
astros = ["Lua", "Vênus", "Sirius", "Marte", "Lua", "Jupiter"]
print("Lista:", astros)

# Os conjuntos nao se repetem
astrosSet = set(astros)
print("Conjunto:", astrosSet)
