import threading
import threadclass as t
import time
global sec1_pir_thread
global sec2_pir_thread
global sec3_pir_thread

global sec1_projector_thread
global sec1_light1_thread
global sec1_light2_thread
global sec1_fan_thread
global sec1_ac_thread

global sec2_light1_thread
global sec2_light2_thread
global sec2_fan_thread

global sec3_light1_thread
global sec3_light2_thread
global sec3_fan_thread

global sec1_device_thread
global sec2_device_thread
global sec3_device_thread

#==========================================================================================================

global sec1_projector_time

#--------------section_projector-------------------start-----------------------------------
sec1_projector_thread=t.thread_section1_projector(33)
#sec1_projector_thread.start()
#sec1_projector_thread.join()
#--------------section_projector-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section1_projector():
    global sec1_projector_thread
    if sec1_projector_thread.isAlive():
        sec1_projector_thread.join()
    return t.thread_section1_projector(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section1_projector--------------------------------------
def start_clock_sec1_projector():
    global sec1_projector_thread
    sec1_projector_thread=get_thread_section1_projector()
    sec1_projector_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec1_projector_uptime():
    global sec1_projector_thread
    v=t.sec1_projector_time
    sec1_projector_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================



#==========================================================================================================

global sec1_light1_time

#--------------section_light1-------------------start-----------------------------------
sec1_light1_thread=t.thread_section1_light1(33)
#sec1_light1_thread.start()
#sec1_light1_thread.join()
#--------------section_light1-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section1_light1():
    global sec1_light1_thread
    if sec1_light1_thread.isAlive():
        sec1_light1_thread.join()
    return t.thread_section1_light1(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section1_light1--------------------------------------
def start_clock_sec1_light1():
    global sec1_light1_thread
    sec1_light1_thread=get_thread_section1_light1()
    sec1_light1_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec1_light1_uptime():
    global sec1_light1_thread
    v=t.sec1_light1_time
    sec1_light1_thread.join()
    return v

#---------------------------------------------------------------------------------------


#==========================================================================================================

global sec1_light2_time

#--------------section_light2-------------------start-----------------------------------
sec1_light2_thread=t.thread_section1_light2(33)
#sec1_light2_thread.start()
#sec1_light2_thread.join()
#--------------section_light2-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section1_light2():
    global sec1_light2_thread
    if sec1_light2_thread.isAlive():
        sec1_light2_thread.join()
    return t.thread_section1_light2(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section1_light2--------------------------------------
def start_clock_sec1_light2():
    global sec1_light2_thread
    sec1_light2_thread=get_thread_section1_light2()
    sec1_light2_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec1_light2_uptime():
    global sec1_light2_thread
    v=t.sec1_light2_time
    sec1_light2_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================


#==========================================================================================================


global sec1_fan_time

#--------------section_fan-------------------start-----------------------------------
sec1_fan_thread=t.thread_section1_fan(33)
#sec1_fan_thread.start()
#sec1_fan_thread.join()
#--------------section_fan-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section1_fan():
    global sec1_fan_thread
    if sec1_fan_thread.isAlive():
        sec1_fan_thread.join()
    return t.thread_section1_fan(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section1_fan--------------------------------------
def start_clock_sec1_fan():
    global sec1_fan_thread
    sec1_fan_thread=get_thread_section1_fan()
    sec1_fan_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec1_fan_uptime():
    global sec1_fan_thread
    v=t.sec1_fan_time
    sec1_fan_thread.join()
    return v

#---------------------------------------------------------------------------------------
#==========================================================================================================


global sec1_ac_time

#--------------section_ac-------------------start-----------------------------------
sec1_ac_thread=t.thread_section1_ac(33)
#sec1_ac_thread.start()
#sec1_ac_thread.join()
#--------------section_ac-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section1_ac():
    global sec1_ac_thread
    if sec1_ac_thread.isAlive():
        sec1_ac_thread.join()
    return t.thread_section1_ac(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section1_ac--------------------------------------
def start_clock_sec1_ac():
    global sec1_ac_thread
    sec1_ac_thread=get_thread_section1_ac()
    sec1_ac_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec1_ac_uptime():
    global sec1_ac_thread
    v=t.sec1_ac_time
    sec1_ac_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================


#++++++++++++++++++++++++++++++++++++++++++++SECTION 1 ENDS HERE+++++++++++++++++++++++++++++++++++++++++++


#==========================================================================================================

global sec2_light1_time

#--------------section_light1-------------------start-----------------------------------
sec2_light1_thread=t.thread_section2_light1(33)
#sec2_light1_thread.start()
#sec2_light1_thread.join()
#--------------section_light1-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section2_light1():
    global sec2_light1_thread
    if sec2_light1_thread.isAlive():
        sec2_light1_thread.join()
    return t.thread_section2_light1(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section2_light1--------------------------------------
def start_clock_sec2_light1():
    global sec2_light1_thread
    sec2_light1_thread=get_thread_section2_light1()
    sec2_light1_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec2_light1_uptime():
    global sec2_light1_thread
    v=t.sec2_light1_time
    sec2_light1_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================


#==========================================================================================================

global sec2_light2_time

#--------------section_light2-------------------start-----------------------------------
sec2_light2_thread=t.thread_section2_light2(33)
#sec2_light2_thread.start()
#sec2_light2_thread.join()
#--------------section_light2-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section2_light2():
    global sec2_light2_thread
    if sec2_light2_thread.isAlive():
        sec2_light2_thread.join()
    return t.thread_section2_light2(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section2_light2--------------------------------------
def start_clock_sec2_light2():
    global sec2_light2_thread
    sec2_light2_thread=get_thread_section2_light2()
    sec2_light2_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec2_light2_uptime():
    global sec2_light2_thread
    v=t.sec2_light2_time
    sec2_light2_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================


#==========================================================================================================

global sec2_fan_time

#--------------section_fan-------------------start-----------------------------------
sec2_fan_thread=t.thread_section2_fan(33)
#sec2_fan_thread.start()
#sec2_fan_thread.join()
#--------------section_fan-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section2_fan():
    global sec2_fan_thread
    if sec2_fan_thread.isAlive():
        sec2_fan_thread.join()
    return t.thread_section2_fan(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section2_fan--------------------------------------
def start_clock_sec2_fan():
    global sec2_fan_thread
    sec2_fan_thread=get_thread_section2_fan()
    sec2_fan_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec2_fan_uptime():
    global sec2_fan_thread
    v=t.sec2_fan_time
    sec2_fan_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================

#++++++++++++++++++++++++++++++++++++++++++++SECTION 2 ENDS HERE+++++++++++++++++++++++++++++++++++++++++++

#==========================================================================================================

global sec3_light1_time

#--------------section_light1-------------------start-----------------------------------
sec3_light1_thread=t.thread_section3_light1(33)
#sec3_light1_thread.start()
#sec3_light1_thread.join()
#--------------section_light1-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section3_light1():
    global sec3_light1_thread
    if sec3_light1_thread.isAlive():
        sec3_light1_thread.join()
    return t.thread_section3_light1(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section3_light1--------------------------------------
def start_clock_sec3_light1():
    global sec3_light1_thread
    sec3_light1_thread=get_thread_section3_light1()
    sec3_light1_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec3_light1_uptime():
    global sec3_light1_thread
    v=t.sec3_light1_time
    sec3_light1_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================


#==========================================================================================================

global sec3_light2_time

#--------------section_light2-------------------start-----------------------------------
sec3_light2_thread=t.thread_section3_light2(33)
#sec3_light2_thread.start()
#sec3_light2_thread.join()
#--------------section_light2-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section3_light2():
    global sec3_light2_thread
    if sec3_light2_thread.isAlive():
        sec3_light2_thread.join()
    return t.thread_section3_light2(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section3_light2--------------------------------------
def start_clock_sec3_light2():
    global sec3_light2_thread
    sec3_light2_thread=get_thread_section3_light2()
    sec3_light2_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec3_light2_uptime():
    global sec3_light2_thread
    v=t.sec3_light2_time
    sec3_light2_thread.join()
    return v

#---------------------------------------------------------------------------------------
#==========================================================================================================


#==========================================================================================================

global sec3_fan_time

#--------------section_fan-------------------start-----------------------------------
sec3_fan_thread=t.thread_section3_fan(33)
#sec3_fan_thread.start()
#sec3_fan_thread.join()
#--------------section_fan-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section3_fan():
    global sec3_fan_thread
    if sec3_fan_thread.isAlive():
        sec3_fan_thread.join()
    return t.thread_section3_fan(33)
#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section3_fan--------------------------------------
def start_clock_sec3_fan():
    global sec3_fan_thread
    sec3_fan_thread=get_thread_section3_fan()
    sec3_fan_thread.start()
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec3_fan_uptime():
    global sec3_fan_thread
    v=t.sec3_fan_time
    sec3_fan_thread.join()
    return v

#---------------------------------------------------------------------------------------

#==========================================================================================================

#++++++++++++++++++++++++++++++++++++++++++++SECTION 3 ENDS HERE+++++++++++++++++++++++++++++++++++++++++++
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((

global sec1_pir_time

#--------------section_pir-------------------start-----------------------------------
sec1_pir_thread=t.thread_section1_pir(133)
#sec1_pir_thread.start()
#sec1_pir_thread.join()
#--------------section_pir-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section1_pir():
    global sec1_pir_thread
    if (sec1_pir_thread.isAlive()):
        sec1_pir_thread.join()
    return t.thread_section1_pir(133)

#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section1_pir--------------------------------------
def start_clock_sec1_pir():
    global sec1_pir_thread
    sec1_pir_thread=get_thread_section1_pir()
    #print("in start clock",sec1_pir_thread.isAlive())
    #print("staring in 2 sec")
    sec1_pir_thread.start()
    
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec1_pir_uptime():
    global sec1_pir_thread
    v=t.sec1_pir_time
    #print("swtiching ooff ",sec1_pir_thread.isAlive())
    sec1_pir_thread.join()
    return v

#---------------------------------------------------------------------------------------


#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((

global sec2_pir_time

#--------------section_pir-------------------start-----------------------------------
sec2_pir_thread=t.thread_section2_pir(233)
#sec2_pir_thread.start()
#sec2_pir_thread.join()
#--------------section_pir-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section2_pir():
    global sec2_pir_thread
    if (sec2_pir_thread.isAlive()):
        sec2_pir_thread.join()
    return t.thread_section2_pir(233)

#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section2_pir--------------------------------------
def start_clock_sec2_pir():
    global sec2_pir_thread
    sec2_pir_thread=get_thread_section2_pir()
    #print("in start clock",sec2_pir_thread.isAlive())
    #print("staring in 2 sec")
    sec2_pir_thread.start()
    
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec2_pir_uptime():
    global sec2_pir_thread
    v=t.sec2_pir_time
    t.sec2_pir_time=0
    #print("swtiching ooff ",sec2_pir_thread.isAlive())
    sec2_pir_thread.join()
    return v

#---------------------------------------------------------------------------------------


#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((

global sec3_pir_time

#--------------section_pir-------------------start-----------------------------------
sec3_pir_thread=t.thread_section3_pir(333)
#sec3_pir_thread.start()
#sec3_pir_thread.join()
#--------------section_pir-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section3_pir():
    global sec3_pir_thread
    if (sec3_pir_thread.isAlive()):
        sec3_pir_thread.join()
    return t.thread_section3_pir(333)

#---------------get_the_thread----------------------------------------------------------

#--------------start the clock for section3_pir--------------------------------------
def start_clock_sec3_pir():
    global sec3_pir_thread
    sec3_pir_thread=get_thread_section3_pir()
    #print("in start clock",sec3_pir_thread.isAlive())
    #print("staring in 2 sec")
    sec3_pir_thread.start()
    
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec3_pir_uptime():
    global sec3_pir_thread
    v=t.sec3_pir_time
    t.sec3_pir_time=0
    #print("swtiching ooff ",sec3_pir_thread.isAlive())
    sec3_pir_thread.join()
    return v

#---------------------------------------------------------------------------------------


#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((

global sec1_device_time

#--------------section_device-------------------start-----------------------------------
sec1_device_thread=t.thread_section1_device(911)
#sec1_device_thread.start()
#sec1_device_thread.join()
#--------------section_device-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section1_device():
    global sec1_device_thread
    if (sec1_device_thread.isAlive()):
        sec1_device_thread.join()
    return t.thread_section1_device(911)

#---------------get_the_thread----------------------------------------------------------

#--------------start the clock forsection3_device--------------------------------------
def start_clock_sec1_device():
    global sec1_device_thread
    sec1_device_thread=get_thread_section1_device()
    #print("in start clock",sec1_device_thread.isAlive())
    #print("staring in 2 sec")
    sec1_device_thread.start()
    
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec1_device_uptime():
    global sec1_device_thread
    v=t.sec1_device_time
    t.sec1_device_time=0
    #print("swtiching ooff ",sec1_device_thread.isAlive())
    sec1_device_thread.join()
    return v

#---------------------------------------------------------------------------------------


#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((

global sec2_device_time

#--------------section_device-------------------start-----------------------------------
sec2_device_thread=t.thread_section2_device(911)
#sec2_device_thread.start()
#sec2_device_thread.join()
#--------------section_device-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section2_device():
    global sec2_device_thread
    if (sec2_device_thread.isAlive()):
        sec2_device_thread.join()
    return t.thread_section2_device(911)

#---------------get_the_thread----------------------------------------------------------

#--------------start the clock forsection3_device--------------------------------------
def start_clock_sec2_device():
    global sec2_device_thread
    sec2_device_thread=get_thread_section2_device()
    #print("in start clock",sec2_device_thread.isAlive())
    #print("staring in 2 sec")
    sec2_device_thread.start()
    
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec2_device_uptime():
    global sec2_device_thread
    v=t.sec2_device_time
    t.sec2_device_time=0
    #print("swtiching ooff ",sec2_device_thread.isAlive())
    sec2_device_thread.join()
    return v

#---------------------------------------------------------------------------------------


#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((

global sec3_device_time

#--------------section_device-------------------start-----------------------------------
sec3_device_thread=t.thread_section3_device(911)
#sec3_device_thread.start()
#sec3_device_thread.join()
#--------------section_device-------------------end-------------------------------------

#---------------get_the_thread----------------------------------------------------------
def get_thread_section3_device():
    global sec3_device_thread
    if (sec3_device_thread.isAlive()):
        sec3_device_thread.join()
    return t.thread_section3_device(911)

#---------------get_the_thread----------------------------------------------------------

#--------------start the clock forsection3_device--------------------------------------
def start_clock_sec3_device():
    global sec3_device_thread
    sec3_device_thread=get_thread_section3_device()
    #print("in start clock",sec3_device_thread.isAlive())
    #print("staring in 2 sec")
    sec3_device_thread.start()
    
#---------------------------------------------------------------------------------------

#-------------stop the clock and get the value------------------------------------------
def get_sec3_device_uptime():
    global sec3_device_thread
    v=t.sec3_device_time
    t.sec3_device_time=0
    #print("swtiching ooff ",sec3_device_thread.isAlive())
    sec3_device_thread.join()
    return v

#---------------------------------------------------------------------------------------


#))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))


#start_clock_sec1_light1()
#time.sleep(3)
#start_clock_sec1_light2()
#time.sleep(7)
#print("total time 1111 :",get_sec1_light1_uptime())
#print("total time 1111 :",get_sec1_light2_uptime())





