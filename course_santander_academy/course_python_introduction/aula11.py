"""
# FUNÇÕES

As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário. As funções nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fáceis de manter.

 
## Definição e chamada de funções

Para definir uma função em Python, utilizamos a palavra-chave def seguida do nome da função e parênteses. Opcionalmente, podemos especificar parâmetros dentro dos parênteses. O bloco de código da função é indentado após os dois pontos.

Para chamar uma função, simplesmente escrevemos o nome da função seguido de parênteses:
"""

def saudacao():
    print("Olá, mundo!")


saudacao()  # Imprime "Olá, mundo!"
"""
## Parâmetros e argumentos

As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. Os parâmetros são especificados dentro dos parênteses na definição da função.
"""
def saudacao(nome):
    print(f"Olá, {nome}!")
# Ao chamar a função, fornecemos os argumentos correspondentes aos parâmetros:

saudacao("João")  # Imprime "Olá, João!"
saudacao("Maria")  # Imprime "Olá, Maria!"

"""
## Valores de retorno

As funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função.

"""

def soma(a, b):
    return a + b


resultado = soma(3, 4)
print(resultado)  # Imprime 7

"""
## Funções anônimas (lambda)

Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. São comumente usadas para funções pequenas e concisas.

"""

quadrado = lambda x: x ** 2
print(quadrado(5))  # Imprime 25

"""
Função normal	                Função lambda equivalente
def soma(a, b): return a + b	lambda a, b: a + b
def quadrado(x): return x**2	lambda x: x**2


Conceito:	    Explicação breve:
lambda:	        Cria uma função anônima (sem nome)
Sintaxe:	    lambda argumentos: resultado
Uso comum:	    Em tarefas rápidas ou como argumento de outra função
Exemplo:	    lambda x: x**2 → retorna o quadrado de x
"""

"""
## Escopo das variáveis (local vs. global)

As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.

"""
def funcao():
    variavel_local = 10
    print(variavel_local)  # Acessível dentro da função


variavel_global = 20


def funcao2():
    print(variavel_global)  # Acessível de qualquer lugar


funcao()  # Imprime 10
funcao2()  # Imprime 20
print(variavel_global)  # Imprime 20
# print(variavel_local)  # Gera um erro, a variável não está definida neste escopo.

"""
### Documentação de funções (docstrings)

É uma boa prática documentar nossas funções utilizando docstrings. Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.

ex:
"""

def area_retangulo(base, altura):
    """
    Calcula a área de um retângulo.


    Args:
        base (float): A base do retângulo.
        altura (float): A altura do retângulo.


    Returns:
        float: A área do retângulo.
    """
    return base * altura

"""
### Funções com número variável de argumentos

Python permite definir funções que aceitem um número variável de argumentos. Isso é feito utilizando o operador * antes do nome do parâmetro.
"""

def soma_variavel(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(soma_variavel(1, 2, 3))  # Imprime 6
print(soma_variavel(4, 5, 6, 7))  # Imprime 22

# As funções são uma ferramenta fundamental na programação e nos permitem estruturar e modularizar nosso código. Com a capacidade de definir funções personalizadas, podemos encapsular tarefas específicas e reutilizá-las em diferentes partes do nosso programa.

# Além das funções definidas pelo usuário, Python também fornece uma ampla gama de funções incorporadas que podemos utilizar diretamente, como print(), len(), range(), entre outras.