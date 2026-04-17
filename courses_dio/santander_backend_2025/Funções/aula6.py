

#APENAS POSICAO
def criar_carro(*, modelo, ano, placa, motor, combustivel):
    print(modelo, ano, placa, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# CARACTER POSICAO *



# KEYWORD E POSICAO( HIBRIDO )
def criar_carro2(modelo, ano, placa, /, *, motor, combustivel):
    print(modelo, ano, placa, motor, combustivel)

criar_carro2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# CARACTER NOME /(item)