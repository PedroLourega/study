def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/ {modelo}/{ano}/{placa}")

# FORMAS DE SALVAR NA FUNÇÃO

# Não muito eficaz pois vários lados negativos.
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Método melhor que o anterior porém ainda possue alguns problemas.
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Método considerado mais eficaz, sem erroz de filtro.
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) 
## OS DOIS ASTERISCOS MOSTRAM QUE É UM DICT PARA O PYTHON