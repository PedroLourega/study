# Leitura dos dados de entrada
peso = float(input())
preco_por_tonelada = float(input())
tipo_cliente = input()

# Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada

# TODO Aplique o desconto conforme o tipo de cliente
if tipo_cliente == "Novo cliente":
  desconto = 0.0
elif tipo_cliente == "Cliente fidelizado":
  desconto = 0.05
elif tipo_cliente == "Cliente premium":
  desconto = 0.10
else:
  desconto = 0.0 
    
valor_final = valor_total * (1 - desconto)

# Exibe o resultado formatado com duas casas decimais
print(f"{valor_final:.2f}")