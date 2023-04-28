import paho.mqtt.client as mqtt
from time import sleep
from mqtt_publish1 import tip


def on_message(client, userdata, message):
    print('Received message:', message.payload.decode())


mqttBroker = "10.21.160.16"
port = 1883
client = mqtt.Client()
client.connect(mqttBroker, port)

client.loop_start()
client.subscribe(tip)
client.on_message = on_message
sleep(2)
client.loop_stop()
