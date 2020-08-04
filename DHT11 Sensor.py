
import RPi.GPIO  as GPIO
Import Adafruit_DHT
import time as t
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup (4,GPIO.OUT)
while True:
   Humidity,temperature = Adafruit_DHT.read_retry (11,4)
 print (‘Temp: (0:0.1F) C Humidity:(1:0.1F)%’,format(temperature,humidity))
