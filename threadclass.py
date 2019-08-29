import threading
import time
import datetime

import paho.mqtt.client as mqtt
mqtt_host="127.0.0.1"
mqtt_port=1883
mqtt_timeinterval=60

def on_connect(client, userdata, flags, rc):
    return True
def on_message(client, userdata, flags, rc):
    return True

mqttthread = mqtt.Client()
mqttthread.on_connect = on_connect
mqttthread.on_message = on_message
mqttthread.username_pw_set("mqttuser","mqttpassword")
mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)

from variables_globals import *
from db_influx import *
global logfile
global sec1_pir_time
global sec2_pir_time
global sec1_device_time
global sec2_device_time
global sec3_device_time

def convert_time(v):
    hh,mm=0,0
    hh=int(v/3600)
    v=v%3600
    mm=int(v/60)
    v=v%60
    ss=int(v/60)
    s=str(hh)+":"+str(mm)+":"+str(v)
    return s
#     return datetime.timedelta(seconds=v)
#++++++++++++++++++++++++++++++++++SECTION 1 THREADS STARTS+++++++++++++++++++++++++++++++++++++++++++++++++

#--------------------------------------------------------------------------
class thread_section1_projector (threading.Thread):
    def __init__(self, name='thread_section1_projector'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec1_projector_time
        sec1_projector_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section1")==False:
                #print("Inside projector thread device status",get_device_status("section1"))
                switching_off_device(sec1_projector_time,"section1","projector_device")
                logfile.write("Sec_1 Projector being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec1_projector_time += 1
                print ("sec1_projector_time ",sec1_projector_time)
            self._stopevent.wait(self._sleepperiod)
        sec1_projector_time=convert_time(sec1_projector_time)
        sec1_projector_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
class thread_section1_light1 (threading.Thread):
    def __init__(self, name='thread_section1_light1'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec1_light1_time
        sec1_light1_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section1")==False:
                print("Sec_1 light1 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec1_light1_time,"section1","light1_device")
                logfile.write("Sec_1 light1 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec1_light1_time += 1
                print ("sec1_light1_time ",sec1_light1_time)
            self._stopevent.wait(self._sleepperiod)
        sec1_light1_time=convert_time(sec1_light1_time)
        sec1_light1_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
class thread_section1_light2 (threading.Thread):
    def __init__(self, name='thread_section1_light2'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec1_light2_time
        sec1_light2_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section1")==False:
                print("Sec_1 light2 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec1_light2_time,"section1","light2_device")
                logfile.write("Sec_1 light2 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec1_light2_time += 1
                print ("sec1_light2_time ",sec1_light2_time)
            self._stopevent.wait(self._sleepperiod)
        sec1_light2_time=convert_time(sec1_light2_time)
        sec1_light2_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
class thread_section1_fan (threading.Thread):
    def __init__(self, name='thread_section1_fan'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec1_fan_time
        sec1_fan_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section1")==False:
                print("Sec_1 fan being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec1_fan_time,"section1","fan_device")
                logfile.write("Sec_1 fan being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec1_fan_time += 1
                print ("sec1_fan_time ",sec1_fan_time)
            self._stopevent.wait(self._sleepperiod)
        sec1_fan_time=convert_time(sec1_fan_time)
        sec1_fan_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
class thread_section1_ac (threading.Thread):
    def __init__(self, name='thread_section1_ac'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec1_ac_time
        sec1_ac_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section1")==False:
                print("Sec_2 ac being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec1_ac_time,"section1","ac_device")
                logfile.write("Sec_2 ac being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec1_ac_time += 1
                print ("sec1_ac_time ",sec1_ac_time)
            self._stopevent.wait(self._sleepperiod)
        sec1_ac_time=convert_time(sec1_ac_time)
        sec1_ac_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------


#++++++++++++++++++++++++++++++++++SECTION 1 THREADS ENDS+++++++++++++++++++++++++++++++++++++++++++++++++


#++++++++++++++++++++++++++++++++++SECTION 2 THREADS STARTS+++++++++++++++++++++++++++++++++++++++++++++++++
#--------------------------------------------------------------------------
class thread_section2_light1 (threading.Thread):
    def __init__(self, name='thread_section2_light1'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec2_light1_time
        sec2_light1_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section2")==False:
                print("Sec_2 light1 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec2_light1_time,"section2","light1_device")
                logfile.write("Sec_2 light1 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
               sec2_light1_time += 1
               print ("sec2_light1_time ",sec2_light1_time)
            self._stopevent.wait(self._sleepperiod)
        sec2_light1_time=convert_time(sec2_light1_time)
        sec2_light1_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
class thread_section2_light2 (threading.Thread):
    def __init__(self, name='thread_section2_light2'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec2_light2_time
        sec2_light2_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section2")==False:
                print("Sec_2 light2 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec2_light2_time,"section2","light2_device")
                logfile.write("Sec_2 light2 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec2_light2_time += 1
                print ("sec2_light2_time ",sec2_light2_time)
            self._stopevent.wait(self._sleepperiod)
        sec2_light2_time=convert_time(sec2_light2_time)
        sec2_light2_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
class thread_section2_fan (threading.Thread):
    def __init__(self, name='thread_section2_fan'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec2_fan_time
        sec2_fan_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section2")==False:
                print("Sec_2 fan being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec2_fan_time,"section2","fan_device")
                logfile.write("Sec_2 fan being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec2_fan_time += 1
                print ("sec2_fan_time ",sec2_fan_time)
            self._stopevent.wait(self._sleepperiod)
        sec2_fan_time=convert_time(sec2_fan_time)
        sec2_fan_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#++++++++++++++++++++++++++++++++++SECTION 2 THREADS ENDS+++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++SECTION 3 THREADS STARTS+++++++++++++++++++++++++++++++++++++++++++++++++
#--------------------------------------------------------------------------
class thread_section3_light1 (threading.Thread):
    def __init__(self, name='thread_section3_light1'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec3_light1_time
        sec3_light1_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section3")==False:
                print("Sec_3 light1 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec3_light1_time,"section3","light1_device")
                logfile.write("Sec_3 light1 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec3_light1_time += 1
                print ("sec3_light1_time ",sec3_light1_time)
            self._stopevent.wait(self._sleepperiod)
        sec3_light1_time=convert_time(sec3_light1_time)
        sec3_light1_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------
class thread_section3_light2 (threading.Thread):
    def __init__(self, name='thread_section3_light2'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec3_light2_time
        sec3_light2_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section3")==False:
                print("Sec_3 light2 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec3_light2_time,"section3","light2_device")
                logfile.write("Sec_3 light2 being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec3_light2_time += 1
                print ("sec3_light2_time ",sec3_light2_time)
            self._stopevent.wait(self._sleepperiod)
        sec3_light2_time=convert_time(sec3_light2_time)
        sec3_light2_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
class thread_section3_fan (threading.Thread):
    def __init__(self, name='thread_section3_fan'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec3_fan_time
        sec3_fan_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section3")==False:
                print("Sec_3 fan being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                switching_off_device(sec3_fan_time,"section3","fan_device")
                logfile.write("Sec_3 fan being turned OFF: Device ERROR!!"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
            else:
                sec3_fan_time += 1
                print ("sec3_fan_time ",sec3_fan_time)
            self._stopevent.wait(self._sleepperiod)
        sec3_fan_time=convert_time(sec3_fan_time)
        sec3_fan_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------

#++++++++++++++++++++++++++++++++++SECTION 3 THREADS Ends+++++++++++++++++++++++++++++++++++++++++++++++++


#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#--------------------------------------------------------------------------
class thread_section1_pir (threading.Thread):
    def __init__(self, name='thread_section1_pir'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec1_pir_time
        sec1_pir_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section1")==False:
                break
            sec1_pir_time += 1
            print ("sec1_pir_time ",sec1_pir_time)
            if sec1_pir_time>=10:
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/section1/pir","0")
                break
#            self._stopevent.wait(self._sleepperiod)
        sec1_pir_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#--------------------------------------------------------------------------
class thread_section2_pir (threading.Thread):
    def __init__(self, name='thread_section2_pir'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec2_pir_time
        sec2_pir_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section2")==False:
                break
            sec2_pir_time += 1
            print ("sec2_pir_time ",sec2_pir_time)
            if sec2_pir_time>=10:
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/section2/pir","0")
                break;
            self._stopevent.wait(self._sleepperiod)
        #del sec1_pir_time
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#--------------------------------------------------------------------------
class thread_section3_pir (threading.Thread):
    def __init__(self, name='thread_section3_pir'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 1.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec3_pir_time
        sec3_pir_time = 0
        while not self._stopevent.isSet(  ):
            if get_device_status("section3")==False:
                break
            sec3_pir_time += 1
            print ("sec3_pir_time ",sec3_pir_time)
            if sec3_pir_time>=10:
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/section3/pir","0")
            self._stopevent.wait(self._sleepperiod)
        #del sec1_pir_time
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

def device_thread(status,status_read,sec1_device_time,section):
    from influxdb import InfluxDBClient
    
    host = "127.0.0.1" # My Ubuntu NUC
    port = 8086 # default port
    user = "rpi-3" # the user/password created for the pi, with write access
    password = "rpi-3" 
    dbname = "iotlab" # the database we created earlier
    interval = 5 # Sample period in seconds
    clientdbflux = InfluxDBClient(host, port, user, password, dbname)
    measurement = "device_status"
    
    #start_clock_sec1_device()
    data = [
    {
      "measurement": measurement,
          "tags": {
              "device": 'NodeMcu',
              "lab" : 'IOT',
              "Section": section,
          },
          "fields": {
              "status" : status,
              "status_Read" : status_read,
              "running_time": sec1_device_time,
          },
          "value": {
              "status_code" : 1,
          },
      }
    ]
    clientdbflux.write_points(data)


#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((
#--------------------------------------------------------------------------
class thread_section1_device (threading.Thread):
    def __init__(self, name='thread_section1_device'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 3.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec1_device_time
        sec1_device_time = 0
        while not self._stopevent.isSet(  ):
            sec1_device_time += 1
            print ("sec1_nodemcu_time ",sec1_device_time)
            self._stopevent.wait(self._sleepperiod)
            if (True):
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/sec2_device_toapp","1")
                device_thread(1,"ONLINE",sec1_device_time,"section1")
            if (sec1_device_time>5):
                device_thread(0,"OFFLINE",sec1_device_time,"section1")
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/sec1_device_toapp","0")
                print("Sec_1 is OFFLINE NOW!!")
                #logfile.write("Sec_1 went OFFLINE"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
                #timeout=None
                #self._stopevent.set(  )
                #threading.Thread.join(self)
        sec1_device_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
class thread_section2_device (threading.Thread):
    def __init__(self, name='thread_section2_device'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 3.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec2_device_time
        sec2_device_time = 0
        while not self._stopevent.isSet(  ):
            sec2_device_time += 1
            print ("sec2_nodemcu_time ",sec2_device_time)
            self._stopevent.wait(self._sleepperiod)
            if (True):
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/sec2_device_toapp","1")
                device_thread(1,"ONLINE",sec2_device_time,"section2")
            if (sec2_device_time>5):
                device_thread(0,"OFFLINE",sec2_device_time,"section2")
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/sec2_device_toapp","0")
                print("Sec_2 is OFFLINE NOW!!")
                logfile.write("Sec_2 went OFFLINE"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
                #timeout=None
                #self._stopevent.set(  )
                #threading.Thread.join(self)
        sec2_device_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
class thread_section3_device (threading.Thread):
    def __init__(self, name='thread_section3_device'):
        self._stopevent = threading.Event(  )
        self._sleepperiod = 3.0
        threading.Thread.__init__(self, name=name)
    def run(self):
        global sec3_device_time
        sec3_device_time = 0
        while not self._stopevent.isSet(  ):
            sec3_device_time += 1
            print ("sec3_nodemcu_time ",sec3_device_time)
            self._stopevent.wait(self._sleepperiod)
            if (True):
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/sec3_device_toapp","1")
                device_thread(1,"ONLINE",sec3_device_time,"section3")
            if (sec3_device_time>5):
                device_thread(0,"OFFLINE",sec3_device_time,"section3")
                mqttthread.connect(mqtt_host, mqtt_port, mqtt_timeinterval)
                mqttthread.publish("cdac/iot/sec3_device_toapp","0")
                print("Sec_3 is OFFLINE NOW!!")
                logfile.write("Sec_3 went OFFLINE"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
                break
                #timeout=None
                #self._stopevent.set(  )
                #threading.Thread.join(self)
        sec3_device_time=0
    def join(self, timeout=None):
        """ Stop the thread. """
        self._stopevent.set(  )
        threading.Thread.join(self, timeout)
#--------------------------------------------------------------------------
#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))



