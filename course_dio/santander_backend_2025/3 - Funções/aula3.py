def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/ {modelo}/{ano}/{placa}")

# FORMAS DE SALVAR NA FUNÇÃO
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) ## OS DOIS ASTERISCOS MOSTRAM QUE É UM DICT PARA O PYTHON