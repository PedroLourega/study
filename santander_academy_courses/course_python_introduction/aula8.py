"""
# TUPLAS

Uma tupla é uma estrutura de dados imutável e ordenada que permite armazenar uma coleção de elementos. Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas.


## Criação e acesso

Para criar uma tupla, encerre os elementos entre parênteses:

ponto = (3, 4)
Para acessar os elementos de uma tupla, utilize o índice do elemento entre colchetes, similar às listas:

print(ponto[0])  # Imprime 3

print(ponto[1])  # Imprime 4
Ao contrário das listas, as tuplas são imutáveis, o que significa que não podem ser modificadas uma vez criadas. Não se pode adicionar, eliminar ou alterar elementos em uma tupla existente.

As tuplas são úteis quando você precisa armazenar uma coleção de elementos que não devem ser modificados, como coordenadas ou dados de configuração.

"""

"""
Métodos de tuplas
Embora as tuplas sejam imutáveis, Python fornece vários métodos úteis para trabalhar com elas:

count(elemento): devolve o número de vezes que um elemento aparece na tupla. 

index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 

len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.

"""
minha_tupla = (1, 2, 3, 2, 4, 2)


print (minha_tupla.index(2))   # Saída: 1

print (minha_tupla.index(2, 2))   #Saída: 3

print (minha_tupla.index(2, 2, 4))   #Saída: 3