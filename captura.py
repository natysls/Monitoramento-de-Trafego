import pandas as pd
import numpy as np

# Defina o arquivo CSV de tráfego a ser analisado
csv_file = 'trafego.csv'

# Carregue o arquivo CSV em um DataFrame do pandas
df = pd.read_csv(csv_file)

# Calcule as estatísticas desejadas
tamanho_medio = df['Tamanho'].mean()
tamanho_desvio_padrao = df['Tamanho'].std()
intervalo_medio = df['Intervalo'].mean()
intervalo_desvio_padrao = df['Intervalo'].std()
numero_pacotes = len(df)

# Imprima as estatísticas
print("Estatísticas do tráfego:")
print(f"Tamanho médio de pacotes: {tamanho_medio}")
print(f"Desvio padrão de pacotes: {tamanho_desvio_padrao}")
print(f"Intervalo médio entre pacotes: {intervalo_medio}")
print(f"Desvio padrão entre pacotes: {intervalo_desvio_padrao}")
print(f"Número de pacotes: {numero_pacotes}")
