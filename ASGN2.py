import RPi.GPIO as GPIO
import time
import pygame

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#initialize pygame mixer
pygame.mixer.init()

# laod in audio files
audio1 = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/bass_drop_c.wav')
audio2 = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/perc_bell.wav')
audio3 = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/misc_crow.wav')
audio4 = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/ambi_choir.wav')

def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.5)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
   
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
   
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 1)
    print("Distance:", distance, "cm")
    return distance
   
def play_audio(distance, last_played):
    # stop all audio
    pygame.mixer.music.stop()
    if distance > 50:
        print("No audio.")
        return -1
    elif 30 <= distance <= 50 and last_played != 0:
        audio1.play()
        return 0
    elif 20 <= distance <= 30 and last_played != 1:
        audio2.play()
        return 1
    elif 10 <= distance <= 20 and last_played != 2:
        audio3.play()
        return 2
    elif distance < 10 and last_played != 3:
        audio4.play()
        return 3
       
def main():
    try:
        last_index = -1
        while True:
            dist = measure_distance()
            last_index = play_audio(dist, last_index)
            time.sleep(0.5) # polling rate
    except KeyboardInterrupt:
        GPIO.cleanup()
        pygame.mixer.quit()
           
main()

   
