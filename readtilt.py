from time import sleep
import RPi.GPIO as GPIO
from sys import exit
from playsound import playsound
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
 
print "Ready."
 
while True:
  ps = playsound()
  try:
    if GPIO.input(24):
      print "HIGH"
      if tilt != "high" and not(ps.isSongPlaying())
        ps.playSong()
        ps.isSongPlaying()
      tilt = "high"
    else:
      print "LO"
      tilt = "low"
      # reset var
      ps.stopPlaying()
    sleep(.7)
  except KeyboardInterrupt:
    exit()