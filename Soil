#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import smtplib


#GPIO SETUP
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
warning = 0   

smtp.connect(self._smtp_host, self._smtp_port)
smtp.ehlo() 
smtp.starttls() 
smtp.ehlo()
      
#setup Email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.login("rpicompsci@gmail.com", "raspberrypi")


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
                server.sendmail("rpicompsci@gmail.com", "phardison@ves.org", "\nNo Water!")
        if GPIO.input(21) == 1:
                warning = warning +1
        elif GPIO.input(21) == 0:
                warning = 0
                
  


