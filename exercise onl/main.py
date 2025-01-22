import json

import paho.mqtt.client as mqttclient
import time
import random

BROKER_ADDRESS = "demo.thingsboard.io"
PORT = 1883
THINGS_BOARD_ACCESS_TOKEN = "ceizen4tq4q7yecnk6h3"

def subscribed(client, userdata,mid,granted_qos):
    print ("Subscribed...")

def recv_message(client, userdata, message):
    print("Received: '" + message.payload.decode("utf-8"))

def connected(client, userdata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("v1/devices/me/rpc/request/+")
    else:
        print("Bad connection Returned code=", rc)

client = mqttclient.Client(client_id="Gateway_Thingsboard")
client.username_pw_set(THINGS_BOARD_ACCESS_TOKEN)

client.on_connect = connected
client.connect(BROKER_ADDRESS, PORT)
client.loop_start()

client.on_subscribe = subscribed
client.on_message = recv_message

temp=30
humi=50
light_intesity = 100
counter=0

longitude = 106.7
latitude = 10.6

while True:
    collect_data={
        'temperature': temp,
        'humidity': humi,
        'light': light_intesity,
        'longitude': longitude,
        'latitude': latitude
    }
    temp+=1
    humi+=1
    light_intesity+=1
    client.publish("v1/devices/me/telemetry",json.dumps(collect_data),qos= 1)
    print(f"Published: {collect_data}")
    time.sleep(5)
