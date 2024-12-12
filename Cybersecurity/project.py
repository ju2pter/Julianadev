#Análise de Pacotes de Rede em Python

from scapy.all import sniff
import pandas as pd
import time


# Função que processa os pacotes capturados
def packet_handler(packet):
     try:
        # Captura os dados importantes do pacote
        data = {
            "Timestamp": time.time(),
            "Source IP": packet[1].src,
            "Destination IP": packet[1].dst,
            "Protocol": packet.proto,
            "Length": len(packet)
        }
        # Adiciona o pacote à lista de dados
        packets_data.append(data)
     except IndexError:
        pass  # Ignorar pacotes sem os campos necessários


# Lista onde vamos armazenar os pacotes
packets_data = []


# Inicia a captura de pacotes (limitada a 100 pacotes, você pode aumentar esse número)
sniff(prn=packet_handler, count=100)


# Cria um DataFrame para armazenar os dados
df = pd.DataFrame(packets_data)


# Exibe os dados capturados
print(df.head())


#pandas



# Analisando os tipos de protocolos capturados
protocol_counts = df["Protocol"].value_counts()
print("Contagem de Protocolos:")
print(protocol_counts)


# Analisando os IPs mais acessados
top_ips = df["Source IP"].value_counts().head(10)
print("\nTop 10 IPs mais acessados:")
print(top_ips)


# Salvando os dados capturados em um CSV
# Linha corrigida
df.to_csv('network_packets.csv', index=False)


#matploitlib


import matplotlib.pyplot as plt


# Gráfico da contagem de protocolos
protocol_counts.plot(kind='bar', title='Contagem de Protocolos')
plt.xlabel('Protocolos')
plt.ylabel('Contagem')
plt.show()