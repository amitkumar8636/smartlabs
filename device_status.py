
import paho.mqtt.client as mqtt
from timeduration import *
mqtt_host="127.0.0.1"
mqtt_port=1883
mqtt_timeinterval=60

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("I am conneted as device_status")
    print("Connected with result code "+str(rc))
    main_mqtt_client.subscribe("cdac/iot/sec1_device")
    main_mqtt_client.subscribe("cdac/iot/sec2_device")
    main_mqtt_client.subscribe("cdac/iot/sec3_device")
    print("Connected with result code "+str(rc))
    # The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print("on message")
    topic_send= str(msg.topic)
    msg_send= str(msg.payload.decode())
    #print("IN section1")
    measurement = "device_status"
    if (topic_send=='cdac/iot/sec1_device' and msg_send=='1'):
        start_clock_sec1_device()
    elif (topic_send=='cdac/iot/sec2_device' and msg_send=='1'):
        start_clock_sec2_device()
    elif (topic_send=='cdac/iot/sec3_device' and msg_send=='1'):
        start_clock_sec3_device()
def on_publish(client,userdata,result):
    print("Publish successful from device sttus")
main_mqtt_client = mqtt.Client()
main_mqtt_client.on_connect = on_connect
main_mqtt_client.on_message = on_message
main_mqtt_client.on_publish = on_publish
main_mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
main_mqtt_client.loop_forever()
