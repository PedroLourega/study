"""
# Leitura e escrita de arquivos

Python nos permite ler e escrever dados em arquivos externos. Podemos abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

"""

"""
## Leitura de arquivos

Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura ("r"). Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().

"""

"""
# LER

arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

"""

#Neste exemplo, o arquivo "dados.txt" é aberto em modo de leitura utilizando open(). Depois, todo o conteúdo do arquivo é lido utilizando o método read() e armazenado na variável conteudo. Finalmente, o conteúdo é mostrado na tela e o arquivo é fechado utilizando o método close().


"""
## Escrita de arquivos

Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.
"""

# ESCREVER

arquivo = open("dados.txt", "w")
arquivo.write("Olá, mundo!")
arquivo.close()

# Neste exemplo, o arquivo "dados.txt" é aberto em modo de escrita utilizando open(). Depois, a string "Olá, mundo!" é escrita no arquivo utilizando o método write(). Finalmente, o arquivo é fechado utilizando o método close().


## !!!! É importante fechar sempre os arquivos depois de utilizá-los para liberar os recursos do sistema. 

"""
Você também pode utilizar a declaração with para manejar a abertura e fechamento de arquivos de maneira automática.

EX:
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


# Neste caso, o arquivo é aberto utilizando a declaração with e é fechado automaticamente uma vez que se sai do bloco with, mesmo se ocorrer uma exceção.
"""



"""
A entrada e saída de dados em Python nos oferece uma grande flexibilidade para interagir com o usuário e manipular arquivos externos. Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos de texto. Lembre-se sempre de manejar adequadamente a abertura e fechamento de arquivos, e considerar as possíveis exceções que podem ocorrer durante as operações de entrada/saída.
"""