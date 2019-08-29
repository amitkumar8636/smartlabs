
import paho.mqtt.client as mqtt
from function import *
import threadclass as t
import devicefunctions
from timeduration import *
from db_influx import *
from variables_globals import *
mqtt_host="127.0.0.1"
mqtt_port=1883
mqtt_timeinterval=60
pir_auto_off_time=5
global operation_mode
operation_mode="automatic"
#operation modes=  manual, automatic , offline




def on_connect(client, userdata, flags, rc):
    print("MQTT Server Connected with result code "+str(rc)," at: ",time.asctime(time.localtime(time.time())))
    print("Loggin is Enabled!!")
    logfile.write(" MQTT Server Connected with result code "+str(rc)+" at: "+str(time.asctime(time.localtime(time.time())))+"\n")
    
    client.subscribe("cdac/iot/section1/pir")
    client.subscribe("cdac/iot/section1/projector")
    client.subscribe("cdac/iot/section1/light1")
    client.subscribe("cdac/iot/section1/light2")
    client.subscribe("cdac/iot/section1/fan")
    client.subscribe("cdac/iot/section1/ac")

    client.subscribe("cdac/iot/section2/pir")
    client.subscribe("cdac/iot/section2/light1")
    client.subscribe("cdac/iot/section2/light2")
    client.subscribe("cdac/iot/section2/fan")

    client.subscribe("cdac/iot/section3/pir")
    client.subscribe("cdac/iot/section3/light1")
    client.subscribe("cdac/iot/section3/light2")
    client.subscribe("cdac/iot/section3/fan")

    client.subscribe("cdac/iot/operation_mode")
    client.subscribe("cdac/iot/sec1_device")
    client.subscribe("cdac/iot/sec2_device")
    client.subscribe("cdac/iot/sec3_device")

def on_message(client, userdata, msg):
    topic_send= str(msg.topic)
    msg_send= str(msg.payload.decode())
    #print("substring",topic_send[9:17])
    if topic_send=='cdac/iot/operation_mode':
        global operation_mode
        operation_mode=msg_send
        print("Operation Mode changed to "+operation_mode," at "+time.asctime(time.localtime(time.time())))
        logfile.write("Operation Mode changed to "+operation_mode+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic_send=='cdac/iot/sec1_device' and msg_send=='1':
        print("Section_1 device is ONLINE at :",time.asctime(time.localtime(time.time())))
        start_clock_sec1_device()
        logfile.write("Section_1 device is ONLINE at :"+time.asctime(time.localtime(time.time()))+"\n")
    elif topic_send=='cdac/iot/sec2_device' and msg_send=='1':
        print("Section_2 device is ONLINE at :",time.asctime(time.localtime(time.time())))
        start_clock_sec2_device()
        logfile.write("Section_2 device is ONLINE at :"+time.asctime(time.localtime(time.time()))+"\n")
    elif topic_send=='cdac/iot/sec3_device' and msg_send=='1':
        print("Section_3 device is ONLINE at :",time.asctime(time.localtime(time.time())))
        start_clock_sec3_device()
        logfile.write("Section_3 device is ONLINE at :"+time.asctime(time.localtime(time.time()))+"\n")
    else:
        if topic_send[9:17]=='section1':
            #print(get_sec1_device_status("section1"))
            if(get_device_status("section1")):
                if topic_send=='cdac/iot/section1/fan' or topic_send=='cdac/iot/section1/ac' or topic_send=='cdac/iot/section1/projector':
                    my_switch(topic_send,msg_send)
                elif operation_mode=='automatic':
                    if topic_send=='cdac/iot/section1/pir':
                        print(t.sec1_pir_time)
                        if msg_send=='1':
                            if t.sec1_pir_time==0:
                                print("Light are OFF in Sec_1 Switching it on")
                                switch_on_section1()
                                #print("Switched ON success")
                                switch_on_sec1_pir() #start the clock
                                logfile.write("Lights are turned ON of Sec_1 in auto_mode"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                            else :
                                print("Already on resetting the clock")
                                switch_on_sec1_pir()#Resetting the clock
                                logfile.write("Motion while Lights in Sec_1 are already on"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                                #print("Success")
                        elif msg_send=='0':
                                if t.sec1_pir_time > pir_auto_off_time:
                                    print("Successfuly switched offf "+sec1_pir_status)
                                    logfile.write("No motion Lights in Sec_1 Switched OFF"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                                    t.sec1_pir_status='OFF'
                                    switch_off_sec1_pir()
                                    switch_off_section1()
                                    t.sec1_pir_time=0
                                elif t.sec1_pir_time==0 :
                                    print("Already off no action required")
                                    logfile.write("No motion Lights in Sec_1 are already Switched OFF"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                else :
                    my_switch(topic_send,msg_send)
            else:
                print("SEC_1 is OFFLINE!!!")
                device_mqtt_client.publish("cdac/iot/sec1_device_toapp","0")
                logfile.write("Sec_1 Device is OFFLINE"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        elif topic_send[9:17]=='section2':
            #print(get_sec2_device_status("section2"))
            if(get_device_status("section2")):
                if topic_send=='cdac/iot/section2/fan':
                    my_switch(topic_send,msg_send)
                elif operation_mode=='automatic':
                    if topic_send=='cdac/iot/section2/pir':
                        print(t.sec2_pir_time)
                        if msg_send=='1':
                            if t.sec2_pir_time==0:
                                print("Lights are OFF in Sec_2, Switching it on")
                                switch_on_section2()
                                #print("Switched ON success")
                                switch_on_sec2_pir() #start the clock
                                logfile.write("Lights are turned ON of Sec_2 in auto_mode"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                            else :
                                print("Already on resetting the clock")
                                switch_on_sec2_pir()#Resetting the clock
                                logfile.write("Motion while Lights in Sec_2 are already on"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                                #print("Success")
                        elif msg_send=='0':
                                if t.sec2_pir_time > pir_auto_off_time:
                                    print("Successfuly switched offf "+sec2_pir_status)
                                    logfile.write("No motion Lights in Sec_2 Switched OFF"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                                    t.sec2_pir_status='OFF'
                                    switch_off_sec2_pir()
                                    switch_off_section2()
                                    t.sec2_pir_time=0
                                elif t.sec2_pir_time==0 :
                                    print("Already off no action required")
                                    logfile.write("No motion Lights in Sec_2 are already Switched OFF"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                elif operation_mode=='manual' :
                    my_switch(topic_send,msg_send)
            else:
                print("Sec_2 is OFFLINE!!!")
                device_mqtt_client.publish("cdac/iot/sec2_device_toapp","0")
                logfile.write("Sec_2 Device is OFFLINE"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        elif topic_send[9:17]=='section3':
            #print(get_Sec3_device_status("section3"))
            if(get_device_status("section3")):
                if topic_send=='cdac/iot/section3/fan':
                    my_switch(topic_send,msg_send)
                elif operation_mode=='automatic':
                    if topic_send=='cdac/iot/section3/pir':
                        print(t.Sec3_pir_time)
                        if msg_send=='1':
                            if t.Sec3_pir_time==0:
                                print("Light are OFF in Sec_3 Switching it on")
                                switch_on_section3()
                                #print("Switched ON success")
                                switch_on_Sec3_pir() #start the clock
                                logfile.write("Lights are turned ON of Sec_3 in auto_mode"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                            else :
                                print("Already on resetting the clock")
                                switch_on_Sec3_pir()#Resetting the clock
                                logfile.write("Motion while Lights in Sec_3 are already on"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                                #print("Success")
                        elif msg_send=='0':
                                if t.Sec3_pir_time > pir_auto_off_time:
                                    print("Successfuly switched offf "+Sec3_pir_status)
                                    logfile.write("No motion Lights in Sec_3 Switched OFF"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                                    t.Sec3_pir_status='OFF'
                                    switch_off_Sec3_pir()
                                    switch_off_section3()
                                    t.Sec3_pir_time=0
                                elif t.Sec3_pir_time==0 :
                                    print("Already off no action required")
                                    logfile.write("No motion Lights in Sec_3 are already Switched OFF"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                else :
                    my_switch(topic_send,msg_send)
            else:
                print("Sec_3 is OFFLINE!!!")
                device_mqtt_client.publish("cdac/iot/sec3_device_toapp","0")
                logfile.write("Sec_3 Device is OFFLINE"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")


    #string_topic=str(msg.topic)
    #if string_topic == 'cdac/iot/section1/light1':
    #print(str(msg.payload.decode()))
    #print(int(msg.payload))
    #motion_hr_value=int(msg.payload)
    #motion_activity="HIGH" if motion_hr_value==1 else "LOW"

def on_publish(client,userdata,result):
    return true

def on_disconnect(client,userdata,result):
    logfile.write("MQTT server disconnect"+str(time.asctime(time.localtime(time.time())))+"\n")
    logfile.close()






time.sleep(1)
device_mqtt_client = mqtt.Client()
device_mqtt_client.on_connect = on_connect
device_mqtt_client.on_message = on_message
device_mqtt_client.on_publish = on_publish
device_mqtt_client.on_disconnect = on_disconnect
device_mqtt_client.username_pw_set("mqttuser","mqttpassword")
device_mqtt_client.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
time.sleep(0)
#device_mqtt_client.publish("cdac/iot/section1/projector","ON")

#thr_dht11=thread_classdht11.thread_for_dht11(1111)
#thr_dht11.start()

try:
    device_mqtt_client.loop_forever()
except KeyboardInterrupt:
    logfile.write("Keyboard Key pressed at "+str(time.asctime(time.localtime(time.time())))+"\n")
    logfile.close()
except Exception as e:
    logfile.write(str(e)+str(time.asctime(time.localtime(time.time())))+"\n")
    logfile.close()




# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#device_mqtt_client.loop_forever()
