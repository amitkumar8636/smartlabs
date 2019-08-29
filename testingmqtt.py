
import time
import paho.mqtt.client as mqtt

# Configure InfluxDB connection variables
host = "127.0.0.1" 
port = 8086 # default port
user = "admin1" # the user/password created for the pi, with write access
password = "admin1" 
dbname = "iotlab" # DATABASE NAME 
interval = 5 # Sample period in seconds

# Create the InfluxDB client object
#lient = InfluxDBClient(host, port, user, password, dbname)

#________mqtt AREA________________________________
def on_connect(client, userdata, flags, rc):
    print("I am conneted main")
def on_publish(client,userdata,result):
    print("published succesfful from main")
def on_disconnect(client,userdata,rc):
    #client.reconnect("127.0.0.1", 1883, 60)
    print("I am disconned from MainClient and not manually reconnect")
mqtt_client1 = mqtt.Client()
def on_connect1(client, userdata, flags, rc):
    print("I am conneted child")
def on_publish1(client,userdata,result):
    print("published succesfful from child")
def on_disconnect1(client,userdata,rc):
    print("I am disconned from childclient")


#mqtt_client1 = mqtt.Client()
mqtt_client1.on_connect = on_connect1
mqtt_client1.on_message = on_disconnect1
mqtt_client1.on_publish = on_publish1
mqtt_client1.on_disconnect=on_disconnect1
mqtt_client1.connect("127.0.0.1", 1883, 3)



mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_disconnect
mqtt_client.on_publish = on_publish
mqtt_client.on_disconnect=on_disconnect
mqtt_client.connect("127.0.0.1", 1883, 60)
#__________________________________________________
count=0
while count!=5:
    print(mqtt_client1.publish("cdac","HI"))
    time.sleep(1)
    count=count+1


mqtt_client1.connect("127.0.0.1", 1883, 60)

if True:
    mqtt_client1.connect("127.0.0.1", 1883, 60)


time.sleep(5)
print(mqtt_client1.publish("cdac","HI"))

#++++++++++++++++++++++++++++++++++SECTION 1 ENDS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#mqtt_client.publish("cdac","JIH")
#switch_on_sec1_projector()
#time.sleep(3)
#switch_off_sec1_projector()

mqtt_client.loop_forever()
