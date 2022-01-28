import time

import Adafruit_DHT as dht

DHT_SENSOR = dht.DHT11
DHT_PIN = 4

while True:
    humidity, temperature = dht.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(
            "Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
        print("raw data: Temp; " + temperature +"C Humidity; " + humidity)
    else:
        print("Sensor failure. Check wiring.")
    time.sleep(15)
