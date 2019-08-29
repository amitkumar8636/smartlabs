
import time

i=0
logFile = open("logfile.log","a")
while i<10:
    print(logFile.write("123456\t"+str(time.asctime(time.localtime(time.time())))+"\n"))
    i=i+1
    time.sleep(1)
logFile.close()
