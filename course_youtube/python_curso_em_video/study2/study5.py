#Funções com parametros opcionais ou padrão

def saudar(nome, saudacao="Olá!"):
    print(f"{saudacao}, {nome}!")

#Valor padrão
saudar("Carlos")
#sem valor padrão
saudar("Carlos", "Bom dia")