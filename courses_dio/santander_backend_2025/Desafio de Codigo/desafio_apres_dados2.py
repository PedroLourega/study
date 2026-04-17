# Leitura do numero de exportações digitado
n = int(input())

# Inicializa o dicionario para armazenar toneladas por pais
exportacoes = {}

# Loop para ler os dados de cada exportacao
for _ in range(n):
    linha = input().strip()
    pais, toneladas = linha.split(",")
    pais = pais.strip()
    toneladas = float(toneladas.strip())
    
    # acumula as toneladas de cada pais no dict
    exportacoes[pais] = exportacoes.get(pais, 0) + toneladas

# Imprime o total de toneladas por pai
for pais, total in exportacoes.items():
    print(f"{pais}: {int(total) if total.is_integer() else total} toneladas")