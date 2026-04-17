# Operadores lógicos

#operador E(AND) AMBOS
saldo = 1000
saque = 200
limite = 100

print(("AND:"),saldo >= saque and saque <= limite)

#operador OU(OR) UM OU OUTRO
saldo2 = 1000
saque2 = 200
limite2 = 100

print(("OR:"),saldo >= saque or saque <= limite)

#operador NÃO(NOT) INVERSO
saldo3 = 1000
saque3 = 200
limite3 = 100

contatos_emergencia = []

print(("NOT:"),not 100 > 1500)
print(("Expressao 1:"),not contatos_emergencia)
print(("Expressao 2:", not"saque 1500"))
print(("Expressao 3:", not""))