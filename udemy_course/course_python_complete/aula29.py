"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condiçoões no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 90 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

# letras maiusculas em nomes de variaveis constantes é uma forma de diferenciar quando atribuimos dados imutaveis.

carro_passou_radar_1 = velocidade > RADAR_1

carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_passou_radar_1:
    print("Velocidade do carro passou do radar 1")
else:
    print("Velocidade do carro NÃO passou do radar 1")

if carro_passou_radar_1:
    print("Carro passou radar 1")

if carro_multado_radar_1 and carro_passou_radar_1:
    print("Carro multado no radar 1")  