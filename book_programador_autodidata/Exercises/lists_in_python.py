#TRABALHANDO COM LISTAS
print("=============================================")
colors = ["blue", "green", "yellow"]
print("Cores inicio:", colors)
colors[1] = "deepblue"
print("Cores depois:", colors)
colorsdel = colors.pop()
print("Cor deletada:", colorsdel)
print("Novo print:", colors)


colors1 = ["black", "red"]
colors2 = ["white", "purple"]

colors3 = colors1 + colors2

print("Cores1:", colors1)
print("Cores2:", colors2)
print("Mistura de duas listas: ", colors3)


print("=============================================")
print("Está na antiga lista: ","blue" in colors)
print("Está na nova lista: ","blue" in colors3)

print("Não está na antiga lista: ","black" not in colors)
print("Não está na nova lista: ","black" not in colors3)

print("=============================================")
print("Números de itens em cada lista.")
print("Lista antiga:", len(colors))
print("Lista nova:", len(colors3))
print("=============================================")
print("===================xxx=======================")
print("=============================================")


#Uso na prática das listas:
cores = ["roxo", 
         "laranja",
         "verde"]

pergunta = input("Pergunte a cor: ")

if pergunta in cores:
    print("Você acertou uma das cores secretas!")
else:
    print("Cor errada, tente de novo!")

