#For: Itera sobre uma sequência (lista, tupla, string). É ideal quando sabemos o número de iterações.
#For: Iterates over a sequence (list, tuple, string). It is ideal when we know the number of iterations.

for i in range(5):
    #inicia um loop for, chamado i com 5 interações.
    #start a for loop, called i with 5 iterations.
    print(i)
    #printa o loop i.
    #print loop i.


#While: Executa enquanto a condição for verdadeira. É útil para condições em que não sabemos o número exato de iterações de antemão.
#While: Executes while the condition is true. It is useful for conditions where we do not know the exact number of iterations in advance.

contador = 0 
#criei uma variavel contador que tem o valor de 0.
#I created a counter variable that has the value of 0.

while contador < 5:
    #cria o contador while, que continuará contando até o valor deixe de ser menor que 5
    #create the while counter, which will continue counting until the value is no longer less than 5.
    print(contador)
    #printa o resultado do contador.
    #prints the counter result.
    contador += 1
    #adiciona mais um à variavel contador no final do loop.
    #add one more to the counter variable at the end of the loop.