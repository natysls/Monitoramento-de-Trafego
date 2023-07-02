# Projeto sobre Monitoramento de Tráfego de Natália Aragão e Rebeca Teófilo
import pandas as pd

# Definindo os arquivos CSV de tráfego a serem analisados
csv_youtube_baixa = 'youtube_baixa.csv'
csv_youtube_media = 'youtube_media.csv'
csv_youtube_alta = 'youtube_alta.csv'
csv_torrent = 'atlantis.csv'

# Carregurando os arquivos CSV em DataFrames do pandas
baixa_df = pd.read_csv(csv_youtube_baixa) # Clipe LSD Sia em 144p
media_df = pd.read_csv(csv_youtube_baixa) # Clipe LSD Sia em 480p
alta_df = pd.read_csv(csv_youtube_alta) # Clipe LSD Sia em 1080p
torrent_df = pd.read_csv(csv_torrent) # Filme Atlatis em 1080p

class trafego:
    def __init__(self, valor):
        self.valor = valor

    def valor(self):
        return self.valor

    # Função para calcular as estatísticas
    def calcular_estatisticas(dataframe):
        tamanho_medio = dataframe['Length'].mean()
        tamanho_desvio_padrao = dataframe['Length'].std()
        intervalos = dataframe['Time'].diff()
        intervalo_medio = intervalos.mean()
        intervalo_desvio_padrao = intervalos.std()
        numero_pacotes = len(dataframe)
        return tamanho_medio, tamanho_desvio_padrao, intervalo_medio, intervalo_desvio_padrao, numero_pacotes

    def imprimir_resultados(nivel, estatisticas):
        print(f"Tipo: {nivel}\n" + 
                f"Tamanho médio de pacotes: {estatisticas[0]}\n" +
                f"Desvio padrão de pacotes: {estatisticas[1]}\n" + 
                f"Intervalo médio entre pacotes: {estatisticas[2]}\n" + 
                f"Desvio padrão entre pacotes: {estatisticas[3]}\n" +
                f"Número de pacotes: {estatisticas[4]}\n")

# Criando uma lista de objetos
tipos_de_trafego = [trafego('Nivel baixo - 144p'), trafego('Nivel medio - 480p'), trafego('Nivel alto - 1080p'),
                    trafego('Torrent')]


print("Estatísticas para tráfego de dados:")
for tipo in tipos_de_trafego:
    if tipo.valor == 'Nivel baixo - 144p':
        filtro = baixa_df['Protocol'] == 'QUIC'  # Ajuste o filtro de acordo com o protocolo usado nos vídeos de streaming
        estatisticas = trafego.calcular_estatisticas(baixa_df[filtro])
        print('Clipe de LSD - Sia no Youtube')
        trafego.imprimir_resultados(tipo.valor, estatisticas)
        
    if tipo.valor == 'Nivel medio - 480p':
        filtro = media_df['Protocol'] == 'QUIC'  # Ajuste o filtro de acordo com o protocolo usado nos vídeos de streaming
        estatisticas = trafego.calcular_estatisticas(media_df[filtro])
        print('Nível do clipe de LSD - Sia no Youtube')
        trafego.imprimir_resultados(tipo.valor, estatisticas)
        
    if tipo.valor == 'Nivel alto - 1080p':
        filtro = alta_df['Protocol'] == 'QUIC'  # Ajuste o filtro de acordo com o protocolo usado nos vídeos de streaming
        estatisticas = trafego.calcular_estatisticas(alta_df[filtro])
        print('Nível do clipe de LSD - Sia no Youtube')
        trafego.imprimir_resultados(tipo.valor, estatisticas)

    if tipo.valor == 'Torrent':
        filtro = torrent_df['Info'] == 'BitTorrent DHT Protocol'  # Ajuste o filtro de acordo com o protocolo ou informação relacionada ao tipo de tráfego
        estatisticas = trafego.calcular_estatisticas(torrent_df[filtro])
        print('Torrent do filme de Atlantis - O Reino Perdido em 1080p')
        trafego.imprimir_resultados(tipo.valor, estatisticas)
        print()

