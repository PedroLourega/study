#Loops for e while permitem que executemos ações repetidamente.
#For and while loops allow us to perform actions repeatedly.


#for loop: Geralmente usado para percorrer uma sequência de elementos, como listas ou faixas de números.
#for loop: Generally used to loop through a sequence of elements, such as lists or ranges of numbers.

for i in range(5):#aqui criamos um loop for, que tem o nome de i e valor in range de 5 vezes (5) , começando em 0.
#here we create a for loop, which has the name i and a value in range of 5 times (5), starting at 0.
    print(i)
#printa a variavel i(loop) até 4.
#print the variable i(loop) up to 4.


#while loop: Continua a executar enquanto uma condição é verdadeira.
#while loop: Continues to execute as long as a condition is true.

contador = 0    
#cria um contador que inicia em 0
#create a counter that starts at 0

while contador < 5:
    #define um loop para o contador enquanto ele for menor que 5
    #define a loop for the counter while it is less than 5
    print(f"Contador é:{contador}")
    #printa a string com a variavel 
    #print the string with the variable
    
    contador += 1 
    #no final soma mais um toda vez que finaliza o loop até chegar ao valor menor mais próximo do 5(que seria 4)

    #at the end add one more every time the loop ends until you reach the smallest value closest to 5 (which would be 4).