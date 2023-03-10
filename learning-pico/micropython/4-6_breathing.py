# Blue light was too bright for night usage
# Simplified to only red-green leds
# Also green is now in and red is out to fit connotations

from machine import Pin
import time

TIMEOUT_MINUTES = 30 # Sleep mode, will auto turn off after n minutes
NO_TIMEOUT_FLAG = 0 # 0 for false (finite), 1 for true (infinite)

red = Pin(15, Pin.OUT) # Breathe out
green = Pin(14, Pin.OUT) # Breathe in

led_list = [red, green]

def main():
    try:
        startup_test() # check all leds turn on; circuit is correct
        for i in range(6 * TIMEOUT_MINUTES): # 6 breath cycles per minute * number of minutes to run
            breathe(green, 4) # breathe in for 4 seconds
            breathe(red, 6) # breathe out for 6 seconds
            i -= NO_TIMEOUT_FLAG # if 'NO_TIMEOUT_FLAG' set to 1, will decrement i causing an infinite loop
            # if NO_TIMEOUT_FLAG = 0 then this line has no impact as i-0 = i
    except: # if any errors arise, turn off
        [led.off() for led in led_list]

def startup_test():
    [led.on() for led in led_list] # turn on all leds
    time.sleep(0.5)
    [led.off() for led in led_list] # turn off all leds
    time.sleep(0.5)

def breathe(led, timing): # 4 for in, 6 for out
    led.on()
    time.sleep(timing)
    led.off()

if __name__ == "__main__":
    main()


# Does it run at all (hope so) YES
# Does timeout / sleep mode work? YES
