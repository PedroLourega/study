"""
# TRATAMENTO DE ERROS E EXCEÇÕES

Quando escrevemos programas, é comum nos depararmos com situações inesperadas ou erros durante a execução. Python fornece um mecanismo para lidar com esses erros de maneira controlada utilizando o tratamento de exceções. Isso nos permite capturar e lidar com erros específicos sem que o programa pare abruptament


Erros comuns em Python

Antes de mergulharmos no tratamento de exceções, vejamos alguns erros comuns que você pode encontrar em Python
"""

"""
## Erro de sintaxe (SyntaxError)

Ocorre quando o código não segue as regras de sintaxe do Python, como esquecer dois pontos após uma declaração de função ou um loop.

def minha_funcao() # Faltam os dois pontos
    print("Olá")

"""

"""
## Erro de nome (NameError)

Ocorre quando se faz referência a uma variável ou função que não foi definida.

print(variavel_nao_definida)

"""

"""
## Erro de tipo (TypeError)

Ocorre quando se realiza uma operação com tipos de dados incompatíveis, como tentar somar um número e uma string.

resultado = 5 + "10"

"""

"""
## Erro de índice (IndexError)

Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência.

lista = [1, 2, 3]
print(lista[3])  # O índice 3 está fora do intervalo


"""
#Estes são apenas alguns exemplos de erros comuns. Quando ocorre um erro, Python gera uma exceção e exibe uma mensagem de erro que inclui o tipo de exceção e uma descrição do problema.