# FUNÇÕES EM PYTHON

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem2(nome="Pedro") # É sempre necessário que preencha quando possui um nome. Caso contrário dará erro.
exibir_mensagem2("Pedro") # Funciona da mesma forma que a opção de cima
exibir_mensagem3()
exibir_mensagem3(nome="Chappie") 