import paho.mqtt.client as mqtt
from time import sleep

mqttBroker = "10.21.160.16"
port = 1883
client = mqtt.Client('Client 2')
client.connect(mqttBroker, port)

tip2 = "I'm client 2"

for c in range(5):
    client.publish('tip', tip2, hostname=mqttBroker, port=port)
    print('It worked! 2°')
    sleep(1)