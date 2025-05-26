"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = 'pedro henrique'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
#string[3] = 'ABC'
#print(string[3]) #IMUTÁVEL -> nao pode mudar o valor
print(outra_variavel)
print(string.capitalize())
print(string.islower())
print(string.zfill(100))