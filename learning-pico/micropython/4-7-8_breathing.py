# https://www.webmd.com/balance/what-to-know-4-7-8-breathing

from machine import Pin
import time

red = Pin(15, Pin.OUT) # Breathe out
green = Pin(16, Pin.OUT) # Hold
blue = Pin(14, Pin.OUT) # Breathe in

led_list = [red, green, blue]

def startup_test():
    [led.on() for led in led_list] # turn on all leds
    time.sleep(0.5)
    [led.off() for led in led_list] # turn off all leds
    time.sleep(0.5)

def breathe(led, timing): # 4 for in, 8 for out
    led.on()
    time.sleep(timing)
    led.off()

startup_test() # check all leds turn on; circuit is correct

while True:
    try:
        # BREATH CYCLE
        breathe(red, 4) # breathe in for 4 seconds
        breathe(green, 7) # hold for 7 seconds
        breathe(blue, 8) # breathe out for 8 seconds
        
    except KeyboardInterrupt: # obviously only works when connected to computer
        print("breaking")
        break
    except: # if any errors arise, turn off
        [led.off() for led in led_list]
[led.off() for led in led_list]
