print( 12, 34, 1011, sep="-", end='##\n') # argumento se='' definine o tipo de separador da função.

# argumento end='' define a funçao de finalizaçao de linha, esta definido como padrão para quebra de linha do windows(CLRF).
print( 56, 78, sep='-', end='\r\n')
print( 13, 12, sep='-', end='\n')
print( 9, 10, sep='-')
# \r\n -> CRLF - quebra de linha
# \n -> LF