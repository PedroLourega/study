# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

# Tudo que está até a / é SOMENTE por POSIÇÃO.

# Tudo que está depois do * é SOMENTE por CHAVE.

# Exemplo de apenas posição:

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

# Exemplo válido pois na barra(/) acima, é limitador para somente posição.
# O código abaixo passa a informar chave-posicao após a barra, isso está correto.
# Após a barra o código é considerado "hibrido", sendo possível utilizar as duas formas de definicao de chave-poscao.
print("Carro válido:")
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Válido

# O código abaixo passa a ser inválido pois define chave-posicao antes da barra(/) limitadora
#print("Carro inválido:")
#criar_carro(modelo="Palio", ano=1999, placa="ABC", marca="Fiat", motor="1.0", combustivel="Gasolina") #Inválido
