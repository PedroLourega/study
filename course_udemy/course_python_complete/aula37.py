"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
contador = 0
numero = int(input("Digite um número da sua escolha: "))

while contador < numero:
    contador += 1 # O Contador em cima do print faz com que ele conte até o numero escolhido.
    print(f"Contando: {contador}")