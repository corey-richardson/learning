from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP) #Create button object from Pin13 , Pin13 to input

delay = 0.05

class colours:
    GREEN = '\033[92m'
    RED = '\033[91m'

try:
    index = 0
    while True:
        if not button.value():
            led.value(1) #Set led turn on
            print(colours.GREEN + "On")
            time.sleep(delay)
        else:
            led.value(0) #Set led turn off
            print(colours.RED + "Off")
            time.sleep(delay)
    
except:
   print("nope")
