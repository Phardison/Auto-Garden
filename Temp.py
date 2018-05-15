from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

while 1 == 1:
  temp = int(round(sense.get_temperature()))
  ftemp = 1.8 * temp + 32
  if ftemp > 85:
    print str(ftemp) + "Warning: Too hot!"
  if ftemp < 50:
    print str(ftemp) + "Warning: Too cold!"
  sleep(5)

"50 F to 85 F"
