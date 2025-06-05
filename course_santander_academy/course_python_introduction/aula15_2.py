"""
# Pacotes

Um pacote é uma forma de organizar módulos relacionados em uma estrutura hierárquica de diretórios. Os pacotes nos permitem agrupar módulos relacionados e evitar conflitos de nomes entre módulos.


"""

"""
## Criar e utilizar pacotes

Para criar um pacote, criamos um diretório com o nome desejado e adicionamos um arquivo especial chamado __init__.py dentro do diretório. Este arquivo pode estar vazio ou conter código de inicialização do pacote.

Por exemplo, criamos um diretório chamado meu_pacote com a seguinte estrutura:


meu_pacote/
    __init__.py
    modulo1.py
    modulo2.py


## Depois, podemos importar e utilizar os módulos do pacote em nosso programa.
"""
from meu_pacote import modulo1, modulo2


modulo1.funcao1()
modulo2.funcao2()

## Neste exemplo, são importados os módulos modulo1 e modulo2 do pacote meu_pacote e são utilizadas as funções definidas neles.

# A importação e criação de módulos e pacotes em Python nos permite organizar e reutilizar nosso código de maneira eficiente. Ao modularizar nosso código, podemos manter um código mais legível, estruturado e fácil de manter.

# Lembre-se de explorar a biblioteca padrão de Python e aproveitar os módulos existentes, que podem facilitar muitas tarefas comuns. Além disso, não hesite em criar seus próprios módulos e pacotes para organizar e reutilizar seu código de maneira eficaz.