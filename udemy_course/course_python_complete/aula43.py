"""
Exercicio Guiado
Calculadora com While
"""

while True:
    #Solicita os números e pergunta qual operador do cálculo
    num1 = input("Digite o primeiro número da operação:")
    num2 = input("Digite o segundo número da operação:")
    operador = input("Digite o operador[ + | - | / | * ]:")

    #Flag de números válidos.
    numeros_validos = None
    num1_float = 0
    num2_float = 0
    
    try:
        #Converte os números para float.
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True #Confirma que os numeros são válidos.
    except:
        numeros_validos = None #Caso não sejam válidos recebem valor None.

    if numeros_validos is None: #Se o número não for válido, exibe a mensagem.
        print('Um dos números são inválidos.')
        continue


    #Flag de operadores permitidos.
    operadores_permitidos = "+-/*"

    #Caso a pessoa digite um operador inválido, volta o código e exibe a mensagem.
    if operador not in operadores_permitidos:
        print('O operador digitado é inválido.')
        continue

    # Caso a pessoa digite mais de um operador, volta o código e exibe a mensagem.    
    if len(operador) > 1:
        print('Digite apenas um operador, por favor.')
        continue

    ###
    print("Realizando seu cálculo... Confira o resultado abaixo:")
    if operador == "+":
        print(f"{num1_float} + {num2_float}=", num1_float + num2_float)
    elif operador == "-":
        print(f"{num1_float} - {num2_float}=", num1_float - num2_float)
    elif operador == "*":
        print(f"{num1_float} * {num2_float}=", num1_float * num2_float)
    elif operador == "/":
        print(f"{num1_float} / {num2_float}=", num1_float / num2_float)
    else:
        print("Nunca vai chegar aqui.")

    # Sair do programa.
    sair = input("Você de seja sair? [s]Sim [n]Não").lower().startswith('s')

    if sair is True:
        break


