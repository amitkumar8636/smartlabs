import time
from devicefunctions import *
from variables_globals import logfile
global logfile
def my_switch(topic,message):
    if topic == 'cdac/iot/section1/projector':
        if message=='OFF':
            print("Projector being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec1_projector()
            logfile.write("Projector being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Projector being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec1_projector()
            logfile.write("Projector being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section1/light1':
        if message=='OFF':
            print("Sec_1 light1 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec1_light1()
            logfile.write("Sec_1 light1 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_1 light1 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec1_light1()
            logfile.write("Sec_1 light1 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section1/light2':
        if message=='OFF':
            print("Sec_1 light2 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec1_light2()
            logfile.write("Sec_2 light1 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_1 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec1_light2()
            logfile.write("Sec_1 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section1/fan':
        if message=='OFF':
            print("Sec_1 fan being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec1_fan()
            logfile.write("Sec_1 fan being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_1 fan being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec1_fan()
            logfile.write("Sec_1 fan being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section1/ac':
        if message=='OFF':
            print("Sec_1 AC being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec1_ac()
            logfile.write("Sec_1 AC being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_1 AC being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec1_ac()
            logfile.write("Sec_1 AC being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section1/pir':
        if message=='OFF':
            switch_off_sec1_pir()
        else:
            switch_on_sec1_pir()
    elif topic == 'cdac/iot/section2/light1':
        if message=='OFF':
            print("Sec_2 light1 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec2_light1()
            logfile.write("Sec_2 light1 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_2 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec2_light1()
            logfile.write("Sec_2 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section2/light2':
        if message=='OFF':
            print("Sec_2 light2 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec2_light2()
            logfile.write("Sec_2 light2 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_2 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec2_light2()
            logfile.write("Sec_2 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section2/fan':
        if message=='OFF':
            print("Sec_2 fan being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec2_fan()
            logfile.write("Sec_2 fan being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_2 fan being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec2_fan()
            logfile.write("Sec_2 fan being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section2/pir':
        if message=='OFF':
            switch_off_sec2_pir()
        else:
            switch_on_sec2_pir()
    elif topic == 'cdac/iot/section3/light1':
        if message=='OFF':
            print("Sec_3 light1 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec3_light1()
            logfile.write("Sec_3 light1 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_3 light1 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec3_light1()
            logfile.write("Sec_3 light1 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section3/light2':
        if message=='OFF':
            print("Sec_3 light2 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec3_light2()
            logfile.write("Sec_3 light2 being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_3 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec3_light2()
            logfile.write("Sec_3 light2 being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section3/fan':
        if message=='OFF':
            print("Sec_3 fan being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_off_sec3_fan()
            logfile.write("Sec_3 fan being turned OFF Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
        else:
            print("Sec_3 fan being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
            switch_on_sec3_fan()
            logfile.write("Sec_3 fan being turned ON Manually"+" at "+str(time.asctime(time.localtime(time.time())))+"\n")
    elif topic == 'cdac/iot/section3/pir':
        if message=='OFF':
            switch_off_sec3_pir()
        else:
            switch_on_sec3_pir()


#mqtt2device_client = mqtt.Client()
#mqtt2device_client.on_connect = on_connect
#mqtt2device_client.on_message = on_message


#client.connect("127.0.0.1", 1883, 60)

