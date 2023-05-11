import paho.mqtt.client as mqtt
import json
import time

device_name = "sensor-umidade"
hub_name = "umidade-hub"
username = "{hub_name}/{device_name}/?api-version=2018-06-30"
key = "HostName=umidade-hub.azure-devices.net;DeviceId=sensor-umidade;SharedAccessKey=A2mJ3zmLNBCnz2cF8Ndl+1Zeu/vlNKlWBzrpCWIMK+U="

# Define o nome do tópico MQTT usado para enviar mensagens
topic = "devices/{device_name}/messages/events/"

# Cria uma mensagem JSON
message = {
    "humidity": 0.0,
}

# Converte a mensagem em um formato JSON
message_json = json.dumps(message)

# Cria um cliente MQTT
client = mqtt.Client(client_id=device_name, protocol=mqtt.MQTTv311)


# Define a função de callback para quando a conexão for estabelecida
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT com código de retorno: {}".format(rc))
    else:
        print("Erro de conexão: código de retorno {}".format(rc))

# Define a função de callback para quando uma mensagem for publicada
def on_publish(client, userdata, mid):
    print("Mensagem publicada com sucesso!")

# Define as credenciais de autenticação
client.username_pw_set(username, key)

# Define as funções de callback
client.on_connect = on_connect
client.on_publish = on_publish

# Conecta ao broker MQTT
try:
    client.connect("umidade-hub.azure-devices.net", port=8883)
except:
    print("Não foi possível conectar ao broker MQTT.")

# Publica a mensagem no tópico especificado
client.publish(topic, payload=message_json)

# Espera um segundo antes de desconectar
time.sleep(1)

# Desconecta do broker MQTT
client.disconnect()