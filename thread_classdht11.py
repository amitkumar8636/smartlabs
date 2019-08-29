import Adafruit_DHT
import threading
from influxdb import InfluxDBClient
import time

# Configure InfluxDB connection variables
host = "127.0.0.1" # My Ubuntu NUC
port = 8086 # default port
user = "rpi-3" # the user/password created for the pi, with write access
password = "rpi-3" 
dbname = "iotlab" # the database we created earlier
interval = 5 # Sample period in seconds
# Create the InfluxDB client object
client = InfluxDBClient(host, port, user, password, dbname)
# Enter the sensor details
sensor = Adafruit_DHT.DHT11
sensor_gpio = 4
# think of measurement as a SQL table, it's not...but...
measurement = "sensor_data"
# location will be used as a grouping tag later
location = "IOTLAB"


class thread_for_dht11 (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        global sec3_fan_time
        sec3_fan_time=0
    def run(self):
        try:
            while True:
            # Read the sensor using the configured driver and gpio
                humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_gpio)
                iso = time.ctime()
                data = [
                {
                  "measurement": measurement,
                      "tags": {
                          "lab": location,
                      },
                      "time": iso,
                      "fields": {
                          "temperature" : temperature,
                          "humidity": humidity
                      }
                  }
                ]
        # Send the JSON data to InfluxDB
                client.write_points(data)
        # Wait until it's time to query again...
                time.sleep(interval)
 
        except KeyboardInterrupt:
            pass
