#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import os
from weather import TotalRain

#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
warning = 0   



print (TotalRain*0.03937008)


def callback(channel):
        if GPIO.input(channel):
                print ("No Water!"),
                print (warning)
        else:
                print ("Water Detected!")


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        callback(21)
        time.sleep(3600)
        if warning >= 12 and (TotalRain*0.03937008) <= 0.7:
                print ("need water")
                os.system('echo "Please water the garden, the plants are thirsty." | mail -s "No Water!" rpicompsci@gmail.com')
                warning = 0
                time.sleep(86400)
        if GPIO.input(21) == 1:
                warning = warning +1
        elif GPIO.input(21) == 0:
                warning = 0
        


  

