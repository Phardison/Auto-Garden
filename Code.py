from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while 1 == 1:
  temp = int(round(sense.get_temperature()))
  ftemp = 1.8 * temp + 32
  print ftemp
  sleep(5)
"This Code is Different than before"
