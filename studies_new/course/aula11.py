#O interpretador, sempre lê da esquerda para a direita, de cima para baixo.
# 1. (n + n) #de dentro para fora, do mais dentro até chegar nos calculos fora.
# 2. **
# 3. *, /, //, %
# 4. + , -
conta_1 = (1 + 1) ** (5 + 5) #1024
conta_2 = 1 + 1 ** 5 + 5 #7
conta_3 = 1 ** 5 #1
conta_4 = 1 + 1 + 5 #7
conta_5 = (1 + int(0.5 + 0.5)) ** (5 + 5) #1024
# conta_1 = 'Valor trocado' #Trocamos o valor da conta_1 para 2
print(conta_1)
print(conta_2)
print(conta_3)
print(conta_4)
print(conta_5)