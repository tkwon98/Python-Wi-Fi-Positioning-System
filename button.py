import requests
import time
import RPi.GPIO as GPIO

url = 'http://nightlight/' # I map this to my internal DNS hosting the node app
gpio_pin=18 # The GPIO pin the button is attached to

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    time.sleep(0.2)

    if GPIO.input(gpio_pin) == False: # Listen for the press, the loop until it steps
        print "Started press"
