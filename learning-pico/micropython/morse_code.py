# SET THE STRING TO BE CONVERTED AND DISPLAYED HERE
message_in_alpha = "merry christmas"

from machine import Pin
import time

led = Pin(15, Pin.OUT) # set "led" to the output of pin number 15

# SET DELAYS
DOT_DELAY = 0.15
DASH_DELAY = DOT_DELAY * 3
SPACE_DELAY = DOT_DELAY * 3
LETTER_DELAY = 0.2

alpha_to_morse = { 
    "A":".-","N":"-.",
	"B":"-...","O":"---",	 
 	"C":"-.-.","P":".--.",	 
 	"D":"-..","Q":"--.-",	 
 	"E":".","R":".-.",	 
 	"F":"..-.","S":"...",	 
 	"G":"--.","T":"-",	 
 	"H":"....","U":"..-",	 
 	"I":"..","V":"...-",	 
 	"J":".---","W":".--",	 
 	"K":"-.-","X":"-..-",	 
 	"L":".-..","Y":"-.--",	 
 	"M":"--","Z":"--..",
    "1":".----","6":"-....",	 
 	"2":"..---","7":"--...",	 
 	"3":"...--","8":"---..",	 
 	"4":"....-","9":"----.",	 
 	"5":".....","0":"-----",
    "?":"..--..",";":"-.-.-.",	 
 	":":"---...","/":"-..-.",	 
 	"-":"-....-","\'":".----.",	 
 	"\"":".-..-.","(":"-.--.",
    ")":"-.--.-","=":"-...-",
    "+":".-.-.","*":"-..-",
    "@":".--.-.","Á":".--.-",
    "Ä":".-.-", "É":"..-..",
    "Ñ":"--.--", "Ö":"---.",
    "Ü":"..--"," ":" "}

# Convert the alphanumeric message into morse code
def convert(message_in_alpha): # func:convert, takes the alphanumeric message as an argument
    message_in_alpha = message_in_alpha.upper() # sanitisation
    message_in_morse = []
    for letter in message_in_alpha:
        try:
            message_in_morse.append(alpha_to_morse[letter])
        except KeyError: # if the letter is not in the dictionary then print a message to the user and replace with a space
            message_in_morse.append(" ")
            print(f"Unknown key: {letter}")
    message_in_morse = " ".join(message_in_morse)
    print(message_in_morse)
    return message_in_morse
    
def flicker(delay): # causes the led to turn on then off with a delay dependent on wheter a dot or dash
    led.value(1)
    time.sleep(delay)
    led.value(0)
    time.sleep(LETTER_DELAY)

message_in_morse = convert(message_in_alpha) # convert alphanumeric --> morse
while True:
    for char in message_in_morse:
        if char == "-":
            flicker(DASH_DELAY)
        elif char == ".":
            flicker(DOT_DELAY)
        else:
            time.sleep(SPACE_DELAY)
    time.sleep(1)
    