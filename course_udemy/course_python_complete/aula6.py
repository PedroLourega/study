# conversão de tipos, coerção
# type convertiom, typecasting, coercion é o ato de converter um tipo em outro tipo imutaveis e primitivos: str, int, float, bool

#os primitivos são imutaveis, ou seja, voce nao pode muda-los
print(int('1'),type(int('1')))
print('pe' + 'dro')
print(int('1') + 1) # Conversao de dados de str para inteiro
print(float('1') + 1) # Todo numero que é colocado em operação com float, se torna float também.
print(bool(''))# str vazia é considerada False.
print(bool(' '))# str com qualquer caracter ou até mesmo espaço é considerada True.
print(str(11) + 'b')