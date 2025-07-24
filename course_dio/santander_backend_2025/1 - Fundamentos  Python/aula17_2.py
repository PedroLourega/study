# Estruturas IF aninhado
conta_normal = False
conta_universitaria = True
conta_especial = True

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:

    if saldo >= saque:
        print("Sque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do chqe especial!")
    else:
        print("Não foi possível realizar o saque.")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
        
elif conta_especial:
    print("Conta especial selecionada!")

else:
    print("Sistema não reconheceu o seu tipo de conta, entre em contato com a sua agência.")