a = 'AAAA'
b = 'BB'
c = 1.1
string = 'b={nome2} a={nome1} a={nome1} a={nome1} c={nome3}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)