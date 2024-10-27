#1 - Adicionando e Removendo Itens: / Adding and Removing Items:
#Para adicionar um item, podemos usar append() ou insert().
#To add an item, we can use append() or insert().

#extend([lista]): Junta outra lista à atual.
#extend([list]): Adds another list to the current one.


#Para remover, temos remove(), pop(), e del.
#To remove, we have remove(), pop(), and del.
#clear(): Esvazia a lista.
#clear(): Empty the list.


#2 - Ordenando e Revertendo Listas: / Sorting and Reversing Lists:
#sort() ordena em ordem crescente, e reverse() inverte a lista.
#sort() sorts in ascending order, and reverse() reverses the list.

#sorted(lista, reverse=True) pode ser usado para uma ordenação decrescente temporária.
#sorted(list, reverse=True) can be used for a temporary descending sort.

#3 - Fatiamento: / Slicing:
#lista[início:fim:passo] permite pegar sublistas.
#list[start:end:step] allows you to get sublists.
#lista[:n]: Pega os primeiros n elementos.
#list[:no]: Get the first n elements.

#4 - Buscar e Contar Elementos: / Search and Count Elements:
#index(item): Retorna o índice do item (primeira ocorrência).
#count(item): Retorna o número de vezes que o item aparece na lista.
#index(item): Returns the index of the item (first occurrence).
#count(item): Returns the number of times the item appears in the list.


jogos = ["Minecraft", "Overwatch", "Undertale", "League of Legends"]
#criamos uma lista que armazena jogos. 
#we create a list that stores games.

jogos.append("Valorant")
#adiciona Valorant na lista jogos no final
#add Valorant to the games list at the end

jogos.insert(2, "The Sims") 
#adiciona The sims na lista, em uma posição específica. 
#adds The Sims to the list, in a specific position.

jogos.remove("Minecraft")
#remove por valor, que seria string "Minecraft".
#remove by value, which would be string "Minecraft".
ultimo_jogo = jogos.pop() 
#remove o ultimo jogo e coloca ele em uma variavel chamada ultimo_jogo.
#remove the last game and put it in a variable called ultimo_jogo.

del jogos[1] 
#remove conforme a posição do jogo, por indice.
#remove according to the game position, by index.


jogos.sort() 
#Coloca em ordem alfabética a ordem
#Alphabetically sort the order

jogos.reverse()
#Inverte a ordem da lista.
#Reverses the order of the list.

print(jogos[1:3])
#mostra apenas do segundo ao terceiro item.
#shows only the second to third item.

print(jogos[::-1])
#Exibe a lista ao contrário.
#Display the list in reverse.

print("Posição Overwatch:", jogos.index("Overwatch"))
#Conta a posição de um item especifico que está na lista.
#Counts the position of a specific item in the list.

print("Quantidade Valorant: ", jogos.count("Valorant"))
#Conta quantas vezes o item está presente na lista.
#Counts how many times the item is present in the list.

print(jogos)
#Mostra os jogos listados.
#Shows the listed games.