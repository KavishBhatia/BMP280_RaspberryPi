import RPi.GPIO as GPIO
import BMP280
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
    #making object of class BMP280
    b = BMP280.BMP280()
    #calling initializing function
    b.init()
    #get temperature
    cTemp = b.temperature()
    #get pressure
    pres = b.pressure()
    #print values
    print "Temperature in Celsius : %.2f C" %cTemp
    print "Pressure : %.2f hPa " %pres
    #sleep of 1s
    time.sleep(1)
