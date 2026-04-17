"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar

click na var + F2 -> muda o nome da variavel e de todas as outras com o mesmo nome.
"""
numero_str = input("Vou dobrar o numero que você digitar: ")

try:
    print("STR: ", numero_str)
    numero_float = float(numero_str)
    print("FLOAT: ", numero_float)
    print(f"o dobro de {numero_str} é {numero_float * 2:.2f}")

except:
   print("Isso não é um número!")