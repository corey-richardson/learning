# define RED 15
# define GREEN 14

int TIMEOUT_MINUTES = 30;
int NO_TIMEOUT_FLAG = 0;

void setup(){
    pinMode(RED, OUTPUT); // set RED as output pin
    pinMode(GREEN, OUTPUT); // set GREEN as output pin

    // Run startup test, flash on/off
    digitalWrite(RED, HIGH); // on
    digitalWrite(GREEN, HIGH); // on
    delay(500); // wait
    digitalWrite(RED, LOW); // off
    digitalWrite(GREEN, LOW); // off
    delay(500); // wait
}

void breathe(int pin, int timing){
    digitalWrite(pin, HIGH); // on
    delay(timing); // wait
    digitalWrite(pin, LOW); // off
}

// the loop function runs forever, i hope 'break;' works on this
void loop(){
    // 6 breath cycles per minute * number of minutes to run
    for (int i = 0; i < 6*TIMEOUT_MINUTES; i++){
        breathe(GREEN, 4); // breathe in for 4 seconds
        breathe(RED, 6); // breathe out for 4 seconds
        i -= NO_TIMEOUT_FLAG; 
        /* if 'NO_TIMEOUT_FLAG' set to 1, will decrement i causing an 
        infinite loop
        if NO_TIMEOUT_FLAG = 0 then this line has no impact as i-0 = i */
    }
    break; // hopefully this will break loop
}

/*
CURRENTLY UNTESTED
To Test:
Does it run at all (hope so)
Does timeout / sleep mode work?
*/