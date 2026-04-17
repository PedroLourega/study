# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 
# P e d r o 
# -5-4-3-2-1

nome = "Pedro"
nome2 = "abcdefghijklmnopqrstuvwxyz"

print(nome[2])
print(nome[-3])
print(nome[1])
print(nome[-4])
print(nome[-5])
print(nome[-4])
print(nome[-3])
print(nome[-2])
print(nome[-1])
print(10 * '-')
print('P' in nome)
print('p' in nome)
print("a" not in nome)
print("o" not in nome)
print(10 * '-')
print(nome2[-21])
print(nome2[21])
print(nome2[15])
print(nome2[-11])
print("12" and "jp" not in nome2)
print('p' or '0' in nome)
print('q' or '12' not in nome2)
print('10' or '12' in nome2)