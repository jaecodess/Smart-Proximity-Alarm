
from gpiozero import Button , LED

import pygame
pygame.init()

#Create the sound objects
drum = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/drum_bass_hard.wav')
bell = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/perc_bell.wav')
bird = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/misc_crow.wav')
vinyl = pygame.mixer.Sound('/home/pi/gpio-music-box/soundsamples/vinyl_hiss.wav') 

#Initializing LEDs

led1 = LED(13)
led2 = LED(19)
led3 = LED(26)
led4 = LED(20)

#Initializing Buttons

btn_bird = Button(17)
btn_bird.when_pressed = bird.play
btn_bird.when_released = led1.off
def bird_action():
    bird.play()
    led1.on()

btn_vinyl = Button(22)
btn_vinyl.when_pressed = vinyl.play
btn_vinyl.when_released = led2.off
def vinyl_action():
    vinyl.play()
    led2.on()

btn_drum = Button(23)
btn_drum.when_pressed = drum.play
btn_drum.when_released = led3.off
def drum_action():
    drum.play()
    led3.on()

btn_bell = button(27)
btn_bell.when_pressed = bell.play
btn_bell.when_released = led4.off
def bell_action():
    drum.play()
    led4.on()
