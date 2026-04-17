#codigo funcao

fluxo_caixa = []

print("______________")
print("@ Fluxo Caixa")
print("______________")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para encerrar este processo #\n")

def adicionar_transacao():
    nome = input("Nome: ")
    valor= float( input("Valor: "))
    fluxo_caixa.append({
        "nome":nome,
        "valor":valor
    })

while True:

    opcao = int( input("Digite a opcao desejada: "))

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()  
    else:
        break

    #nota fiscal
    total = 0
    for fc in fluxo_caixa:
        print("Nome:", fc['nome'], ", Valor: R$", fc['valor'])
        total = total + fc['valor']

    print("Saldo atual: R$", total)
     


