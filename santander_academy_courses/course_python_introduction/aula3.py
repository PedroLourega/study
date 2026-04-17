"""
#Declaração e atribuição de variáveis
As variáveis são contêineres que nos permitem armazenar e manipular dados em nossos programas. Para declarar e atribuir um valor a uma variável em Python, utilizamos o operador de atribuição =. O nome da variável vai à esquerda do operador, e o valor que você deseja atribuir vai à direita. Por exemplo:

nome = "Juan"
idade = 25
altura = 1.75
eh_estudante = True
##No exemplo, declaramos e atribuímos valores às variáveis nome, idade, altura e eh_estudante. O Python infere automaticamente o tipo de dados de cada variável com base no valor atribuído.

Você também pode atribuir o mesmo valor a várias variáveis em uma única linha usando o operador de atribuição múltipla:
a = b = c = 10
### Neste caso, as variáveis a, b e c terão o valor 10.

-------------

Regras para nomear variáveis

1.Os nomes das variáveis só podem conter letras (a-z, A-Z), números (0-9) e sublinhados (_). Não podem começar com um número.

2.O Python diferencia maiúsculas de minúsculas, então nome e Nome são variáveis diferentes.


3.Não se pode usar palavras-chave reservadas do Python como nomes de variáveis (por exemplo, if, else, for, while, etc.).

4.Recomenda-se usar nomes descritivos para as variáveis, que indiquem claramente seu propósito: nome, idade, total_vendas, etc.


##Seguindo essas regras, alguns exemplos de nomes de variáveis válidos são:
idade
nome_completo
total_vendas
_contador


E alguns exemplos de nomes de variáveis inválidos são:

1idade   # Começa com um número
nome-completo   # Usa um hífen em vez de um sublinhado
if   # Palavra-chave reservada do Python
"""