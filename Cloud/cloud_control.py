import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import time
import paho.mqtt.client as mqtt
import ast

#==================================================
#Setting up InfluxDB Connection

bucket = '4f71c92eed8d6ea3' 
org = '2739d165137ff495'
token = '2NK5ebiVWLj19rXIgIR3xcrUEIn0SdzTHp3IsDb5KtRH2vVfJzyRhN4y5imjDq5s_clV3UZDThhxvNN5jrksow=='
url = 'https://us-east-1-1.aws.cloud2.influxdata.com'

client = influxdb_client.InfluxDBClient(
    url = url,
    token = token,
    org = org
)

write_api = client.write_api(write_options=SYNCHRONOUS)

#===================================================
#Setting up MQTT Connection

temperature = 0
user = ''

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):

    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))
    message = ast.literal_eval(msg.payload.decode('utf-8'))
    if (msg.topic == 'my/test/topic'):
        p = influxdb_client.Point('measurements').tag('User',message['user']).field('temperature',message['temperature'])
        write_api.write(bucket = bucket, org = org, record = p)
        if (message['temperature'] > 30):
            alert(message['user'])

# Creating function to send alert to device
def alert(user):
    topic = 'my/{}/topic'.format(str(user))
    message = json.dumps({'alert': 1})
    client.publish(topic, message)

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("DELL_LAPTOP", "Abcd1234")

# connect to HiveMQ Cloud on port 8883
client.connect("26d2ed39011f420086e3c922524409ac.s1.eu.hivemq.cloud", 8883)

# subscribe to the topic "my/test/topic"
client.subscribe("my/test/topic")
client.subscribe('my/DELL_LAPTOP/topic')
client.subscribe('my/RASPBERRY_PI/topic')

client.loop_forever()