import RPi.GPIO as GPIO
import time


TRIG = 23
ECHO = 24
BUZZER =26

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    
    print("Distance measurement in Progress")
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 1)
    print("Distance:", distance, "cm")
    
    return distance

# Calculates the frequency of beeping depending on the measured distance
def beep_freq():
    # Measure the distance
    dist = measure_distance()
    # If the distance is larger than 50 cm, there is no beep
    if dist > 50:
        return -1
    # If the distance is between 50 and 30 cm, beep once a second
    elif dist <= 50 and dist >=30:
        return 1
    # If the distance is between 30 and 20 cm, beep twice a second
    elif dist < 30 and dist >= 20:
        return 0.5
    # If the distance is between 20 and 10 cm, beep four times a second
    elif dist < 20 and dist >= 10:
        return 0.25
    # If the distance is smaller than 10 cm, beep constantly
    else:
        return 0
    
# Main function
def main():
    try:
    # Repeat till the program is ended by the user
        while True:
            # Get the beeping frequency
            freq = beep_freq()
        
            # No beeping
            if freq == -1:
                GPIO.output(BUZZER, False)
                time.sleep(0.25)
            
            # Constant beeping
            elif freq == 0:
                GPIO.output(BUZZER, True)
                time.sleep(0.25)
            
            # Beeping on certain frequency
            else:
                GPIO.output(BUZZER, True)
                time.sleep(0.2) # Beep is 0.2 seconds long
                GPIO.output(BUZZER, False)
                time.sleep(freq) # Pause between beeps = beeping frequency
            
        # If the program is ended, stop beeping and clean up GPIOs
    except KeyboardInterrupt:
        GPIO.output(BUZZER, False)
        GPIO.cleanup()

main()
