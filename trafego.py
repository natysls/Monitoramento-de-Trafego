#Projeto de Natália Aragão e Rebeca Teófilo
import pandas as pd

# Defina o arquivo CSV de tráfego a ser analisado
csv_file = 'trafego.csv'

# Carregue o arquivo CSV em um DataFrame do pandas
df = pd.read_csv(csv_file)

# Função para calcular as estatísticas
def calcular_estatisticas(dataframe):
    tamanho_medio = dataframe['Length'].mean()
    tamanho_desvio_padrao = dataframe['Length'].std()
    intervalos = dataframe['Time'].diff()
    intervalo_medio = intervalos.mean()
    intervalo_desvio_padrao = intervalos.std()
    numero_pacotes = len(dataframe)

    return tamanho_medio, tamanho_desvio_padrao, intervalo_medio, intervalo_desvio_padrao, numero_pacotes

# Calcular estatísticas para vídeos de streaming
print("Estatísticas para vídeos de streaming:")
for nivel in range(3):
    filtro = df['Protocol'] == 'HTTP'  # Ajuste o filtro de acordo com o protocolo usado nos vídeos de streaming
    estatisticas = calcular_estatisticas(df[filtro])
    print(f"Nível: {nivel}")
    print(f"Tamanho médio de pacotes: {estatisticas[0]}")
    print(f"Desvio padrão de pacotes: {estatisticas[1]}")
    print(f"Intervalo médio entre pacotes: {estatisticas[2]}")
    print(f"Desvio padrão entre pacotes: {estatisticas[3]}")
    print(f"Número de pacotes: {estatisticas[4]}")
    print()

# Calcular estatísticas para tráfego de dados
print("Estatísticas para tráfego de dados:")
for tipo in ['páginas_web', 'download_arquivos', 'p2p']:  # Ajuste os tipos de tráfego conforme suas colunas ou informações específicas
    filtro = df['Info'] == 'Aplication Data'  # Ajuste o filtro de acordo com o protocolo ou informação relacionada ao tipo de tráfego
    estatisticas = calcular_estatisticas(df[filtro])
    print(f"Tipo: {tipo}")
    print(f"Tamanho médio de pacotes: {estatisticas[0]}")
    print(f"Desvio padrão de pacotes: {estatisticas[1]}")
    print(f"Intervalo médio entre pacotes: {estatisticas[2]}")
    print(f"Desvio padrão entre pacotes: {estatisticas[3]}")
    print(f"Número de pacotes: {estatisticas[4]}")
    print()
