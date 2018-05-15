#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time


#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
warning = 0   


#setup Email



def callback(channel):
        if GPIO.input(channel):
                print "aint no wata fam"
        else:
                print "Water Detected!"


GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change
 
# infinite loop
while True:
        callback(21)
        time.sleep(3)
        print warning
        if warning >= 10:
                print "need water"
        if GPIO.input(21) == 1:
                warning = warning +1
        elif GPIO.input(21) == 0:
                warning = 0
                
  

