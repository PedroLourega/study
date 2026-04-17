"""
# ENTRADAS / SAÍDAS

Em Python, a entrada e saída de dados nos permite interagir com o usuário e manipular arquivos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos externos.

"""
"""
## Entrada de dados do usuário

Para obter informações do usuário durante a execução do programa, podemos utilizar a função input(). Esta função mostra uma mensagem na tela e espera que o usuário insira um valor.

"""
# nome = input("Insira seu nome: ")
# idade = input("Insira sua idade: ")


# print("Olá, " + nome + "!")
# print("Você tem " + idade + " anos.")

# Neste exemplo, solicita-se ao usuário que insira seu nome e idade utilizando a função input(). Os valores inseridos são armazenados nas variáveis nome e idade, respectivamente. Em seguida, essas variáveis são utilizadas para mostrar uma saudação personalizada na tela.

# IMPORTANTE
# A função input() sempre retorna uma cadeia de texto. Se você deseja trabalhar com outros tipos de dados, como números inteiros ou flutuantes, deve realizar uma conversão explícita utilizando funções como int() ou float().

idade = int(input("Insira sua idade: "))


if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Neste exemplo, solicita-se ao usuário que insira sua idade e converte o valor inserido para um número inteiro utilizando int(). Em seguida, utiliza-se uma estrutura condicional para verificar se a idade é maior ou igual a 18 e mostrar uma mensagem correspondente.

"""
## Saída de dados

Para mostrar informações na tela, utilizamos a função print(). Esta função recebe um ou mais argumentos e os mostra no console.

Podemos utilizar a f-string (formatação de cadeias) para inserir variáveis diretamente dentro de uma cadeia de texto.


EX: 

nome = "Juan"
idade = 25


print(f"Olá, meu nome é {nome} e tenho {idade} anos.")
"""
# Neste caso, as variáveis são inseridas dentro da cadeia utilizando chaves {} e a cadeia é precedida pela letra f para indicar que é uma f-string.

 