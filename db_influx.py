import time
import sys
import datetime
from influxdb import InfluxDBClient
from devicefunctions import *
import paho.mqtt.client as mqtt
global logfile
# Configure InfluxDB connection variables
host = "127.0.0.1" # My Ubuntu NUC
port = 8086 # default port
user = "rpi-3" # the user/password created for the pi, with write access
password = "rpi-3" 
dbname = "iotlab" # the database we created earlier
interval = 5 # Sample period in seconds
# Create the InfluxDB client object
clientinflux = InfluxDBClient(host, port, user, password, dbname)

mqtt_host="127.0.0.1"
mqtt_port=1883
mqtt_timeinterval=60
#________mqtt AREA________________________________
def on_connect(client, userdata, flags, rc):
    print("Fault_tolerant Mechanism started......")
    logfile.write("Fault_tolerant Mechanism started......"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
def on_publish(client,userdata,result):
    return True
def on_disconnect(client,userdata,rc):
    print("Error in Fault Tolerance System"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    logfile.write("Fault_tolerant Mechanism Stopped......"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")

mqtt_fault_client = mqtt.Client()
mqtt_fault_client.username_pw_set("mqttuser","mqttpassword")
mqtt_fault_client.on_connect = on_connect
mqtt_fault_client.on_message = on_disconnect
mqtt_fault_client.on_publish = on_publish
mqtt_fault_client.on_disconnect=on_disconnect
mqtt_fault_client.username_pw_set("mqttuser","mqttpassword")
mqtt_fault_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)

def get_device_status(section):
    #query="SELECT total_time FROM section1 WHERE (device = 'fan') ORDER BY time desc"
    #print("inside get_devicebefore querey")
    query="SELECT * FROM device_status where (Section = '"+section+"') order by time desc limit 1"
    loginRecords = clientinflux.query(query)
    a = list(loginRecords.get_points())
    #return a[0]["status_Read"]
    if len(a)==0:
        return False
    if a[0]["status_Read"]=='ONLINE':
        return True
    return False
def convert_time_1(v):
    hh,mm=0,0
    hh=int(v/3600)
    v=v%3600
    mm=int(v/60)
    v=v%60
    ss=int(v/60)
    s=str(hh)+":"+str(mm)+":"+str(v)
    return s
def get_current_time():
    st=time.asctime(time.localtime(time.time()))
    year=st[-4:-1]+st[-1]
    month=st[4:7]
    day=st[0:3]
    dd=int(st[8:10])
    hh=st[11:13]
    mm=st[14:16]
    ss=st[17:19]
    current_time={'year':int(year),'month':month,'day':day,'dd':dd,'hh':hh,'mm':mm,'ss':ss}
    return current_time
#-----------------------------------------------------------------------------------
def switching_off_device(total_time,measure,device_name):
    mqtt_fault_client.username_pw_set("mqttuser","mqttpassword")
    mqtt_fault_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_fault_client.publish("cdac/iot/"+measure+"/"+device_name,0)
    #total_time=total_time
    #print("Uptime got")
    measurement = measure #"section1"
    timedata=get_current_time()
    #print("timedata calculated")
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    #print(type(uptime))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device_name,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "status" : "OFF",
              "uptime" : "NA",
              "downtime" : str(downtime),
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    clientinflux.write_points(data)
#-----------------------------------------------------------------------------------

 

# Print the time series query results

#print(type(loginRecords))
#print(loginRecords.get_points())
#a = list(loginRecords.get_points())
#print(a)
#print(type(a))
#print(a[0]["status_Read"])


