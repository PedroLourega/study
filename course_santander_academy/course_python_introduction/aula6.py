"""
##LOOPS
Os loops nos permitem repetir um bloco de código várias vezes. Em Python, os loops mais comuns são for e while.


### FOR
O loop for é utilizado para iterar sobre uma sequência(como uma lista, uma tupla ou uma string) ou qualquer objeto iterável. A sintaxe básica é a seguinte:

for variável in sequência:
    #bloco de código que vai repetir
ex:

frutas = ["maça", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

Neste exemplo, o loop for itera sobre a lista frutas. Em cada iteração, a variável fruta assume o valor de um elemento da lista, e o bloco de código dentro do loop é executado. Neste caso, cada fruta é impressa em uma linha separada.

"""
"""
### WHILE

O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira. A sintaxe básica é a seguinte:

while condição:

    # Bloco de código a repetir
    instruções

Exemplo:

contador = 0


while contador < 5:

    print(contador)
    contador += 1

    
Neste exemplo, o loop while é executado enquanto a variável contador for menor que 5. Em cada iteração, o valor de contador é impresso e depois incrementado em 1 pela instrução contador += 1. O loop será interrompido quando contador atingir o valor de 5.

É importante ter cuidado ao usar o loop while, pois, se a condição nunca se tornar falsa, o loop será executado indefinidamente, o que é conhecido como um loop infinito.    
"""

print("Números de 1 a 5 multiplicados por 2 com função for:")
for numero in range(1, 6):
    print(numero * 2)

print("\n Números de 1 a 5 multiplicados por 2 com função for:")

contador = 1
while contador <= 5:
    print(contador*2)
    contador += 1

"""
#CONTROLE DE LOOPS

Python fornece algumas instruções especiais para controlar o fluxo de execução dentro dos loops:

### Break
A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição. Quando um break é encontrado, o loop é interrompido e o fluxo de execução continua com a próxima instrução fora do loop.

contador = 0


while True:

    print(contador)
    contador += 1


    if contador == 5:
        break

Neste exemplo, o loop while é executado indefinidamente devido à condição True. No entanto, dentro do loop é utilizada uma estrutura condicional if para verificar se contador é igual a 5. Quando essa condição é satisfeita, a instrução break é executada, fazendo com que o loop seja interrompido e o fluxo de execução continue com a próxima instrução fora do loop.

"""
"""
### Continua 

A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.

Exemplo:

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
Neste exemplo, o loop for itera sobre os números de 0 a 9 utilizando a função range(). Dentro do loop, verifica-se se o número é divisível por 2 utilizando o operador de módulo %. Se o número for divisível por 2 (ou seja, se for par), a instrução continue é executada, fazendo com que o restante do bloco de código seja pulado e passando para a próxima iteração do loop. Como resultado, apenas os números ímpares serão impressos.

"""

"""
### Pass
A instrução pass é uma operação nula que não faz nada. É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada.

Exemplo:

for i in range(5):
    pass
Neste exemplo, o loop for itera sobre os números de 0 a 4, mas nenhuma ação é realizada dentro do loop devido à instrução pass. Isso pode ser útil quando se está desenvolvendo um programa e se deseja reservar um bloco de código para implementá-lo mais tarde.

"""