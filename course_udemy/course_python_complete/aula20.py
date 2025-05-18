#Operadores lógicos

# and(e) | or(ou) | not(não)

#and -> Todas as condições precisam ser True.

#OBS: Se qualquer valor for considerado falso, a expressão inteira será avalidade naquele valor.

#São considerados falsy: 0|0.0|''|False


#Também existe o tipo None que é usado para representar um "Não Valor".

entrada = input("[E]Entrar [S]Sair:")
senha_digitada = input("Senha:")

senha_permitida = "123456"

if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
    print("Entrar")
else:   
    print("Sair")

