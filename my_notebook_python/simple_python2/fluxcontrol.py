#break interrompe o loop completamente.
#continue pula para a próxima iteração sem terminar o loop.

#break stops the loop completely.
#continue skips to the next iteration without ending the loop.

for i in range(10):
    #cria um loop for, com o nome de i e com limite até (10)
    #create a for loop, named i and with limit up to (10)
    if i == 5: 
        # cria um loop enquanto i não for igual(==) a 5 ele continua.
        # creates a loop while i is not equal(==) to 5 it continues.
        break 
    #Para o loop
    #stop the loop.
    print(i)