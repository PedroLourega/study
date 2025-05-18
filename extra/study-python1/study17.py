import os
#os.getcws() - Obtém o diretório de trabalho atual.
#os.listdir(path) - Lista os arquivos e diretórios em um caminho específico.
#os.path.join(path, *paths) - Combina partes de caminhos para formar um novo caminho.
#os.path.exists(path) - Verifica se um caminho existe.
#os.mkdir(path) - Cria um novo diretório.
#os.remove(path) - Remove um arquivo.
#os.rename(src, dst) - Renomeia um arquivo ou diretório.
#os.environ - Deicionário com variáveis de ambiente do sistema.
#os.system(command) - Executa um comando no sistema.
#os.chdir - Altera o diretório de trabalho atual.

mensagens = []

nome= input("Nome: ")

while True:

    #limpando terminal

    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_________________")       

    #obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    #adcionando mensagem na lista
    mensagens.append({
        "nome":nome,
        "texto":texto
    })
