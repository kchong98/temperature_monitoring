import paho.mqtt.client as mqtt
import board
import Adafruit_DHT
import json
import time

# Setting up temperature sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("______________", "______________")

# connect to HiveMQ Cloud on port 8883
client.connect("______________", 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic")

while(1):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        message = json.dumps({"temperature":temperature, "user": "______________"})
        client.publish("my/test/topic", message) # Publish message to MQTT broker
        print(message)
    else:
        print('Sensor failure. Check wiring.')
    time.sleep(5)

### Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
