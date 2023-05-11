import json
import time
from azure.iot.device import IoTHubDeviceClient, Message

deviceConnectionString = "HostName=umidade-hub.azure-devices.net;DeviceId=sensor-umidade;SharedAccessKey=A2mJ3zmLNBCnz2cF8Ndl+1Zeu/vlNKlWBzrpCWIMK+U="
device_client = IoTHubDeviceClient.create_from_connection_string(deviceConnectionString)

message = {
    "humidity": 69.0
}

# Adiciona a propriedade personalizada "sensorID" à mensagem
message_props = message["properties"] if "properties" in message else {}
message_props["sensorID"] = "VSLog"
message["properties"] = message_props

message_json = json.dumps(message)
print(message_json)
device_client.send_message(Message(message_json))


