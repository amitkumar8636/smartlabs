import time
import sys
import datetime
import threadclass as p
import paho.mqtt.client as mqtt
from function import *
from timeduration import *
from influxdb import InfluxDBClient
from variables_globals import *

# Configure InfluxDB connection variables
host = "127.0.0.1" 
port = 8086 # default port
user = "rpi-3" # the user/password created for the pi, with write access
password = "rpi-3" 
dbname = "iotlab" # DATABASE NAME 
interval = 5 # Sample period in seconds

# Create the InfluxDB client object
client = InfluxDBClient(host, port, user, password, dbname)

mqtt_host="127.0.0.1"
mqtt_port=1883
mqtt_timeinterval=60
#________mqtt AREA________________________________
def on_connect(client, userdata, flags, rc):
    print("I am conneted Sir")
def on_publish(client,userdata,result):
    print("published succesfful from device fucnction")
def on_disconnect(client,userdata,rc):
    print("I am disconned from devicefunction")

mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.on_disconnect=on_disconnect
mqtt_client.username_pw_set("mqttuser","mqttpassword")
mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
#__________________________________________________



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

#++++++++++++++++++++++++++++++++++SECTION 1 STARTS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-----------------------------------------------------------------------------------
def switch_off_sec1_projector():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/projector_device",0)
    uptime=get_sec1_projector_uptime()
    #print("Uptime got")
    device="projector"
    measurement = "iot"
    #print("Before timedata")
    timedata=get_current_time()
    #print("timedata calculated")
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    #print(type(uptime))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "status" : "OFF",
              "section": "section1",
              "uptime" : "NA",
              "downtime" : str(downtime),
          },
          "fields": {
              "total_time" : uptime,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec1_projector():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/projector_device",1)
    start_clock_sec1_projector() #starting the clock
    device="projector_device"
    measurement = "iot"
    #total_time=datetime.timedelta(seconds=0)
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_off_sec1_light1():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/light1_device",0)
    total_time=get_sec1_light1_uptime()
    device="light1_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec1_light1():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/light1_device",1)
    start_clock_sec1_light1() #starting the clock
    device="light1_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_off_sec1_light2():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/light2_device",0)
    total_time=get_sec1_light2_uptime()
    device="light2_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec1_light2():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/light2_device",1)
    start_clock_sec1_light2() #starting the clock
    device="light2_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_off_sec1_fan():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/fan_device",0)
    total_time=get_sec1_fan_uptime()
    device="fan_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec1_fan():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/fan_device",1)
    start_clock_sec1_fan() #starting the clock
    device="fan_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
def switch_off_sec1_ac():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/ac_device",0)
    total_time=get_sec1_ac_uptime()
    device="ac_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec1_ac():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/ac_device",1)
    start_clock_sec1_ac() #starting the clock
    device="ac_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section1",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------
#++++++++++++++++++++++++++++++++++SECTION 1 ENDS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#++++++++++++++++++++++++++++++++++SECTION 2 STARTS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-----------------------------------------------------------------------------------
def switch_off_sec2_light1():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section2/light1_device",0)
    total_time=get_sec2_light1_uptime()
    device="light1_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section2",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec2_light1():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section2/light1_device",1)
    start_clock_sec2_light1() #starting the clock
    device="light1_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section2",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_off_sec2_light2():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section2/light2_device",0)
    total_time=get_sec2_light2_uptime()
    device="light2_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section2",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec2_light2():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section2/light2_device",1)
    start_clock_sec2_light2() #starting the clock
    device="light2_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section2",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_off_sec2_fan():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section2/fan_device",0)
    total_time=get_sec2_fan_uptime()
    device="fan_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section2",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec2_fan():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section2/fan_device",1)
    start_clock_sec2_fan() #starting the clock
    device="fan_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section2",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------
#++++++++++++++++++++++++++++++++++SECTION 2 ENDS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#++++++++++++++++++++++++++++++++++SECTION 3 STARTS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#-----------------------------------------------------------------------------------
def switch_off_sec3_light1():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section3/light1_device",0)
    total_time=get_sec3_light1_uptime()
    device="light1_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section3",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec3_light1():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section3/light1_device",1)
    start_clock_sec3_light1() #starting the clock
    device="light1_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section3",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_off_sec3_light2():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section3/light2_device",0)
    total_time=get_sec3_light2_uptime()
    device="light2_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section3",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec3_light2():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section3/light2_device",1)
    start_clock_sec3_light2() #starting the clock
    device="light2_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section3",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_off_sec3_fan():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section3/fan_device",0)
    total_time=get_sec3_fan_uptime()
    device="fan_device"
    measurement = "iot"
    timedata=get_current_time()
    downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : "NA",
              "downtime" : str(downtime),
              "status" : "OFF",
              "section": "section3",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 0,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
def switch_on_sec3_fan():
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section3/fan_device",1)
    start_clock_sec3_fan() #starting the clock
    device="fan_device"
    measurement = "iot"
    total_time=0
    timedata=get_current_time()
    uptime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": device,
              "year" : timedata["year"],
              "month": timedata["month"],
              "day" : timedata["day"],
              "date" : timedata["dd"],
              "uptime" : str(uptime),
              "downtime" : "NA",
              "status" : "ON",
              "section": "section3",
          },
          "fields": {
              "total_time" : total_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    client.write_points(data)
#-----------------------------------------------------------------------------------
#++++++++++++++++++++++++++++++++++SECTION 1 ENDS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
def switch_off_sec1_pir():
    #global section1_pir_clock_time
    #mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    #mqtt_client.publish("cdac/iot/section3/fan_device",0)
    #section1_pir_clock_time=get_sec1_pir_uptime()
    #device="fan"
    return get_sec1_pir_uptime()
    #measurement = "section3"
    #timedata=get_current_time()
    #downtime=str(timedata["hh"])+":"+str(timedata["mm"]+":"+str(timedata["ss"]))
def switch_on_sec1_pir():
    #mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    #mqtt_client.publish("cdac/iot/section3/fan_device",1)
    start_clock_sec1_pir() #starting the clock
    #total_time=0
    #timedata=get_current_time()




#)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
def switch_off_sec2_pir():
    return get_sec2_pir_uptime()
def switch_on_sec2_pir():
    start_clock_sec2_pir() #starting the clock
#)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
def switch_off_sec3_pir():
    return get_sec3_pir_uptime()
def switch_on_sec3_pir():
    start_clock_sec3_pir() #starting the clock
#)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))


#****************************************************************************
def switch_on_section1():
    print("No_Motion Switching OFF Sec_1"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/light1_device",1)
    mqtt_client.publish("cdac/iot/section1/light2_device",1)
    logfile.write("Motion activity Holding ON Sec_1 lights"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
def switch_off_section1():
    print("Motion activity Holding ON Sec_1 lights"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
    mqtt_client.publish("cdac/iot/section1/light1_device",0)
    mqtt_client.publish("cdac/iot/section1/light2_device",0)
    mqtt_client.publish("cdac/iot/section1/fan_device",0)
    mqtt_client.publish("cdac/iot/section1/ac_device",0)
    logfile.write("No_Motion Switched OFF Sec_1"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
#****************************************************************************



'''def database_flux_device():
    from influxdb import InfluxDBClient
    import threadclass as t
    mqtt_host="127.0.0.1"
    mqtt_port=1883
    mqtt_timeinterval=60
    pir_auto_off_time=10
    dbname="iotlab"
    user="rpi-3"
    password="rpi-3"
    clientdb = InfluxDBClient(host, port, user, password, dbname)
        data = [
        {
          "measurement": measurement,
              "tags": {
                  "device": 'NodeMcu',
                  "lab" : 'IOT',
                  "Section": 'sec_1',
              },
              "fields": {
                  "status" : 1,
                  "status_Read" : 'ONLINE',
              },
              "value": {
                  "status_code" : 1,
              },
          }
        ]
        clientdb.write_points(data)'''


#mqtt_client.publish("cdac","JIH")
#switch_on_sec1_projector()
#time.sleep(3)
#switch_off_sec1_projector()
mqtt_client.username_pw_set("mqttuser","mqttpassword")
mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
#mqtt_client.loop_forever()
