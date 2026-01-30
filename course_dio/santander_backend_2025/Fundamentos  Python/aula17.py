# Estruturas Condicionais

saldo = 2000
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Seu saque já está sendo efetuado, aguarda alguns instantes...")
else:
    print("Não é possível sacar neste momento, você não possui o saldo em conta.")

opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))

elif opcao == 2:
    print("Exibindo o extrato ...")
    
else: 
    sys.exit("Opção inválida.")