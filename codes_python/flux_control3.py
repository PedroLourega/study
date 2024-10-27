# O controle de fluxo permite que o programa execute blocos de código baseados em condições. Python usa if, elif, e else com identação para delimitar o bloco.

#Flow control allows the program to execute blocks of code based on conditions. Python uses if, elif, and else with indentation to delimit the block.

#exemplo:
#exemple:

idade = 20 #defini a variavel idade o valor de 20 
#set the age variable to a value of 20
if idade >= 18: #Construi um fluxo com if, utilizei a variavel idade, para saber se é MAIOR ou IGUAL a 18.
#Build a flow with if, I used the age variable, to know if it is GREATER or EQUAL to 18.
    print("Maior de idade")#se o usuário foi maior de idade, está mensagem que "printamos" aparece na tela.
    #if the user is of legal age, this message that "we printed" appears on the screen.
else: #finaliza o fluxo if
    print("Menor de idade")#se não atender o if de >=18, o sistema mostra está frase.
